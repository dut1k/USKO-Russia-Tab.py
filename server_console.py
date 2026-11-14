"""Окно серверного режима. Сеть и FastAPI работают в дочернем процессе."""
from collections import deque
from datetime import datetime
from html import escape
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import time
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
import styleCSS as css
from competition_results import MODES, SIDES, load_results
from server_worker import SERVER_ALREADY_RUNNING, JsonLogFormatter, ParentWatch, server_instance_lock


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


class ServerDialog(QtWidgets.QDialog):
    def __init__(self, title, parent):
        super().__init__(parent)
        self.setWindowTitle(title)
        # Системный заголовок Windows не принимает шрифт Qt. Заголовок внутри
        # окна позволяет использовать Gotham и убрать системную кнопку справки.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("serverDialog")
        self.setStyleSheet("QDialog#serverDialog { background: white; border: 1px solid #dce2eb; }")
        self.setFont(css.font_l_13)

        self.content = QtWidgets.QVBoxLayout(self)
        title_row = QtWidgets.QHBoxLayout()
        self.title = QtWidgets.QLabel(self.windowTitle())
        self.title.setFont(css.font_m_20)
        self.title.installEventFilter(self)
        title_row.addWidget(self.title, 1)
        dismiss = QtWidgets.QToolButton()
        dismiss.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton))
        dismiss.setAccessibleName("Закрыть")
        dismiss.clicked.connect(self.reject)
        title_row.addWidget(dismiss)
        self.content.addLayout(title_row)

    def eventFilter(self, watched, event):
        if (watched is self.title and event.type() == QtCore.QEvent.MouseButtonPress
                and event.button() == QtCore.Qt.LeftButton):
            return self.windowHandle().startSystemMove()
        return super().eventFilter(watched, event)

    @staticmethod
    def style_buttons(*buttons):
        for button in buttons:
            button.setFont(css.font_l_15)
            button.setStyleSheet(css.btn_style_1)
            button.setMinimumHeight(32)
            button.setMinimumWidth(button.fontMetrics().horizontalAdvance(button.text()) + 20)


class DelaySettingsDialog(ServerDialog):
    def __init__(self, port, token, parent):
        super().__init__("Настройка задержки трансляции", parent)
        self.resize(470, 420)
        self.setSizeGripEnabled(True)
        self.rows = []
        self.reply = None
        self.network = QtNetwork.QNetworkAccessManager(self)
        self.request = QtNetwork.QNetworkRequest(QtCore.QUrl(
            "http://127.0.0.1:{}/api/delays".format(port)))
        self.request.setRawHeader(b"X-USKO-Delay-Token", token.encode("ascii"))
        self.request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
        self.request.setTransferTimeout(2000)

        layout = self.content
        hint = QtWidgets.QLabel("Серым показаны столы, которые отключились или давно не подавали сигнал.")
        hint.setFont(css.font_l_13)
        hint.setWordWrap(True)
        layout.addWidget(hint)
        self.list = QtWidgets.QListWidget()
        self.list.setStyleSheet("QListWidget { selection-background-color: #e5ecff; }")
        self.list.currentRowChanged.connect(self._select_row)
        layout.addWidget(self.list, 1)

        controls = QtWidgets.QHBoxLayout()
        caption = QtWidgets.QLabel("Задержка")
        caption.setFont(css.font_l_13)
        self.delay = QtWidgets.QDoubleSpinBox()
        self.delay.setFont(css.font_l_15)
        self.delay.setRange(0, 3600)
        self.delay.setSuffix(" с")
        self.delay.setSingleStep(0.1)
        caption.setBuddy(self.delay)
        controls.addWidget(caption)
        controls.addWidget(self.delay)
        self.save = QtWidgets.QPushButton("Сохранить")
        self.save.clicked.connect(lambda: self._change(delay_sec=self.delay.value()))
        controls.addWidget(self.save)
        self.remove = QtWidgets.QPushButton("Удалить")
        self.remove.clicked.connect(lambda: self._change(delete=True))
        controls.addWidget(self.remove)
        layout.addLayout(controls)
        self.status = QtWidgets.QLabel()
        self.status.setFont(css.font_l_13)
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        close = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Close)
        close_button = close.button(QtWidgets.QDialogButtonBox.Close)
        close_button.setText("Закрыть")
        self.style_buttons(self.save, self.remove, close_button)
        close.rejected.connect(self.reject)
        layout.addWidget(close)
        self._select_row(-1)

        # Список обновляется без блокировки Qt и без сброса введённой задержки.
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(1500)
        self._refresh()

    def _refresh(self):
        if self.reply is None:
            self.reply = self.network.get(self.request)
            self.reply.finished.connect(self._received)

    def _select_row(self, index):
        enabled = 0 <= index < len(self.rows)
        for widget in (self.delay, self.save, self.remove):
            widget.setEnabled(enabled)
        if enabled:
            self.delay.setValue(self.rows[index]["delay_sec"])

    def _change(self, **values):
        if self.reply is not None and self.reply.operation() == QtNetwork.QNetworkAccessManager.GetOperation:
            self.reply.finished.disconnect(self._received)
            self.reply.abort()
            self.reply.deleteLater()
            self.reply = None
        if self.reply is None and self.list.currentRow() >= 0:
            row = self.rows[self.list.currentRow()]
            body = json.dumps(dict(values, ip=row["ip"])).encode("utf-8")
            self.reply = self.network.post(self.request, body)
            self.reply.finished.connect(self._received)

    def _received(self):
        reply = self.reply
        self.reply = None
        try:
            data = json.loads(bytes(reply.readAll()))
        except (ValueError, UnicodeError):
            data = None
        if reply.error() != QtNetwork.QNetworkReply.NoError or not isinstance(data, list):
            detail = data.get("detail") if isinstance(data, dict) else None
            self.status.setText(detail if isinstance(detail, str) else "Не удалось получить настройки сервера.")
        else:
            self.status.setText("" if data else "Список пока пуст. Столы появятся после передачи данных.")
            self._update_rows(data)
        reply.deleteLater()

    def _update_rows(self, rows):
        if rows == self.rows:
            return
        index = self.list.currentRow()
        previous = self.rows[index] if index >= 0 else None
        edited = self.delay.value()
        self.rows = rows
        with QtCore.QSignalBlocker(self.list):
            self.list.clear()
            selected = -1
            for index, row in enumerate(rows):
                seconds = QtCore.QLocale().toString(float(row["delay_sec"]), "g", 10)
                title = f"Татами {row['tatami_id']} · {seconds} с"
                # Строку рисует виджет с двумя подписями. Текст DisplayRole
                # Qt нарисовал бы под ним повторно, особенно заметно при выборе.
                item = QtWidgets.QListWidgetItem()
                item.setData(QtCore.Qt.AccessibleTextRole, title + " · " + row["ip"])
                item.setData(QtCore.Qt.AccessibleDescriptionRole,
                             "Активен" if row["active"] else "Нет недавних обновлений")
                self.list.addItem(item)
                widget = QtWidgets.QWidget()
                labels = QtWidgets.QVBoxLayout(widget)
                labels.setContentsMargins(8, 4, 8, 4)
                labels.setSpacing(2)
                tatami = QtWidgets.QLabel(title)
                tatami.setFont(css.font_m_15)
                tatami.setTextFormat(QtCore.Qt.PlainText)
                if not row["active"]:
                    tatami.setStyleSheet("color: #666;")
                ip = QtWidgets.QLabel(row["ip"])
                ip.setFont(css.font_l_12)
                ip.setStyleSheet("color: #666;")
                labels.addWidget(tatami)
                labels.addWidget(ip)
                item.setSizeHint(widget.sizeHint())
                self.list.setItemWidget(item, widget)
                if previous and row["ip"] == previous["ip"]:
                    selected = index
            self.list.setCurrentRow(selected if selected >= 0 else (0 if rows else -1))
        self._select_row(self.list.currentRow())
        if selected >= 0 and edited != round(previous["delay_sec"], self.delay.decimals()):
            self.delay.setValue(edited)


class ResultsPanel(QtWidgets.QWidget):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.records = []
        self.filters = []
        layout = QtWidgets.QVBoxLayout(self)
        filters_row = QtWidgets.QGridLayout()
        for column, (label, placeholder) in enumerate((
            ("Дата", "Все даты"), ("Татами", "Все татами"),
            ("Вид соревнований", "Все виды"), ("Категория", "Все категории"),
        )):
            combo = QtWidgets.QComboBox()
            combo.setStyleSheet(css.combo_style_1)
            combo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
            combo.setMinimumContentsLength(9)
            combo.setAccessibleName(label)
            combo.currentIndexChanged.connect(self._filter)
            self.filters.append((combo, placeholder))
            filters_row.addWidget(QtWidgets.QLabel(label), 0, column)
            filters_row.addWidget(combo, 1, column)
        header = QtWidgets.QWidget()
        header.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        header.setLayout(filters_row)
        filters_row.setContentsMargins(0, 0, 0, 0)
        self.search_fields = {}
        for column, (field, caption) in enumerate((("name", "ФИО или номер"), ("region", "Регион"))):
            search = QtWidgets.QLineEdit()
            search.setStyleSheet(css.LEdit_style_1)
            search.setPlaceholderText(caption)
            search.setAccessibleName(caption)
            search.setClearButtonEnabled(True)
            search.textChanged.connect(self._filter)
            self.search_fields[field] = search
            filters_row.addWidget(search, 2, column * 2, 1, 2)
        layout.addWidget(header)

        splitter = QtWidgets.QSplitter()
        self.entries = QtWidgets.QListWidget()
        self.entries.setAccessibleName("Список результатов")
        self.entries.currentItemChanged.connect(self._show_result)
        self.detail = QtWidgets.QTextBrowser()
        self.detail.setAccessibleName("Подробности результата")
        self.detail.setOpenLinks(False)
        splitter.addWidget(self.entries)
        splitter.addWidget(self.detail)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([340, 530])
        layout.addWidget(splitter, 1)
        self.timer = QtCore.QTimer(self, interval=1500)
        self.timer.timeout.connect(self.refresh)
        self._signature = None

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh()
        self.timer.start()

    def hideEvent(self, event):
        self.timer.stop()
        super().hideEvent(event)

    @staticmethod
    def _values(record):
        date = datetime.fromisoformat(record["time"]).strftime("%d.%m.%Y")
        return date, record["tatami_id"], MODES[record["mode"]], record["category"]

    def refresh(self):
        try:
            stat = self.path.stat() if self.path.exists() else None
            signature = (stat.st_mtime_ns, stat.st_size) if stat else ()
            if signature == self._signature:
                return
            records = load_results(self.path)
        except (OSError, sqlite3.Error, ValueError) as exc:
            self._signature = None
            self.detail.setPlainText(f"Не удалось прочитать архив результатов. {exc}")
            return
        self._signature = signature
        # Если оператор смотрел самую свежую запись, новая запись сразу
        # откроется. При просмотре старой карточки сохраняем выбор.
        follow_latest = self.entries.currentRow() == 0
        self.records = records
        values = [self._values(record) for record in records]
        for index, (combo, placeholder) in enumerate(self.filters):
            old = combo.currentData()
            # При появлении нового результата сохраняем выбранные фильтры.
            with QtCore.QSignalBlocker(combo):
                combo.clear()
                combo.addItem(placeholder, None)
                options = dict.fromkeys(row[index] for row in values if row[index])
                for value in options:
                    combo.addItem(value, value)
                combo.setCurrentIndex(max(0, combo.findData(old)))
        self._filter(follow_latest=follow_latest)

    def _filter(self, *_, follow_latest=False):
        selected = self.entries.currentItem()
        old_key = selected.data(QtCore.Qt.UserRole)["key"] if selected and not follow_latest else None
        criteria = [combo.currentData() for combo, _ in self.filters]
        queries = {field: search.text().casefold().replace("ё", "е").split()
                   for field, search in self.search_fields.items() if search.text().strip()}
        target = 0
        with QtCore.QSignalBlocker(self.entries):
            self.entries.clear()
            for record in self.records:
                if any(wanted is not None and wanted != actual
                       for wanted, actual in zip(criteria, self._values(record))):
                    continue
                # Оба поля проверяем для одной стороны, чтобы фамилия АКА
                # и регион СИРО не давали ложного совпадения.
                if queries and not any(
                    all(word in record[side][field].casefold().replace("ё", "е")
                        for field, words in queries.items() for word in words)
                    for side in SIDES if side in record
                ):
                    continue
                stamp = datetime.fromisoformat(record["time"]).strftime("%d.%m.%Y · %H:%M:%S")
                names = [record[side]["name"] for side in SIDES if side in record]
                summary = MODES[record["mode"]]
                if record["mode"] == "kumite":
                    summary += " · " + ":".join(str(record[side]["score"] or "0") for side in SIDES)
                    if record["kind"] != "result":
                        summary += " · Без итогового решения"
                elif record["mode"] == "kata_final":
                    summary += " · " + record["total"]
                if record["key"] == old_key:
                    target = self.entries.count()
                item = QtWidgets.QListWidgetItem(
                    f"{stamp} · Татами {record['tatami_id']}\n{summary}\n{' / '.join(names)}"
                )
                item.setData(QtCore.Qt.UserRole, record)
                self.entries.addItem(item)
            if self.entries.count():
                self.entries.setCurrentRow(target)
        self._show_result(self.entries.currentItem())

    def _show_result(self, item, previous=None):
        if item is None:
            self.detail.setPlainText("По выбранным фильтрам результатов нет." if self.records else
                                     "В архиве пока нет результатов.")
            return
        result = item.data(QtCore.Qt.UserRole)
        mode = result["mode"]
        stamp = datetime.fromisoformat(result["time"]).strftime("%d.%m.%Y · %H:%M:%S")
        category = escape(result["category"])
        parts = [f"<p>{stamp} · Татами {escape(result['tatami_id'])} · {category}</p>",
                 f"<h2>{MODES[mode]}</h2>"]
        for side in SIDES:
            if side not in result:
                continue
            athlete = result[side]
            label = "АКА" if side == "aka" else "СИРО"
            if mode == "kata_qual" and result["winner"] == side:
                label = f'<span style="color:#15803d;">{label}</span>'
            name, region = escape(athlete["name"]), escape(athlete["region"])
            parts.append(f"<p><b>{label}</b> &nbsp; {name} &nbsp; <small>{region}</small></p>")
        if mode == "kata_final":
            cells = []
            for index in range(1, 8):
                score = escape(result["scores"][f"ref{index}"])
                if score:
                    mark = f"<s>{score}</s>" if index in result["excluded"] else score
                    cells.append(f'<td align="center"><small>Судья {index}</small><br>{mark}</td>')
            parts.append('<table cellspacing="5" cellpadding="4"><tr>' + "".join(cells) + "</tr></table>")
            parts.append(f"<h3>Итоговая сумма &nbsp; {escape(result['total'])}</h3>")
        else:
            if mode == "kumite":
                aka, siro = (escape(str(result[side]["score"] or "0")) for side in SIDES)
                parts.append(f"<h2>{aka} : {siro}</h2>")
            if result.get("winner"):
                winner = "АКА" if result["winner"] == "aka" else "СИРО"
                parts.append(f"<p><b>Победитель · {winner}</b></p>")
            else:
                parts.append("<p><b>Без итогового решения</b></p>")
            if result.get("timeline"):
                parts.append("<h3>Ход поединка</h3>")
                parts.append("<small>Время у события — остаток на табло</small>")
                for side, action, seconds in result["timeline"]:
                    remaining = "" if seconds is None else f"{seconds // 60:02d}:{seconds % 60:02d}"
                    label = "АКА" if side == "aka" else "СИРО"
                    # Цвет задаём только буквам: QTextBrowser может растянуть
                    # фон текстового фрагмента при переносе строки.
                    color = "#bf293c" if side == "aka" else "#53677e"
                    label = f'<b><span style="color:{color};">{label}</span></b>'
                    parts.append(f"<p>{label} {escape(action)} <small>{remaining}</small></p>")
        self.detail.setHtml("".join(parts))


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
        self.tables_network = QtNetwork.QNetworkAccessManager(self)
        self.tables_reply = None
        self.table_rows = []
        self.known_tables = {}
        self.delay_token = None
        self.tables_timer = QtCore.QTimer(self)
        self.tables_timer.setInterval(1500)
        self.tables_timer.timeout.connect(self._refresh_tables)
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
        self.delay_button = QtWidgets.QPushButton("Настройка задержки")
        self.delay_button.setFixedHeight(38)
        self.delay_button.setEnabled(False)
        self.delay_button.clicked.connect(self._show_delay_settings)
        header.addWidget(self.delay_button)
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
        self.tables_scroll = QtWidgets.QScrollArea()
        self.tables_scroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tables_scroll.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        self.tables_scroll.setFixedHeight(22)
        self.tables_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tables_scroll.setStyleSheet("""
            QScrollArea#sessionTables, QWidget#sessionTablesViewport, QWidget#sessionTableStrip {
                background: transparent;
            }
            QScrollBar:horizontal { height: 4px; background: transparent; margin: 0; }
            QScrollBar::handle:horizontal { background: #a8b8cc; min-width: 16px; border-radius: 2px; }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: transparent; }
        """)
        self.tables_scroll.setObjectName("sessionTables")
        self.tables_scroll.viewport().setObjectName("sessionTablesViewport")
        self.tables_scroll.viewport().installEventFilter(self)
        self.table_strip = QtWidgets.QWidget()
        self.table_strip.setObjectName("sessionTableStrip")
        self.table_strip.setFixedSize(0, 18)
        self.table_layout = QtWidgets.QHBoxLayout(self.table_strip)
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setSpacing(4)
        self.tables_scroll.setWidget(self.table_strip)
        # QScrollArea сам включает заливку фона у вложенного виджета.
        self.table_strip.setAutoFillBackground(False)
        self.tables_scroll.viewport().setAutoFillBackground(False)
        journal_tools.addWidget(self.tables_scroll, 1)
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
        self.journal_tabs = QtWidgets.QTabWidget()
        self.journal_tabs.addTab(self.log_splitter, "Журнал")
        self.results = ResultsPanel(self.log_dir / "results.sqlite3")
        self.journal_tabs.addTab(self.results, "Результаты")
        journal_layout.addWidget(self.journal_tabs)
        # Кнопка находится внутри содержимого, поэтому остаётся в отделённом
        # журнале, а стандартный заголовок и системная рамка Qt сохраняются.
        self.dock.setWidget(journal)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock)
        self.resizeDocks([self.dock], [390], QtCore.Qt.Vertical)
        view_menu = self.menuBar().addMenu("Вид")
        view_menu.addAction(self.dock.toggleViewAction())
        results_action = view_menu.addAction("Результаты")
        results_action.triggered.connect(self._show_results)
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

    def _show_results(self):
        self.dock.show()
        self.dock.raise_()
        self.journal_tabs.setCurrentWidget(self.results)

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

    def _show_delay_settings(self):
        dialog = DelaySettingsDialog(self.port.value(), self.delay_token, self)
        dialog.exec_()
        dialog.deleteLater()

    def eventFilter(self, watched, event):
        if watched is self.tables_scroll.viewport() and event.type() == QtCore.QEvent.Wheel:
            bar = self.tables_scroll.horizontalScrollBar()
            delta = event.angleDelta().y()
            if bar.maximum() and delta:
                bar.setValue(bar.value() - delta // 6)
                return True
        return super().eventFilter(watched, event)

    def _refresh_tables(self):
        if self.tables_reply is None:
            request = QtNetwork.QNetworkRequest(QtCore.QUrl(
                "http://127.0.0.1:{}/api/session-tables".format(self.port.value())))
            request.setRawHeader(b"X-USKO-Delay-Token", self.delay_token.encode("ascii"))
            request.setTransferTimeout(2000)
            self.tables_reply = self.tables_network.get(request)
            self.tables_reply.finished.connect(self._read_tables)

    def _read_tables(self):
        reply = self.tables_reply
        self.tables_reply = None
        if self.state == "running" and reply.error() == QtNetwork.QNetworkReply.NoError:
            try:
                rows = json.loads(bytes(reply.readAll()))
            except ValueError:
                rows = None
            if isinstance(rows, list):
                # При перезапуске процесса сохраняем обнаруженные столы
                # до выхода из окна сервера. Новые сообщения обновляют их.
                self.known_tables.update((row["ip"], row) for row in rows)
                self._set_table_rows(list(self.known_tables.values()))
        reply.deleteLater()

    def _set_table_rows(self, rows):
        rows = sorted(rows, key=lambda row: (not row["active"], row["tatami_id"].zfill(4), row["ip"]))
        if rows == self.table_rows:
            return
        self.table_rows = rows
        # Меняем содержимое только при смене состава или статуса. Полоса
        # занимает свободную ширину заголовка, даже если татами много.
        bar = self.tables_scroll.horizontalScrollBar()
        position = bar.value()
        while self.table_layout.count():
            badge = self.table_layout.takeAt(0).widget()
            badge.hide()
            badge.deleteLater()
        size = self.table_strip.height()
        for row in rows:
            badge = QtWidgets.QLabel()
            badge.setTextFormat(QtCore.Qt.PlainText)
            badge.setText(row["tatami_id"])
            tatami = f"татами №{row['tatami_id']}"
            status = (f"Есть связь с компьютером {tatami}" if row["active"]
                      else f"Связь с компьютером {tatami} потеряна")
            tooltip = f"{status}\nIP: {row['ip']}"
            if row.get("disconnected_at"):
                stamp = datetime.fromisoformat(row["disconnected_at"]).astimezone()
                tooltip += f"\nОтключение: {stamp:%d.%m.%Y %H:%M:%S}"
            badge.setToolTip(tooltip)
            badge.setFont(css.font_m_13)
            badge.setAlignment(QtCore.Qt.AlignCenter)
            badge.setFixedSize(size, size)
            # Зелёная рамка и серая заливка взяты из значков загрузки Excel.
            color, background = ("#20744A", "#ffffff") if row["active"] else ("#4b5563", "#C9C9C9")
            # Подсказка Qt наследует таблицу стилей квадратика, поэтому
            # задаём ей отдельные цвета и шрифт, как у подписей журнала.
            badge.setStyleSheet("""
                QLabel { background: %s; color: %s; border: 1px solid %s; border-radius: 3px; }
                QToolTip { background: #ffffff; color: #263346; border: 1px solid #ccd6eb;
                           padding: 3px 5px; font: %dpx "%s"; }
            """ % (background, color, color, css.font_l_13.pixelSize(), css.font_l_13.family()))
            if badge.fontMetrics().horizontalAdvance(badge.text()) > badge.width() - 2:
                badge.setFont(css.font_l_10)
            self.table_layout.addWidget(badge)
        gaps = max(0, len(rows) - 1) * self.table_layout.spacing()
        self.table_strip.setFixedWidth(len(rows) * size + gaps)
        bar.setValue(position)

    def _set_state(self, state):
        self.state = state
        if state == "running" and self.delay_token:
            self.tables_timer.start()
            self._refresh_tables()
        else:
            self.tables_timer.stop()
            if self.tables_reply is not None:
                self.tables_reply.abort()
            stopped_at = datetime.now().astimezone().isoformat(timespec="seconds")
            for ip, row in self.known_tables.items():
                if row["active"]:
                    self.known_tables[ip] = dict(row, active=False, disconnected_at=stopped_at)
            self._set_table_rows(list(self.known_tables.values()))
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
        self.delay_button.setEnabled(state == "running")
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
            lock_path = self.log_dir / "server.lock"
            # Обычно конфликт можно показать до создания дочернего процесса.
            # Сам сервер проверяет блокировку ещё раз при одновременном запуске.
            with server_instance_lock(lock_path) as acquired:
                pass
            if not acquired:
                self._show_server_already_running()
                return
            if self.session:
                self.session.cleanup()
            self.session = tempfile.TemporaryDirectory(prefix="usko-server-")
            self.stop_file = Path(self.session.name) / "stop"
            self.ready_file = Path(self.session.name) / "ready"
            self.delay_token = uuid.uuid4().hex
            name = "server-" + datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:8] + ".jsonl"
            log_file = self.log_dir / name
            self.tail = LogTail(log_file)
            # Проверяем права до запуска: работа без сохранённого журнала
            # не должна выглядеть как успешный запуск сервера.
            log_file.touch(exist_ok=False)
            args = ["--port", str(self.port.value()), "--log-file", str(log_file),
                    "--stop-file", str(self.stop_file), "--ready-file", str(self.ready_file),
                    "--parent-pid", str(os.getpid()), "--version", self.app_version,
                    "--delay-file", str(self.log_dir / "delays.json"), "--delay-token", self.delay_token,
                    "--instance-lock", str(lock_path)]
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

    def _confirm(self, title, message):
        dialog = ServerDialog(title, self)
        label = QtWidgets.QLabel(message)
        label.setFont(css.font_l_13)
        label.setWordWrap(True)
        dialog.content.addWidget(label)
        buttons = QtWidgets.QDialogButtonBox()
        yes = buttons.addButton("Да", QtWidgets.QDialogButtonBox.YesRole)
        no = buttons.addButton("Нет", QtWidgets.QDialogButtonBox.NoRole)
        dialog.style_buttons(yes, no)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        dialog.content.addWidget(buttons)
        dialog.setMinimumWidth(420)
        yes.setAutoDefault(False)
        no.setDefault(True)
        no.setFocus()
        confirmed = dialog.exec_() == QtWidgets.QDialog.Accepted
        dialog.deleteLater()
        return confirmed

    def _show_server_already_running(self):
        dialog = ServerDialog("Сервер уже запущен", self)
        message = QtWidgets.QLabel("Сервер трансляции работает в другой копии программы. "
                                   "Чтобы запустить его здесь, сначала остановите тот сервер.")
        message.setFont(css.font_l_13)
        message.setWordWrap(True)
        dialog.content.addWidget(message)
        buttons = QtWidgets.QDialogButtonBox()
        close = buttons.addButton("Понятно", QtWidgets.QDialogButtonBox.AcceptRole)
        dialog.style_buttons(close)
        buttons.accepted.connect(dialog.accept)
        dialog.content.addWidget(buttons)
        dialog.setMinimumWidth(420)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.open()

    def confirm_stop(self):
        if self._confirm("Остановить сервер?", "Трансляция всех подключённых татами будет прервана."):
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
        if code == SERVER_ALREADY_RUNNING and exit_status == QtCore.QProcess.NormalExit and not was_stopping:
            self._set_state("off")
            self._poll()
            self._show_server_already_running()
            return
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
                    # Служебные обновления индикаторов остаются в файле
                    # журнала и не вытесняют запросы судейских столов на экране.
                    if (record.get("source") == "uvicorn.access"
                            and record.get("path") in ("/api/session-tables", "/api/presence/heartbeat")
                            and record.get("status") == 200):
                        continue
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
            if not self._confirm("Перейти в режим табло?",
                                 "Сервер будет остановлен. Трансляция всех татами прервётся."):
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
                if not self._confirm("Выйти из программы?",
                                     "Сервер работает. Выход остановит трансляцию всех татами."):
                    event.ignore()
                    return
                self.close_pending = True
                self.stop_server()
            event.ignore()
            return
        event.accept()
        self.timer.stop()
        self.known_tables.clear()
        self._set_table_rows([])
        if self.session:
            self.session.cleanup()
            self.session = None
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
        QtWidgets.QApplication.instance().quit()
