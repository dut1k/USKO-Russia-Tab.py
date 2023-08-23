from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QTimer
from Kata20210324 import KataMainWindow
from Kumite20210324 import KumiteMainWindow

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


#        self.pushButton_1.clicked.connect(self.passingInformation)
#        ui2.pushButton_11.clicked.connect(self.passi)
#        ui_kata12.Calc_Button.clicked.connect(ui_kata1.passingInformation)
#        ui_kata1.Calc_Button.clicked.connect(self.print_scoore)

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Ката"))
        self.pushButton_2.setText(_translate("Form", "Кумите\nне работает"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()
        self.setupUi0(self)

        self.pushButton_1.clicked.connect(self.passinon)
        self.pushButton_2.clicked.connect(self.passi)

        self.ui_kata = KataMainWindow()
        self.ui_kumite = KumiteMainWindow()

        ##################################
        self.ui_kata.Calc_Button.clicked.connect(self.ui_kata.passingInformation)
        self.ui_kata.Clear_Button.clicked.connect(self.ui_kata.clear_Data)

        self.ui_kumite.pushButton_start.clicked.connect(self.ui_kumite.start_timer)
        self.ui_kumite.pushButton_pause.clicked.connect(self.ui_kumite.reset_timer)
        self.ui_kumite.pushButton_reset.clicked.connect(self.ui_kumite.reset_all)

        self.ui_kumite.plus5sec.clicked.connect(self.ui_kumite.upTime)
        self.ui_kumite.minus5sec.clicked.connect(self.ui_kumite.downTime)

        self.ui_kumite.score_red_0.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_1.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_2.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_3.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_4.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_5.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_red_6.toggled.connect(self.ui_kumite.onClickedR)
        self.ui_kumite.score_white_0.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_1.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_2.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_3.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_4.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_5.toggled.connect(self.ui_kumite.onClickedW)
        self.ui_kumite.score_white_6.toggled.connect(self.ui_kumite.onClickedW)

        self.ui_kumite.h_red1.toggled.connect(self.ui_kumite.penaltyButton_hmr1)
        self.ui_kumite.h_red2.clicked.connect(self.ui_kumite.penaltyButton_hmr2)
        self.ui_kumite.h_red3.clicked.connect(self.ui_kumite.penaltyButton_hmr3)
        self.ui_kumite.h_red4.clicked.connect(self.ui_kumite.penaltyButton_hmr4)

        self.ui_kumite.j_red1.toggled.connect(self.ui_kumite.penaltyButton_jr1)
        self.ui_kumite.j_red2.clicked.connect(self.ui_kumite.penaltyButton_jr2)
        self.ui_kumite.j_red3.clicked.connect(self.ui_kumite.penaltyButton_jr3)
        self.ui_kumite.j_red4.clicked.connect(self.ui_kumite.penaltyButton_jr4)

        self.ui_kumite.h_white1.toggled.connect(self.ui_kumite.penaltyButton_hmw1)
        self.ui_kumite.h_white2.clicked.connect(self.ui_kumite.penaltyButton_hmw2)
        self.ui_kumite.h_white3.clicked.connect(self.ui_kumite.penaltyButton_hmw3)
        self.ui_kumite.h_white4.clicked.connect(self.ui_kumite.penaltyButton_hmw4)

        self.ui_kumite.j_white1.toggled.connect(self.ui_kumite.penaltyButton_jw1)
        self.ui_kumite.j_white2.clicked.connect(self.ui_kumite.penaltyButton_jw2)
        self.ui_kumite.j_white3.clicked.connect(self.ui_kumite.penaltyButton_jw3)
        self.ui_kumite.j_white4.clicked.connect(self.ui_kumite.penaltyButton_jw4)
######################################

    def passinon(self):
        self.ui_kata.openSecondWin()
        self.ui_kata.show()


    def passi(self):
        self.ui_kumite.openSecondWinKumite()
        self.ui_kumite.show()


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

    







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui0 = MenuWindow()
    ui0.show()
    sys.exit(app.exec_())