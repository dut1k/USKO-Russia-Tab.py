import sys
from 0_main20210325
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer

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

        self.label_sum2.setGeometry(QtCore.QRect(1090, 50, 760, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_sum2.sizePolicy().hasHeightForWidth())
        self.label_sum2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(250)

        self.label_sum2.setFont(font)
        self.label_sum2.setAutoFillBackground(False)
        self.label_sum2.setStyleSheet("background-color: white;")
        self.label_sum2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sum2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_sum2.setLineWidth(1)
        self.label_sum2.setMidLineWidth(0)
        self.label_sum2.setScaledContents(False)
        self.label_sum2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum2.setObjectName("label_sum2")

        self.label_1.setEnabled(True)
        self.label_1.setGeometry(QtCore.QRect(70, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_1.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_1.setObjectName("label_1")

        self.label_2.setGeometry(QtCore.QRect(325, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_2.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(580, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_3.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(835, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_4.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(1090, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_5.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")

        self.label_6.setGeometry(QtCore.QRect(1345, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_6.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")

        self.label_7.setGeometry(QtCore.QRect(1600, 680, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(26)
        self.label_7.setStyleSheet("color: grey")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
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
                self.input_referee1.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee2.text():
                self.input_referee2.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee3.text():
                self.input_referee3.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee4.text():
                self.input_referee4.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee5.text():
                self.input_referee5.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee6.text():
                self.input_referee6.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif min(m) == self.input_referee7.text():
                self.input_referee7.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            else:
                pass
            if max(m) == self.input_referee2.text():
                self.label_2.setText('2')
                self.input_referee2.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee1.text():
                self.label_1.setText('1')
                self.input_referee1.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee3.text():
                self.label_3.setText('3')
                self.input_referee3.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee4.text():
                self.label_4.setText('4')
                self.input_referee4.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee5.text():
                self.label_5.setText('5')
                self.input_referee5.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee6.text():
                self.label_6.setText('6')
                self.input_referee6.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
            elif max(m) == self.input_referee7.text():
                self.label_7.setText('7')
                self.input_referee7.setStyleSheet(
                    "background-color: white; font-family: Gotham; color: Grey; font-size: 100px; text-align : left")
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

class KataMainWindow_Ui(object):
    def setupUi(self, Form11):
        Form11.setObjectName("Form2")
        Form11.setEnabled(True)
        Form11.resize(901, 500)
        Form11.setWindowOpacity(1.0)
        Form11.setToolTipDuration(-1)
        Form11.setStatusTip("")
        Form11.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MenuButton = QtWidgets.QPushButton(Form11)
        self.MenuButton.setGeometry(QtCore.QRect(710, 10, 75, 20))
        self.MenuButton.setObjectName("MenuButton")

        self.KumiteButton = QtWidgets.QPushButton(Form11)
        self.KumiteButton.setGeometry(QtCore.QRect(800, 10, 75, 20))
        self.KumiteButton.setObjectName("KumiteButton")

        self.Calc_Button = QtWidgets.QPushButton(Form11)
        self.Calc_Button.setGeometry(QtCore.QRect(60, 410, 130, 30))
        self.Calc_Button.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham;"
                                       "color: white; font-size: 15pt;")
        self.Calc_Button.setObjectName("Calc_Button")

        self.Clear_Button = QtWidgets.QPushButton(Form11)
        self.Clear_Button.setGeometry(QtCore.QRect(710, 410, 130, 30))
        self.Clear_Button.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham;"
                                       "color: white; font-size: 15pt;")
        self.Clear_Button.setObjectName("Clear_Button")

        self.heading_sum = QtWidgets.QLabel(Form11)
        self.heading_sum.setGeometry(QtCore.QRect(110, 0, 200, 20))
        self.heading_sum.setStyleSheet("font-family: Gotham; font-weight: bold; font-size: 15pt;")
        self.heading_sum.setObjectName("heading_sum")

        self.label_sum = QtWidgets.QLabel(Form11)
        self.label_sum.setGeometry(QtCore.QRect(60, 20, 300, 130))
        self.label_sum.setStyleSheet("font-family: Gotham; color: grey; font-size: 15pt;")
        self.label_sum.setObjectName("label_sum")

        self.referee_point = QtWidgets.QLabel(Form11)
        self.referee_point.setGeometry(QtCore.QRect(100, 180, 700, 90))
        self.referee_point.setAlignment(QtCore.Qt.AlignCenter)
        self.referee_point.setStyleSheet("font: 50pt;")
        self.referee_point.setObjectName("referee_point")

        self.label_help = QtWidgets.QLabel(Form11)
        self.label_help.setGeometry(QtCore.QRect(335, 367, 250, 13))
        self.label_help.setStyleSheet("color: grey; font-size: 7;")
        self.label_help.setObjectName("label_help")

        self.lineEdit_referee1 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee1.setGeometry(QtCore.QRect(70, 300, 100, 60))
        self.lineEdit_referee1.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee1.setInputMask('9,9')
        self.lineEdit_referee1.setText(str('0,0'))
        self.lineEdit_referee1.setObjectName("lineEdit_referee1")

        self.lineEdit_referee2 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee2.setGeometry(QtCore.QRect(180, 300, 100, 60))
        self.lineEdit_referee2.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee2.setInputMask('9,9')
        self.lineEdit_referee2.setText(str('0,0'))
        self.lineEdit_referee2.setObjectName("lineEdit_referee2")

        self.lineEdit_referee3 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee3.setGeometry(QtCore.QRect(290, 300, 100, 60))
        self.lineEdit_referee3.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee3.setInputMask('9,9')
        self.lineEdit_referee3.setText(str('0,0'))
        self.lineEdit_referee3.setObjectName("lineEdit_referee3")

        self.lineEdit_referee4 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee4.setGeometry(QtCore.QRect(400, 300, 100, 60))
        self.lineEdit_referee4.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee4.setInputMask('9,9')
        self.lineEdit_referee4.setText(str('0,0'))
        self.lineEdit_referee4.setObjectName("lineEdit_referee4")

        self.lineEdit_referee5 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee5.setGeometry(QtCore.QRect(510, 300, 100, 60))
        self.lineEdit_referee5.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee5.setInputMask('9,9')
        self.lineEdit_referee5.setText(str('0,0'))
        self.lineEdit_referee5.setObjectName("lineEdit_referee5")

        self.lineEdit_referee6 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee6.setGeometry(QtCore.QRect(620, 300, 100, 60))
        self.lineEdit_referee6.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee6.setInputMask('9,9')
        self.lineEdit_referee6.setText(str('0,0'))
        self.lineEdit_referee6.setObjectName("lineEdit_referee6")

        self.lineEdit_referee7 = QtWidgets.QLineEdit(Form11)
        self.lineEdit_referee7.setGeometry(QtCore.QRect(730, 300, 100, 60))
        self.lineEdit_referee7.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham; font: 35pt;")
        self.lineEdit_referee7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_referee7.setInputMask('9,9')
        self.lineEdit_referee7.setText(str('0,0'))
        self.lineEdit_referee7.setObjectName("lineEdit_referee7")

        self.label_1 = QtWidgets.QLabel(Form11)
        self.label_1.setGeometry(QtCore.QRect(70, 280, 100, 13))
        self.label_1.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(Form11)
        self.label_2.setGeometry(QtCore.QRect(180, 280, 100, 13))
        self.label_2.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form11)
        self.label_3.setGeometry(QtCore.QRect(290, 280, 100, 13))
        self.label_3.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form11)
        self.label_4.setGeometry(QtCore.QRect(400, 280, 100, 13))
        self.label_4.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form11)
        self.label_5.setGeometry(QtCore.QRect(510, 280, 100, 13))
        self.label_5.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form11)
        self.label_6.setGeometry(QtCore.QRect(620, 280, 100, 13))
        self.label_6.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form11)
        self.label_7.setGeometry(QtCore.QRect(730, 280, 100, 13))
        self.label_7.setStyleSheet("color: grey; font-family: Gotham; font: 10pt;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form11)
        QtCore.QMetaObject.connectSlotsByName(Form11)

    def retranslateUi(self, Form11):
        _translate = QtCore.QCoreApplication.translate
        Form11.setWindowTitle(_translate("Form11", "Form"))
        self.MenuButton.setText(_translate("Form11", "Главное меню"))
        self.KumiteButton.setText(_translate("Form11", "Кумите"))
        self.Clear_Button.setText(_translate("Form11", "Очистить"))
        self.Calc_Button.setText(_translate("Form11", "Рассчитать"))
        self.heading_sum.setText(_translate("Form11", "Сумма балов"))
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


class KataMainWindow(QWidget, KataMainWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.KataSecondWindow = KataSecondWindow()
#        self.KataSecondWindow.show()

        # self.Calc_Button.clicked.connect(self.passingInformation)
        # self.Clear_Button.clicked.connect(self.clear_Data)

#        self.MenuButton.clicked.connect(self.clear_Data)

    def openSecondWin(self):
        self.KataSecondWindow.show()

    def passingInformation(self):
        self.KataSecondWindow.label_1.setText('1')
        self.KataSecondWindow.label_2.setText('2')
        self.KataSecondWindow.label_3.setText('3')
        self.KataSecondWindow.label_4.setText('4')
        self.KataSecondWindow.label_5.setText('5')
        self.KataSecondWindow.label_6.setText('6')
        self.KataSecondWindow.label_7.setText('7')

        self.label_sum.setStyleSheet('font-family: Gotham; font: 90pt; color: rgb(0, 178, 80);')
        self.KataSecondWindow.input_referee1.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee2.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee3.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee4.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee5.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee6.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
        self.KataSecondWindow.input_referee7.setStyleSheet(
            "background-color: white; font-family: Gotham; color: black; font-size: 135px; text-align: left")
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
            if n == ',':
                e.append(0.0)
            else:
                e.append(n.replace(",", "."))
        l = e
        newlst = [float(x) for x in l]

        m = newlst
        m = [num for num in m if num != 0]
        m_tuple = tuple(newlst)

        if len(m) < 3:
            self.label_sum.setStyleSheet("font-family: Gotham; font: 15pt; color: red")
            self.label_sum.setText('введи оценки судей')
            self.KataSecondWindow.label_sum2.setText('')
        else:
            m.remove(max(m))
            m.remove(min(m))
            m1 = round(sum(m), 1)  # +++ round
            m2 = str(m1).replace(".", ",")
            self.label_sum.setText(m2)
            l1 = str(m_tuple[0])
            self.lineEdit_referee1.setText(l1)
            self.KataSecondWindow.label_sum2.setText(self.label_sum.text().replace(",", "."))

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

        self.KataSecondWindow.Extream_Value()

    def clear_Data(self):
        self.label_sum.setText("Нажми кнопку «Рассчитать»")
        self.label_sum.setStyleSheet("font-family: Gotham; color: grey; font-size: 15pt;")
        self.lineEdit_referee1.setText('0,0')
        self.lineEdit_referee2.setText('0,0')
        self.lineEdit_referee3.setText('0,0')
        self.lineEdit_referee4.setText('0,0')
        self.lineEdit_referee5.setText('0,0')
        self.lineEdit_referee6.setText('0,0')
        self.lineEdit_referee7.setText('0,0')

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


class dialogWindow_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 150, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 200, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))


class dialogWindow(QWidget, dialogWindow_Ui):
    def __init__(self, openWin=None):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.openNewWindows(openWin, closeWin))
        self.buttonBox.rejected.connect(Dialog.reject)

    def openNewWindows(self, openWin, closeWin):
        self.openWin.show()
        self.closeWin.hide()