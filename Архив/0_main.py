import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QTimer

from Kata20210321 import KataMainWindow
from Kata20210321 import KataSecondWindow
from Kumite20210320 import KumiteMainWindow

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init UI Kata
Form111 = QtWidgets.QWidget()
ui_kata1 = KataMainWindow()
ui_kata1.setupUi(Form111)
#Form12 = QtWidgets.QWidget()
#ui_kata2 = KataSecondWindow()
#ui_kata2.setupUi_Kata2(Form12)
#demo.show()

# Create form and init UI Kumite
Form2 = KumiteMainWindow()
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
        self.pushButton_1.clicked.connect(self.passingInformation)
        self.pushButton_2.clicked.connect(self.passi)
#        self.pushButton_1.clicked.connect(self.passingInformation)
#        ui2.pushButton_11.clicked.connect(self.passi)

    def passingInformation(self):
#        Form12.show()
        Form111.show()

    def passi(self):
        Form.show()


    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "1111"))
        self.pushButton_2.setText(_translate("Form", "2222"))


# Run main loop
if __name__ == "__main__":
    Form0 = QtWidgets.QWidget()
    ui0 = Ui_Form0()
    ui0.setupUi0(Form0)
    Form0.show()
    sys.exit(app.exec_())