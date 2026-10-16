from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
import styleCSS as css
from adaptive_display import AdaptiveDisplay
from PyQt5.QtSvg import QSvgRenderer


class RegionFlag(QtWidgets.QWidget):
    """Готовый SVG региона и рамка остаются векторными до отрисовки."""
    def __init__(self, parent):
        super().__init__(parent)
        self.renderer = QSvgRenderer(self)
        self.frame_renderer = QSvgRenderer(':/Images/icon_regions/flags/00_Curcle.svg', self)
        self.hide()

    def set_region(self, code):
        loaded = bool(code) and self.renderer.load(f':/Images/icon_regions/flags/{code}.svg')
        self.setVisible(loaded)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # Круг масштабируется вместе со сценой; исходные SVG не меняются.
        clip = QtGui.QPainterPath()
        clip.addEllipse(QtCore.QRectF(self.rect()))
        painter.setClipPath(clip)
        self.renderer.render(painter, QtCore.QRectF(self.rect()))
        self.frame_renderer.render(painter, QtCore.QRectF(self.rect()))


class KataSecondWindow_Ui(object):
    SCORE_STYLE = 'background: transparent; border: none; font-family: Gotham-Medium; font-size: 120px; color: black;'

    def __init__(self):
        self.font_m_35 = css.font_m_35

    def setupUi_Kata2(self, Form12):
        Form12.setObjectName('Form')
        Form12.setFixedSize(1920, 1080)
        Form12.setStyleSheet('background-color: white;')
        Form12.setWindowTitle(' ')
        Form12.setWindowIcon(QtGui.QIcon(':/Images/Empty.png'))

        def label(text, rect, family, size, color='black', alignment=Qt.AlignCenter):
            widget = QtWidgets.QLabel(text, Form12)
            widget.setGeometry(QtCore.QRect(*rect))
            widget.setAlignment(alignment)
            widget.setTextFormat(Qt.PlainText)
            widget.setStyleSheet(f'background: transparent; border: none; font-family: {family}; font-size: {size}px; color: {color};')
            return widget

        def panel(rect):
            widget = QtWidgets.QFrame(Form12)
            widget.setGeometry(QtCore.QRect(*rect))
            widget.setStyleSheet('background: white; border: 2px solid grey; border-radius: 15px;')
            return widget

        self.matchName2 = label('', (40, 20, 1840, 150), 'Gotham-Medium', 66, 'grey')
        self.matchName2.setWordWrap(True)
        self.person_panel = panel((40, 220, 1000, 440))
        self.sum_panel = panel((1080, 220, 800, 440))
        self.flag_red = RegionFlag(Form12)
        self.flag_red.setGeometry(80, 295, 150, 150)
        self.label_name_red_2 = label('ФАМИЛИЯ', (260, 250, 740, 250), 'Gotham-Bold', 110, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.label_name_red_2.setWordWrap(True)
        self.region_line = QtWidgets.QFrame(Form12)
        self.region_line.setGeometry(80, 520, 920, 2)
        self.region_line.setStyleSheet('background: grey; border: none;')
        self.label_region_red_2 = label('регион', (80, 540, 920, 100), 'Gotham-Light', 56, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.label_region_red_2.setWordWrap(True)
        self.sum_heading = label('ИТОГОВЫЙ БАЛЛ', (1100, 245, 760, 65), 'Gotham-Medium', 45, 'grey')
        self.label_sum2 = label('', (1100, 315, 760, 315), 'Gotham-Medium', 310)
        self.score_panels = []
        self.score_notes = []
        for index in range(1, 8):
            self.score_panels.append(panel((0, 740, 250, 260)))
            setattr(self, f'label_{index}', label(f'Судья {index}', (0, 765, 250, 50), 'Gotham-Medium', 32, 'grey'))
            score = label('', (0, 815, 250, 140), 'Gotham-Medium', 120)
            setattr(self, f'input_referee{index}', score)
            self.score_notes.append(label('', (0, 950, 250, 40), 'Gotham-Light', 24, 'grey'))
        self.set_judge_count(7)
        QtCore.QMetaObject.connectSlotsByName(Form12)

    @staticmethod
    def fit_label(widget, text, family, maximum, color='black'):
        # Подбираем шрифт по фактическому зрительскому прямоугольнику, а не
        # по метрикам судейского поля. Масштаб экрана применяет только сцена.
        widget.setText(text)
        rect = widget.contentsRect().adjusted(2, 2, -2, -2)
        size = maximum
        while size > 20:
            font = QtGui.QFont(family)
            font.setPixelSize(size)
            bounds = QtGui.QFontMetrics(font).boundingRect(rect, Qt.TextWordWrap, text)
            if bounds.width() <= rect.width() and bounds.height() <= rect.height():
                break
            size -= 1
        widget.setStyleSheet(f'background: transparent; border: none; font-family: {family}; font-size: {size}px; color: {color};')

    def set_athlete(self, name, region, code):
        self.flag_red.set_region(code)
        # Неизвестный регион не оставляет флаг предыдущего участника.
        self.label_name_red_2.setGeometry(260 if code and not self.flag_red.isHidden() else 80, 250,
                                          740 if code and not self.flag_red.isHidden() else 920, 250)
        self.fit_label(self.label_name_red_2, name, 'Gotham-Bold', 110)
        self.fit_label(self.label_region_red_2, region, 'Gotham-Light', 56)

    def set_judge_count(self, count):
        # Все части карточки перемещаются вместе при переходе 5 ↔ 7 судей.
        width = 352 if count == 5 else 250
        left = 70
        gap = 5
        for index in range(1, 8):
            x = left + (index - 1) * (width + gap)
            items = (self.score_panels[index - 1], getattr(self, f'label_{index}'),
                     getattr(self, f'input_referee{index}'), self.score_notes[index - 1])
            for widget, y, height in zip(items, (740, 765, 815, 950), (260, 50, 140, 40)):
                widget.setGeometry(x, y, width, height)
                widget.setVisible(index <= count)
            getattr(self, f'label_{index}').setText(f'Судья {index}')

    def reset_score_marks(self):
        for index in range(1, 8):
            score = getattr(self, f'input_referee{index}')
            score.setStyleSheet(self.SCORE_STYLE)
            font = score.font()
            font.setStrikeOut(False)
            score.setFont(font)
            self.score_notes[index - 1].clear()


class KataSecondWindow(AdaptiveDisplay, KataSecondWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_Kata2(self.canvas)
        self.mount_canvas()

    def Extream_Value(self):
        self.reset_score_marks()
        values = []
        for index in range(1, 8):
            try:
                value = float(getattr(self, f'input_referee{index}').text())
            except ValueError:
                continue
            if value != 0:
                values.append((index, value))
        if len(values) < 3:
            return
        # Сохраняем прежний порядок выбора одинаковых крайних оценок:
        # минимум — первый судья, максимум — сначала второй, затем первый.
        minimum = min(values, key=lambda item: item[1])[0]
        maximum_value = max(value for _, value in values)
        maximum = next(index for index in (2, 1, 3, 4, 5, 6, 7)
                       if (index, maximum_value) in values)
        for index, note in ((minimum, 'мин. исключён'), (maximum, 'макс. исключён')):
            self.extreamLabelStyle(getattr(self, f'input_referee{index}'))
            self.score_notes[index - 1].setText(note)

    def extreamLabelStyle(self, input_referee):
        input_referee.setStyleSheet(self.SCORE_STYLE.replace('color: black', 'color: Grey'))
        font = input_referee.font()
        font.setStrikeOut(True)
        input_referee.setFont(font)


class Frame_Header(QWidget):
    def __init__(self, parent):
        super(Frame_Header, self).__init__()
        self.parent = parent

        self.btn_style_header = css.btn_style_header

        self.font_l_13 = css.font_l_13

        self.font_l_22 = css.font_l_22

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.frame_title = QtWidgets.QFrame(self)
        self.frame_title.setStyleSheet("border-top: 1px solid gray; border-bottom: none; border-left: 1px solid gray;"
                                       "border-right: none;")
        self.frame_title.setFixedSize(690, 31)

        self.pixmap = QtGui.QPixmap(':/Images/icon_30px.ico')
        self.pixmap2 = self.pixmap.scaled(16, 16, QtCore.Qt.KeepAspectRatio)
        self.pixmap_label = QLabel(self.frame_title)
        self.pixmap_label.setGeometry(QtCore.QRect(8, 0, 30, 31))
        self.pixmap_label.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.pixmap_label.setPixmap(self.pixmap2)

        self.label_windowsTitle = QLabel("КАТА ФИНАЛ/ПОЛУФИНАЛ. Судейское окно", self.frame_title)
        self.label_windowsTitle.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.label_windowsTitle.move(30, 9)

        self.frame_combo = QtWidgets.QFrame(self)
        self.frame_combo.setGeometry(QtCore.QRect(0, 0, 153, 31))

        self.frame_combo_border = QtWidgets.QFrame(self.frame_combo)
        self.frame_combo_border.setStyleSheet("background-color: grey;")
        self.frame_combo_border.setGeometry(QtCore.QRect(0, 0, 200, 1))

        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.combo.setGeometry(0, 4, 147, 24)
        self.combo.addItems(["Главное меню", "Ката отбороч.", "Кумите"])
        self.combo.setFont(self.font_l_13)

        self.frame_btn = QtWidgets.QFrame(self)
        self.frame_btn.setFixedSize(51, 31)
        self.frame_btn.setStyleSheet("border-top: 1px solid gray; border-bottom: none; border-left: none;"
                                     "border-right: 1px solid gray;")

        self.btn_showMinimized = QtWidgets.QPushButton("_", self.frame_btn)
        self.btn_showMinimized.setGeometry(QtCore.QRect(0, 4, 24, 24))
        self.btn_showMinimized.setStyleSheet(self.btn_style_header)
        self.btn_showMinimized.setFont(self.font_l_13)
        self.btn_showMinimized.clicked.connect(self.btn_showMinimized_clicked)

        self.btn_closeWin = QtWidgets.QPushButton("×", self.frame_btn)
        self.btn_closeWin.setStyleSheet(self.btn_style_header)
        self.btn_closeWin.setFont(self.font_l_22)
        self.btn_closeWin.setGeometry(QtCore.QRect(23, 4, 24, 24))

        self.layout.addWidget(self.frame_title)
        self.layout.addWidget(self.frame_combo)
        self.layout.addWidget(self.frame_btn)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(Frame_Header, self).resizeEvent(QResizeEvent)
        self.label_windowsTitle.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_showMinimized_clicked(self):
        self.parent.showMinimized()


class KataMainWindow_Ui(QWidget):
    def __init__(self):
        super(KataMainWindow_Ui, self).__init__()
        QWidget.setWindowTitle(self, "Ката финал. Судейское окно")

        self.Form11 = QtWidgets.QFrame(self)
        self.Form11.setFixedSize(900, 500)
        self.Form11.setStyleSheet("background-color: white;")

        self.USKO_PC = css.USKO_PC  # Номер татами если наши ПК

        self.Calc_Button = QtWidgets.QPushButton("Рассчитать", self.Form11)
        self.Clear_Button = QtWidgets.QPushButton("Очистить", self.Form11)
        self.heading_sum = QtWidgets.QLabel("Сумма баллов", self.Form11)
        self.label_sum = QtWidgets.QLabel("Нажми кнопку\n«Рассчитать»", self.Form11)
        self.referee_point = QtWidgets.QLabel("Оценки судей", self.Form11)
        self.label_help = QtWidgets.QLabel("Переключайся между судьями кнопкой Tab", self.Form11)

        self.frame_sportsmans = QtWidgets.QFrame(self.Form11)
        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.label_name_red_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.Form11)
        self.label_region_red_1 = QtWidgets.QLabel("регион", self.Form11)
        self.pers_com_lbl = QtWidgets.QLabel("/", self.frame_sportsmans)
        self.pers_lbl = QtWidgets.QLabel("Личные", self.frame_sportsmans)
        self.com_lbl = QtWidgets.QLabel("Командные", self.frame_sportsmans)
        self.pers_com_qbx = QtWidgets.QCheckBox(self.frame_sportsmans)
        self.male = QtWidgets.QRadioButton("М", self.frame_sex)
        self.female = QtWidgets.QRadioButton("Ж", self.frame_sex)
        self.sex_1 = QtWidgets.QLabel("Пол", self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel("Возраст", self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)
        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(self.Form11, placeholderText="Введите имя спортсмена")
        self.lineEdit_region_red_1 = QtWidgets.QComboBox(self.Form11)
        self.frame_matchName = QtWidgets.QFrame(self.Form11)
        self.label_matchName1 = QtWidgets.QLabel('<b>Название категории</b>', self.frame_matchName)
        # self.matchName1 = QtWidgets.QLineEdit("Татами №#, Возраст", self.frame_matchName)
        self.matchName1 = QtWidgets.QLineEdit(f"Татами №{self.USKO_PC}, Возраст", self.frame_matchName)

        self.frame_pyatnov = QtWidgets.QFrame(self.Form11)

        self.pyatnov_label = QtWidgets.QLabel("Выберите спортсмена", self.frame_pyatnov)
        self.pyatnov_name = QtWidgets.QComboBox(self.frame_pyatnov)
        self.pyatnov_kata_label = QtWidgets.QLabel("Ката", self.frame_pyatnov)
        self.pyatnov_kata_name = QtWidgets.QComboBox(self.frame_pyatnov)

        self.btn_clearData = QtWidgets.QPushButton("Очистить данные", self.Form11)
        self.btn_NewCategory = QtWidgets.QPushButton("Новая\nкатегория", self.Form11)
        self.btn_showData = QtWidgets.QPushButton("Показать фамилию\nна экране", self.Form11)

        self.frame_referee = QtWidgets.QFrame(self.Form11)
        self.lineEdit_referee1 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee2 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee3 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee4 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee5 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee6 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee7 = QtWidgets.QLineEdit(self.frame_referee)
        self.label_1 = QtWidgets.QLabel("1 судья", self.frame_referee)
        self.label_2 = QtWidgets.QLabel("2 судья", self.frame_referee)
        self.label_3 = QtWidgets.QLabel("3 судья", self.frame_referee)
        self.label_4 = QtWidgets.QLabel("4 судья", self.frame_referee)
        self.label_5 = QtWidgets.QLabel("5 судья", self.frame_referee)
        self.label_6 = QtWidgets.QLabel("6 судья", self.frame_referee)
        self.label_7 = QtWidgets.QLabel("7 судья", self.frame_referee)

        self.frame_bottom = QtWidgets.QFrame(self.Form11)
        self.frame_left = QtWidgets.QFrame(self.Form11)
        self.frame_right = QtWidgets.QFrame(self.Form11)

        self.pers_com_qbx_style_1 = css.pers_com_qbx_style_1

        self.btn_style_1 = css.btn_style_1

        self.btn_style_2 = css.btn_style_2

        self.LEdit_style_referee = css.LEdit_style_referee
        self.LEdit_style_1 = css.LEdit_style_1

        self.combo_style_2 = css.combo_style_2

        self.label_style_1 = css.label_style_1

        self.font_l_10 = css.font_l_10
        self.font_l_12 = css.font_l_12
        self.font_l_13 = css.font_l_13
        self.font_m_13 = css.font_m_13
        self.font_b_13 = css.font_b_13
        self.font_l_16 = css.font_l_16
        self.font_l_20 = css.font_l_20
        self.font_m_20 = css.font_m_20
        self.font_b_20 = css.font_b_20
        self.font_m_33 = css.font_m_33
        self.font_b_40 = css.font_b_40

        self.frame_paytnov_file_save_status = QtWidgets.QFrame(self.frame_matchName)
        self.pfss_pixmap = QtGui.QPixmap(':/Images/pfss_pixmap_save.svg')
        self.pfss_pixmap2 = self.pfss_pixmap.scaled(15, 15, QtCore.Qt.KeepAspectRatio)
        self.pfss_pixmap_label = QLabel(self.frame_paytnov_file_save_status)
        self.pfss_pixmap_label.setGeometry(QtCore.QRect(0, 0, 15, 15))
        self.pfss_pixmap_label.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.pfss_pixmap_label.setPixmap(self.pfss_pixmap2)
        self.pfss_pair_name = QtWidgets.QLabel("Иванов - Петров", self.frame_paytnov_file_save_status)
        self.pfss_status = QtWidgets.QLabel("Сохранение в файл...", self.frame_paytnov_file_save_status)

        self.btn_refresh_display_position = QtWidgets.QPushButton(self.Form11)
        self.btn_refresh_display_position.setGeometry(QtCore.QRect(855, 5, 10, 10))
        self.btn_refresh_display_position.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_refresh_display_position.setToolTip("Обновить позицию окон")
        self.btn_refresh_display_position.setStyleSheet(css.btn_refresh_display_position)

        self.frame_overlay_status = QtWidgets.QFrame(self.Form11)
        self.img_overlay_offline = QtGui.QPixmap(":/Images/overlay_offline.svg")
        self.img_overlay_online = QtGui.QPixmap(":/Images/overlay_online.svg")
        self.img_overlay_no_data = QtGui.QPixmap(":/Images/overlay_no_data.svg")
        self.label_img_overlay_offline = QtWidgets.QLabel(self.frame_overlay_status)
        self.label_img_overlay_online = QtWidgets.QLabel(self.frame_overlay_status)
        self.label_img_overlay_no_data = QtWidgets.QLabel(self.frame_overlay_status)

        self.frame_sportsmans_load_status = QtWidgets.QFrame(self.Form11)
        self.img_sportsmans_not_loaded = QtGui.QPixmap(":/Images/sportsmans_not_loaded.svg")
        self.img_spotrsmans_uploaded = QtGui.QPixmap(":/Images/spotrsmans_uploaded.svg")
        self.label_img_sportsmans_not_loaded = QtWidgets.QLabel(self.frame_sportsmans_load_status)
        self.label_img_spotrsmans_uploaded = QtWidgets.QLabel(self.frame_sportsmans_load_status)

        self.frame_paytnov_file_save_status.hide()
        self.frame_paytnov_file_save_status.setGeometry(QtCore.QRect(0, 55, 500, 15))
        self.frame_paytnov_file_save_status.setStyleSheet("background-color: none;")
        self.pfss_pair_name.setGeometry(QtCore.QRect(23, 0, 295, 15))
        self.pfss_pair_name.setFont(self.font_l_10)
        self.pfss_pair_name.setAlignment(QtCore.Qt.AlignLeft)
        self.pfss_status.setGeometry(QtCore.QRect(320, 0, 180, 15))
        self.pfss_status.setFont(self.font_l_10)
        self.pfss_status.setAlignment(QtCore.Qt.AlignLeft)
        self.pfss_status.setStyleSheet("color: grey;")

        self.frame_bottom.setGeometry(QtCore.QRect(0, 499, 900, 1))
        self.frame_bottom.setStyleSheet("background-color: grey;")
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 1, 500))
        self.frame_left.setStyleSheet("background-color: grey;")
        self.frame_left.setObjectName("frame_left")
        self.frame_right.setGeometry(QtCore.QRect(899, 0, 1, 500))
        self.frame_right.setStyleSheet("background-color: grey;")
        self.frame_right.setObjectName("frame_right")

        self.frame_matchName.setGeometry(QtCore.QRect(200, 0, 500, 70))
        self.frame_matchName.setObjectName("matchName")

        self.label_matchName1.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_matchName1.setFont(self.font_l_20)
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.matchName1.setGeometry(QtCore.QRect(0, 25, 500, 30))
        self.matchName1.setStyleSheet(self.LEdit_style_1)
        self.matchName1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.matchName1.setObjectName("matchName1")

        self.frame_pyatnov.setGeometry(QtCore.QRect(0, 420, 900, 95))
        self.frame_pyatnov.setStyleSheet("background-color: none;")
        self.frame_pyatnov.setObjectName("frame_pyatnov")

        self.pyatnov_label.setGeometry(QtCore.QRect(40, 35, 150, 25))
        self.pyatnov_label.setFont(self.font_l_13)
        self.pyatnov_label.setStyleSheet("color: grey;")
        self.pyatnov_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pyatnov_label.setObjectName("pyatnov_label")

        self.pyatnov_name.setEnabled(False)
        self.pyatnov_name.setGeometry(QtCore.QRect(200, 35, 390, 25))
        self.pyatnov_name.setFont(self.font_l_12)
        self.pyatnov_name.setObjectName("pyatnov_name")

        self.pyatnov_kata_label.setGeometry(QtCore.QRect(660, 35, 60, 25))
        self.pyatnov_kata_label.setFont(self.font_l_13)
        self.pyatnov_kata_label.setStyleSheet("color: grey;")
        self.pyatnov_kata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pyatnov_kata_label.setObjectName("pyatnov_kata_label")

        self.pyatnov_kata_name.setEnabled(False)
        self.pyatnov_kata_name.setGeometry(QtCore.QRect(720, 35, 160, 25))
        self.pyatnov_kata_name.setFont(self.font_l_12)
        self.pyatnov_kata_name.setObjectName("pyatnov_kata_name")

        self.btn_clearData.hide()
        self.btn_clearData.setGeometry(QtCore.QRect(710, 385, 170, 30))
        self.btn_clearData.setStyleSheet(self.btn_style_2)
        self.btn_clearData.setFont(self.font_l_16)
        # self.btn_clearData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
        #                                         "font-size: 16px;")
        self.btn_clearData.setObjectName("btn_clearData")

        self.btn_NewCategory.hide()
        self.btn_NewCategory.setGeometry(QtCore.QRect(780, 440, 100, 40))
        self.btn_NewCategory.setStyleSheet(self.btn_style_2)
        self.btn_NewCategory.setFont(self.font_l_13)
        # self.btn_NewCategory.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
        #                                           "font-size: 13px;")
        # self.btn_NewCategory.setObjectName("btn_NewCategory")

        self.btn_showData.setGeometry(QtCore.QRect(650, 330, 230, 45))
        self.btn_showData.setStyleSheet(self.btn_style_2)
        self.btn_showData.setFont(self.font_l_16)
        # self.btn_showData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Medium;"
        #                                        "font-size: 16px;")
        self.btn_showData.setObjectName("btn_showData")

        self.label_name_red_1.setGeometry(QtCore.QRect(360, 40, 405, 100))
        self.label_name_red_1.setFont(self.font_m_33)
        self.label_name_red_1.setStyleSheet("background-color: none; color: grey;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(360, 90, 405, 100))
        self.label_region_red_1.setFont(self.font_m_20)
        self.label_region_red_1.setStyleSheet("background-color: none; color: grey;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 440, 900, 60))
        self.frame_sportsmans.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sportsmans.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sportsmans.setStyleSheet("background-color: none;")
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.pers_com_lbl.setGeometry(QtCore.QRect(88, 0, 7, 13))
        self.pers_com_lbl.setFont(self.font_b_13)
        self.pers_com_lbl.setStyleSheet("color: black;")
        self.pers_com_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pers_com_lbl.setObjectName("pers_com_lbl")

        self.pers_lbl.setGeometry(QtCore.QRect(7, 0, 80, 13))
        self.pers_lbl.setFont(self.font_b_13)
        self.pers_lbl.setStyleSheet("color: black;")
        self.pers_lbl.setAlignment(QtCore.Qt.AlignRight)
        self.pers_lbl.setObjectName("pers_lbl")

        self.com_lbl.setGeometry(QtCore.QRect(96, 0, 80, 13))
        self.com_lbl.setFont(self.font_l_13)
        self.com_lbl.setStyleSheet("color: grey;")
        self.com_lbl.setAlignment(QtCore.Qt.AlignLeft)
        self.com_lbl.setObjectName("com_lbl")

        self.pers_com_qbx.setGeometry(QtCore.QRect(65, 20, 50, 25))
        self.pers_com_qbx.setStyleSheet(self.pers_com_qbx_style_1)
        self.pers_com_qbx.setObjectName("pers_com_lbl")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(380, 20, 111, 25))
        self.comboBox_age.setFont(self.font_l_13)
        self.comboBox_age.setObjectName("comboBox_age")

        self.frame_sex.setGeometry(QtCore.QRect(200, 20, 150, 25))
        self.frame_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sex.setObjectName("frame_sex")

        self.male.setGeometry(QtCore.QRect(20, 0, 40, 25))
        self.male.setFont(self.font_b_20)
        self.male.setObjectName("male")

        self.female.setGeometry(QtCore.QRect(90, 0, 40, 25))
        self.female.setFont(self.font_b_20)
        self.female.setObjectName("female")

        self.sex_1.setGeometry(QtCore.QRect(200, 0, 150, 13))
        self.sex_1.setFont(self.font_b_13)
        self.sex_1.setStyleSheet("color: black;")
        self.sex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_1.setObjectName("sex_1")

        self.age_1.setGeometry(QtCore.QRect(380, 0, 110, 13))
        self.age_1.setFont(self.font_l_13)
        self.age_1.setStyleSheet("color: grey;")
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(510, 20, 350, 25))
        self.comboBox_name_red_1.setFont(self.font_l_13)
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.name_red_1.setGeometry(QtCore.QRect(510, 0, 350, 16))
        self.name_red_1.setFont(self.font_l_13)
        self.name_red_1.setStyleSheet("color: grey;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(280, 350, 340, 30))
        self.lineEdit_name_red_1.setStyleSheet(self.LEdit_style_1)
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(300, 400, 300, 25))
        # self.lineEdit_region_red_1.setStyleSheet(self.LEdit_style_1)
        # self.lineEdit_region_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        # self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")
        self.lineEdit_region_red_1.setStyleSheet(self.combo_style_2)
        self.lineEdit_region_red_1.setFont(self.font_l_13)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        self.Calc_Button.setGeometry(QtCore.QRect(60, 330, 170, 45))
        self.Calc_Button.setStyleSheet(self.btn_style_1)
        self.Calc_Button.setFont(self.font_m_20)
        self.Calc_Button.setObjectName("Calc_Button")

        self.Clear_Button.setGeometry(QtCore.QRect(90, 385, 110, 30))
        self.Clear_Button.setStyleSheet(self.btn_style_1)
        self.Clear_Button.setFont(self.font_l_16)
        self.Clear_Button.setObjectName("Clear_Button")

        self.heading_sum.setGeometry(QtCore.QRect(0, 60, 300, 20))
        self.heading_sum.setFont(self.font_m_13)
        self.heading_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_sum.setObjectName("heading_sum")

        self.label_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum.setGeometry(QtCore.QRect(0, 80, 300, 130))
        self.label_sum.setFont(self.font_l_20)
        self.label_sum.setStyleSheet("background-color: None; color: grey;")
        self.label_sum.setObjectName("label_sum")

        self.referee_point.setGeometry(QtCore.QRect(300, 180, 300, 50))
        self.referee_point.setAlignment(QtCore.Qt.AlignCenter)
        self.referee_point.setFont(self.font_b_40)
        self.referee_point.setObjectName("referee_point")

        self.label_help.setGeometry(QtCore.QRect(335, 317, 250, 13))
        self.label_help.setFont(self.font_l_10)
        self.label_help.setStyleSheet("color: grey;")
        self.label_help.setObjectName("label_help")

        self.frame_referee.setGeometry(QtCore.QRect(0, 230, 900, 80))
        self.frame_referee.setStyleSheet("border: none;")

        self.lineEdit_referee1.setGeometry(QtCore.QRect(70, 20, 100, 60))
        self.lineEdit_referee1.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee1.setInputMask('9.9')
        self.lineEdit_referee1.setText(str('0.0'))
        self.lineEdit_referee1.setObjectName("lineEdit_referee1")

        self.lineEdit_referee2.setGeometry(QtCore.QRect(180, 20, 100, 60))
        self.lineEdit_referee2.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee2.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee2.setInputMask('9.9')
        self.lineEdit_referee2.setText(str('0.0'))
        self.lineEdit_referee2.setObjectName("lineEdit_referee2")

        self.lineEdit_referee3.setGeometry(QtCore.QRect(290, 20, 100, 60))
        self.lineEdit_referee3.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee3.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee3.setInputMask('9.9')
        self.lineEdit_referee3.setText(str('0.0'))
        self.lineEdit_referee3.setObjectName("lineEdit_referee3")

        self.lineEdit_referee4.setGeometry(QtCore.QRect(400, 20, 100, 60))
        self.lineEdit_referee4.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee4.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee4.setInputMask('9.9')
        self.lineEdit_referee4.setText(str('0.0'))
        self.lineEdit_referee4.setObjectName("lineEdit_referee4")

        self.lineEdit_referee5.setGeometry(QtCore.QRect(510, 20, 100, 60))
        self.lineEdit_referee5.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee5.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee5.setInputMask('9.9')
        self.lineEdit_referee5.setText(str('0.0'))
        self.lineEdit_referee5.setObjectName("lineEdit_referee5")

        self.lineEdit_referee6.setGeometry(QtCore.QRect(620, 20, 100, 60))
        self.lineEdit_referee6.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee6.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee6.setInputMask('9.9')
        self.lineEdit_referee6.setText(str('0.0'))
        self.lineEdit_referee6.setObjectName("lineEdit_referee6")

        self.lineEdit_referee7.setGeometry(QtCore.QRect(730, 20, 100, 60))
        self.lineEdit_referee7.setStyleSheet(self.LEdit_style_referee)
        self.lineEdit_referee7.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee7.setInputMask('9.9')
        self.lineEdit_referee7.setText(str('0.0'))
        self.lineEdit_referee7.setObjectName("lineEdit_referee7")

        self.label_1.setGeometry(QtCore.QRect(70, 0, 100, 13))
        self.label_1.setFont(self.font_l_13)
        self.label_1.setStyleSheet("color: grey;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.label_2.setGeometry(QtCore.QRect(180, 0, 100, 13))
        self.label_2.setFont(self.font_l_13)
        self.label_2.setStyleSheet("color: grey;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(290, 0, 100, 13))
        self.label_3.setFont(self.font_l_13)
        self.label_3.setStyleSheet("color: grey;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(400, 0, 100, 13))
        self.label_4.setFont(self.font_l_13)
        self.label_4.setStyleSheet("color: grey;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(510, 0, 100, 13))
        self.label_5.setFont(self.font_l_13)
        self.label_5.setStyleSheet("color: grey;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6.setGeometry(QtCore.QRect(620, 0, 100, 13))
        self.label_6.setFont(self.font_l_13)
        self.label_6.setStyleSheet("color: grey;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7.setGeometry(QtCore.QRect(730, 0, 100, 13))
        self.label_7.setFont(self.font_l_13)
        self.label_7.setStyleSheet("color: grey;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        # self.comboBox_age.raise_()
        # self.frame_sex.raise_()
        # self.sex_1.raise_()
        # self.age_1.raise_()
        # self.comboBox_name_red_1.raise_()
        # self.name_red_1.raise_()

        QtCore.QMetaObject.connectSlotsByName(self.Form11)

        self.KataSecondWindow = KataSecondWindow()

        self.Frame_Header = Frame_Header(self)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(self.Frame_Header)
        self.layout2.addWidget(self.Form11, 1)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.setSpacing(0)

        self.frame_overlay_status.setGeometry(QtCore.QRect(870, 5, 15, 10))
        self.frame_overlay_status.setStyleSheet("background-color: none;")
        self.frame_overlay_status.setObjectName("overlay_status_label")

        self.label_img_overlay_offline.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_overlay_offline.setObjectName("label_img_overlay_offline")
        self.label_img_overlay_offline.setPixmap(self.img_overlay_offline)

        self.label_img_overlay_online.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_overlay_online.setObjectName("label_img_overlay_online")
        self.label_img_overlay_online.setPixmap(self.img_overlay_online)

        self.label_img_overlay_no_data.setGeometry(QtCore.QRect(0, 0, 15, 10))
        self.label_img_overlay_no_data.setObjectName("label_img_overlay_no_data")
        self.label_img_overlay_no_data.setPixmap(self.img_overlay_no_data)

        self.frame_sportsmans_load_status.setGeometry(QtCore.QRect(885, 5, 15, 10))
        self.frame_sportsmans_load_status.setStyleSheet("background-color: none;")
        self.frame_sportsmans_load_status.setObjectName("frame_sportsmans_load_status")

        self.label_img_sportsmans_not_loaded.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_sportsmans_not_loaded.setObjectName("label_img_sportsmans_not_loaded")
        self.label_img_sportsmans_not_loaded.setPixmap(self.img_sportsmans_not_loaded)

        self.label_img_spotrsmans_uploaded.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_spotrsmans_uploaded.setObjectName("label_img_spotrsmans_uploaded")
        self.label_img_spotrsmans_uploaded.setPixmap(self.img_spotrsmans_uploaded)

        self.label_img_spotrsmans_uploaded.hide()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.lineEdit_referee1.textChanged.connect(self.onChanged)
        self.lineEdit_referee2.textChanged.connect(self.onChanged)
        self.lineEdit_referee3.textChanged.connect(self.onChanged)
        self.lineEdit_referee4.textChanged.connect(self.onChanged)
        self.lineEdit_referee5.textChanged.connect(self.onChanged)
        self.lineEdit_referee6.textChanged.connect(self.onChanged)
        self.lineEdit_referee7.textChanged.connect(self.onChanged)

    def onChanged(self, text):
        # Новые оценки больше не должны выглядеть исключёнными из прошлой суммы.
        self.KataSecondWindow.reset_score_marks()
        sender = self.sender()
        if text == "0.":
            text = "0.0"
        elif text == "1.":
            text = "1.0"
        elif text == "2.":
            text = "2.0"
        elif text == "3.":
            text = "3.0"
        elif text == "4.":
            text = "4.0"
        elif text == "5.":
            text = "5.0"
        elif text == "6.":
            text = "6.0"
        elif text == "7.":
            text = "7.0"
        elif text == "8.":
            text = "8.0"
        elif text == "9.":
            text = "9.0"
        if text == ".":
            text = None
        else:
            if sender == self.lineEdit_referee1:
                self.KataSecondWindow.input_referee1.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee1.setText(text)
            elif sender == self.lineEdit_referee2:
                self.KataSecondWindow.input_referee2.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee2.setText(text)
            elif sender == self.lineEdit_referee3:
                self.KataSecondWindow.input_referee3.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee3.setText(text)
            elif sender == self.lineEdit_referee4:
                self.KataSecondWindow.input_referee4.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee4.setText(text)
            elif sender == self.lineEdit_referee5:
                self.KataSecondWindow.input_referee5.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee5.setText(text)
            elif sender == self.lineEdit_referee6:
                self.KataSecondWindow.input_referee6.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee6.setText(text)
            elif sender == self.lineEdit_referee7:
                self.KataSecondWindow.input_referee7.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
                self.KataSecondWindow.input_referee7.setText(text)
        self.isShowSportsmanName()

    def isShowSportsmanName(self):
        if not self.label_name_red_1.text() and not self.label_region_red_1.text() or \
                self.label_name_red_1.text() == "ФАМИЛИЯ" and self.label_region_red_1.text() == "регион":
            self.setSportsmanName()

    def calc_display_moveCoord(self, display_coord_x1, display_coord_y1, display_width, display_height,
                               display_coord_x1_secW, display_coord_y1_secW):
        try:
            self.KataSecondWindow = KataSecondWindow()
            self.KataSecondWindow.move(display_coord_x1_secW, display_coord_y1_secW)
            self.KataSecondWindow.show()
            self.show()
            coord_x1 = display_coord_x1 + (display_width - self.size().width())//2
            coord_y1 = display_coord_y1 + (display_height - self.size().height())//2
            self.move(coord_x1, coord_y1)
        except Exception as e:
            print('_______Exception calc_display_moveCoord:', e)

    def closeSecondWin(self):
        self.KataSecondWindow.close()
        self.close()

    def calcResult(self):
        self.KataSecondWindow.label_1.setText('1')
        self.KataSecondWindow.label_2.setText('2')
        self.KataSecondWindow.label_3.setText('3')
        self.KataSecondWindow.label_4.setText('4')
        self.KataSecondWindow.label_5.setText('5')
        self.KataSecondWindow.label_6.setText('6')
        self.KataSecondWindow.label_7.setText('7')

        q1 = self.lineEdit_referee1.text()
        q2 = self.lineEdit_referee2.text()
        q3 = self.lineEdit_referee3.text()
        q4 = self.lineEdit_referee4.text()
        q5 = self.lineEdit_referee5.text()
        q6 = self.lineEdit_referee6.text()
        q7 = self.lineEdit_referee7.text()

        l = [q1, q2, q3, q4, q5, q6, q7]
        e = []

        for n in l:
            if n == '.':
                e.append(0.0)
            else:
                e.append(n)
        l = e
        newlst = [float(x) for x in l]

        m = newlst
        m = [num for num in m if num != 0]
        m_tuple = tuple(newlst)

        if len(m) < 3:
            self.label_sum.setText('Введи оценки судей')
            self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light;"
                                         "color: red; font-size: 20px;")
            self.KataSecondWindow.label_sum2.setText('')
            return
        else:
            m.remove(max(m))
            m.remove(min(m))
            m1 = round(sum(m), 1)
            m2 = str(m1)
            self.label_sum.setText(m2)
            l1 = str(m_tuple[0])
            self.lineEdit_referee1.setText(l1)
            self.KataSecondWindow.label_sum2.setText(self.label_sum.text())

        n_tuple = list(m_tuple)
        for num in range(len(n_tuple)):
            if n_tuple[0] == 0.0:
                n_tuple[0] = ''
                self.KataSecondWindow.label_1.setText('')
            elif n_tuple[1] == 0.0:
                n_tuple[1] = ''
                self.KataSecondWindow.label_2.setText('')
            elif n_tuple[2] == 0.0:
                n_tuple[2] = ''
                self.KataSecondWindow.label_3.setText('')
            elif n_tuple[3] == 0.0:
                n_tuple[3] = ''
                self.KataSecondWindow.label_4.setText('')
            elif n_tuple[4] == 0.0:
                n_tuple[4] = ''
                self.KataSecondWindow.label_5.setText('')
            elif n_tuple[5] == 0.0:
                n_tuple[5] = ''
                self.KataSecondWindow.label_6.setText('')
            elif n_tuple[6] == 0.0:
                n_tuple[6] = ''
                self.KataSecondWindow.label_7.setText('')

        self.KataSecondWindow.input_referee1.setText(str(n_tuple[0]))
        self.KataSecondWindow.input_referee2.setText(str(n_tuple[1]))
        self.KataSecondWindow.input_referee3.setText(str(n_tuple[2]))
        self.KataSecondWindow.input_referee4.setText(str(n_tuple[3]))
        self.KataSecondWindow.input_referee5.setText(str(n_tuple[4]))
        self.KataSecondWindow.input_referee6.setText(str(n_tuple[5]))
        self.KataSecondWindow.input_referee7.setText(str(n_tuple[6]))
        self.label_sum.setStyleSheet('background-color: None; font-family: Gotham-Light;'
                                     'font-size: 120px; color: rgb(0, 178, 80);')
        self.labelStyle(self.KataSecondWindow.input_referee1)
        self.labelStyle(self.KataSecondWindow.input_referee2)
        self.labelStyle(self.KataSecondWindow.input_referee3)
        self.labelStyle(self.KataSecondWindow.input_referee4)
        self.labelStyle(self.KataSecondWindow.input_referee5)
        self.labelStyle(self.KataSecondWindow.input_referee6)
        self.labelStyle(self.KataSecondWindow.input_referee7)

        self.lineEdit_referee1.setText(str(n_tuple[0]))
        self.lineEdit_referee2.setText(str(n_tuple[1]))
        self.lineEdit_referee3.setText(str(n_tuple[2]))
        self.lineEdit_referee4.setText(str(n_tuple[3]))
        self.lineEdit_referee5.setText(str(n_tuple[4]))
        self.lineEdit_referee6.setText(str(n_tuple[5]))
        self.lineEdit_referee7.setText(str(n_tuple[6]))

        self.KataSecondWindow.Extream_Value()
        self.fiveReferee(n_tuple[5])

    def labelStyle(self, input_referee):
        input_referee.setStyleSheet(self.KataSecondWindow.SCORE_STYLE)
        font = input_referee.font()
        font.setStrikeOut(False)
        input_referee.setFont(font)

    def fiveReferee(self, tuple_five_referee_score):
        self.KataSecondWindow.set_judge_count(5 if tuple_five_referee_score == '' else 7)

    def clearKataData(self):
        self.label_sum.setText("Нажми кнопку\n«Рассчитать»")
        self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light; color: grey; font-size: 20px;")
        self.lineEdit_referee1.setText('0.0')
        self.lineEdit_referee2.setText('0.0')
        self.lineEdit_referee3.setText('0.0')
        self.lineEdit_referee4.setText('0.0')
        self.lineEdit_referee5.setText('0.0')
        self.lineEdit_referee6.setText('0.0')
        self.lineEdit_referee7.setText('0.0')

        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_region_red_1.setText("регион")
        self.lineEdit_name_red_1.clear()
        try:
            self.lineEdit_region_red_1.lineEdit().clear()
        except:
            self.lineEdit_region_red_1.clear()

        self.KataSecondWindow.label_sum2.setText('')
        self.KataSecondWindow.input_referee1.setText('')
        self.KataSecondWindow.input_referee2.setText('')
        self.KataSecondWindow.input_referee3.setText('')
        self.KataSecondWindow.input_referee4.setText('')
        self.KataSecondWindow.input_referee5.setText('')
        self.KataSecondWindow.input_referee6.setText('')
        self.KataSecondWindow.input_referee7.setText('')
        self.KataSecondWindow.label_1.setText('1')
        self.KataSecondWindow.label_2.setText('2')
        self.KataSecondWindow.label_3.setText('3')
        self.KataSecondWindow.label_4.setText('4')
        self.KataSecondWindow.label_5.setText('5')
        self.KataSecondWindow.label_6.setText('6')
        self.KataSecondWindow.label_7.setText('7')

        self.KataSecondWindow.set_athlete('ФАМИЛИЯ', 'регион', '')
        self.KataSecondWindow.reset_score_marks()
        self.KataSecondWindow.set_judge_count(7)

    def setMatchName(self):
        text = self.matchName1.text().strip()
        # Обычно татами уже входит в matchName1 (Excel и ручной ввод).
        # Начальный экран тоже должен показывать номер, без дублирования.
        if 'татами' not in text.lower():
            text = f'Татами №{self.USKO_PC}, ' + text
        self.KataSecondWindow.fit_label(self.KataSecondWindow.matchName2, text,
                                       'Gotham-Medium', 66, 'grey')

    def setSportsmanName(self):
        self.setMatchName()
        name = self.lineEdit_name_red_1.text()
        region = self.lineEdit_region_red_1.currentText()
        self.label_name_red_1.setText(name)
        self.label_region_red_1.setText(region)
        # Используем тот же справочник и нормализацию, что у трансляции.
        key = region.split(' - ком')[0].replace(' ', '').lower()
        code = getattr(self, 'flags_dict', {}).get(key, '')
        self.KataSecondWindow.set_athlete(name, region, code)
