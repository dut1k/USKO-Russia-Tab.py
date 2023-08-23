from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class KataSecondWindow_Ui(object):
    def setupUi_Kata2(self, Form12):
        Form12.setObjectName("Form")
        Form12.setEnabled(True)
        Form12.resize(1920, 1080)
        Form12.setWindowOpacity(1.0)
        Form12.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_sum2 = QtWidgets.QLabel(Form12)
        self.input_referee1 = QtWidgets.QLabel(Form12)
        self.input_referee2 = QtWidgets.QLabel(Form12)
        self.input_referee3 = QtWidgets.QLabel(Form12)
        self.input_referee4 = QtWidgets.QLabel(Form12)
        self.input_referee5 = QtWidgets.QLabel(Form12)
        self.input_referee6 = QtWidgets.QLabel(Form12)
        self.input_referee7 = QtWidgets.QLabel(Form12)
        self.label_1 = QtWidgets.QLabel(Form12)
        self.label_2 = QtWidgets.QLabel(Form12)
        self.label_3 = QtWidgets.QLabel(Form12)
        self.label_4 = QtWidgets.QLabel(Form12)
        self.label_5 = QtWidgets.QLabel(Form12)
        self.label_6 = QtWidgets.QLabel(Form12)
        self.label_7 = QtWidgets.QLabel(Form12)
        self.matchName2 = QtWidgets.QLabel(Form12)
        self.label_name_red_2 = QtWidgets.QLabel(Form12)
        self.label_region_red_2 = QtWidgets.QLabel(Form12)

        self.label_sum2.setGeometry(QtCore.QRect(1050, 150, 800, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_sum2.sizePolicy().hasHeightForWidth())
        self.label_sum2.setStyleSheet("background-color: white; font-family: Gotham-Bold; font-size: 350px; ")
        self.label_sum2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sum2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_sum2.setLineWidth(1)
        self.label_sum2.setMidLineWidth(0)
        self.label_sum2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum2.setObjectName("label_sum2")

        self.label_1.setEnabled(True)
        self.label_1.setGeometry(QtCore.QRect(70, 680, 250, 50))
        self.label_1.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_1.setObjectName("label_1")

        self.label_2.setGeometry(QtCore.QRect(325, 680, 250, 50))
        self.label_2.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(580, 680, 250, 50))
        self.label_3.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(835, 680, 250, 50))
        self.label_4.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(1090, 680, 250, 50))
        self.label_5.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")

        self.label_6.setGeometry(QtCore.QRect(1345, 680, 250, 50))
        self.label_6.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")

        self.label_7.setGeometry(QtCore.QRect(1600, 680, 250, 50))
        self.label_7.setStyleSheet("font-family: Gotham-Light; font-size: 35px; ")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")

        self.input_referee1.setGeometry(QtCore.QRect(70, 740, 250, 250))
        self.input_referee1.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee1.setObjectName("input_referee1")

        self.input_referee2.setGeometry(QtCore.QRect(325, 740, 250, 250))
        self.input_referee2.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee2.setObjectName("input_referee2")

        self.input_referee3.setGeometry(QtCore.QRect(580, 740, 250, 250))
        self.input_referee3.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee3.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee3.setObjectName("input_referee3")

        self.input_referee4.setGeometry(QtCore.QRect(835, 740, 250, 250))
        self.input_referee4.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee4.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee4.setObjectName("input_referee4")

        self.input_referee5.setGeometry(QtCore.QRect(1090, 740, 250, 250))
        self.input_referee5.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee5.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee5.setObjectName("input_referee5")

        self.input_referee6.setGeometry(QtCore.QRect(1345, 740, 250, 250))
        self.input_referee6.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee6.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee6.setObjectName("input_referee6")

        self.input_referee7.setGeometry(QtCore.QRect(1600, 740, 250, 250))
        self.input_referee7.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee7.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee7.setObjectName("input_referee7")

        self.matchName2.setGeometry(QtCore.QRect(20, 10, 1880, 100))
        self.matchName2.setStyleSheet("font-family: Gotham-Medium; font-size: 100px; color: grey;")
        self.matchName2.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName2.setObjectName("matchName2")

        self.label_name_red_2.setGeometry(QtCore.QRect(40, 120, 1000, 200))
        self.label_name_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium; font-size: 133px;")
        self.label_name_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_2.setObjectName("label_name_red_2")

        self.label_region_red_2.setGeometry(QtCore.QRect(40, 400, 1000, 100))
        self.label_region_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium; font-size: 53px;")
        self.label_region_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_2.setObjectName("label_region_red_2")


        self.retranslateUi(Form12)
        QtCore.QMetaObject.connectSlotsByName(Form12)

    def retranslateUi(self, Form12):
        _translate = QtCore.QCoreApplication.translate
        Form12.setWindowTitle(_translate("Form12", " "))
        self.label_sum2.setText(_translate("Form12", ""))
        self.label_1.setText(_translate("Form12", "1"))
        self.label_3.setText(_translate("Form12", "3"))
        self.label_4.setText(_translate("Form12", "4"))
        self.label_2.setText(_translate("Form12", "2"))
        self.label_5.setText(_translate("Form12", "5"))
        self.label_7.setText(_translate("Form12", "7"))
        self.label_6.setText(_translate("Form12", "6"))
        self.input_referee6.setText(_translate("Form12", ""))
        self.input_referee4.setText(_translate("Form12", ""))
        self.input_referee2.setText(_translate("Form12", ""))
        self.input_referee7.setText(_translate("Form12", ""))
        self.input_referee1.setText(_translate("Form12", ""))
        self.input_referee3.setText(_translate("Form12", ""))
        self.input_referee5.setText(_translate("Form12", ""))
        self.matchName2.setText(_translate("Form12", "Татами №# М/Ж - возраст"))
        self.label_region_red_2.setText(_translate("Form12", "регион"))
        self.label_name_red_2.setText(_translate("Form12", "ФАМИЛИЯ"))


class KataSecondWindow(QWidget, KataSecondWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_Kata2(self)

    def Extream_Value(self):
        q1 = self.input_referee1.text()
        q2 = self.input_referee2.text()
        q3 = self.input_referee3.text()
        q4 = self.input_referee4.text()
        q5 = self.input_referee5.text()
        q6 = self.input_referee6.text()
        q7 = self.input_referee7.text()

        l = [q1, q2, q3, q4, q5, q6, q7]
        m = [num for num in l if num != '']
        try:
            if min(m) == self.input_referee1.text():
                self.extreamLabelStyle(self.input_referee1)
            elif min(m) == self.input_referee2.text():
                self.extreamLabelStyle(self.input_referee2)
            elif min(m) == self.input_referee3.text():
                self.extreamLabelStyle(self.input_referee3)
            elif min(m) == self.input_referee4.text():
                self.extreamLabelStyle(self.input_referee4)
            elif min(m) == self.input_referee5.text():
                self.extreamLabelStyle(self.input_referee5)
            elif min(m) == self.input_referee6.text():
                self.extreamLabelStyle(self.input_referee6)
            elif min(m) == self.input_referee7.text():
                self.extreamLabelStyle(self.input_referee7)
            else:
                pass
            if max(m) == self.input_referee2.text():
                self.extreamLabelStyle(self.input_referee2)
            elif max(m) == self.input_referee1.text():
                self.extreamLabelStyle(self.input_referee1)
            elif max(m) == self.input_referee3.text():
                self.extreamLabelStyle(self.input_referee3)
            elif max(m) == self.input_referee4.text():
                self.extreamLabelStyle(self.input_referee4)
            elif max(m) == self.input_referee5.text():
                self.extreamLabelStyle(self.input_referee5)
            elif max(m) == self.input_referee6.text():
                self.extreamLabelStyle(self.input_referee6)
            elif max(m) == self.input_referee7.text():
                self.extreamLabelStyle(self.input_referee7)
            else:
                pass

        except ValueError:
            self.label_1.setText('1')
            self.label_2.setText('2')
            self.label_3.setText('3')
            self.label_4.setText('4')
            self.label_5.setText('5')
            self.label_6.setText('6')
            self.label_7.setText('7')

    def extreamLabelStyle(self, input_referee):
        input_referee.setStyleSheet("background-color: white; font-family: Gotham-Medium;"
                      "color: Grey; font-size: 120px; text-align : left")


class KataMainWindow_Ui(object):
    def setupUi(self, Form11):
        Form11.setObjectName("Form2")
        Form11.setEnabled(True)
        Form11.setFixedSize(900, 500)
        Form11.setWindowOpacity(1.0)
        Form11.setToolTipDuration(-1)
        Form11.setStatusTip("")
        Form11.setStyleSheet("background-color: rgb(255, 255, 255);")


        self.frame_sportsmans = QtWidgets.QFrame(Form11)

        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.label_name_red_1 = QtWidgets.QLabel(Form11)
        self.label_region_red_1 = QtWidgets.QLabel(Form11)
        self.male = QtWidgets.QRadioButton(self.frame_sex)
        self.female = QtWidgets.QRadioButton(self.frame_sex)
        self.sex_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel(self.frame_sportsmans)
        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_region_red_1 = QtWidgets.QLineEdit(Form11)
        self.frame_matchName = QtWidgets.QFrame(Form11)
        self.label_matchName1 = QtWidgets.QLabel(self.frame_matchName)
        self.label_matchName2 = QtWidgets.QLabel(self.frame_matchName)
        self.matchName1 = QtWidgets.QLineEdit(self.frame_matchName)

        self.pushButton_clearData = QtWidgets.QPushButton(Form11)
        self.pushButton_NewCategory = QtWidgets.QPushButton(Form11)
        self.pushButton_showData = QtWidgets.QPushButton(Form11)

        self.frame_matchName.setGeometry(QtCore.QRect(290, 0, 480, 60))
        self.frame_matchName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_matchName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_matchName.setObjectName("matchName")

        self.label_matchName1.setGeometry(QtCore.QRect(0, 0, 400, 15))
        self.label_matchName1.setStyleSheet("font-family: Gotham-Light; font-size: 13px;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.label_matchName2.setGeometry(QtCore.QRect(0, 45, 480, 15))
        self.label_matchName2.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 12px;")
        self.label_matchName2.setObjectName("label_matchName2")

        self.matchName1.setGeometry(QtCore.QRect(0, 15, 400, 30))
        self.matchName1.setStyleSheet("background-color: rgb(252, 252, 252);"
                                             "font-family: Gotham-Light; font-size: 20px;")
        self.matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName1.setObjectName("matchName")

        self.pushButton_clearData.setGeometry(QtCore.QRect(710, 400, 170, 30))
        self.pushButton_clearData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                                "font-size: 16px;")
        self.pushButton_clearData.setObjectName("pushButton_clearData")

        self.pushButton_NewCategory.setGeometry(QtCore.QRect(780, 440, 100, 40))
        self.pushButton_NewCategory.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                                  "font-size: 13px;")
        self.pushButton_NewCategory.setObjectName("pushButton_NewCategory")

        self.pushButton_showData.setGeometry(QtCore.QRect(650, 350, 230, 40))
        self.pushButton_showData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Medium;"
                                               "font-size: 16px;")
        self.pushButton_showData.setObjectName("pushButton_showData")

        self.label_name_red_1.setGeometry(QtCore.QRect(360, 40, 405, 100))
        self.label_name_red_1.setStyleSheet("background-color: none; color: grey; font-family: Gotham-Medium;"
                                            "font-size: 33px;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(360, 90, 405, 100))
        self.label_region_red_1.setStyleSheet("background-color: none; color: grey; font-family: Gotham-Medium;"
                                              "font-size: 20px;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 440, 900, 60))
        self.frame_sportsmans.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sportsmans.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(250, 20, 111, 25))
        self.comboBox_age.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_age.setObjectName("comboBox_age")

        self.frame_sex.setGeometry(QtCore.QRect(60, 20, 150, 25))
        self.frame_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sex.setObjectName("frame_sex")

        self.male.setGeometry(QtCore.QRect(20, 0, 40, 25))
        self.male.setStyleSheet("font-family: Gotham-Bold; font-size: 20px;")
        self.male.setObjectName("male")

        self.female.setGeometry(QtCore.QRect(90, 0, 40, 25))
        self.female.setStyleSheet("font-family: Gotham-Bold; font-size: 20px;")
        self.female.setObjectName("female")

        self.sex_1.setGeometry(QtCore.QRect(60, 0, 150, 13))
        self.sex_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 13px;")
        self.sex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_1.setObjectName("sex_1")

        self.age_1.setGeometry(QtCore.QRect(250, 0, 110, 13))
        self.age_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(400, 20, 350, 25))
        self.comboBox_name_red_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.name_red_1.setGeometry(QtCore.QRect(400, 0, 350, 16))
        self.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(280, 350, 340, 30))
        self.lineEdit_name_red_1.setStyleSheet("background-color: none; font-family: Gotham-Light; font-size: 20px;")
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(300, 400, 300, 30))
        self.lineEdit_region_red_1.setStyleSheet("background-color: none; font-family: Gotham-Light; font-size: 13px;")
        self.lineEdit_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        self.MenuButton = QtWidgets.QPushButton(Form11)
        self.MenuButton.setGeometry(QtCore.QRect(765, 5, 110, 20))
        self.MenuButton.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                        "font-size: 13px;")
        self.MenuButton.setObjectName("MenuButton")

        self.KataQualButton = QtWidgets.QPushButton(Form11)
        self.KataQualButton.setGeometry(QtCore.QRect(765, 30, 110, 20))
        self.KataQualButton.setStyleSheet("background-color: rgb(242, 242, 242); "
                                      "font-family: Gotham-Light; font-size: 13px;")
        self.KataQualButton.setObjectName("KataQualButton")

        self.KumiteButton = QtWidgets.QPushButton(Form11)
        self.KumiteButton.setGeometry(QtCore.QRect(765, 55, 110, 20))
        self.KumiteButton.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
                                        "font-size: 13px;")
        self.KumiteButton.setObjectName("KumiteButton")

        self.Calc_Button = QtWidgets.QPushButton(Form11)
        self.Calc_Button.setGeometry(QtCore.QRect(60, 330, 170, 45))
        self.Calc_Button.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham-Medium;"
                                       "color: white; font-size: 20pt;")
        self.Calc_Button.setObjectName("Calc_Button")

        self.Clear_Button = QtWidgets.QPushButton(Form11)
        self.Clear_Button.setGeometry(QtCore.QRect(90, 385, 110, 25))
        self.Clear_Button.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham-Light;"
                                        "color: white; font-size: 16px;")
        self.Clear_Button.setObjectName("Clear_Button")

        self.heading_sum = QtWidgets.QLabel(Form11)
        self.heading_sum.setGeometry(QtCore.QRect(40, 60, 120, 20))
        self.heading_sum.setStyleSheet("font-family: Gotham-Light; font-size: 13px;")
        self.heading_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_sum.setObjectName("heading_sum")

        self.label_sum = QtWidgets.QLabel(Form11)
        self.label_sum.setGeometry(QtCore.QRect(0, 80, 300, 130))
        self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light; color: grey; font-size: 20px;")
        self.label_sum.setObjectName("label_sum")

        self.referee_point = QtWidgets.QLabel(Form11)
        self.referee_point.setGeometry(QtCore.QRect(300, 180, 300, 50))
        self.referee_point.setAlignment(QtCore.Qt.AlignCenter)
        self.referee_point.setStyleSheet("font-family: Gotham-Bold; font-size: 40px;")
        self.referee_point.setObjectName("referee_point")

        self.label_help = QtWidgets.QLabel(Form11)
        self.label_help.setGeometry(QtCore.QRect(335, 317, 250, 13))
        self.label_help.setStyleSheet("color: grey; font-size: 10px;")
        self.label_help.setObjectName("label_help")

        self.lineEdit_referee1 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee1.setGeometry(QtCore.QRect(70, 250, 100, 60))
        self.lineEdit_referee1.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee1.setInputMask('9.9')
        self.lineEdit_referee1.setText(str('0.0'))
        self.lineEdit_referee1.setObjectName("lineEdit_referee1")

        self.lineEdit_referee2 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee2.setGeometry(QtCore.QRect(180, 250, 100, 60))
        self.lineEdit_referee2.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee2.setInputMask('9.9')
        self.lineEdit_referee2.setText(str('0.0'))
        self.lineEdit_referee2.setObjectName("lineEdit_referee2")

        self.lineEdit_referee3 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee3.setGeometry(QtCore.QRect(290, 250, 100, 60))
        self.lineEdit_referee3.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee3.setInputMask('9.9')
        self.lineEdit_referee3.setText(str('0.0'))
        self.lineEdit_referee3.setObjectName("lineEdit_referee3")

        self.lineEdit_referee4 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee4.setGeometry(QtCore.QRect(400, 250, 100, 60))
        self.lineEdit_referee4.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee4.setInputMask('9.9')
        self.lineEdit_referee4.setText(str('0.0'))
        self.lineEdit_referee4.setObjectName("lineEdit_referee4")

        self.lineEdit_referee5 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee5.setGeometry(QtCore.QRect(510, 250, 100, 60))
        self.lineEdit_referee5.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee5.setInputMask('9.9')
        self.lineEdit_referee5.setText(str('0.0'))
        self.lineEdit_referee5.setObjectName("lineEdit_referee5")

        self.lineEdit_referee6 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee6.setGeometry(QtCore.QRect(620, 250, 100, 60))
        self.lineEdit_referee6.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee6.setInputMask('9.9')
        self.lineEdit_referee6.setText(str('0.0'))
        self.lineEdit_referee6.setObjectName("lineEdit_referee6")

        self.lineEdit_referee7 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee7.setGeometry(QtCore.QRect(730, 250, 100, 60))
        self.lineEdit_referee7.setStyleSheet("background-color: rgb(242, 242, 242);"
                                             "font-family: Gotham-Light; font-size: 46px;")
        self.lineEdit_referee7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee7.setInputMask('9.9')
        self.lineEdit_referee7.setText(str('0.0'))
        self.lineEdit_referee7.setObjectName("lineEdit_referee7")

        self.label_1 = QtWidgets.QLabel(Form11)
        self.label_1.setGeometry(QtCore.QRect(70, 230, 100, 13))
        self.label_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(Form11)
        self.label_2.setGeometry(QtCore.QRect(180, 230, 100, 13))
        self.label_2.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form11)
        self.label_3.setGeometry(QtCore.QRect(290, 230, 100, 13))
        self.label_3.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form11)
        self.label_4.setGeometry(QtCore.QRect(400, 230, 100, 13))
        self.label_4.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form11)
        self.label_5.setGeometry(QtCore.QRect(510, 230, 100, 13))
        self.label_5.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form11)
        self.label_6.setGeometry(QtCore.QRect(620, 230, 100, 13))
        self.label_6.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form11)
        self.label_7.setGeometry(QtCore.QRect(730, 230, 100, 13))
        self.label_7.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form11)

        self.comboBox_age.raise_()
        self.frame_sex.raise_()
        self.sex_1.raise_()
        self.age_1.raise_()
        self.comboBox_name_red_1.raise_()
        self.name_red_1.raise_()

        QtCore.QMetaObject.connectSlotsByName(Form11)

    def retranslateUi(self, Form11):
        _translate = QtCore.QCoreApplication.translate
        Form11.setWindowTitle(_translate("Form11", "Экран для судей. Ката финал"))
        self.label_matchName1.setText(_translate("Form11", '<b>Заголовок</b>'))
        self.label_matchName2.setText(_translate("Form11", 'Любой текст, после которого ставится <b>запятая</b>, не меняется программой'))
        self.matchName1.setText(_translate("Form11", "Татами №#, М/Ж - возраст"))
        self.MenuButton.setText(_translate("Form11", "Главное меню"))
        self.KataQualButton.setText(_translate("Form11", "Ката отбороч."))
        self.KumiteButton.setText(_translate("Form11", "Кумите"))
        self.Clear_Button.setText(_translate("Form11", "Очистить"))
        self.Calc_Button.setText(_translate("Form11", "Рассчитать"))
        self.heading_sum.setText(_translate("Form11", "<b>Сумма баллов</b>"))
        self.label_sum.setText(_translate("Form11", "Нажми кнопку «Рассчитать»"))
        self.referee_point.setText(_translate("Form11", "Оценки судей"))
        self.label_help.setText(_translate("Form11", "Переключайся между судьями кнопкой Tab"))
        self.label_1.setText(_translate("Form11", "1 судья"))
        self.label_2.setText(_translate("Form11", "2 судья"))
        self.label_3.setText(_translate("Form11", "3 судья"))
        self.label_4.setText(_translate("Form11", "4 судья"))
        self.label_5.setText(_translate("Form11", "5 судья"))
        self.label_6.setText(_translate("Form11", "6 судья"))
        self.label_7.setText(_translate("Form11", "7 судья"))
        self.label_name_red_1.setText(_translate("Form11", "ФАМИЛИЯ"))
        self.label_region_red_1.setText(_translate("Form11", "регион"))
        self.male.setText(_translate("Form11", "М"))
        self.female.setText(_translate("Form11", "Ж"))
        self.sex_1.setText(_translate("Form11", "Пол"))
        self.age_1.setText(_translate("Form11", "Возраст"))
        self.name_red_1.setText(_translate("Form11", "Выберите спортсмена"))
        self.lineEdit_name_red_1.setText(_translate("Form11", "Введите имя спортсмена"))
        self.lineEdit_region_red_1.setText(_translate("Form11", "Введите регион"))

        self.pushButton_clearData.setText(_translate("Form21", "Очистить данные"))
        self.pushButton_NewCategory.setText(_translate("Form21", "Новая \n категория"))
        self.pushButton_showData.setText(_translate("Form21", "Показать фамилию \n на экране"))


class KataMainWindow(QWidget, KataMainWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.KataSecondWindow = KataSecondWindow()

        self.lineEdit_referee1.textChanged.connect(self.onChanged)
        self.lineEdit_referee2.textChanged.connect(self.onChanged)
        self.lineEdit_referee3.textChanged.connect(self.onChanged)
        self.lineEdit_referee4.textChanged.connect(self.onChanged)
        self.lineEdit_referee5.textChanged.connect(self.onChanged)
        self.lineEdit_referee6.textChanged.connect(self.onChanged)
        self.lineEdit_referee7.textChanged.connect(self.onChanged)

    def onChanged(self, text):
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
                self.KataSecondWindow.input_referee1.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee1.setText(text)
            elif sender == self.lineEdit_referee2:
                self.KataSecondWindow.input_referee2.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee2.setText(text)
            elif sender == self.lineEdit_referee3:
                self.KataSecondWindow.input_referee3.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee3.setText(text)
            elif sender == self.lineEdit_referee4:
                self.KataSecondWindow.input_referee4.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee4.setText(text)
            elif sender == self.lineEdit_referee5:
                self.KataSecondWindow.input_referee5.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee5.setText(text)
            elif sender == self.lineEdit_referee6:
                self.KataSecondWindow.input_referee6.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee6.setText(text)
            elif sender == self.lineEdit_referee7:
                self.KataSecondWindow.input_referee7.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee7.setText(text)

    def openSecondWin(self):
        self.KataSecondWindow.show()

    def closeSecondWin(self):
        self.KataSecondWindow.close()

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
        input_referee.setStyleSheet(
            "background-color: white; font-family: Gotham-Medium; color: black; font-size: 150px; text-align: left")

    def fiveReferee(self, tuple_five_referee_score):
        if tuple_five_referee_score == '':
            self.KataSecondWindow.input_referee1.setGeometry(QtCore.QRect(70, 740, 352, 250))
            self.KataSecondWindow.input_referee2.setGeometry(QtCore.QRect(427, 740, 352, 250))
            self.KataSecondWindow.input_referee3.setGeometry(QtCore.QRect(784, 740, 352, 250))
            self.KataSecondWindow.input_referee4.setGeometry(QtCore.QRect(1141, 740, 352, 250))
            self.KataSecondWindow.input_referee5.setGeometry(QtCore.QRect(1498, 740, 352, 250))
            self.KataSecondWindow.input_referee6.hide()
            self.KataSecondWindow.input_referee7.hide()
            self.KataSecondWindow.label_1.setGeometry(QtCore.QRect(70, 680, 352, 50))
            self.KataSecondWindow.label_2.setGeometry(QtCore.QRect(427, 680, 352, 50))
            self.KataSecondWindow.label_3.setGeometry(QtCore.QRect(784, 680, 352, 50))
            self.KataSecondWindow.label_4.setGeometry(QtCore.QRect(1141, 680, 352, 50))
            self.KataSecondWindow.label_5.setGeometry(QtCore.QRect(1498, 680, 352, 50))
            self.KataSecondWindow.label_6.hide()
            self.KataSecondWindow.label_7.hide()
        else:
            self.KataSecondWindow.input_referee1.setGeometry(QtCore.QRect(70, 740, 250, 250))
            self.KataSecondWindow.input_referee2.setGeometry(QtCore.QRect(325, 740, 250, 250))
            self.KataSecondWindow.input_referee3.setGeometry(QtCore.QRect(580, 740, 250, 250))
            self.KataSecondWindow.input_referee4.setGeometry(QtCore.QRect(835, 740, 250, 250))
            self.KataSecondWindow.input_referee5.setGeometry(QtCore.QRect(1090, 740, 250, 250))
            self.KataSecondWindow.input_referee6.show()
            self.KataSecondWindow.input_referee7.show()
            self.KataSecondWindow.label_1.setGeometry(QtCore.QRect(70, 680, 250, 50))
            self.KataSecondWindow.label_2.setGeometry(QtCore.QRect(325, 680, 250, 50))
            self.KataSecondWindow.label_3.setGeometry(QtCore.QRect(580, 680, 250, 50))
            self.KataSecondWindow.label_4.setGeometry(QtCore.QRect(835, 680, 250, 50))
            self.KataSecondWindow.label_5.setGeometry(QtCore.QRect(1090, 680, 250, 50))
            self.KataSecondWindow.label_6.setGeometry(QtCore.QRect(1345, 680, 250, 50))
            self.KataSecondWindow.label_7.setGeometry(QtCore.QRect(1600, 680, 250, 50))
            self.KataSecondWindow.label_6.show()
            self.KataSecondWindow.label_7.show()

    def clearKataData(self):
        self.label_sum.setText("Нажми кнопку «Рассчитать»")
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

        self.KataSecondWindow.label_name_red_2.setText("ФАМИЛИЯ")
        self.KataSecondWindow.label_region_red_2.setText("регион")

    def setMatchTitle(self):
        self.KataSecondWindow.matchName2.setText(self.matchName1.text())
        self.label_name_red_1.setText(self.lineEdit_name_red_1.text())
        self.label_region_red_1.setText(self.lineEdit_region_red_1.text())
        firstWindowNameRed = self.lineEdit_name_red_1.fontMetrics().boundingRect(self.lineEdit_name_red_1.text()).width()
        firstWindowRegionRed = self.lineEdit_region_red_1.fontMetrics().boundingRect(self.lineEdit_region_red_1.text()).width()

        if firstWindowNameRed > 145:
            n = "background-color: none; font-family: Gotham-Medium; font-size: "+ str(int(19.3 * (1000 / (firstWindowNameRed)))) + "px;"
            self.KataSecondWindow.label_name_red_2.setStyleSheet(n)
        else:
            self.KataSecondWindow.label_name_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium;"
                                                                 "font-size: 133px;")

        if firstWindowRegionRed > 235:
            n = "background-color: none; font-family: Gotham-Medium; font-size: "+ str(int(12.5 * (1000 / firstWindowRegionRed))) + "px;"
            self.KataSecondWindow.label_region_red_2.setStyleSheet(n)
        else:
            self.KataSecondWindow.label_region_red_2.setStyleSheet(
                "background-color: None; font-family: Gotham-Medium; font-size: 53px;")
        self.KataSecondWindow.label_name_red_2.setText(self.lineEdit_name_red_1.text())
        self.KataSecondWindow.label_region_red_2.setText(self.lineEdit_region_red_1.text())
