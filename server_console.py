"""Окно серверного режима. Сеть и FastAPI работают в дочернем процессе."""
from collections import deque
from datetime import datetime
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import sys
import tempfile
import time
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
import styleCSS as css
from server_worker import JsonLogFormatter, ParentWatch


def console_icon(kind, color):
    """Рисуем контурные значки в координатах 24×24, без зависимости от шрифта.

    Запас разрешения сохраняет чёткость на экранах с масштабированием Windows.
    Готовые изображения приложения при этом не изменяются.
    """
    pixmap = QtGui.QPixmap(72, 72)
    pixmap.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(pixmap)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    painter.scale(3, 3)
    painter.setPen(QtGui.QPen(QtGui.QColor(color), 1.6, QtCore.Qt.SolidLine,
                            QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    if kind == "power":
        painter.drawArc(QtCore.QRectF(4, 4, 16, 16), 135 * 16, 270 * 16)
        painter.drawLine(QtCore.QPointF(12, 2), QtCore.QPointF(12, 11))
    elif kind == "link":
        painter.translate(12, 12)
        painter.rotate(-45)
        painter.drawRoundedRect(QtCore.QRectF(-4, -11, 8, 13), 4, 4)
        painter.drawRoundedRect(QtCore.QRectF(-4, -2, 8, 13), 4, 4)
    elif kind == "pin":
        painter.drawRoundedRect(QtCore.QRectF(3, 3, 18, 18), 2, 2)
        painter.drawLine(QtCore.QPointF(3, 15), QtCore.QPointF(21, 15))
    painter.end()
    pixmap.setDevicePixelRatio(3)
    return QtGui.QIcon(pixmap)


class LogTail:
    """Читаем журнал порциями, закрывая файл до возможной ротации в Windows."""
    def __init__(self, path):
        self.path = Path(path)
        self.identity = None
        self.offset = 0
        self.pending = b""

    def read(self):
        try:
            with self.path.open("rb") as stream:
                stat = os.fstat(stream.fileno())
                identity = (stat.st_dev, stat.st_ino)
                if identity != self.identity or stat.st_size < self.offset:
                    self.offset = 0
                    self.pending = b""
                    self.identity = identity
                stream.seek(self.offset)
                data = stream.read(64 * 1024)
                self.offset = stream.tell()
        except FileNotFoundError:
            return []
        parts = (self.pending + data).split(b"\n")
        self.pending = parts.pop()
        records = []
        for part in parts:
            try:
                records.append(json.loads(part.decode("utf-8")))
            except (ValueError, UnicodeError):
                records.append(dict(time="", level="WARNING", source="journal",
                                    message=part.decode("utf-8", errors="replace")))
        return records


class ServerWindow(QtWidgets.QMainWindow):
    mode_requested = QtCore.pyqtSignal()

    def __init__(self, log_dir=None, worker_command=None, app_version="development"):
        super().__init__()
        self.setFont(css.font_l_13)
        self.setStyleSheet("QMainWindow, QDockWidget { background-color: white; }")
        self.setWindowTitle("USKO Tab — Сервер трансляции")
        self.resize(960, 620)
        # Две панели с отдельными заголовками и кнопками требуют места:
        # ниже этого размера Qt начинает обрезать статус и элементы управления.
        self.setMinimumSize(640, 480)
        self.process = QtCore.QProcess(self)
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.finished.connect(self._finished)
        self.process.errorOccurred.connect(self._process_error)
        self.process.readyReadStandardOutput.connect(self._process_output)
        self.worker_command = worker_command
        self.app_version = app_version
        self.state = "off"
        self.session = None
        self.tail = None
        self.worker_watch = None
        self.pending_finish = None
        self.close_pending = False
        self.back_pending = False
        self.queue = deque(maxlen=2000)
        # Частые HTTP-запросы не должны вытеснять события и ошибки сервера.
        self.request_queue = deque(maxlen=2000)
        self.log_dir = Path(log_dir) if log_dir else Path(
            QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.GenericDataLocation)
        ) / "USKO-Tab" / "logs"
        self.logger = logging.getLogger("usko.controller." + uuid.uuid4().hex)
        self.logger.propagate = False
        self.logger.setLevel(logging.INFO)
        self.log_available = False
        self._build_ui()
        try:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            # Журналы каждого сеанса ротируются по размеру, старые сеансы
            # удаляются через 14 дней. Ошибка удаления не мешает запуску.
            self._prune_logs()
            name = "controller-" + datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:8] + ".jsonl"
            handler = RotatingFileHandler(self.log_dir / name, maxBytes=1024 * 1024,
                                          backupCount=1, encoding="utf-8")
            handler.setFormatter(JsonLogFormatter())
            self.logger.addHandler(handler)
            self.log_available = True
            self._set_state("off")
            self._note("INFO", "USKO Tab {}. Сервер выключен; автоматический запуск отключён.".format(app_version))
        except OSError as exc:
            self._note("ERROR", "Не удалось открыть журнал: " + str(exc))
            self.start_button.setEnabled(False)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._poll)
        self.timer.start(200)
        self.stop_timer = QtCore.QTimer(self)
        self.stop_timer.setSingleShot(True)
        self.stop_timer.timeout.connect(self._force_stop)
        self.start_timer = QtCore.QTimer(self)
        self.start_timer.setSingleShot(True)
        self.start_timer.timeout.connect(self._start_timeout)

    def _build_ui(self):
        center = QtWidgets.QWidget()
        center.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.setCentralWidget(center)
        layout = QtWidgets.QVBoxLayout(center)
        # При скрытом журнале QMainWindow отдаёт всё место центральной панели.
        # Верхнее выравнивание не позволяет растянуть расстояния между строками.
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(14)
        header = QtWidgets.QHBoxLayout()
        heading = QtWidgets.QVBoxLayout()
        self.heading = QtWidgets.QLabel("Сервер трансляции")
        heading.addWidget(self.heading)
        self.status = QtWidgets.QLabel("Сервер остановлен")
        heading.addWidget(self.status)
        header.addLayout(heading)
        header.addStretch()
        self.start_button = QtWidgets.QPushButton("Запустить сервер")
        self.start_button.clicked.connect(self._primary_clicked)
        header.addWidget(self.start_button)
        layout.addLayout(header)
        address_row = QtWidgets.QHBoxLayout()
        address_row.setSpacing(12)
        captions = []

        def field_group(title, field):
            group = QtWidgets.QVBoxLayout()
            group.setSpacing(6)
            caption = QtWidgets.QLabel(title)
            captions.append(caption)
            group.addWidget(caption)
            group.addWidget(field)
            return group

        self.port = QtWidgets.QSpinBox()
        self.port.setRange(1024, 65535)
        self.port.setValue(8000)
        self.address = QtWidgets.QComboBox()
        self.address.setToolTip("Выберите адрес сети соревнований. 127.0.0.1 работает только на этом компьютере.")
        self.address.setMinimumContentsLength(16)
        # Показываем все сетевые адреса: при нескольких адаптерах нельзя
        # достоверно выбрать сеть соревнований автоматически.
        addresses = sorted({a.toString() for a in QtNetwork.QNetworkInterface.allAddresses()
                            if a.protocol() == QtNetwork.QAbstractSocket.IPv4Protocol
                            and not a.isLoopback()})
        self.address.addItems(addresses + ["127.0.0.1"])
        address_row.addLayout(field_group("Адрес для табло", self.address), 1)
        address_row.addLayout(field_group("Порт", self.port))
        copy = QtWidgets.QPushButton("Копировать адрес")
        copy.clicked.connect(lambda: QtWidgets.QApplication.clipboard().setText(self.base_url()))
        address_row.addWidget(copy, 0, QtCore.Qt.AlignBottom)
        layout.addLayout(address_row)
        separator = QtWidgets.QFrame()
        separator.setFixedHeight(1)
        separator.setStyleSheet("background: #e7eaf0;")
        layout.addWidget(separator)
        overlay_row = QtWidgets.QHBoxLayout()
        overlay_row.setSpacing(12)
        self.tatami = QtWidgets.QSpinBox()
        self.tatami.setRange(1, 999)
        overlay_row.addLayout(field_group("Татами", self.tatami))
        overlay = QtWidgets.QPushButton("Ссылка для OBS")
        overlay.setIcon(console_icon("link", "#3e6ae1"))
        overlay.setIconSize(QtCore.QSize(18, 18))
        overlay.clicked.connect(lambda: QtWidgets.QApplication.clipboard().setText(
            self.base_url() + "/overlay/" + str(self.tatami.value())))
        overlay_row.addWidget(overlay, 0, QtCore.Qt.AlignBottom)
        self.overlay_url = QtWidgets.QLabel()
        self.overlay_url.setWordWrap(True)
        self.overlay_url.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        # Длинная ссылка переносится, не расширяя минимальную ширину окна.
        self.overlay_url.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        overlay_row.addWidget(self.overlay_url, 1, QtCore.Qt.AlignBottom)
        self.instruction_link = QtWidgets.QLabel(
            '<a style="color: #3e6ae1;" href="https://docs.google.com/document/d/'
            '1sA8vr42zpf9ZTD6yyJlhifmp6pUJuSRxUroRUGe1ung/edit">Инструкция по трансляции</a>')
        self.instruction_link.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.instruction_link.setOpenExternalLinks(True)
        self.instruction_link.setToolTip("Открыть инструкцию в браузере")
        overlay_row.addWidget(self.instruction_link, 0, QtCore.Qt.AlignBottom)
        self.address.currentTextChanged.connect(self._update_overlay_url)
        self.port.valueChanged.connect(self._update_overlay_url)
        self.tatami.valueChanged.connect(self._update_overlay_url)
        self._update_overlay_url()
        layout.addLayout(overlay_row)
        self.dock = QtWidgets.QDockWidget("Журнал сервера", self)
        self.dock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea | QtCore.Qt.TopDockWidgetArea)
        # Встроенный заголовок скрываем только в прикреплённом состоянии.
        # При отделении обязательно возвращаем штатный заголовок Qt:
        # иначе Windows убирает системную рамку плавающего окна.
        self._hidden_dock_title = QtWidgets.QWidget(self.dock)
        self._hidden_dock_title.setFixedHeight(0)
        self.dock.setTitleBarWidget(self._hidden_dock_title)
        self.log_splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.log_splitter.setChildrenCollapsible(False)
        self.log_splitter.setHandleWidth(3)
        self.log_splitter.setStyleSheet("QSplitter::handle:horizontal { background: #d8dde3; }")
        events_panel, self.terminal = self._log_panel("События сервера", False)
        requests_panel, self.requests_terminal = self._log_panel("HTTP-запросы", True)
        self.log_splitter.addWidget(events_panel)
        self.log_splitter.addWidget(requests_panel)
        self.log_splitter.setStretchFactor(0, 2)
        self.log_splitter.setStretchFactor(1, 1)
        self.log_splitter.setSizes([600, 300])
        journal = QtWidgets.QWidget()
        journal_layout = QtWidgets.QVBoxLayout(journal)
        journal_layout.setContentsMargins(20, 4, 20, 16)
        journal_layout.setSpacing(12)
        journal_tools = QtWidgets.QHBoxLayout()
        journal_tools.addWidget(QtWidgets.QLabel("Журнал сервера"))
        journal_tools.addStretch()
        self.attach_log_button = QtWidgets.QPushButton("Примагнитить")
        self.attach_log_button.setObjectName("journalPin")
        self.attach_log_button.setIcon(console_icon("pin", "#738096"))
        self.attach_log_button.clicked.connect(self.attach_log)
        self.attach_log_button.setEnabled(False)
        journal_tools.addWidget(self.attach_log_button)
        for title, icon, action in (
                ("Отделить", QtWidgets.QStyle.SP_TitleBarNormalButton, lambda: self.dock.setFloating(True)),
                ("Закрыть", QtWidgets.QStyle.SP_TitleBarCloseButton, self.dock.close)):
            button = QtWidgets.QToolButton()
            button.setToolTip(title)
            button.setIcon(self.style().standardIcon(icon))
            button.setAutoRaise(True)
            button.clicked.connect(action)
            journal_tools.addWidget(button)
        journal_layout.addLayout(journal_tools)
        journal_layout.addWidget(self.log_splitter)
        # Кнопка находится внутри содержимого, поэтому остаётся в отделённом
        # журнале, а стандартный заголовок и системная рамка Qt сохраняются.
        self.dock.setWidget(journal)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock)
        self.resizeDocks([self.dock], [390], QtCore.Qt.Vertical)
        view_menu = self.menuBar().addMenu("Вид")
        view_menu.addAction(self.dock.toggleViewAction())
        self.attach_log_action = view_menu.addAction("Примагнитить к основному окну")
        self.attach_log_action.triggered.connect(self.attach_log)
        self.attach_log_action.setEnabled(False)
        self.dock.topLevelChanged.connect(self.attach_log_action.setEnabled)
        self.dock.topLevelChanged.connect(self.attach_log_button.setEnabled)
        self.dock.topLevelChanged.connect(self._journal_floating_changed)
        self.settings_action = self.menuBar().addAction("Настройки/режим работы")
        self.settings_action.triggered.connect(self.mode_requested)
        self.folder_action = self.menuBar().addAction("Папка журналов")
        self.folder_action.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(
            QtCore.QUrl.fromLocalFile(str(self.log_dir))))
        self.show_log_action = self.menuBar().addAction("Показать журнал")
        self.show_log_action.setToolTip("Вернуть журнал сервера в основное окно")
        self.show_log_action.triggered.connect(self.attach_log)
        # Окна и дочерние виджеты со своими стилями не всегда наследуют QFont
        # от QMainWindow. Задаём шрифт явно, включая меню и отделённую панель.
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.setFont(css.font_l_15)
            if widget.objectName() == "journalCaption":
                widget.setFont(css.font_l_13)
        view_menu.setFont(css.font_l_15)
        for action in self.menuBar().actions():
            action.setFont(css.font_l_15)
        self.heading.setFont(css.font_m_20)
        self.instruction_link.setFont(css.font_l_13)
        for caption in captions + [self.overlay_url]:
            caption.setFont(css.font_l_13)
            caption.setStyleSheet("color: #738096;")
        self.terminal.setFont(css.font_l_13)
        self.requests_terminal.setFont(css.font_l_13)
        # Текстовые действия журнала остаются компактными на тёмном фоне;
        # для всей панели используем существующие шрифты и обычные виджеты Qt.
        for button in self.findChildren(QtWidgets.QPushButton):
            button.setFont(css.font_l_15)
            if button.objectName() in ("journalAction", "journalPin"):
                button.setFont(css.font_l_13)
                button.setStyleSheet("""
                    QPushButton { border: none; padding: 3px 4px; background: transparent; color: #a8b8cc; }
                    QPushButton:hover { color: #ffffff; background: #1c2935; }
                    QPushButton:disabled { color: #738096; }
                """ if button.objectName() == "journalAction" else """
                    QPushButton { border: none; padding: 4px; color: #526782; background: transparent; }
                    QPushButton:hover { color: #3e6ae1; background: #f0f4ff; }
                    QPushButton:disabled { color: #738096; }
                """)
                continue
            button.setStyleSheet(css.btn_style_1)
            button.setMinimumHeight(32)
            button.setMinimumWidth(button.fontMetrics().horizontalAdvance(button.text()) + 20)
            if not button.icon().isNull():
                button.setMinimumWidth(button.minimumWidth() + 24)
        control_style = """
            QComboBox, QSpinBox { background: #f6f8fb; color: #263346;
                border: 1px solid #dce2eb; border-radius: 7px; padding: 0 10px; }
            QComboBox:focus, QSpinBox:focus { border-color: #3e6ae1; }
            QComboBox::drop-down { border: none; width: 24px; }
            QComboBox::down-arrow { image: url(:/Images/icon_regions/flags/QComboBox_down_arrow.svg);
                width: 16px; height: 16px; }
            QComboBox QAbstractItemView { background: white; color: #263346;
                selection-background-color: #3e6ae1; selection-color: white; }
            QSpinBox:disabled { color: #8590a1; background: #eef1f5; }
        """
        secondary_style = """
            QPushButton { background: white; color: #3e6ae1; border: 1px solid #ccd6eb;
                border-radius: 7px; padding: 0 12px; }
            QPushButton:hover { background: #f0f4ff; border-color: #3e6ae1; }
            QPushButton:pressed { background: #e5ecff; }
        """
        for button in (copy, overlay):
            button.setStyleSheet(secondary_style)
            button.setFixedHeight(38)
        self.address.setStyleSheet(control_style)
        self.address.setFixedHeight(38)
        # Проверка диапазона чисел сохраняется; системные стрелки не нужны.
        for field, width in ((self.port, 90), (self.tatami, 75)):
            field.setFont(css.font_l_15)
            field.setStyleSheet(control_style)
            field.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            field.setFixedHeight(38)
            field.setFixedWidth(width)
        self.start_button.setFixedHeight(38)
        self.start_button.setMinimumWidth(190)
        self._set_state("off")

    def _journal_floating_changed(self, floating):
        self.dock.setTitleBarWidget(None if floating else self._hidden_dock_title)
        if floating:
            self._hidden_dock_title.hide()

    def _update_overlay_url(self):
        self.overlay_url.setText(self.base_url() + "/overlay/" + str(self.tatami.value()))

    def _primary_clicked(self):
        # Одна кнопка меняет действие по состоянию процесса. Подтверждение
        # остановки остаётся обязательным, чтобы не оборвать трансляцию случайно.
        if self.state in ("off", "error"):
            self.start_server()
        elif self.state in ("starting", "running"):
            self.confirm_stop()

    def _log_panel(self, title, requests):
        panel = QtWidgets.QWidget()
        panel.setObjectName("terminalPanel")
        panel.setStyleSheet("QWidget#terminalPanel { background: #101820; }")
        panel.setMinimumWidth(240)
        layout = QtWidgets.QVBoxLayout(panel)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(6)
        tools = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(title)
        label.setObjectName("journalCaption")
        label.setStyleSheet("color: #a8b8cc;")
        tools.addWidget(label)
        tools.addStretch()
        terminal = QtWidgets.QPlainTextEdit()
        terminal.setReadOnly(True)
        terminal.setMaximumBlockCount(3000)
        terminal.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        terminal.setStyleSheet("""
            QPlainTextEdit {
                background: #101820; color: #d7e2ed;
                selection-background-color: #345777; border: none;
            }
            QScrollBar:vertical { background: #101820; width: 5px; margin: 0; border: none; }
            QScrollBar:horizontal { background: #101820; height: 5px; margin: 0; border: none; }
            QScrollBar::handle:vertical { background: #536476; min-height: 24px; border-radius: 2px; }
            QScrollBar::handle:horizontal { background: #536476; min-width: 24px; border-radius: 2px; }
            QScrollBar::handle:hover { background: #8090a1; }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; border: none; }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; border: none; }
            QScrollBar::add-page, QScrollBar::sub-page { background: none; }
            QScrollBar::up-arrow, QScrollBar::down-arrow,
            QScrollBar::left-arrow, QScrollBar::right-arrow { image: none; }
            QAbstractScrollArea::corner { background: #101820; border: none; }
        """)
        # В макете над журналом только очистка. Полное копирование сохраняем
        # в контекстном меню вместе со штатным копированием выделенного текста.
        copy_log = QtWidgets.QAction("Копировать всё", terminal)
        copy_log.triggered.connect(lambda: QtWidgets.QApplication.clipboard().setText(terminal.toPlainText()))
        terminal.addAction(copy_log)
        terminal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        def context_menu(position):
            menu = terminal.createStandardContextMenu()
            menu.setFont(css.font_l_13)
            menu.addSeparator()
            menu.addAction(copy_log)
            menu.exec_(terminal.mapToGlobal(position))
            menu.deleteLater()

        terminal.customContextMenuRequested.connect(context_menu)
        clear = QtWidgets.QPushButton("Очистить")
        clear.setObjectName("journalAction")
        clear.clicked.connect(lambda: self.clear_screen(requests))
        tools.addWidget(clear)
        layout.addLayout(tools)
        layout.addWidget(terminal)
        return panel, terminal

    def attach_log(self):
        # Возвращаем также спрятанную или оказавшуюся за пределами экрана
        # отделённую панель. Сам журнал и его выделение не пересоздаются.
        self.dock.setFloating(False)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock)
        self.dock.show()
        self.dock.raise_()
        self.resizeDocks([self.dock], [max(160, self.height() - self.centralWidget().sizeHint().height() - 30)],
                         QtCore.Qt.Vertical)

    def showEvent(self, event):
        super().showEvent(event)
        # После показа Qt уже знает размеры панели управления. Остальное место
        # отдаём журналу, а не пустому полю над ним; разделитель можно двигать.
        QtCore.QTimer.singleShot(0, lambda: self.resizeDocks(
            [self.dock], [max(150, self.height() - self.centralWidget().sizeHint().height() - 30)],
            QtCore.Qt.Vertical))

    def _prune_logs(self):
        from time import time
        for pattern in ("server-*.jsonl*", "controller-*.jsonl*"):
            for path in self.log_dir.glob(pattern):
                try:
                    if time() - path.stat().st_mtime > 14 * 86400:
                        path.unlink()
                except OSError:
                    # Другая копия могла уже удалить старый журнал или держать
                    # его открытым. Это не должно запрещать запуск сервера.
                    pass

    def base_url(self):
        return "http://{}:{}".format(self.address.currentText(), self.port.value())

    def _note(self, level, message):
        self.logger.log(getattr(logging, level), message)
        self.queue.append(dict(time=datetime.now().isoformat(timespec="seconds"),
                               level=level, source="USKO", message=message))

    def _set_state(self, state):
        self.state = state
        titles = {"off": "Сервер остановлен", "starting": "Запускается…",
                  "running": "Сервер работает", "stopping": "Останавливается…", "error": "Ошибка сервера"}
        colors = {"off": "#b91c1c", "starting": "#a16207", "running": "#15803d",
                  "stopping": "#a16207", "error": "#b91c1c"}
        self.status.setText(titles[state])
        self.status.setStyleSheet("color: " + colors[state])
        idle = state in ("off", "error")
        self.start_button.setText("Запустить сервер" if idle else
                                  "Останавливается…" if state == "stopping" else "Остановить сервер")
        self.start_button.setIcon(console_icon("power", "#ffffff" if idle else "#b91c1c"))
        self.start_button.setIconSize(QtCore.QSize(18, 18))
        self.start_button.setEnabled((idle and self.log_available) or state in ("starting", "running"))
        self.start_button.setStyleSheet("""
            QPushButton { border-radius: 7px; padding: 0 14px; border: 1px solid %s;
                background: %s; color: %s; }
            QPushButton:hover { background: %s; }
            QPushButton:disabled { background: #eef1f5; color: #8590a1; border-color: #dce2eb; }
        """ % (("#3e6ae1", "#3e6ae1", "white", "#3158c4") if idle else
                  ("#e5bfc3", "white", "#b91c1c", "#fff0f1")))
        self.port.setEnabled(idle)

    def start_server(self):
        if self.process.state() != QtCore.QProcess.NotRunning or self.pending_finish or not self.log_available:
            return
        try:
            if self.session:
                self.session.cleanup()
            self.session = tempfile.TemporaryDirectory(prefix="usko-server-")
            self.stop_file = Path(self.session.name) / "stop"
            self.ready_file = Path(self.session.name) / "ready"
            name = "server-" + datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:8] + ".jsonl"
            log_file = self.log_dir / name
            self.tail = LogTail(log_file)
            # Проверяем права до запуска: работа без сохранённого журнала
            # не должна выглядеть как успешный запуск сервера.
            log_file.touch(exist_ok=False)
            args = ["--port", str(self.port.value()), "--log-file", str(log_file),
                    "--stop-file", str(self.stop_file), "--ready-file", str(self.ready_file),
                    "--parent-pid", str(os.getpid()), "--version", self.app_version]
            if self.worker_command:
                program, prefix = self.worker_command
            elif getattr(sys, "frozen", False):
                program, prefix = sys.executable, ["--usko-server-worker"]
            else:
                program, prefix = sys.executable, [str(Path(__file__).with_name("USKO-Russia-Tab.py")),
                                                  "--usko-server-worker"]
            self._note("INFO", "Запуск сервера на порту {}. Журнал: {}".format(self.port.value(), log_file))
            self._set_state("starting")
            self.process.start(program, prefix + args)
            self.start_timer.start(20000)
        except OSError as exc:
            self._note("ERROR", "Ошибка запуска: " + str(exc))
            self._set_state("error")

    def _process_output(self):
        text = bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="replace").strip()
        if text:
            self._note("WARNING", text)

    def _process_error(self, error):
        self._note("ERROR", self.process.errorString())
        if error == QtCore.QProcess.FailedToStart:
            self.start_timer.stop()
            self._set_state("error")

    def _start_timeout(self):
        if self.state == "starting":
            self._note("ERROR", "Сервер не подтвердил запуск за 20 секунд")
            self.stop_server()

    def confirm_stop(self):
        if QtWidgets.QMessageBox.question(self, "Остановить сервер?",
                "Трансляция всех подключённых татами будет прервана.",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            self.stop_server()

    def stop_server(self):
        if self.process.state() == QtCore.QProcess.NotRunning:
            return
        self.start_timer.stop()
        self._set_state("stopping")
        self._note("INFO", "Остановка сервера…")
        try:
            self.stop_file.touch()
        except OSError as exc:
            self._note("ERROR", "Не удалось передать команду остановки: " + str(exc))
        # Ожидание асинхронное: окно остаётся доступным даже при зависшем сервере.
        self.stop_timer.start(8000)

    def _force_stop(self):
        if self.worker_watch and self.worker_watch.alive():
            self._note("WARNING", "Принудительное завершение процесса сервера")
            try:
                self.worker_watch.terminate()
            except OSError as exc:
                self._note("ERROR", "Не удалось завершить сервер: " + str(exc))
        if self.process.state() != QtCore.QProcess.NotRunning:
            self._note("WARNING", "Сервер не ответил на остановку; процесс будет завершён принудительно")
            self.process.kill()

    def _finished(self, code, exit_status):
        self.start_timer.stop()
        self.stop_timer.stop()
        self._attach_worker()
        if self.worker_watch and self.worker_watch.alive():
            # QProcess может наблюдать загрузчик PyInstaller, а не сервер.
            # Не разрешаем перезапуск и не удаляем stop-файл, пока жив сервер.
            self.pending_finish = (code, exit_status, self.state == "stopping")
            self.finish_deadline = time.monotonic() + 8
            self._set_state("stopping")
            self._note("WARNING", "Процесс запуска завершён; ожидаем остановки сервера")
            try:
                self.stop_file.touch()
            except OSError as exc:
                self._note("ERROR", str(exc))
            return
        self._complete_finish(code, exit_status, self.state == "stopping")

    def _complete_finish(self, code, exit_status, was_stopping):
        expected = was_stopping and code == 0
        if self.worker_watch:
            self.worker_watch.close()
            self.worker_watch = None
        self.pending_finish = None
        self._set_state("off" if expected else "error")
        self._poll()
        self._note("INFO" if expected else "ERROR",
                   "Сервер остановлен" if expected else "Процесс сервера завершился: код {}".format(code))
        if self.back_pending:
            self.back_pending = False
            self.hide()
            self.return_to_table()
        if self.close_pending:
            self.close()

    def _attach_worker(self):
        if self.worker_watch is None and self.session and self.ready_file.exists():
            try:
                self.worker_watch = ParentWatch(int(self.ready_file.read_text(encoding="utf-8")))
            except (OSError, ValueError):
                # Процесс мог завершиться между записью готовности и чтением.
                pass

    def _poll(self):
        if self.pending_finish:
            if not self.worker_watch.alive():
                code, status, was_stopping = self.pending_finish
                self._complete_finish(code, status, was_stopping)
                return
            if time.monotonic() >= self.finish_deadline:
                self._force_stop()
                self.finish_deadline = time.monotonic() + 8
        if self.tail:
            try:
                for record in self.tail.read():
                    target = self.request_queue if record.get("source") == "uvicorn.access" else self.queue
                    target.append(record)
            except OSError as exc:
                self.tail = None
                self._note("ERROR", "Не удалось прочитать журнал: " + str(exc))
        if self.state == "starting" and self.ready_file.exists():
            self._attach_worker()
        if self.state == "starting" and self.worker_watch and self.worker_watch.alive():
            self.start_timer.stop()
            self._set_state("running")
            self._note("INFO", "Адрес подключения для OBS и табло: " + self.base_url())
        # Ограничиваем работу за один тик, чтобы поток сообщений не блокировал Qt.
        for pending in (self.queue, self.request_queue):
            for _ in range(min(100, len(pending))):
                self._append(pending.popleft())

    def _append(self, record):
        terminal = self.requests_terminal if record.get("source") == "uvicorn.access" else self.terminal
        bar = terminal.verticalScrollBar()
        follow = bar.value() == bar.maximum() and not terminal.textCursor().hasSelection()
        position = bar.value()
        cursor = QtGui.QTextCursor(terminal.document())
        cursor.movePosition(QtGui.QTextCursor.End)
        level = record.get("level", "INFO")
        colors = {"DEBUG": "#8293a7", "INFO": "#d7e2ed", "WARNING": "#f5c86a",
                  "ERROR": "#ff7f87", "CRITICAL": "#ff7f87"}
        color = colors.get(level, "#d7e2ed")
        message = record.get("message", "")
        if level == "INFO" and "Сервер остановлен" in message:
            color = "#ff7f87"
        elif level == "INFO" and "готов" in message:
            color = "#7ee2a8"
        elif level == "INFO" and record.get("source") == "usko.connections":
            color = "#74c7ec"
        if record.get("source") == "uvicorn.access" and isinstance(record.get("status"), int):
            status = record["status"]
            color = "#ff7f87" if status >= 500 else "#f5c86a" if status >= 400 else "#7ee2a8"
        fmt = QtGui.QTextCharFormat()
        fmt.setForeground(QtGui.QColor(color))
        # Переименовываем только отображение: техническое имя в JSONL остаётся
        # исходным, чтобы диагностика и разделение потоков были однозначны.
        source = record.get("source", "")
        if source == "uvicorn.access" and "method" in record:
            # В узкой правой панели сначала видны метод, путь и ответ;
            # адрес отправителя доступен дальше по строке. В файле остаются
            # полное время, исходный текст и отдельные поля HTTP-запроса.
            stamp = record.get("time", "").split("T")[-1]
            line = "{} {} {} {} | {}".format(stamp, record["method"], record.get("path", ""),
                                              record.get("status", ""), record.get("client", ""))
        else:
            source = {"USKO": "Программа", "root": "Сервер", "uvicorn.error": "Сервер",
                      "uvicorn.access": "HTTP", "usko.connections": "Подключения"}.get(source, source)
            line = "{} [{}] {}: {}".format(record.get("time", ""), level, source, message)
        cursor.insertText(line + "\n", fmt)
        bar.setValue(bar.maximum() if follow else position)

    def clear_screen(self, requests=False):
        (self.request_queue if requests else self.queue).clear()
        (self.requests_terminal if requests else self.terminal).clear()

    def request_table_mode(self, callback):
        if self.process.state() != QtCore.QProcess.NotRunning or self.pending_finish:
            if QtWidgets.QMessageBox.question(self, "Перейти в режим табло?",
                    "Сервер будет остановлен. Трансляция всех татами прервётся.",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No) != QtWidgets.QMessageBox.Yes:
                return
            self.return_to_table = callback
            self.back_pending = True
            self.stop_server()
        else:
            self.hide()
            callback()

    def closeEvent(self, event):
        if self.process.state() != QtCore.QProcess.NotRunning or self.pending_finish:
            if not self.close_pending:
                if QtWidgets.QMessageBox.question(self, "Выйти из программы?",
                        "Сервер работает. Выход остановит трансляцию всех татами.",
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                        QtWidgets.QMessageBox.No) != QtWidgets.QMessageBox.Yes:
                    event.ignore()
                    return
                self.close_pending = True
                self.stop_server()
            event.ignore()
            return
        event.accept()
        self.timer.stop()
        if self.session:
            self.session.cleanup()
            self.session = None
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
        QtWidgets.QApplication.instance().quit()
