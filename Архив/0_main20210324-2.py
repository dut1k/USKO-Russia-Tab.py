import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QTimer


#from Kata20210322 import *
from Kata20210323 import KataMainWindow
from Kata20210323 import KataMainWindow_Ui
from Kata20210323 import KataSecondWindow
from Kata20210323 import KataSecondWindow_Ui
from Kumite20210320 import KumiteMainWindow
from Kumite20210320 import KumiteMainWindow_Ui
from Kumite20210320 import KumiteSecondWindow
from Kumite20210320 import KumiteSWindow_Ui


# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI Kata
Form11 = QtWidgets.QWidget()

ui_kata12 = KataMainWindow_Ui()
ui_kata12.setupUi(Form11)
ui_kata11 = KataMainWindow()
ui_kata11.setupUi(Form11)

Form12 = QtWidgets.QWidget()

ui_kata21 = KataSecondWindow_Ui()
ui_kata21.setupUi_Kata2(Form12)
ui_kata22 = KataSecondWindow()
ui_kata22.setupUi_Kata2(Form12)

# Create form and init UI Kumite
#Form2 = KumiteMainWindow()
#Form2.show()
Form2 = QtWidgets.QWidget()

ui_kumite12 = KumiteMainWindow_Ui()
ui_kumite12.setupUi(Form2)
ui_kumite11 = KumiteMainWindow()
ui_kumite11.setupUi(Form2)

Form = QtWidgets.QWidget()

ui_kumite21 = KumiteSWindow_Ui()
ui_kumite21.setupUi2(Form)
ui_kumite22 = KumiteSecondWindow()
ui_kumite22.setupUi2(Form)

class Ui_Form0(object):
    def setupUi0(self, Form0):
        Form0.setObjectName("Form00")
        Form0.setEnabled(True)
        Form0.resize(901, 500)
        Form0.setWindowOpacity(1.0)
        Form0.setToolTipDuration(-1)
        Form0.setStatusTip("")
        Form0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_1 = QtWidgets.QPushButton(Form0)
        self.pushButton_1.setGeometry(QtCore.QRect(240, 130, 75, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form0)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 140, 75, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)
        self.pushButton_1.clicked.connect(self.passinon)
        self.pushButton_2.clicked.connect(self.passi)
#        self.pushButton_1.clicked.connect(self.passingInformation)
#        ui2.pushButton_11.clicked.connect(self.passi)
#        ui_kata12.Calc_Button.clicked.connect(ui_kata1.passingInformation)
#        ui_kata1.Calc_Button.clicked.connect(self.print_scoore)
        ui_kata11.Calc_Button.clicked.connect(ui_kata11.passingInformation)
        ui_kata11.Clear_Button.clicked.connect(ui_kata11.clear_Data)

        ui_kumite11.pushButton_start.clicked.connect(ui_kumite11.start_timer)
        ui_kumite11.pushButton_pause.clicked.connect(ui_kumite11.reset_timer)
        ui_kumite11.pushButton_reset.clicked.connect(ui_kumite11.reset_all)

        ui_kumite11.plus5sec.clicked.connect(ui_kumite11.upTime)
        ui_kumite11.minus5sec.clicked.connect(ui_kumite11.downTime)

        ui_kumite11.score_red_0.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_1.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_2.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_3.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_4.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_5.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_red_6.toggled.connect(ui_kumite11.onClickedR)
        ui_kumite11.score_white_0.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_1.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_2.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_3.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_4.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_5.toggled.connect(ui_kumite11.onClickedW)
        ui_kumite11.score_white_6.toggled.connect(ui_kumite11.onClickedW)

        ui_kumite11.h_red1.toggled.connect(ui_kumite11.penaltyButton_hmr1)
        ui_kumite11.h_red2.clicked.connect(ui_kumite11.penaltyButton_hmr2)
        ui_kumite11.h_red3.clicked.connect(ui_kumite11.penaltyButton_hmr3)
        ui_kumite11.h_red4.clicked.connect(ui_kumite11.penaltyButton_hmr4)

        ui_kumite11.j_red1.toggled.connect(ui_kumite11.penaltyButton_jr1)
        ui_kumite11.j_red2.clicked.connect(ui_kumite11.penaltyButton_jr2)
        ui_kumite11.j_red3.clicked.connect(ui_kumite11.penaltyButton_jr3)
        ui_kumite11.j_red4.clicked.connect(ui_kumite11.penaltyButton_jr4)

        ui_kumite11.h_white1.toggled.connect(ui_kumite11.penaltyButton_hmw1)
        ui_kumite11.h_white2.clicked.connect(ui_kumite11.penaltyButton_hmw2)
        ui_kumite11.h_white3.clicked.connect(ui_kumite11.penaltyButton_hmw3)
        ui_kumite11.h_white4.clicked.connect(ui_kumite11.penaltyButton_hmw4)

        ui_kumite11.j_white1.toggled.connect(ui_kumite11.penaltyButton_jw1)
        ui_kumite11.j_white2.clicked.connect(ui_kumite11.penaltyButton_jw2)
        ui_kumite11.j_white3.clicked.connect(ui_kumite11.penaltyButton_jw3)
        ui_kumite11.j_white4.clicked.connect(ui_kumite11.penaltyButton_jw4)

    def passinon(self):
        Form12.show()
        Form11.show()

#    def print_scoore(self):
#        ui_kata1.Clear_Button.setText('111')
#        ui_kata2.label_sum2.setText('111')

    def passi(self):
        Form.show()
        Form2.show()


    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Ката"))
        self.pushButton_2.setText(_translate("Form", "Кумите\nне работает"))

class Menu_Form01(object):
    def setupUi01(self, Form01):
        Form0.setObjectName("Form01")
        Form0.setEnabled(True)
        Form0.resize(400, 200)
        Form0.setWindowOpacity(1.0)
        Form0.setToolTipDuration(-1)
        Form0.setStatusTip("")
        Form0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_1 = QtWidgets.QPushButton(Form0)
        self.pushButton_1.setGeometry(QtCore.QRect(240, 130, 75, 25))
        self.pushButton_1.setObjectName("pushButton_1")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)
        self.pushButton_1.clicked.connect(self.passinon)
        ui_kata11.Calc_Button.clicked.connect(ui_kata11.passingInformation)
        ui_kata11.Clear_Button.clicked.connect(ui_kata11.clear_Data)

    def passinon(self):
        Form12.show()
        Form11.show()

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Ката"))

# Run main loop
if __name__ == "__main__":
    Form0 = QtWidgets.QWidget()
    ui0 = Ui_Form0()
    ui0.setupUi0(Form0)
    Form0.show()
    sys.exit(app.exec_())