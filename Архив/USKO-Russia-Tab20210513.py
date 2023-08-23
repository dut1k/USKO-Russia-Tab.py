from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox
# from openpyxl import load_workbook
import pandas as pd
# import numpy as np
# import winsound
# import time
from Kata_final import KataMainWindow
from Kata_qual import KataQual_MainWindow
from Kumite import KumiteMainWindow
import resources


class Ui_Form0(object):
    def setupUi0(self, Form0):
        Form0.setObjectName("Form00")
        Form0.setEnabled(True)
        Form0.setFixedSize(900, 500)
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
        self.combo.hide()
        self.combo.setMaxCount(30)
        self.combo.setObjectName("combo")

        self.file = str()
        self.user_choise = str()
        self.user_choise_list = list()
        self.xl = str()
        self.x = int()

        self.pushButton_select_file.setGeometry(QtCore.QRect(60, 50, 200, 30))
        self.pushButton_select_file.setToolTip('Можно загрузить файл со сводными списками в Excel')
        self.pushButton_select_file.setStyleSheet("font-family: Gotham-Light; font-size: 15px;")
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

        self.status_file.setGeometry(QtCore.QRect(60, 90, 780, 30))
        self.status_file.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10pt;")
        self.status_file.setObjectName("status_file")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form0", "Form"))
        self.status_file.setText(_translate("Form0", "Выберите файл"))
        self.pushButton_select_file.setText(_translate("Form0", "Выбрать файл"))
        self.pushButton_Kata_qual.setText(_translate("Form0", "Ката по флажкам"))
        self.pushButton_Kata_final.setText(_translate("Form0", "Ката финал"))
        self.pushButton_Kumite.setText(_translate("Form0", "Кумите"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()
        self.setupUi0(self)

        self.TempSet = set()
        self.df_Single_list = []

        self.individ_kata_dict = {}
        self.individ_kata_male_dict = {}
        self.individ_kata_female_dict = {}
        self.individ_kumite_dict = {}
        self.individ_kumite_male_dict = {}
        self.individ_kumite_female_dict = {}
        self.team_kata_dict = {}
        self.team_kata_male_dict = {}
        self.team_kata_female_dict = {}
        self.team_kumite_dict = {}
        self.team_kumite_male_dict = {}
        self.team_kumite_female_dict = {}
        self.male_label_dict = {}
        self.female_label_dict = {}
        self.sportsmans_ages_dict = {}
        self.matchName_dict = {}

        self.pushButton_Kata_qual.clicked.connect(self.showKataQualWin)
        self.pushButton_Kata_final.clicked.connect(self.showKataFinalWin)
        self.pushButton_Kumite.clicked.connect(self.showKumiteWin)

        self.combo.activated[str].connect(self.userChoise)

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

        self.ui_kataQual.pushButton_clearData.clicked.connect(self.ui_kataQual.clearKataData)
        self.ui_kataQual.pushButton_NewCategory.clicked.connect(self.ui_kataQual.NewCategory)
        self.ui_kataQual.pushButton_NewCategory.clicked.connect(self.calcTabKata_Reset)

        self.ui_kataQual.male.clicked.connect(self.useExportDataKataQualMale)
        self.ui_kataQual.female.clicked.connect(self.useExportDataKataQualFemale)
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansRed)
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansWhite)
        self.ui_kataQual.comboBox_name_red_1.activated[str].connect(self.setLabelRed)
        self.ui_kataQual.comboBox_name_white_1.activated[str].connect(self.setLabelWhite)

        self.ui_kataQual.pushButton_showData.clicked.connect(self.kata_Qual_matchName)
        self.ui_kataQual.pushButton_showData.clicked.connect(self.ui_kataQual.setDataKata)

        self.ui_kataQual.winnerRed.toggled.connect(self.ui_kataQual.setWinnerRed)
        self.ui_kataQual.winnerWhite.toggled.connect(self.ui_kataQual.setWinnerWhite)

        self.ui_kataFinal.Calc_Button.clicked.connect(self.ui_kataFinal.passingInformation)
        self.ui_kataFinal.Clear_Button.clicked.connect(self.ui_kataFinal.clearKataData)

        self.ui_kataFinal.male.clicked.connect(self.useExportDataKataFinalMale)
        self.ui_kataFinal.female.clicked.connect(self.useExportDataKataFinalFemale)
        self.ui_kataFinal.comboBox_age.activated[str].connect(self.calcTabKataFinalSpotrsmansRed)
        self.ui_kataFinal.comboBox_name_red_1.activated[str].connect(self.setLabelRedkataFinal)

        self.ui_kataFinal.pushButton_showData.clicked.connect(self.kata_Final_matchName)
        self.ui_kataFinal.pushButton_showData.clicked.connect(self.ui_kataFinal.setDataKata)

        self.ui_kataQual.MenuButton.clicked.connect(self.showKataQualMenu)
        self.ui_kataFinal.MenuButton.clicked.connect(self.showKataFinalMenu)
        self.ui_kumite.MenuButton.clicked.connect(self.showKumiteMenu)

        ########   в окне КАТА отб. кнопка ГЛАВНОЕ МЕНЮ
        self.ui_KataQualMenu.buttonBox.accepted.connect(self.showMainMenu)
        self.ui_KataQualMenu.buttonBox.accepted.connect(self.ui_kataQual.NewCategory)

        ########   в окне КАТА отб. кнопка КАТА ФИНАЛ
        self.ui_kataQual.KataFinalButton.clicked.connect(self.showDialogWindowKataQualToKataFinal)
        self.ui_KataQualToKataFinal.buttonBox.accepted.connect(self.ui_kataQual.NewCategory)
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

    def clearDataMember(self):
        self.TempSet = set()
        self.df_Single_list = []
        self.individ_kata_dict = {}
        self.individ_kata_male_dict = {}
        self.individ_kata_female_dict = {}
        self.individ_kumite_dict = {}
        self.individ_kumite_male_dict = {}
        self.individ_kumite_female_dict = {}
        self.team_kata_dict = {}
        self.team_kata_male_dict = {}
        self.team_kata_female_dict = {}
        self.team_kumite_dict = {}
        self.team_kumite_male_dict = {}
        self.team_kumite_female_dict = {}
        self.male_label_dict = {}
        self.female_label_dict = {}
        self.sportsmans_ages_dict = {}
        self.matchName_dict = {}

    def select_file(self):
        try:
            self.combo.clear()

            self.file, _ = QFileDialog.getOpenFileName(self, 'Открыть файл со сводными списками в формате *xlsx', './',
                                                  "Excel (*.xlsx)")
            filename = str(self.file.split('/')[len(self.file.split('/')) - 1])
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 10pt;")
            self.status_file.setText('Файл обрабатывается')
            self.xl = pd.ExcelFile(self.file)

            if len(self.xl.sheet_names) > 1:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 10pt;")
                self.status_file.setText(f'В файле  <b>{filename}</b> несколько листов, выберите нужный')
                self.combo.setGeometry(QtCore.QRect(60, 130, 350, 22))
                self.combo.show()
                self.combo.addItems(['-Выберите лист-'] + self.xl.sheet_names)

            else:
                self.combo.hide()
                self.user_choise = 0
                self.data_processing()
        except:
            if self.sportsmans_ages_dict != {}:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 10pt;")
                self.status_file.setText(f'Файл  <b>{filename}</b> загружен')
                return
            else:
                # self.status_file.setText("Выберите файл")
                return
                # self.combo.hide()
                # self.combo.clear()
                # self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 10pt;")
                # self.status_file.setText('Файл не выбран')
                #
                # self.clearDataMember()

            # else:
            #     self.combo.clear()

    def userChoise(self):
        self.user_choise_list = ['-Выберите лист-'] + self.xl.sheet_names
        self.user_choise = self.user_choise_list.index(self.combo.currentText()) - 1
        self.data_processing()

    def data_processing(self):
        filename = str(self.file.split('/')[len(self.file.split('/')) - 1])

        if self.file:
            try:
                sheet1 = pd.read_excel(self.file, sheet_name= self.xl.sheet_names[self.user_choise])
                cols2skip = [4, 5, 6, 7]
                cols = [i for i in range(len(sheet1.columns) - 2) if i not in cols2skip]
                k = []
                for z in range(10, len(sheet1.columns) + 4):
                    k.append('a' + str(z))
                sheet = pd.read_excel(self.file, usecols=cols, header=None, names=k)
                kat_name = set(sheet.columns) - {'a10', 'a11', 'a12', 'a13'}
                list_kat_name = list(sorted(kat_name))

                df_Single_names = []
                self.df_Single_list = []
                df_Group_names = []
                df_Group_list = []

                for k_n in list_kat_name:
                    # ЛИЧНЫЕ СОРЕВНОВАНИЯ
                    # Поиск строк со значением "*" в столбце "k_n"
                    #           (Поиск всех смортсменов, у которых в категории (столбце "k_n") поставлена ЗВЕЗДОЧКА "*")
                    df2 = sheet.loc[sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]
                    # Создание словаря из найденых спортсменов
                    df_Temp_Single_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                       'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                    # КОМАНДНЫЕ СОРЕВНОВАНИЯ
                    # Если в столбце "k_n" пустой словарь, то осуществляется поиск строк со значением "ком1, ком2 и тд"
                    #                                               (Поиск всех смортсменов в командных соревнованиях)
                    if df_Temp_Single_list == {}:
                        df2 = sheet.loc[sheet[k_n] == 'ком1', ['a10', 'a11', 'a12', 'a13']]
                        df_Temp1_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                                      'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                        df2 = sheet.loc[sheet[k_n] == 'ком2', ['a10', 'a11', 'a12', 'a13']]
                        df_Temp2_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                                      'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                        df2 = sheet.loc[sheet[k_n] == 'ком3', ['a10', 'a11', 'a12', 'a13']]
                        df_Temp3_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                                      'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                        df2 = sheet.loc[sheet[k_n] == 'ком4', ['a10', 'a11', 'a12', 'a13']]
                        df_Temp4_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                                      'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                        df2 = sheet.loc[sheet[k_n] == 'ком5', ['a10', 'a11', 'a12', 'a13']]
                        df_Temp5_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                                      'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                        df_Temp1_Group_list = df_Temp1_Group_list | df_Temp2_Group_list | \
                                              df_Temp3_Group_list | df_Temp4_Group_list | df_Temp5_Group_list
                        df_Group_list.append(df_Temp1_Group_list)

                    df_Single_names.append(k_n)
                    df_Group_names.append(k_n)
                    self.df_Single_list.append(df_Temp_Single_list)  ################################################################



                self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 10pt;")
                self.status_file.setText(f'Файл  <b>{filename}</b> загружен')
                # self.combo.addItems(sorted(self.df_Single_list[0]))
                # self.combo.addItems(sorted(df_list33[0]))
            #               self.combo.addItems(sorted(self.df_Single_list[0]))
# Ката личн     ############################################
                individ_kata = sheet.loc[[3]].where(sheet == 'один').dropna(how='all').dropna(axis=1)
                # print('Личное ката', len(individ_kata.columns.tolist()), individ_kata.index.tolist(),
                #       'individ_kata.columns', individ_kata.columns.tolist())

                sss = []
                for i in range(1, len(individ_kata.columns.tolist()) + 1):
                    sss.append('КатаЛич')
                self.individ_kata_dict = dict(zip(individ_kata.columns.tolist(), sss))
                # print(individ_kata_dict)
#Кумите личн    ############################################
                individ_kumite = sheet.loc[[3]].where(sheet == 'личн').dropna(how='all').dropna(axis=1)
                # print('Личное кумите', len(individ_kumite.columns.tolist()), individ_kumite.index.tolist(),
                #       'individ_kumite.columns', individ_kumite.columns.tolist())

                sss = []
                for i in range(1, len(individ_kumite.columns.tolist()) + 1):
                    sss.append('КумитеЛич')
                self.individ_kumite_dict = dict(zip(individ_kumite.columns.tolist(), sss))
                # print(individ_kumite_dict)
# Ката груп     ############################################
                team_kata = sheet.loc[[3]].where(sheet == 'груп').dropna(how='all').dropna(axis=1)
                # print('Командное ката', len(team_kata.columns.tolist()), team_kata.index.tolist(), 'team_kata.columns',
                #       team_kata.columns.tolist())

                sss = []
                for i in range(1, len(team_kata.columns.tolist()) + 1):
                    sss.append('КатаКом')
                self.team_kata_dict = dict(zip(team_kata.columns.tolist(), sss))
                # print(team_kata_dict)
# Кумите личн   ############################################
                team_kumite = sheet.loc[[3]].where(sheet == 'ком').dropna(how='all').dropna(axis=1)
                # print('Командное кумите', len(team_kumite.columns.tolist()), team_kumite.index.tolist(),
                #       'team_kumite.columns', team_kumite.columns.tolist())

                sss = []
                for i in range(1, len(team_kumite.columns.tolist()) + 1):
                    sss.append('КумитеКом')
                self.team_kumite_dict = dict(zip(team_kumite.columns.tolist(), sss))
                # print(team_kumite_dict)
# М             ############################################
                male_label = sheet.loc[[7]].where(sheet == 'м').dropna(how='all').dropna(axis=1)
                # print('Мужчины', len(male_label.columns.tolist()), male_label.index.tolist(), 'male_label.columns',
                #       male_label.columns.tolist())

                sss = []
                for i in range(1, len(male_label.columns.tolist()) + 1):
                    sss.append('Мужчины')
                self.male_label_dict = dict(zip(male_label.columns.tolist(), sss))
                # print(male_label_dict)
# Ж             ############################################
                female_label = sheet.loc[[7]].where(sheet == 'ж').dropna(how='all').dropna(axis=1)
                # print('Женщины', len(female_label.columns.tolist()), female_label.index.tolist(),
                #       'female_label.columns', female_label.columns.tolist())

                sss = []
                for i in range(1, len(female_label.columns.tolist()) + 1):
                    sss.append('Женщины')
                self.female_label_dict = dict(zip(female_label.columns.tolist(), sss))
                # print('female_label_dict =', self.female_label_dict)
# Все возроста  ############################################
                self.sportsmans_ages_dict = sheet.iloc[4].to_dict()
                list(map(self.sportsmans_ages_dict.__delitem__,
                         filter(self.sportsmans_ages_dict.__contains__, ('a10', 'a11', 'a12', 'a13'))))
                print('sheet.iloc[4].to_dict()', self.sportsmans_ages_dict)
# Ката М личн   ############################################
                self.individ_kata_male_dict = self.individ_kata_dict.copy()
                for g in set(self.female_label_dict):
                    if g in self.individ_kata_male_dict:
                        self.individ_kata_male_dict.pop(g)
# Ката Ж личн   ############################################
                self.individ_kata_female_dict = self.individ_kata_dict.copy()
                for g in set(self.male_label_dict):
                    if g in self.individ_kata_female_dict:
                        self.individ_kata_female_dict.pop(g)
# Кумите М личн ############################################
                self.individ_kumite_male_dict = self.individ_kumite_dict.copy()
                for g in set(self.female_label_dict):
                    if g in self.individ_kumite_male_dict:
                        self.individ_kumite_male_dict.pop(g)
# Кумите Ж личн ############################################
                self.individ_kumite_female_dict = self.individ_kumite_dict.copy()
                for g in set(self.male_label_dict):
                    if g in self.individ_kumite_female_dict:
                        self.individ_kumite_female_dict.pop(g)
# конструктор для matchName ############################################
                self.matchName_dict1 = sheet.iloc[0].to_dict()
                list(map(self.matchName_dict1.__delitem__,
                         filter(self.matchName_dict1.__contains__, ('a10', 'a11', 'a12', 'a13'))))
                print('matchName_dict1', self.matchName_dict1)
                self.matchName_dict2 = sheet.iloc[4].to_dict()
                list(map(self.matchName_dict2.__delitem__,
                         filter(self.matchName_dict2.__contains__, ('a10', 'a11', 'a12', 'a13'))))
                print('matchName_dict2', self.matchName_dict2)
                list1 = [self.matchName_dict1, self.matchName_dict2]
                keylist = list1[0].keys()
                self.matchName = dict((k, str.capitalize(' '.join(list(map(lambda d: d[k], list1))))) for k in keylist)
                print('mydata =', self.matchName)

                # print()

            except:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 10pt;")
                self.status_file.setText('Выбран неверный файл или лист')

    # def calcTabKataSpotrsmans(self):
    #     sender = self.sender()
    #     if sender.text() == "М":  # pushButton pressed:
    #         someDict = self.female_label_dict
    #     if sender.text() == "Ж":  # pushButton pressed:
    #         someDict = self.male_label_dict
    #     self.ui_kataQual.clearKataData()
    #     self.TempSet.clear()
    #     self.TempSet = set(self.individ_kata_dict) - set(someDict)
    #     self.ui_kataQual.comboBox_age.setEnabled(True)
    #     self.ui_kataQual.comboBox_age.clear()
    #     self.ui_kataQual.comboBox_age.setStyleSheet("background-color: white")
    #     self.ui_kataQual.age_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 10pt;")
    #     self.ui_kataQual.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
    #     self.ui_kataQual.name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
    #     self.ui_kataQual.comboBox_name_red_1.setStyleSheet("background-color: rgb(242, 242, 242)")
    #     self.ui_kataQual.comboBox_name_white_1.setStyleSheet("background-color: rgb(242, 242, 242)")
    #     self.ui_kataQual.comboBox_name_red_1.setEnabled(False)
    #     self.ui_kataQual.comboBox_name_red_1.clear()
    #     self.ui_kataQual.comboBox_name_white_1.setEnabled(False)
    #     self.ui_kataQual.comboBox_name_white_1.clear()
    #     self.ui_kataQual.comboBox_age.addItems(sorted([self.sportsmans_ages_dict[x] for x in self.TempSet]))
    #     # self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansRed)
    #     # self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansWhite)

    def useExportDataKataQualMale(self):
        someDict =self.female_label_dict
        dict_KataOrKumite = self.individ_kata_dict
        comboBox_age = self.ui_kataQual.comboBox_age
        age_1 = self.ui_kataQual.age_1
        name_red_1 = self.ui_kataQual.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(someDict, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                          name_white_1, comboBox_name_red_1, comboBox_name_white_1)

    def useExportDataKataQualFemale(self):
        someDict =self.male_label_dict
        dict_KataOrKumite = self.individ_kata_dict
        comboBox_age = self.ui_kataQual.comboBox_age
        age_1 = self.ui_kataQual.age_1
        name_red_1 = self.ui_kataQual.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(someDict, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                          name_white_1, comboBox_name_red_1, comboBox_name_white_1)


    def useExportDataKataFinalMale(self):
        someDict =self.female_label_dict
        dict_KataOrKumite = self.individ_kata_dict
        comboBox_age = self.ui_kataFinal.comboBox_age
        age_1 = self.ui_kataFinal.age_1
        name_red_1 = self.ui_kataFinal.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataFinal.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(someDict, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                          name_white_1, comboBox_name_red_1, comboBox_name_white_1)

    def useExportDataKataFinalFemale(self):
        someDict =self.male_label_dict
        dict_KataOrKumite = self.individ_kata_dict
        comboBox_age = self.ui_kataFinal.comboBox_age
        age_1 = self.ui_kataFinal.age_1
        name_red_1 = self.ui_kataFinal.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataFinal.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(someDict, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                          name_white_1, comboBox_name_red_1, comboBox_name_white_1)



    def calcTabKataSpotrsmans(self, someDict, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                              name_white_1, comboBox_name_red_1, comboBox_name_white_1):
    # def calcTabKataSpotrsmans(self, x):
        # sender = self.sender()
        # if sender.text() == "М":  # pushButton pressed:
        #     someDict = self.female_label_dict
        # if sender.text() == "Ж":  # pushButton pressed:
        #     someDict = self.male_label_dict

        self.ui_kataQual.clearKataData()
        self.TempSet.clear()
        self.TempSet = set(dict_KataOrKumite) - set(someDict)
        comboBox_age.setEnabled(True)
        comboBox_age.clear()
        comboBox_age.setStyleSheet("background-color: white")
        age_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 10pt;")
        name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
        name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
        comboBox_name_red_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        comboBox_name_white_1.setStyleSheet("background-color: rgb(242, 242, 242)")
        comboBox_name_red_1.setEnabled(False)
        comboBox_name_red_1.clear()
        comboBox_name_white_1.setEnabled(False)
        comboBox_name_white_1.clear()
        comboBox_age.addItems(sorted([self.sportsmans_ages_dict[x] for x in self.TempSet]))
        # self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansRed)
        # self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansWhite)

    def calcTabKataFinalSpotrsmansRed(self):
        self.calcTab(self.ui_kataFinal.name_red_1, self.ui_kataFinal.comboBox_name_red_1)

    def calcTabKataSpotrsmansRed(self):
        self.calcTab(self.ui_kataQual.name_red_1, self.ui_kataQual.comboBox_name_red_1)

    def calcTabKataSpotrsmansWhite(self):
        self.calcTab(self.ui_kataQual.name_white_1, self.ui_kataQual.comboBox_name_white_1)

    def calcTab(self, name, comboBox_name):
        comboBox_name.clear()
        if name == self.ui_kataQual.name_red_1:
            n = self.ui_kataQual.comboBox_age.currentText()
        elif name == self.ui_kataQual.name_white_1:
            n = self.ui_kataQual.comboBox_age.currentText()
        elif name == self.ui_kataFinal.name_red_1:
            n = self.ui_kataFinal.comboBox_age.currentText()
        elif name == self.ui_kataFinal.name_white_1:
            n = self.ui_kataFinal.comboBox_age.currentText()
        self.ui_kataQual.matchName1.setText('Татами №#, ' + self.matchName[list(self.matchName.keys())[self.x]])


        a2 = {k: v for k, v in zip(sorted(list(self.TempSet)), sorted([self.sportsmans_ages_dict[x] for x in self.TempSet]))}
        self.x = list(self.sportsmans_ages_dict.keys()).index(list(a2.keys())[list(a2.values()).index(n)])
        name.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 10pt;")
        comboBox_name.setStyleSheet("background-color: white")
        comboBox_name.addItems(sorted(self.df_Single_list[self.x]))
        comboBox_name.setEnabled(True)


    def setLabelRed(self):
        print('RED')
        name = self.df_Single_list[self.x].get(self.ui_kataQual.comboBox_name_red_1.currentText())
#это конструктор имя, состоящий из Фамилии и первого символа Имя
#''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.'])
        self.ui_kataQual.lineEdit_name_red_1.setText(''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.']))
        self.ui_kataQual.lineEdit_region_red_1.setText(name.split('a11')[1])

    def setLabelRedkataFinal(self):
        print('RED')
        name = self.df_Single_list[self.x].get(self.ui_kataFinal.comboBox_name_red_1.currentText())
        # это конструктор имя, состоящий из Фамилии и первого символа Имя
        # ''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.'])
        self.ui_kataFinal.lineEdit_name_red_1.setText(
            ''.join([name.replace('a12', '').split('a13')[0], ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
        self.ui_kataFinal.lineEdit_region_red_1.setText(name.split('a11')[1])



#     def setLabelRed(self):
#         print('RED')
#         name = self.df_Single_list[self.x].get(self.ui_kataQual.comboBox_name_red_1.currentText())
# #это конструктор имя, состоящий из Фамилии и первого символа Имя
# #''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.'])
#         self.ui_kataQual.lineEdit_name_red_1.setText(''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.']))
#         self.ui_kataQual.lineEdit_region_red_1.setText(name.split('a11')[1])

    def setLabelWhite(self):
        print('WHITE')
        name = str(self.df_Single_list[self.x].get(self.ui_kataQual.comboBox_name_white_1.currentText()))
        self.ui_kataQual.lineEdit_name_white_1.setText(''.join([name.replace('a12','').split('a13')[0], ' '+name.split('a13')[1].split('a11')[0][0]+'.']))
        self.ui_kataQual.lineEdit_region_white_1.setText(name.split('a11')[1])




    def calcTabKata_Reset(self):
        self.TempSet |= set(self.individ_kata_dict) #добавляем в пустой список все столбцы что

    def kata_Qual_matchName(self):
        try:
            if len(self.ui_kataQual.matchName1.text().split(', ')) > 1:
                kk = self.ui_kataQual.matchName1.text().split(', ')[0]
                print('len(kk) =', len(self.ui_kataQual.matchName1.text().split(', ')))
                print('kk =', kk)
                print('222= ', kk, self.matchName[list(self.matchName.keys())[self.x]])
                self.ui_kataQual.matchName1.setText(kk + ', ' + self.matchName[list(self.matchName.keys())[self.x]])
            else:
                print('333')
                self.ui_kataQual.matchName1.setText(self.matchName[list(self.matchName.keys())[self.x]])
        # self.ui_kataQual.matchName1.setText(kk.split(', ')[0] + self.matchName[list(self.matchName.keys())[self.x]])
        except:
            print('444')
            pass

    def kata_Final_matchName(self):
        try:
            if len(self.ui_kataFinal.matchName1.text().split(', ')) > 1:
                kk = self.ui_kataFinal.matchName1.text().split(', ')[0]
                print('len(k) =', len(self.ui_kataFinal.matchName1.text().split(', ')))
                print('k =', kk)
                print('2= ', kk, self.matchName[list(self.matchName.keys())[self.x]])
                self.ui_kataFinal.matchName1.setText(kk + ', ' + self.matchName[list(self.matchName.keys())[self.x]])
            else:
                print('3')
                self.ui_kataFinal.matchName1.setText(self.matchName[list(self.matchName.keys())[self.x]])
        # self.ui_kataQual.matchName1.setText(kk.split(', ')[0] + self.matchName[list(self.matchName.keys())[self.x]])
        except:
            print('4')
            pass


    def showKataQualWin(self):
        self.closeAllWin()
        self.ui_kataQual.openSecondWin()
        self.ui_kataQual.show()
        self.close()
        if self.sportsmans_ages_dict == {}:
            self.ui_kataQual.sex_1.hide()
            self.ui_kataQual.age_1.hide()
            self.ui_kataQual.comboBox_age.hide()
            self.ui_kataQual.comboBox_name_red_1.hide()
            self.ui_kataQual.comboBox_name_white_1.hide()
            self.ui_kataQual.male.hide()
            self.ui_kataQual.female.hide()
            self.ui_kataQual.name_red_1.hide()
            self.ui_kataQual.name_white_1.hide()
        else:
            self.ui_kataQual.sex_1.show()
            self.ui_kataQual.age_1.show()
            self.ui_kataQual.comboBox_age.show()
            self.ui_kataQual.comboBox_name_red_1.show()
            self.ui_kataQual.comboBox_name_white_1.show()
            self.ui_kataQual.male.show()
            self.ui_kataQual.female.show()
            self.ui_kataQual.name_red_1.show()
            self.ui_kataQual.name_white_1.show()



    def showKataFinalWin(self):
        self.closeAllWin()
        self.ui_kataFinal.openSecondWin()
        self.ui_kataFinal.show()
        self.close()
        if self.sportsmans_ages_dict == {}:
            self.ui_kataFinal.sex_1.hide()
            self.ui_kataFinal.age_1.hide()
            self.ui_kataFinal.comboBox_age.hide()
            self.ui_kataFinal.comboBox_name_red_1.hide()
            self.ui_kataFinal.male.hide()
            self.ui_kataFinal.female.hide()
            self.ui_kataFinal.name_red_1.hide()
        else:
            self.ui_kataFinal.sex_1.show()
            self.ui_kataFinal.age_1.show()
            self.ui_kataFinal.comboBox_age.show()
            self.ui_kataFinal.comboBox_name_red_1.show()
            self.ui_kataFinal.male.show()
            self.ui_kataFinal.female.show()
            self.ui_kataFinal.name_red_1.show()

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
        Dialog.setFixedSize(400, 120)
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
