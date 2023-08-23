from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class KataQual_SecondWindow_Ui(object):
    def setupUi2(self, Form22):
        Form22.setObjectName("Form22")
        Form22.setEnabled(True)
        Form22.resize(1920, 1080)
        Form22.setWindowOpacity(1.0)
        Form22.setStyleSheet("background-color: rgb(255, 255, 255);")

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

        self.label_name_white_2.setGeometry(QtCore.QRect(20, 0, 1800, 250))
        self.label_name_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; font-size: 250px; ")
        self.label_name_white_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_white_2.setObjectName("label_name_white_2")

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
        self.matchName2.setText(_translate("Form22", "Татами №# М/Ж - возраст"))
        self.label_name_white_2.setText(_translate("Form22", "ФАМИЛИЯ"))
        self.label_region_white_2.setText(_translate("Form22", "регион"))
        self.label_region_red_2.setText(_translate("Form22", "регион"))
        self.label_name_red_2.setText(_translate("Form22", "ФАМИЛИЯ"))
        self.label_winner.setText(_translate("Form22", "ПОБЕДИТЕЛЬ"))


class KataQual_SecondWindow(QWidget, KataQual_SecondWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)


class KataQual_MainWindow_Ui(object):
    def setupUi(self, Form21):
        Form21.setObjectName("Form21")
        Form21.setEnabled(True)
        Form21.setFixedSize(900, 500)
        Form21.setWindowOpacity(1.0)
        Form21.setToolTipDuration(-1)
        Form21.setStatusTip("")
        Form21.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.KumiteButton = QtWidgets.QPushButton(Form21)
        self.KataFinalButton = QtWidgets.QPushButton(Form21)
        self.MenuButton = QtWidgets.QPushButton(Form21)
        self.label_matchName1 = QtWidgets.QLabel(Form21)
        self.label_matchName2 = QtWidgets.QLabel(Form21)
        self.matchName1 = QtWidgets.QLineEdit(Form21)
        self.line1 = QtWidgets.QFrame(Form21)
        self.frame_red1 = QtWidgets.QFrame(Form21)
        self.label_name_red_1 = QtWidgets.QLabel(self.frame_red1)
        self.label_region_red_1 = QtWidgets.QLabel(self.frame_red1)
        self.frame_white1 = QtWidgets.QFrame(Form21)
        self.label_name_white_1 = QtWidgets.QLabel(self.frame_white1)
        self.label_region_white_1 = QtWidgets.QLabel(self.frame_white1)
        self.pushButton_clearData = QtWidgets.QPushButton(Form21)
        self.pushButton_NewCategory = QtWidgets.QPushButton(Form21)
        self.pushButton_showData = QtWidgets.QPushButton(Form21)

        self.frame_sportsmans = QtWidgets.QFrame(Form21)

        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.male = QtWidgets.QRadioButton(self.frame_sex)
        self.female = QtWidgets.QRadioButton(self.frame_sex)
        self.sex_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.comboBox_name_white_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.name_white_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(Form21)
        self.lineEdit_region_red_1 = QtWidgets.QLineEdit(Form21)
        self.lineEdit_name_white_1 = QtWidgets.QLineEdit(Form21)
        self.lineEdit_region_white_1 = QtWidgets.QLineEdit(Form21)
        self.frame_winner = QtWidgets.QFrame(Form21)
        self.winnerRed = QtWidgets.QRadioButton(self.frame_winner)
        self.winnerWhite = QtWidgets.QRadioButton(self.frame_winner)

        self.label_matchName1.setGeometry(QtCore.QRect(20, 0, 405, 15))
        self.label_matchName1.setStyleSheet("font-family: Gotham-Light; font-size: 13px;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.label_matchName2.setGeometry(QtCore.QRect(20, 45, 700, 15))
        self.label_matchName2.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_matchName2.setObjectName("label_matchName2")

        self.matchName1.setGeometry(QtCore.QRect(20, 15, 405, 30))
        self.matchName1.setStyleSheet("background-color: rgb(252, 252, 252); "
                                      "font-family: Gotham-Light; font-size: 20px;")
        self.matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName1.setObjectName("matchName1")

        self.MenuButton.setGeometry(QtCore.QRect(765, 5, 110, 20))
        self.MenuButton.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                        "font-size: 13px;")
        self.MenuButton.setObjectName("MenuButton")

        self.KataFinalButton.setGeometry(QtCore.QRect(765, 30, 110, 20))
        self.KataFinalButton.setStyleSheet("background-color: rgb(242, 242, 242); "
                                      "font-family: Gotham-Light; font-size: 13px;")
        self.KataFinalButton.setObjectName("KataFinalButton")

        self.KumiteButton.setGeometry(QtCore.QRect(765, 55, 110, 20))
        self.KumiteButton.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                        "font-size: 13px;")
        self.KumiteButton.setObjectName("KumiteButton")

        self.line1.setGeometry(QtCore.QRect(447, 80, 6, 150))
        font = QtGui.QFont()
        font.setKerning(True)
        self.line1.setFont(font)
        self.line1.setLineWidth(1)
        self.line1.setMidLineWidth(6)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        self.frame_red1.setGeometry(QtCore.QRect(475, 80, 400, 150))
        self.frame_red1.setStyleSheet("background-color: rgb(255, 222, 219);")
        self.frame_red1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red1.setObjectName("frame_red1")

        self.label_name_red_1.setGeometry(QtCore.QRect(50, 50, 300, 40))
        self.label_name_red_1.setStyleSheet("background-color: rgb(252, 252, 252); font-family: Gotham-Medium; "
                                            "font-size: 33px;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(75, 100, 250, 40))
        self.label_region_red_1.setStyleSheet("background-color: rgb(252, 252, 252); font-family: Gotham-Medium; "
                                            "font-size: 13px;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.frame_white1.setGeometry(QtCore.QRect(25, 80, 400, 150))
        self.frame_white1.setStyleSheet("background-color: rgb(252, 252, 252)")
        self.frame_white1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white1.setObjectName("frame_white1")

        self.label_name_white_1.setGeometry(QtCore.QRect(50, 50, 300, 40))
        self.label_name_white_1.setStyleSheet("background-color: rgb(232, 232, 232); font-family: Gotham-Medium; "
                                            "font-size: 33px;")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_white_1.setObjectName("label_name_white_1")

        self.label_region_white_1.setGeometry(QtCore.QRect(75, 100, 250, 40))
        self.label_region_white_1.setStyleSheet("background-color: rgb(232, 232, 232); font-family: Gotham-Medium; "
                                            "font-size: 13px;")
        self.label_region_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setObjectName("label_region_white_1")

        self.pushButton_clearData.setGeometry(QtCore.QRect(475, 330, 200, 35))
        self.pushButton_clearData.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham-Light;"
                                       "color: white; font-size: 20px;")
        self.pushButton_clearData.setObjectName("pushButton_clearData")

        self.pushButton_NewCategory.setGeometry(QtCore.QRect(775, 320, 100, 45))
        self.pushButton_NewCategory.setStyleSheet("font-family: Gotham-Light; font-size: 13px;")
        self.pushButton_NewCategory.setObjectName("pushButton_NewCategory")

        self.pushButton_showData.setGeometry(QtCore.QRect(175, 330, 250, 35))
        self.pushButton_showData.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham-Light;"
                                       "color: white; font-size: 20px;")
        self.pushButton_showData.setObjectName("pushButton_showData")

        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 380, 900, 120))
        self.frame_sportsmans.setStyleSheet("background-color: none;")
        self.frame_sportsmans.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sportsmans.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(480, 20, 111, 22))
        self.comboBox_age.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_age.setObjectName("comboBox_age")

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

        self.age_1.setGeometry(QtCore.QRect(480, 0, 111, 13))
        self.age_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(510, 70, 350, 25))
        self.comboBox_name_red_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.comboBox_name_white_1.setEnabled(False)
        self.comboBox_name_white_1.setGeometry(QtCore.QRect(40, 70, 350, 25))
        self.comboBox_name_white_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_name_white_1.setObjectName("comboBox_name_white_1")

        self.name_red_1.setGeometry(QtCore.QRect(510, 50, 350, 16))
        self.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.name_white_1.setGeometry(QtCore.QRect(40, 50, 350, 16))
        self.name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_white_1.setObjectName("name_white_1")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(510, 240, 340, 30))
        self.lineEdit_name_red_1.setStyleSheet("background-color: rgb(252, 252, 252);"
                                             "font-family: Gotham-Light; font-size: 20px;")
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(530, 290, 300, 30))
        self.lineEdit_region_red_1.setStyleSheet("background-color: rgb(252, 252, 252);"
                                               "font-family: Gotham-Light; font-size: 13px;")
        self.lineEdit_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        self.lineEdit_name_white_1.setGeometry(QtCore.QRect(50, 240, 340, 30))
        self.lineEdit_name_white_1.setStyleSheet("background-color: rgb(252, 252, 252); "
                                             "font-family: Gotham-Light; font-size: 20px;")
        self.lineEdit_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name_white_1.setObjectName("lineEdit_name_white_1")

        self.lineEdit_region_white_1.setGeometry(QtCore.QRect(70, 290, 300, 30))
        self.lineEdit_region_white_1.setStyleSheet("background-color: rgb(252, 252, 252);"
                                               "font-family: Gotham-Light; font-size: 13px;")
        self.lineEdit_region_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_region_white_1.setObjectName("lineEdit_region_white_1")

        self.frame_winner.setGeometry(QtCore.QRect(135, 80, 630, 25))
        self.frame_winner.setStyleSheet("background-color: none")
        self.frame_winner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_winner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_winner.setObjectName("frame_winner")

        self.winnerRed.setGeometry(QtCore.QRect(455, 0, 200, 25))
        self.winnerRed.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerRed.setObjectName("winnerRed")

        self.winnerWhite.setGeometry(QtCore.QRect(0, 0, 200, 25))
        self.winnerWhite.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerWhite.setObjectName("winnerWhite")

        self.frame_red1.raise_()
        self.line1.raise_()
        self.frame_white1.raise_()
        self.pushButton_clearData.raise_()
        self.pushButton_NewCategory.raise_()
        self.pushButton_showData.raise_()
        self.comboBox_age.raise_()
        self.frame_sex.raise_()
        self.sex_1.raise_()
        self.age_1.raise_()
        self.comboBox_name_red_1.raise_()
        self.comboBox_name_white_1.raise_()
        self.name_red_1.raise_()
        self.name_white_1.raise_()
        self.MenuButton.raise_()
        self.KataFinalButton.raise_()
        self.KumiteButton.raise_()
        self.label_matchName1.raise_()
        self.label_matchName2.raise_()
        self.matchName1.raise_()
        self.frame_winner.raise_()


        self.retranslateUi(Form21)
        QtCore.QMetaObject.connectSlotsByName(Form21)

    def retranslateUi(self, Form21):
        _translate = QtCore.QCoreApplication.translate
        Form21.setWindowTitle(_translate("Form21", "Экран для судей. Ката по флажкам"))
        self.label_matchName1.setText(_translate("Form21", '<b>Заголовок</b>'))
        self.label_matchName2.setText(_translate("Form21", 'Любой текст, после которого ставится <b>запятая</b>, не меняется программой'))
        self.matchName1.setText(_translate("Form21", "Татами №#, М/Ж - возраст"))
        self.MenuButton.setText(_translate("Form21", "Главное меню"))
        self.KataFinalButton.setText(_translate("Form21", "Ката финал"))
        self.KumiteButton.setText(_translate("Form21", "Кумите"))
        self.label_name_red_1.setText(_translate("Form21", "ФАМИЛИЯ"))
        self.label_region_red_1.setText(_translate("Form21", "регион"))
        self.label_name_white_1.setText(_translate("Form21", "ФАМИЛИЯ"))
        self.label_region_white_1.setText(_translate("Form21", "регион"))
        self.pushButton_clearData.setText(_translate("Form21", "Очистить данные"))
        self.pushButton_NewCategory.setText(_translate("Form21", "Новая \n категория"))
        self.pushButton_showData.setText(_translate("Form21", "Показать на экране"))
        self.male.setText(_translate("Form21", "М"))
        self.female.setText(_translate("Form21", "Ж"))
        self.sex_1.setText(_translate("Form21", "Пол"))
        self.age_1.setText(_translate("Form21", "Возраст"))
        self.name_red_1.setText(_translate("Form21", "Выберите спортсмена"))
        self.name_white_1.setText(_translate("Form21", "Выберите спортсмена"))
        self.lineEdit_name_red_1.setText(_translate("Form21", "АКА. Введите имя спортсмена"))
        self.lineEdit_region_red_1.setText(_translate("Form21", "АКА. Введите регион"))
        self.lineEdit_name_white_1.setText(_translate("Form21", "СИРО. Введите имя спортсмена"))
        self.lineEdit_region_white_1.setText(_translate("Form21", "СИРО. Введите регион"))
        self.winnerRed.setText(_translate("Form21", "Победил АКА"))
        self.winnerWhite.setText(_translate("Form21", "Победил СИРО"))


class KataQual_MainWindow(QWidget, KataQual_MainWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.KataQual_SecondWindow = KataQual_SecondWindow()

    def openSecondWin(self):
        self.KataQual_SecondWindow.show()

    def closeSecondWin(self):
        self.KataQual_SecondWindow.hide()

    def clearKataData(self):
        self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_name_white_2.setText("ФАМИЛИЯ")
        self.KataQual_SecondWindow.label_region_white_2.setText("регион")
        self.KataQual_SecondWindow.label_region_red_2.setText("регион")
        self.KataQual_SecondWindow.label_name_red_2.setText("ФАМИЛИЯ")
        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setText("регион")
        self.label_name_white_1.setText("ФАМИЛИЯ")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setText("регион")
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
            "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
        self.KataQual_SecondWindow.label_region_white_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_region_red_2.setStyleSheet(
            "background-color: none; font-family: Gotham-Light; font-size: 150px;")
        self.KataQual_SecondWindow.label_name_white_2.setText("ФАМИЛИЯ")
        self.KataQual_SecondWindow.label_region_white_2.setText("регион")
        self.KataQual_SecondWindow.label_region_red_2.setText("регион")
        self.KataQual_SecondWindow.label_name_red_2.setText("ФАМИЛИЯ")
        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_region_red_1.setText("регион")
        self.label_name_white_1.setText("ФАМИЛИЯ")
        self.label_region_white_1.setText("регион")
        self.comboBox_age.clear()
        self.comboBox_name_red_1.clear()
        self.comboBox_name_white_1.clear()
        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_name_white_1.setEnabled(False)
        self.comboBox_name_white_1.setStyleSheet("background-color: rgb(242, 242, 242)")
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
        self.age_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.lineEdit_name_red_1.setText("АКА. Введите имя спортсмена")
        self.lineEdit_region_red_1.setText("АКА. Введите регион")
        self.lineEdit_name_white_1.setText("СИРО. Введите имя спортсмена")
        self.lineEdit_region_white_1.setText("СИРО. Введите регион")
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.label_winner.hide()


    def setDataKata(self):
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)
        self.KataQual_SecondWindow.matchName2.setText(self.matchName1.text())
        self.label_name_red_1.setText(self.lineEdit_name_red_1.text())
        self.label_region_red_1.setText(self.lineEdit_region_red_1.text())
        self.KataQual_SecondWindow.label_name_red_2.setText(self.lineEdit_name_red_1.text())
        self.KataQual_SecondWindow.label_region_red_2.setText(self.lineEdit_region_red_1.text())
        self.label_name_white_1.setText(self.lineEdit_name_white_1.text())
        self.label_region_white_1.setText(self.lineEdit_region_white_1.text())
        self.KataQual_SecondWindow.label_name_white_2.setText(self.lineEdit_name_white_1.text())
        self.KataQual_SecondWindow.label_region_white_2.setText(self.lineEdit_region_white_1.text())
        self.KataQual_SecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 1840, 400))
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 600, 1840, 400))
        self.KataQual_SecondWindow.frame_red2.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.label_winner.hide()
        # self.KataQual_SecondWindow.label_name_red_2.show()
        # self.KataQual_SecondWindow.label_region_red_2.show()
        # self.KataQual_SecondWindow.label_name_white_2.show()
        # self.KataQual_SecondWindow.label_region_white_2.show()

        firstWindowNameRed = self.label_name_red_1.fontMetrics().boundingRect(self.label_name_red_1.text()).width()
        firstWindowRegionRed = self.label_region_red_1.fontMetrics().boundingRect(self.label_region_red_1.text()).width()


        firstWindowNameWhite = self.label_name_white_1.fontMetrics().boundingRect(self.label_name_white_1.text()).width()
        firstWindowRegionWhite = self.label_region_white_1.fontMetrics().boundingRect(
            self.label_region_white_1.text()).width()

        if firstWindowNameWhite > 237 or firstWindowNameRed > 237:
            max_value = max(firstWindowNameWhite, firstWindowNameRed)
            n = "font-family: Gotham-Medium; font-size: " + str(int(300 * (198 / max_value))) + "px;"
            self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(n)
            self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(n)
        else:
            self.KataQual_SecondWindow.label_name_white_2.setStyleSheet(
                "background-color: none; font-family: Gotham-Medium; font-size: 250px;")
            self.KataQual_SecondWindow.label_name_red_2.setStyleSheet(
                "background-color: none; font-family: Gotham-Medium; font-size: 250px;")

        if firstWindowRegionWhite > 93 or firstWindowRegionRed > 93:
            max_value = max(firstWindowRegionWhite, firstWindowRegionRed)
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

    def setWinnerWhite(self):
        self.KataQual_SecondWindow.frame_white2.setGeometry(QtCore.QRect(40, 350, 1840, 400))
        self.KataQual_SecondWindow.label_winner.show()
        self.KataQual_SecondWindow.frame_white2.show()
        self.KataQual_SecondWindow.frame_red2.hide()
