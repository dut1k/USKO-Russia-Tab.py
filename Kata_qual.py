from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
import styleCSS as css


class KataQual_SecondWindow_Ui(object):
    def setupUi2(self, Form22):
        Form22.setObjectName("Form22")
        Form22.setEnabled(True)
        Form22.setFixedSize(1920, 1080)
        Form22.setWindowOpacity(1.0)
        Form22.setStyleSheet("background-color: white;")
        Form22.setWindowIcon(QtGui.QIcon(':/Images/Empty.png'))

        self.line2 = QtWidgets.QFrame(Form22)
        self.matchName2 = QtWidgets.QLabel(Form22)

        self.frame_white2 = QtWidgets.QFrame(Form22)
        self.label_winner_white_2 = QtWidgets.QLabel(self.frame_white2)
        self.background_white21 = QtWidgets.QFrame(self.frame_white2)
        self.background_white22 = QtWidgets.QFrame(self.frame_white2)
        self.label_name_white_2 = QtWidgets.QLabel(self.frame_white2)
        self.label_region_white_2 = QtWidgets.QLabel(self.frame_white2)

        self.frame_red2 = QtWidgets.QFrame(Form22)
        self.label_winner_red_2 = QtWidgets.QLabel(self.frame_red2)
        self.background_red21 = QtWidgets.QFrame(self.frame_red2)
        self.background_red22 = QtWidgets.QFrame(self.frame_red2)
        self.label_name_red_2 = QtWidgets.QLabel(self.frame_red2)
        self.label_region_red_2 = QtWidgets.QLabel(self.frame_red2)

        self.label_winner = QtWidgets.QLabel(Form22)

        self.matchName2.setGeometry(QtCore.QRect(20, 10, 1880, 100))
        self.matchName2.setStyleSheet("font-family: Gotham-Medium; font-size: 100px; color: grey;")
        self.matchName2.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName2.setObjectName("matchName2")

        self.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.frame_white2.setStyleSheet("background-color: None;")
        self.frame_white2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white2.setObjectName("frame_white2")

        self.label_winner_white_2.hide()
        self.label_winner_white_2.setGeometry(QtCore.QRect(0, 0, 300, 60))
        self.label_winner_white_2.setStyleSheet("font-family: Gotham-Medium; font-size: 65px;")
        self.label_winner_white_2.setObjectName("label_winner_white_2")

        self.background_white21.setGeometry(QtCore.QRect(0, 0, 1840, 280))
        self.background_white21.setStyleSheet("background-color: None; border-top-left-radius: 15px;"
                                              "border-top-right-radius: 15px; border: 2px solid grey")
        self.background_white21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white21.setObjectName("background_white21")

        self.background_white22.setGeometry(QtCore.QRect(0, 250, 1840, 150))
        self.background_white22.setStyleSheet("background-color: white; border-radius: 15px;"
                                              "border: 2px solid grey")
        self.background_white22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white22.setObjectName("background_white22")

        self.label_name_white_2.setGeometry(QtCore.QRect(20, 0, 1800, 250))
        self.label_name_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; font-size: 250px; ")
        self.label_name_white_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_white_2.setObjectName("label_name_white_2")

        self.label_region_white_2.setGeometry(QtCore.QRect(20, 250, 1800, 150))
        self.label_region_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px; ")
        self.label_region_white_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_2.setObjectName("label_region_white_2")

        self.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.frame_red2.setStyleSheet("background-color: None; ")
        self.frame_red2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red2.setObjectName("frame_red2")

        self.label_winner_red_2.hide()
        self.label_winner_red_2.setGeometry(QtCore.QRect(0, 0, 300, 60))
        self.label_winner_red_2.setStyleSheet("font-family: Gotham-Medium; color: white; font-size: 65px;")
        self.label_winner_red_2.setObjectName("label_winner_red_2")

        self.background_red21.setGeometry(QtCore.QRect(0, 0, 1840, 280))
        self.background_red21.setStyleSheet("background-color: rgb(255, 95, 95); border-top-left-radius: 15px;"
                                            "border-top-right-radius: 15px; border: 2px solid grey")
        self.background_red21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red21.setObjectName("background_red21")

        self.background_red22.setGeometry(QtCore.QRect(0, 250, 1840, 150))
        self.background_red22.setStyleSheet("background-color: white; border-radius: 15px;"
                                            "border: 2px solid grey")
        self.background_red22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red22.setObjectName("background_red22")

        self.label_name_red_2.setGeometry(QtCore.QRect(20, 0, 1800, 250))
        self.label_name_red_2.setStyleSheet(
            "background-color: none; color: white; font-family: Gotham-Bold; font-size: 250px; ")
        self.label_name_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_2.setObjectName("label_name_red_2")

        self.label_region_red_2.setGeometry(QtCore.QRect(20, 250, 1800, 150))
        self.label_region_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px; ")
        self.label_region_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_2.setObjectName("label_region_red_2")

        self.label_winner.hide()
        self.label_winner.setGeometry(QtCore.QRect(0, 150, 1920, 200))
        self.label_winner.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px; ")
        self.label_winner.setAlignment(QtCore.Qt.AlignCenter)
        self.label_winner.setObjectName("label_winner")

        self.frame_red2.raise_()
        self.frame_white2.raise_()
        self.line2.raise_()
        self.matchName2.raise_()
        self.label_winner.raise_()

        self.retranslateUi(Form22)
        QtCore.QMetaObject.connectSlotsByName(Form22)

    def retranslateUi(self, Form22):
        _translate = QtCore.QCoreApplication.translate
        Form22.setWindowTitle(_translate("Form22", " "))
        self.matchName2.setText(_translate("Form22", "Татами №#, Возраст"))
        self.label_name_white_2.setText(_translate("Form22", ""))
        self.label_region_white_2.setText(_translate("Form22", ""))
        self.label_region_red_2.setText(_translate("Form22", ""))
        self.label_name_red_2.setText(_translate("Form22", ""))
        self.label_winner.setText(_translate("Form22", "ПОБЕДИТЕЛЬ"))


class KataQual_SecondWindow(QWidget, KataQual_SecondWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)


class Frame_Header(QWidget):
    def __init__(self, parent):
        super(Frame_Header, self).__init__()
        self.parent = parent

        self.btn_style_header = css.btn_style_header

        self.font_l_13 = QtGui.QFont()
        self.font_l_13.setFamily("Gotham-Light")
        self.font_l_13.setPixelSize(13)

        self.font_l_22 = QtGui.QFont()
        self.font_l_22.setFamily("Gotham-Light")
        self.font_l_22.setPixelSize(22)

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

        self.label_windowsTitle = QLabel("КАТА ГО ХАКУ. Судейское окно", self.frame_title)
        self.label_windowsTitle.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.label_windowsTitle.move(30, 9)

        self.frame_combo = QtWidgets.QFrame(self)
        self.frame_combo.setGeometry(QtCore.QRect(0, 0, 153, 31))

        self.frame_combo_border = QtWidgets.QFrame(self.frame_combo)
        self.frame_combo_border.setStyleSheet("background-color: grey;")
        self.frame_combo_border.setGeometry(QtCore.QRect(0, 0, 200, 1))

        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.combo.setGeometry(0, 4, 147, 24)
        self.combo.addItems(["Главное меню", "Ката финал", "Кумите"])
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


class KataQual_MainWindow_Ui(QWidget):
    def __init__(self):
        super(KataQual_MainWindow_Ui, self).__init__()
        QWidget.setWindowTitle(self, "Ката го хаку. Судейское окно")

        self.Form21 = QtWidgets.QFrame(self)
        self.Form21.setFixedSize(900, 530)
        self.Form21.setStyleSheet("background-color: white;")

        self.frame_matchName = QtWidgets.QFrame(self.Form21)
        self.label_matchName1 = QtWidgets.QLabel('<b>Заголовок</b>', self.frame_matchName)
        self.matchName1 = QtWidgets.QLineEdit("Татами №#, Возраст", self.frame_matchName)
        self.btn_clearData = QtWidgets.QPushButton("ОЧИСТИТЬ\nДАННЫЕ", self.Form21)
        self.btn_NewCategory = QtWidgets.QPushButton("НОВАЯ\nКАТЕГОРИЯ", self.Form21)
        self.btn_showData = QtWidgets.QPushButton("ПОКАЗАТЬ\nНА ЭКРАНЕ", self.Form21)

        self.frame_red1 = QtWidgets.QFrame(self.Form21)
        self.label_name_red_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.frame_red1)
        self.label_region_red_1 = QtWidgets.QLabel("регион", self.frame_red1)
        self.frame_white1 = QtWidgets.QFrame(self.Form21)
        self.label_name_white_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.frame_white1)
        self.label_region_white_1 = QtWidgets.QLabel("регион", self.frame_white1)

        self.frame_sportsmans = QtWidgets.QFrame(self.Form21)

        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.male = QtWidgets.QRadioButton("М", self.frame_sex)
        self.female = QtWidgets.QRadioButton("Ж", self.frame_sex)
        self.sex_1 = QtWidgets.QLabel("Пол", self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel("Возраст", self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.comboBox_name_white_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)
        self.name_white_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)
        self.horizon_line_red = QtWidgets.QFrame(self.frame_red1)
        self.horizon_line_white = QtWidgets.QFrame(self.frame_white1)
        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(self.frame_red1, placeholderText="АКА. Введите имя спортсмена")
        self.lineEdit_name_white_1 = QtWidgets.QLineEdit(self.frame_white1,
                                                         placeholderText="СИРО. Введите имя спортсмена")
        self.lineEdit_region_red_1 = QtWidgets.QComboBox(self.frame_red1)
        self.lineEdit_region_white_1 = QtWidgets.QComboBox(self.frame_white1)
        self.frame_winner = QtWidgets.QFrame(self.Form21)
        self.winnerRed = QtWidgets.QRadioButton("Победил АКА", self.frame_winner)
        self.winnerWhite = QtWidgets.QRadioButton("Победил СИРО", self.frame_winner)

        self.frame_pyatnov = QtWidgets.QFrame(self.Form21)

        self.pyatnov_label = QtWidgets.QLabel("Выберите пару", self.frame_pyatnov)
        self.pyatnov_name = QtWidgets.QComboBox(self.frame_pyatnov)

        self.btn_style_1 = css.btn_style_1

        self.btn_style_2 = css.btn_style_2

        self.LEdit_style_1 = css.LEdit_style_1

        self.combo_style_2 = css.combo_style_2

        self.font_l_12 = css.font_l_12

        self.font_l_13 = css.font_l_13

        self.font_m_13 = css.font_m_13

        self.font_l_20 = css.font_l_20

        self.frame_bottom = QtWidgets.QFrame(self.Form21)
        self.frame_left = QtWidgets.QFrame(self.Form21)
        self.frame_right = QtWidgets.QFrame(self.Form21)

        self.frame_bottom.setGeometry(QtCore.QRect(0, 529, 900, 1))
        self.frame_bottom.setStyleSheet("background-color: grey;")
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 1, 530))
        self.frame_left.setStyleSheet("background-color: grey;")
        self.frame_left.setObjectName("frame_left")
        self.frame_right.setGeometry(QtCore.QRect(899, 0, 1, 530))
        self.frame_right.setStyleSheet("background-color: grey;")
        self.frame_right.setObjectName("frame_right")

        self.frame_matchName.setGeometry(QtCore.QRect(200, 0, 500, 70))
        self.frame_matchName.setObjectName("matchName")

        self.label_matchName1.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_matchName1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.matchName1.setGeometry(QtCore.QRect(0, 25, 500, 30))
        self.matchName1.setStyleSheet(self.LEdit_style_1)
        self.matchName1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.matchName1.setObjectName("matchName1")

        self.frame_red1.setGeometry(QtCore.QRect(465, 90, 400, 250))
        self.frame_red1.setStyleSheet("background-color: #FF4546; border-radius: 15px;")
        self.frame_red1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red1.setObjectName("frame_red1")

        self.label_name_red_1.setGeometry(QtCore.QRect(25, 50, 350, 40))
        self.label_name_red_1.setStyleSheet("font-family: Gotham-Medium; color: white; font-size: 33px;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(75, 100, 250, 40))
        self.label_region_red_1.setStyleSheet("font-family: Gotham-Medium; color: white; font-size: 13px;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.frame_white1.setGeometry(QtCore.QRect(35, 90, 400, 250))
        self.frame_white1.setStyleSheet("background-color: none; border-radius: 15px; border: 1px solid grey;")
        self.frame_white1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white1.setObjectName("frame_white1")

        self.label_name_white_1.setGeometry(QtCore.QRect(25, 50, 350, 40))
        self.label_name_white_1.setStyleSheet("font-family: Gotham-Medium; color: grey; font-size: 33px; border: none;")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_white_1.setObjectName("label_name_white_1")

        self.label_region_white_1.setGeometry(QtCore.QRect(75, 100, 250, 40))
        self.label_region_white_1.setStyleSheet(
            "font-family: Gotham-Medium; color: grey; font-size: 13px; border: none;")
        self.label_region_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setObjectName("label_region_white_1")

        self.btn_clearData.setGeometry(QtCore.QRect(530, 360, 120, 50))
        self.btn_clearData.setStyleSheet(self.btn_style_1)
        self.btn_clearData.setFont(self.font_m_13)
        self.btn_clearData.setObjectName("btn_clearData")

        self.btn_NewCategory.setGeometry(QtCore.QRect(775, 365, 100, 45))
        self.btn_NewCategory.setStyleSheet(self.btn_style_1)
        self.btn_NewCategory.setFont(self.font_m_13)
        self.btn_NewCategory.setObjectName("btn_NewCategory")

        self.btn_showData.setGeometry(QtCore.QRect(390, 360, 120, 50))
        self.btn_showData.setStyleSheet(self.btn_style_1)
        self.btn_showData.setFont(self.font_m_13)
        self.btn_showData.setToolTip('Показать номер татами, ФИО и регион')

        self.btn_showData.setObjectName("btn_showData")

        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 420, 900, 95))
        self.frame_sportsmans.setStyleSheet("background-color: none;")
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.frame_sex.setGeometry(QtCore.QRect(270, 20, 151, 25))
        self.frame_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sex.setObjectName("frame_sex")

        self.male.setGeometry(QtCore.QRect(20, 0, 40, 25))
        self.male.setStyleSheet("font-family: Gotham-Medium; font-size: 20px;")
        self.male.setObjectName("male")

        self.female.setGeometry(QtCore.QRect(90, 0, 40, 25))
        self.female.setStyleSheet("font-family: Gotham-Medium; font-size: 20px;")
        self.female.setObjectName("female")

        self.sex_1.setGeometry(QtCore.QRect(330, 0, 50, 13))
        self.sex_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 13px;")
        self.sex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_1.setObjectName("sex_1")

        self.age_1.setGeometry(QtCore.QRect(490, 0, 110, 13))
        self.age_1.setStyleSheet("color: grey;")
        self.age_1.setFont(self.font_l_13)
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(490, 20, 110, 22))
        self.comboBox_age.setFont(self.font_l_13)
        self.comboBox_age.setObjectName("comboBox_age")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(470, 70, 390, 25))
        self.comboBox_name_red_1.setFont(self.font_l_12)
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.comboBox_name_white_1.setEnabled(False)
        self.comboBox_name_white_1.setGeometry(QtCore.QRect(40, 70, 390, 25))
        self.comboBox_name_white_1.setFont(self.font_l_12)
        self.comboBox_name_white_1.setObjectName("comboBox_name_white_1")

        self.name_red_1.setGeometry(QtCore.QRect(470, 50, 390, 16))
        self.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.name_white_1.setGeometry(QtCore.QRect(40, 50, 390, 16))
        self.name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_white_1.setObjectName("name_white_1")

        self.horizon_line_red.setGeometry(QtCore.QRect(10, 150, 380, 1))
        self.horizon_line_red.setStyleSheet("background-color: white;")

        self.horizon_line_white.setGeometry(QtCore.QRect(10, 150, 380, 1))
        self.horizon_line_white.setStyleSheet("background-color: grey;")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(30, 170, 340, 30))
        self.lineEdit_name_red_1.setStyleSheet(self.LEdit_style_1)
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(50, 210, 300, 30))
        self.lineEdit_region_red_1.setStyleSheet(self.combo_style_2)
        self.lineEdit_region_red_1.setFont(self.font_l_13)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        self.lineEdit_name_white_1.setGeometry(QtCore.QRect(30, 170, 340, 30))
        self.lineEdit_name_white_1.setStyleSheet(self.LEdit_style_1)
        self.lineEdit_name_white_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_white_1.setObjectName("lineEdit_name_white_1")

        self.lineEdit_region_white_1.setGeometry(QtCore.QRect(50, 210, 300, 30))
        self.lineEdit_region_white_1.setStyleSheet(self.combo_style_2)
        self.lineEdit_region_white_1.setFont(self.font_l_13)
        self.lineEdit_region_white_1.setObjectName("lineEdit_region_white_1")

        self.frame_winner.setGeometry(QtCore.QRect(145, 100, 610, 25))
        self.frame_winner.setStyleSheet("background-color: none")
        self.frame_winner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_winner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_winner.setObjectName("frame_winner")

        self.winnerRed.setGeometry(QtCore.QRect(435, 0, 200, 25))
        self.winnerRed.setStyleSheet("color: white; font-family: Gotham-Light; font-size: 20px;")
        self.winnerRed.setObjectName("winnerRed")

        self.winnerWhite.setGeometry(QtCore.QRect(0, 0, 200, 25))
        self.winnerWhite.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerWhite.setObjectName("winnerWhite")

        self.frame_pyatnov.setGeometry(QtCore.QRect(0, 420, 900, 95))
        self.frame_pyatnov.setStyleSheet("background-color: none;")
        self.frame_pyatnov.setObjectName("frame_pyatnov")

        self.pyatnov_name.setEnabled(False)
        self.pyatnov_name.setGeometry(QtCore.QRect(270, 35, 390, 25))
        self.pyatnov_name.setFont(self.font_l_12)
        self.pyatnov_name.setObjectName("pyatnov_name")

        self.pyatnov_label.setGeometry(QtCore.QRect(150, 35, 110, 25))
        self.pyatnov_label.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.pyatnov_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pyatnov_label.setObjectName("pyatnov_label")

        self.KataQual_SecondWindow = KataQual_SecondWindow()

        self.Frame_Header = Frame_Header(self)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(self.Frame_Header)
        self.layout2.addWidget(self.Form21, 1)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint)

    def calc_display_moveCoord(self, display_coord_x1, display_coord_y1, display_width, display_height,
                               display_coord_x1_secW, display_coord_y1_secW):
        self.KataQual_SecondWindow.move(display_coord_x1_secW, display_coord_y1_secW)
        self.KataQual_SecondWindow.show()
        self.show()
        self.calc_display_move(display_coord_x1, display_coord_y1, display_width, display_height)
        # coord_x1 = display_coord_x1 + (display_width - self.size().width())//2
        # coord_y1 = display_coord_y1 + (display_height - self.size().height())//2
        # self.move(coord_x1, coord_y1)

    def calc_display_move(self, display_coord_x1, display_coord_y1, display_width, display_height):
        try:
            coord_x1 = display_coord_x1 + (display_width - self.size().width()) // 2
            coord_y1 = display_coord_y1 + (display_height - self.size().height()) // 2
            self.move(coord_x1, coord_y1)
        except Exception as e:
            print('calc_display_move  ', e)

    def closeSecondWin(self):
        self.KataQual_SecondWindow.close()
        self.close()

    def clearKataData(self):
        self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(
            "background-color: none; color: white; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_name_white_2.clear()
        self.KataQual_SecondWindow.label_region_white_2.clear()
        self.KataQual_SecondWindow.label_region_red_2.clear()
        self.KataQual_SecondWindow.label_name_red_2.clear()
        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setText("регион")
        self.label_name_white_1.setText("ФАМИЛИЯ")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setText("регион")
        self.lineEdit_name_red_1.clear()
        self.lineEdit_name_white_1.clear()
        try:
            self.lineEdit_region_red_1.lineEdit().clear()
            self.lineEdit_region_white_1.lineEdit().clear()
        except:
            self.lineEdit_region_red_1.clear()
            self.lineEdit_region_white_1.clear()
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.label_winner.hide()

    def NewCategory(self):
        self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(
            "background-color: none; color: white; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_name_white_2.clear()
        self.KataQual_SecondWindow.label_region_white_2.clear()
        self.KataQual_SecondWindow.label_region_red_2.clear()
        self.KataQual_SecondWindow.label_name_red_2.clear()
        self.KataQual_SecondWindow.matchName2.setText(self.matchName1.text())
        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setText("регион")
        self.label_name_white_1.setText("ФАМИЛИЯ")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setText("регион")
        self.comboBox_age.clear()
        self.comboBox_name_red_1.clear()
        self.comboBox_name_white_1.clear()
        self.comboBox_age.setEnabled(False)
        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_white_1.setEnabled(False)
        self.male.setAutoExclusive(False)
        self.female.setAutoExclusive(False)
        self.male.setChecked(False)
        self.female.setChecked(False)
        self.male.setAutoExclusive(True)
        self.female.setAutoExclusive(True)
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)
        self.age_1.setStyleSheet("color: grey;")
        self.age_1.setFont(self.font_l_13)
        self.name_red_1.setStyleSheet("color: grey;")
        self.name_red_1.setFont(self.font_l_13)
        self.name_white_1.setStyleSheet("color: grey;")
        self.name_white_1.setFont(self.font_l_13)
        self.lineEdit_name_red_1.setText('')
        self.lineEdit_name_white_1.setText('')
        try:
            self.lineEdit_region_red_1.lineEdit().clear()
            self.lineEdit_region_white_1.lineEdit().clear()
        except:
            self.lineEdit_region_red_1.clear()
            self.lineEdit_region_white_1.clear()
        self.lineEdit_name_red_1.setPlaceholderText("АКА. Введите имя спортсмена")
        self.lineEdit_name_white_1.setPlaceholderText("СИРО. Введите имя спортсмена")
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.label_winner.hide()

    def setMatchName(self):
        matchName1_width = self.matchName1.fontMetrics().boundingRect(self.matchName1.text()).width()

        if matchName1_width > 356:
            n = "font-family: Gotham-Medium; font-size: "\
                + str(int(17.8 * (1880 / matchName1_width))) + "px; color: grey;"
            self.KataQual_SecondWindow.matchName2.setStyleSheet(n)
        else:
            self.KataQual_SecondWindow.matchName2.setStyleSheet(
                "font-family: Gotham-Medium; font-size: 100px; color: grey;")
        self.KataQual_SecondWindow.matchName2.setText(self.matchName1.text())

    def setSportsmanName(self):
        self.setMatchName()
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)
        self.label_name_red_1.setText(self.lineEdit_name_red_1.text())
        self.label_region_red_1.setText(self.lineEdit_region_red_1.currentText())
        self.KataQual_SecondWindow.label_name_red_2.setText(self.lineEdit_name_red_1.text())
        self.KataQual_SecondWindow.label_region_red_2.setText(self.lineEdit_region_red_1.currentText())
        self.label_name_white_1.setText(self.lineEdit_name_white_1.text())
        self.label_region_white_1.setText(self.lineEdit_region_white_1.currentText())
        self.KataQual_SecondWindow.label_name_white_2.setText(self.lineEdit_name_white_1.text())
        self.KataQual_SecondWindow.label_region_white_2.setText(self.lineEdit_region_white_1.currentText())
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.label_winner.hide()
        # self.KataQual_SecondWindow.label_name_red_2.show()
        # self.KataQual_SecondWindow.label_region_red_2.show()
        # self.KataQual_SecondWindow.label_name_white_2.show()
        # self.KataQual_SecondWindow.label_region_white_2.show()

        first_window_name_red = self.label_name_red_1.fontMetrics().boundingRect(self.label_name_red_1.text()).width()
        first_window_region_red = self.label_region_red_1.fontMetrics(). \
            boundingRect(self.label_region_red_1.text()).width()

        first_window_name_white = self.label_name_white_1.fontMetrics().boundingRect(
            self.label_name_white_1.text()).width()
        first_window_region_white = self.label_region_white_1.fontMetrics().boundingRect(
            self.label_region_white_1.text()).width()

        if first_window_name_white > 237 or first_window_name_red > 237:
            max_value = max(first_window_name_white, first_window_name_red)
            nw = "font-family: Gotham-Medium; font-size: " + str(int(300 * (198 / max_value))) + "px;"
            nr = "color: white; font-family: Gotham-Medium; font-size: " + str(int(300 * (198 / max_value))) + "px;"

            self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(nw)
            self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(nr)
        else:
            self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(
                "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
            self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(
                "background-color: none; color: white; font-family: Gotham-Medium; font-size: 250px;")

        if first_window_region_white > 93 or first_window_region_red > 93:
            max_value = max(first_window_region_white, first_window_region_red)
            n = "font-family: Gotham-Light; font-size: " + str(int(150 * (155 / max_value))) + "px;"
            self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(n)
            self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(n)
        else:
            self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(
                "background-color: none; font-family: Gotham-Light; font-size: 150px;")
            self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(
                "background-color: none; font-family: Gotham-Light; font-size: 150px;")

    def setWinnerRed(self):
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 350, 1840, 400))
        self.KataQual_SecondWindow.label_winner.show()
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.hide()
        print("           setWinnerRed")

    def setWinnerWhite(self):
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 350, 1840, 400))
        self.KataQual_SecondWindow.label_winner.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.frame_red2.hide()
