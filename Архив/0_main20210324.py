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

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI Kata
Form111 = QtWidgets.QWidget()
ui_kata1 = KataMainWindow()
ui_kata1.setupUi(Form111)

Form113 = QtWidgets.QWidget()
ui_kata12 = KataMainWindow_Ui()
ui_kata12.setupUi(Form113)

Form112 = QtWidgets.QWidget()
ui_kata2 = KataSecondWindow()
ui_kata2.setupUi_Kata2(Form112)
#demo.show()



# Create form and init UI Kumite
#Form2 = KumiteMainWindow()
#Form2.show()

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
        self.pushButton_1.setGeometry(QtCore.QRect(240, 130, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form0)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)
        self.pushButton_1.clicked.connect(self.passinon)
#        self.pushButton_2.clicked.connect(self.passi)
#        self.pushButton_1.clicked.connect(self.passingInformation)
#        ui2.pushButton_11.clicked.connect(self.passi)
#        ui_kata12.Calc_Button.clicked.connect(ui_kata1.passingInformation)
#        ui_kata1.Calc_Button.clicked.connect(self.print_scoore)
        ui_kata1.Calc_Button.clicked.connect(ui_kata1.passingInformation)
        ui_kata1.Clear_Button.clicked.connect(ui_kata1.clear_Data)

    def passinon(self):
        Form112.show()
        Form111.show()

#    def print_scoore(self):
#        ui_kata1.Clear_Button.setText('111')
#        ui_kata2.label_sum2.setText('111')

#    def passi(self):
#        Form.show()


    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Ката"))
        self.pushButton_2.setText(_translate("Form", "Кумите\nне работает"))


# Run main loop
if __name__ == "__main__":
    Form0 = QtWidgets.QWidget()
    ui0 = Ui_Form0()
    ui0.setupUi0(Form0)
    Form0.show()
    sys.exit(app.exec_())