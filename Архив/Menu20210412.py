from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import winsound
import time
from Kata_final import KataMainWindow
from Kata_qual import KataQual_MainWindow
from Kumite import KumiteMainWindow
import resources2


class Ui_Form0(object):
    def setupUi0(self, Form0):
        Form0.setObjectName("Form00")
        Form0.setEnabled(True)
        Form0.resize(900, 500)
        Form0.setWindowOpacity(1.0)
        Form0.setToolTipDuration(-1)
        Form0.setStatusTip("")
        Form0.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pushButton_select_file = QtWidgets.QPushButton(Form0)
        self.pushButton_Kata_qual = QtWidgets.QPushButton(Form0)
        self.pushButton_Kata_final = QtWidgets.QPushButton(Form0)
        self.pushButton_Kumite = QtWidgets.QPushButton(Form0)
        self.status_file = QtWidgets.QLabel(Form0)

        self.combo = QComboBox(self)
#        self.combo.addItems(None)
        self.combo.setGeometry(QtCore.QRect(60, 150, 350, 22))
        self.combo.setMaxCount(30)
        self.combo.setObjectName("combo")

        self.pushButton_select_file.setGeometry(QtCore.QRect(60, 50, 200, 30))
        self.pushButton_select_file.setStyleSheet("font-family: Gotham-Light; font-size: 15px; ")
        self.pushButton_select_file.setObjectName("pushButton_Kata_qual")

        self.pushButton_Kata_qual.setGeometry(QtCore.QRect(100, 350, 350, 50))
        self.pushButton_Kata_qual.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 35px; ")
        self.pushButton_Kata_qual.setObjectName("pushButton_Kata_qual")

        self.pushButton_Kata_final.setGeometry(QtCore.QRect(100, 410, 350, 50))
        self.pushButton_Kata_final.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 35px; ")
        self.pushButton_Kata_final.setObjectName("pushButton_Kata_final")

        self.pushButton_Kumite.setGeometry(QtCore.QRect(500, 350, 200, 50))
        self.pushButton_Kumite.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 35px; ")
        self.pushButton_Kumite.setObjectName("pushButton_Kumite")

        self.status_file.setGeometry(QtCore.QRect(60, 90, 700, 30))
        self.status_file.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10pt;")
        self.status_file.setObjectName("status_file")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form0", "Form"))
        self.status_file.setText(_translate("Form0", "Выбрать файл"))
        self.pushButton_select_file.setText(_translate("Form0", "Выбрать файл"))
        self.pushButton_Kata_qual.setText(_translate("Form0", "Ката по флажкам"))
        self.pushButton_Kata_final.setText(_translate("Form0", "Ката финал"))
        self.pushButton_Kumite.setText(_translate("Form0", "Кумите"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()
        self.setupUi0(self)

        self.pushButton_Kata_qual.clicked.connect(self.showKataQualWin)
        self.pushButton_Kata_final.clicked.connect(self.showKataFinalWin)
        self.pushButton_Kumite.clicked.connect(self.showKumiteWin)

        self.ui_kataQual = KataQual_MainWindow()  # Окна с КАТА по флажкам
        self.ui_kataFinal = KataMainWindow()  # Окна с КАТА финал (по балам)
        self.ui_kumite = KumiteMainWindow()  # Окна КУМИТЕ
        self.ui_KataQualToKataFinal = KataQualToKataFinal()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "КАТА ФИНАЛ"
        self.ui_KataFinalToKataQual = KataFinalToKataQual()  # ДИАЛ.окно из КАТА ФИНАЛ при нажатии кнопки "КАТА отбороч."
        self.ui_KataFinalToKumite = KataFinalToKumite()  # ДИА.окно из КАТА ФИНАЛ при нажатии кнопки "КУМИТЕ"
        self.ui_KataQualToKumite = KataQualToKumite()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "КУМИТЕ"
        self.ui_KumiteToKataQual = KumiteToKataQual()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "КАТА отбороч."
        self.ui_KumiteToKataFinal = KumiteToKataFinal()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "КАТА ФИНАЛ"
        self.ui_KataQualMenu = KataQualMenu()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "ГАВНОЕ МЕНЮ"
        self.ui_KataFinalMenu = KataFinalMenu()  # ДИАЛ.окно из КАТА ФИНАЛ при нажатии кнопки "ГАВНОЕ МЕНЮ"
        self.ui_KumiteMenu = KumiteMenu()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "ГАВНОЕ МЕНЮ"

        self.ui_kataFinal.Calc_Button.clicked.connect(self.ui_kataFinal.passingInformation)
        self.ui_kataFinal.Clear_Button.clicked.connect(self.ui_kataFinal.clearKataData)

        self.ui_kataQual.MenuButton.clicked.connect(self.showKataQualMenu)
        self.ui_kataFinal.MenuButton.clicked.connect(self.showKataFinalMenu)
        self.ui_kumite.MenuButton.clicked.connect(self.showKumiteMenu)

        ########   в окне КАТА отб. кнопка ГЛАВНОЕ МЕНЮ
        self.ui_KataQualMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KataQualMenu.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)

        ########   в окне КАТА отб. кнопка КАТА ФИНАЛ
        self.ui_kataQual.KataFinalButton.clicked.connect(self.showDialogWindowKataQualToKataFinal)
        self.ui_KataQualToKataFinal.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KataQualToKataFinal.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataQualToKataFinal.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KataQualToKataFinal.buttonBox.accepted.connect(self.showKataFinalWin)

        ########   в окне КАТА отб. кнопка КУМИТЕ
        self.ui_kataQual.KumiteButton.clicked.connect(self.showDialogWindowKataQualToKumite)
        self.ui_KataQualToKumite.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KataQualToKumite.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataQualToKumite.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KataQualToKumite.buttonBox.accepted.connect(self.showKumiteWin)

        ########   в окне КАТА ФИНАЛ кнопка ГЛАВНОЕ МЕНЮ
        self.ui_KataFinalMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KataFinalMenu.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)

        ########   в окне КАТА ФИНАЛ кнопка КАТА отб.
        self.ui_KataFinalToKataQual.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KataFinalToKataQual.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataFinalToKataQual.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KataFinalToKataQual.buttonBox.accepted.connect(self.showKataQualWin)

        ########   в окне КАТА ФИНАЛ кнопка КУМИТЕ
        self.ui_kataFinal.KumiteButton.clicked.connect(self.showDialogWindowKataFinalToKumite)
        self.ui_KataFinalToKumite.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataFinalToKumite.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KataFinalToKumite.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KataFinalToKumite.buttonBox.accepted.connect(self.showKumiteWin)

        ########   в окне КУМИТЕ кнопка ГЛАВНОЕ МЕНЮ
        self.ui_KumiteMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KumiteMenu.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)

        ########   в окне КУМИТЕ кнопка КАТА отб.
        self.ui_KumiteToKataQual.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KumiteToKataQual.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KumiteToKataQual.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KumiteToKataQual.buttonBox.accepted.connect(self.showKataQualWin)

        ########   в окне КУМИТЕ кнопка КАТА ФИНАЛ
        self.ui_KumiteToKataFinal.buttonBox.accepted.connect(self.ui_kataFinal.clearKataData)
        self.ui_KumiteToKataFinal.buttonBox.accepted.connect(self.ui_kataQual.clearKataData)
        self.ui_KumiteToKataFinal.buttonBox.accepted.connect(self.ui_kumite.clearKumiteData)
        self.ui_KumiteToKataFinal.buttonBox.accepted.connect(self.showKataFinalWin)

        ########   в окне КАТА ФИНАЛ кнопка КАТА отб.
        self.ui_kataFinal.KataQualButton.clicked.connect(self.showDialogWindowKataFinalToKataQual)

        ########   в окне КУМИТЕ кнопка КАТА ФИНАЛ
        self.ui_kumite.KataFinalButton.clicked.connect(self.showDialogWindowKumiteToKataFinal)
        ########   в окне КУМИТЕ кнопка КАТА отб.
        self.ui_kumite.KataQualButton.clicked.connect(self.showDialogWindowKumiteToKataQual)

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

        self.pushButton_select_file.clicked.connect(self.select_file)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Открыть файл со сводными списками в формате *xlsx', './',
                                              "Excel (*.xlsx)")
        filename = str(file.split('/')[ len(file.split('/')) - 1 ])

        if file:
            try:
                sheet1 = pd.read_excel(file)
                cols2skip = [4, 5, 6, 7]
                cols = [i for i in range(len(sheet1.columns) - 2) if i not in cols2skip]
                k = []
                for z in range(10, len(sheet1.columns) + 4):
                    k.append('a' + str(z))
                sheet = pd.read_excel(file, usecols=cols, names=k)
                kat_name = set(sheet.columns) - {'a10', 'a11', 'a12', 'a13'}
                list_kat_name = list(sorted(kat_name))

#                print(list_kat_name)
                df_list = []
                df_names = []
                for k_n in list_kat_name:
                    df2 = sheet.loc[sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]
                    df_dict = dict(zip(df2.a12 + ' ' + df2.a13, df2.a11))
                    df_names.append(k_n)
                    df_list.append(df_dict)

                print(type(df_dict), df_dict)
                print(df_list)
                print(len(df_list))
                print(df_names)
                print(type(df_list), df_list)
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 15pt;")
                self.status_file.setText(f'Файл  <b>{filename}</b> загружен')
                self.combo.addItems(df_list[0])
            except:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 15pt;")
                self.status_file.setText('Выбран неверный файл')

    def showKataQualWin(self):
        self.closeAllWin()
        self.ui_kataQual.openSecondWin()
        self.ui_kataQual.show()
        self.close()

    def showKataFinalWin(self):
        self.closeAllWin()
        self.ui_kataFinal.openSecondWin()
        self.ui_kataFinal.show()
        self.close()

    def showKumiteWin(self):
        self.closeAllWin()
        self.ui_kumite.openSecondWinKumite()
        self.ui_kumite.show()
        self.close()

    def closeAllWin(self):
        self.ui_kumite.closeSecondWinKumite()
        self.ui_kumite.close()
        self.ui_kataQual.closeSecondWin()
        self.ui_kataQual.close()
        self.ui_kataFinal.closeSecondWin()
        self.ui_kataFinal.close()

    def showDialogWindowKataQualToKumite(self):
        self.ui_KataQualToKumite.show()

    def showDialogWindowKataQualToKataFinal(self):
        self.ui_KataQualToKataFinal.show()

    def showDialogWindowKataFinalToKataQual(self):
        self.ui_KataFinalToKataQual.show()

    def showDialogWindowKataQual(self):
        self.ui_dialogKataQual.show()

    def showDialogWindowKumiteToKataQual(self):
        self.ui_KumiteToKataQual.show()

    def showDialogWindowKataFinalToKumite(self):
        self.ui_KataFinalToKumite.show()

    def showDialogWindowKumiteToKataFinal(self):
        self.ui_KumiteToKataFinal.show()

    def showKataQualMenu(self):
        self.ui_KataQualMenu.show()

    def showKataFinalMenu(self):
        self.ui_KataFinalMenu.show()

    def showKumiteMenu(self):
        self.ui_KumiteMenu.show()

    def showMainMenu(self):
        self.closeAllWin()
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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


class KataQualToKumite(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Кумите</b>\"?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataQualMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataFinalToKataQual(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката по флажкам</b>\"?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataQualToKataFinal(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката финал</b>\"?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataFinalToKumite(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Кумите</b>\"?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KataFinalMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KumiteToKataFinal(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката финал</b>\"?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KumiteToKataQual(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката по флажкам</b>\"?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


class KumiteMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")
        self.buttonBox.accepted.connect(self.closeWin)

    def closeWin(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/DS-Digital.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Light.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Medium.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Bold.ttf")
    ui0 = MenuWindow()
    ui0.show()
    sys.exit(app.exec_())
