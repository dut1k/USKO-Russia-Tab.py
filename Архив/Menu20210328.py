from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from Kata import KataMainWindow
from Kumite import KumiteMainWindow
import resources2


class Ui_Form0(object):
    def setupUi0(self, Form0):
        Form0.setObjectName("Form00")
        Form0.setEnabled(True)
        Form0.resize(901, 500)
        Form0.setWindowOpacity(1.0)
        Form0.setToolTipDuration(-1)
        Form0.setStatusTip("")
        Form0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Kata = QtWidgets.QPushButton(Form0)
        self.pushButton_Kata.setGeometry(QtCore.QRect(200, 350, 150, 50))
        self.pushButton_Kata.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 35px; ")
        self.pushButton_Kata.setObjectName("pushButton_Kata")
        self.pushButton_Kumite = QtWidgets.QPushButton(Form0)
        self.pushButton_Kumite.setGeometry(QtCore.QRect(500, 350, 200, 50))
        self.pushButton_Kumite.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 35px; ")
        self.pushButton_Kumite.setObjectName("pushButton_Kumite")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)


    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Kata.setText(_translate("Form", "Ката"))
        self.pushButton_Kumite.setText(_translate("Form", "Кумите"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()
        self.setupUi0(self)

        self.pushButton_Kata.clicked.connect(self.showKataWin)
        self.pushButton_Kumite.clicked.connect(self.showKumiteWin)

        self.ui_kata = KataMainWindow()
        self.ui_kumite = KumiteMainWindow()
        self.ui_dialogKata = KataToKumite()
        self.ui_dialogKumite = KumiteToKata()
        self.ui_KataMenu = KataMenu()
        self.ui_KumiteMenu = KumiteMenu()

        self.ui_kata.Calc_Button.clicked.connect(self.ui_kata.passingInformation)
        self.ui_kata.Clear_Button.clicked.connect(self.ui_kata.clearKataData)

        self.ui_kata.MenuButton.clicked.connect(self.showKataMenu)
        self.ui_kumite.MenuButton.clicked.connect(self.showKumiteMenu)

        self.ui_dialogKumite.buttonBox.accepted.connect(self.ui_kata.clearKataData)
        self.ui_dialogKumite.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_dialogKumite.buttonBox.accepted.connect(self.showKataWin)

        self.ui_dialogKata.buttonBox.accepted.connect(self.ui_kata.clearKataData)
        self.ui_dialogKata.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_dialogKata.buttonBox.accepted.connect(self.showKumiteWin)

        self.ui_KataMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KataMenu.buttonBox.accepted.connect(self.ui_kata.clearKataData)
        self.ui_KumiteMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KumiteMenu.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)

        self.ui_kata.KumiteButton.clicked.connect(self.showDialogWindowKata)
        self.ui_kumite.KataButton.clicked.connect(self.showDialogWindowKumite)

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

    def showKataWin(self):
        self.ui_kumite.closeSecondWinKumite()
        self.ui_kumite.close()
        self.ui_kata.openSecondWin()
        self.ui_kata.show()
        self.close()


    def showKumiteWin(self):
        self.ui_kata.closeSecondWin()
        self.ui_kata.close()
        self.ui_kumite.openSecondWinKumite()
        self.ui_kumite.show()
        self.close()

    def showDialogWindowKata(self):
        self.ui_dialogKata.show()

    def showDialogWindowKumite(self):
        self.ui_dialogKumite.show()

    def showKataMenu(self):
        self.ui_KataMenu.show()

    def showKumiteMenu(self):
        self.ui_KumiteMenu.show()

    def showMainMenu(self):
        self.ui_kata.closeSecondWin()
        self.ui_kata.close()
        self.ui_kumite.closeSecondWinKumite()
        self.ui_kumite.close()
        self.show()


class dialogWindow_Ui(object):
    def setupUi_dialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        Dialog.setStyleSheet("background-color: white;")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(125, 70, 150, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(62, 106, 225); font-family: Gotham-Light;"
                                     "color: white;  font-size: 15pt;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 20, 400, 20))
        self.label.setStyleSheet("font-family: Gotham-Light; font-size: 15pt;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(0, 40, 400, 20))
        self.label2.setStyleSheet("font-family: Gotham-Light; font-size: 7;")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label")

        self.buttonBox.rejected.connect(Dialog.close)

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label2.setText(_translate("Dialog", "TextLabel"))


class KataToKumite(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно Кумите?")
        self.label2.setText("Окно Ката закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно Ката закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KumiteToKata(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно Ката?")
        self.label2.setText("Окно Кумите закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KumiteMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно Кумите закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Light.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Medium.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Bold.ttf")
    ui0 = MenuWindow()
    ui0.show()
    sys.exit(app.exec_())
