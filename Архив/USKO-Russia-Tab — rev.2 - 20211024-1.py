from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox
import pandas as pd
from Kata_final import KataMainWindow_Ui
from Kata_qual import KataQual_MainWindow_Ui
from Kumite import KumiteMainWindow_Ui
import resources


class Ui_Form0(object):
    def setupUi0(self, Form0):
        Form0.setObjectName("Form0")
        Form0.setEnabled(True)
        Form0.setFixedSize(900, 500)
        Form0.setWindowOpacity(1.0)
        Form0.setToolTipDuration(-1)
        Form0.setStatusTip("")
        Form0.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.btn_select_file = QtWidgets.QPushButton(Form0)
        self.btn_Kata_qual = QtWidgets.QPushButton(Form0)
        self.btn_Kata_final = QtWidgets.QPushButton(Form0)
        self.btn_Kumite = QtWidgets.QPushButton(Form0)
        self.status_file = QtWidgets.QLabel(Form0)

        self.frame_combo = QtWidgets.QFrame(Form0)

        self.combo = QtWidgets.QComboBox(self.frame_combo)

        self.btn_style_1 = """
            QPushButton {
                border: 2px solid #3e6ae1;
                color: #3e6ae1;
                background-color: none;
                }
            QPushButton:hover {
                border: 3px solid white;
                background-color: #3e6ae1;
                color: white;                }
            QPushButton:pressed {
                border: 1px solid white;
                background-color: #FAF9F9;
                color: black;
                }
        """

        self.btn_style_2 = """
            QPushButton {
                border: 2px solid #555B6E;
                color: #555B6E;
                background-color: none;
                }
            QPushButton:hover {
                border: 1px solid white;
                background-color: #FAF9F9;
                color: black;
                }
            QPushButton:pressed {
                border: 1px solid white;
                background-color: #555B6E;
                color: white;
                }
        """
        # для придания стиля выпадающему списку во всех случаях использую этот способ,
        # помещаю combo_box в прозрачный frame
        self.frame_combo.setGeometry(QtCore.QRect(60, 130, 350, 24))
        self.frame_combo.setStyleSheet("background-color: none;")
        self.frame_combo.setObjectName("frame_combo")

        self.combo.setGeometry(QtCore.QRect(0, 0, 350, 24))
        self.combo.hide()
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(12)
        self.combo.setFont(font)
        self.combo.setObjectName("combo")

        # назначаем переменные, необходимые для импортирования списков участников из Excel
        self.file = str()
        self.user_choise = str()
        self.user_choise_list = list()
        self.xl = str()
        self.x = int()

        # создаем кнопки в Главном меню
        self.btn_select_file.setGeometry(QtCore.QRect(60, 50, 200, 30))
        self.btn_select_file.setToolTip('Можно загрузить файл со сводными списками в Excel')
        self.btn_select_file.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(15)
        self.btn_select_file.setFont(font)
        self.btn_select_file.setObjectName("btn_select_file")

        self.btn_Kata_qual.setGeometry(QtCore.QRect(100, 350, 350, 50))
        self.btn_Kata_qual.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(35)
        self.btn_Kata_qual.setFont(font)
        self.btn_Kata_qual.setObjectName("btn_Kata_qual")

        self.btn_Kata_final.setGeometry(QtCore.QRect(100, 410, 350, 50))
        self.btn_Kata_final.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(35)
        self.btn_Kata_final.setFont(font)
        self.btn_Kata_final.setObjectName("btn_Kata_final")

        self.btn_Kumite.setGeometry(QtCore.QRect(500, 350, 200, 50))
        self.btn_Kumite.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(35)
        self.btn_Kumite.setFont(font)
        self.btn_Kumite.setObjectName("btn_Kumite")

        self.status_file.setGeometry(QtCore.QRect(60, 90, 780, 30))
        self.status_file.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10pt;")
        self.status_file.setObjectName("status_file")

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form0", "Главное меню"))
        Form0.setWindowIcon(QtGui.QIcon(':/Images/icon.ico'))
        self.status_file.setText(_translate("Form0", "Выберите файл"))
        self.btn_select_file.setText(_translate("Form0", "Выбрать файл"))
        self.btn_Kata_qual.setText(_translate("Form0", "Ката по флажкам"))
        self.btn_Kata_final.setText(_translate("Form0", "Ката финал"))
        self.btn_Kumite.setText(_translate("Form0", "Кумите"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()
        self.setupUi0(self)

        # Создаем словари, множества для формирования списков участник в индивидуальных кумите и ката + муж/жен
        self.TempSet = set()
        self.df_Single_list = []

        self.individ_dict = {}
        self.team_dict = {}
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
        self.tatamiName = ""

        self.btn_Kata_qual.clicked.connect(self.showKataQualWin)
        self.btn_Kata_final.clicked.connect(self.showKataFinalWin)
        self.btn_Kumite.clicked.connect(self.showKumiteWin)

        self.combo.activated[str].connect(self.userChoise)

        self.KumiteWindowsClose = KumiteWindowsClose()  # ДИА.окно КУМИТЕ закрытие окна
        self.KataQualWindowsClose = KataQualWindowsClose()  # ДИА.окно КАТА ОТБОРОЧ. закрытие окна
        self.KataFinalWindowsClose = KataFinalWindowsClose()  # ДИА.окно КАТА ФИНАЛ закрытие окна
        self.ui_kataQual = KataQual_MainWindow_Ui()  # Окно с КАТА по флажкам
        self.ui_kataFinal = KataMainWindow_Ui()  # Окно с КАТА финал (по балам)
        self.ui_kumite = KumiteMainWindow_Ui()  # Окно КУМИТЕ
        self.ui_KataQualToKataFinal = KataQualToKataFinal()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "КАТА ФИНАЛ"
        self.ui_KataFinalToKataQual = KataFinalToKataQual()  # ДИАЛ.окно из КАТА ФИНАЛ при нажатии кнопки "КАТА отбороч."
        self.ui_KataFinalToKumite = KataFinalToKumite()  # ДИА.окно из КАТА ФИНАЛ при нажатии кнопки "КУМИТЕ"
        self.ui_KataQualToKumite = KataQualToKumite()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "КУМИТЕ"
        self.ui_KumiteToKataQual = KumiteToKataQual()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "КАТА отбороч."
        self.ui_KumiteToKataFinal = KumiteToKataFinal()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "КАТА ФИНАЛ"
        self.ui_KataQualMenu = KataQualMenu()  # ДИАЛ.окно из КАТА отбороч. при нажатии кнопки "ГАВНОЕ МЕНЮ"
        self.ui_KataFinalMenu = KataFinalMenu()  # ДИАЛ.окно из КАТА ФИНАЛ при нажатии кнопки "ГАВНОЕ МЕНЮ"
        self.ui_KumiteMenu = KumiteMenu()  # ДИАЛ.окно из КУМИТЕ при нажатии кнопки "ГАВНОЕ МЕНЮ"

        # Назначаем различные методы по нажатию кнопок во всех видах соревнований (во всех окнах)
        # Кнопка закрытия окна в окне Кумите вызывает диалоговое окно, позволяющее перейти в главное меню.
        # Программа полностью не закрывается
        self.ui_kumite.Frame_Header.btn_closeWin.clicked.connect(self.KumiteWindowsClose.show)
        self.KumiteWindowsClose.btn_OK.clicked.connect(self.ui_kumite.clearKumiteData)
        self.KumiteWindowsClose.btn_OK.clicked.connect(self.showMainMenu)

        # Кнопка закрытия окна в Ката по флажкам, работает аналогично кнопке "Закрыть" в Кумите
        self.ui_kataQual.Frame_Header.btn_closeWin.clicked.connect(self.KataQualWindowsClose.show)
        self.KataQualWindowsClose.btn_OK.clicked.connect(self.ui_kataQual.clearKataData)
        self.KataQualWindowsClose.btn_OK.clicked.connect(self.showMainMenu)

        # Кнопка закрытия окна в Ката финал, работает аналогично кнопке "Закрыть" в Кумите
        self.ui_kataFinal.Frame_Header.btn_closeWin.clicked.connect(self.KataFinalWindowsClose.show)
        self.KataFinalWindowsClose.btn_OK.clicked.connect(self.ui_kataFinal.clearKataData)
        self.KataFinalWindowsClose.btn_OK.clicked.connect(self.showMainMenu)

        # Кнопка очистки данных в Ката по флажкам, очищает ФИО и Регион с экрана телевизора
        self.ui_kataQual.btn_clearData.clicked.connect(self.ui_kataQual.clearKataData)
        self.ui_kataQual.btn_NewCategory.clicked.connect(self.calcTabKata_Reset)
        self.ui_kataQual.btn_NewCategory.clicked.connect(self.ui_kataQual.NewCategory)

        ########   в окне КАТА отб. кнопка ГЛАВНОЕ МЕНЮ
        # self.ui_kataQual.MenuButton.clicked.connect(self.showDialogWindow)
        self.ui_KataQualMenu.btn_OK.clicked.connect(self.ui_kataQual.NewCategory)
        self.ui_KataQualMenu.btn_OK.clicked.connect(self.showMainMenu)
        ########   в окне КАТА отб. кнопка КУМИТЕ
        # self.ui_kataQual.KumiteButton.clicked.connect(self.showDialogWindow)
        self.ui_KataQualToKumite.btn_OK.clicked.connect(self.ui_kataQual.NewCategory)
        self.ui_KataQualToKumite.btn_OK.clicked.connect(self.showKumiteWin)
        ########   в окне КАТА отб. кнопка КАТА ФИНАЛ
        # self.ui_kataQual.KataFinalButton.clicked.connect(self.showDialogWindow)
        self.ui_KataQualToKataFinal.btn_OK.clicked.connect(self.ui_kataQual.NewCategory)
        self.ui_KataQualToKataFinal.btn_OK.clicked.connect(self.showKataFinalWin)
        ########   в окне КАТА ФИНАЛ кнопка ГЛАВНОЕ МЕНЮ
        # self.ui_kataFinal.MenuButton.clicked.connect(self.showDialogWindow)
        self.ui_KataFinalMenu.btn_OK.clicked.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataFinalMenu.btn_OK.clicked.connect(self.showMainMenu)
        ########   в окне КАТА ФИНАЛ кнопка КАТА отб.
        # self.ui_kataFinal.KataQualButton.clicked.connect(self.showDialogWindow)
        self.ui_KataFinalToKataQual.btn_OK.clicked.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataFinalToKataQual.btn_OK.clicked.connect(self.showKataQualWin)
        ########   в окне КАТА ФИНАЛ кнопка КУМИТЕ
        # self.ui_kataFinal.KumiteButton.clicked.connect(self.showDialogWindow)
        self.ui_KataFinalToKumite.btn_OK.clicked.connect(self.ui_kataFinal.clearKataData)
        self.ui_KataFinalToKumite.btn_OK.clicked.connect(self.showKumiteWin)
        ########   в окне КУМИТЕ кнопка ГЛАВНОЕ МЕНЮ
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.ui_kumite.clearKumiteData)
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.showMainMenu)
        ########   в окне КУМИТЕ кнопка КАТА отб.
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.ui_kumite.clearKumiteData)
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.showKataQualWin)
        ########   в окне КУМИТЕ кнопка КАТА ФИНАЛ
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.ui_kumite.clearKumiteData)
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.showKataFinalWin)

        # Все окна операторов (кроме главного меню) имею кастомную панель с кнопками свернуть, закрыть.
        # выпадающий список (Frame_Header.combo) - выбор программы,
        # в которую можно перейти, тут перечислены такие методы
        self.ui_kataQual.Frame_Header.combo.activated[str].connect(self.choiseCompitition_kataQual)
        self.ui_kataFinal.Frame_Header.combo.activated[str].connect(self.choiseCompitition_kataFinal)
        self.ui_kumite.Frame_Header.combo.activated[str].connect(self.choiseCompitition_Kumite)

        # Кнопки и списки из окна Ката по флажкам,
        # отображаются только в случае, если загружен список участников из Excel

        # Кнопки (QRadioButton) "Мужчины" и "Женщины" - первый этап соритровки списков
        self.ui_kataQual.male.clicked.connect(self.useExportDataKataQualMale)
        self.ui_kataQual.female.clicked.connect(self.useExportDataKataQualFemale)
        # Выбор списка участников по возрасту, выбранная возрастная категория передается в comboBox_name
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansRed)
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansWhite)
        # Из списка участников выбирается спортсмент для красных и для белых
        self.ui_kataQual.comboBox_name_red_1.activated[str].connect(self.setLabelRed)
        self.ui_kataQual.comboBox_name_white_1.activated[str].connect(self.setLabelWhite)
        # В окне Ката по флажкам кнопка "Показать на экране"
        self.ui_kataQual.btn_showData.clicked.connect(self.kata_matchName)
        self.ui_kataQual.btn_showData.clicked.connect(self.ui_kataQual.setSportsmanName)
        # В окне Ката по флажкам кнопка "Поделил Ака/Сиро"
        self.ui_kataQual.winnerRed.toggled.connect(self.ui_kataQual.setWinnerRed)
        self.ui_kataQual.winnerWhite.toggled.connect(self.ui_kataQual.setWinnerWhite)
        # В окне Ката финала нажата кнопка "Рассчитать"
        self.ui_kataFinal.Calc_Button.clicked.connect(self.ui_kataFinal.calcResult)
        self.ui_kataFinal.Clear_Button.clicked.connect(self.ui_kataFinal.clearKataData)

        # Кнопки и списки из окна Ката финал, принцып, как в Ката по флажкам
        self.ui_kataFinal.male.clicked.connect(self.useExportDataKataFinalMale)
        self.ui_kataFinal.female.clicked.connect(self.useExportDataKataFinalFemale)
        self.ui_kataFinal.comboBox_age.activated[str].connect(self.calcTabKataFinalSpotrsmansRed)
        self.ui_kataFinal.comboBox_name_red_1.activated[str].connect(self.setLabelRedkataFinal)
        # В окне Ката по флажкам кнопка "Показать на экране"
        self.ui_kataFinal.btn_showData.clicked.connect(self.kata_matchName)
        self.ui_kataFinal.btn_showData.clicked.connect(self.ui_kataFinal.setSportsmanName)
        # В окне Кумите кнопка "Показать на экране"
        self.ui_kumite.btn_showData.clicked.connect(self.kumite_matchName)
        self.ui_kumite.btn_showData.clicked.connect(self.ui_kumite.setSportsmanName)
        # Коннекторы для кнопок в окне Кумите
        self.ui_kumite.winnerRed.toggled.connect(self.ui_kumite.setWinner)
        self.ui_kumite.winnerWhite.toggled.connect(self.ui_kumite.setWinner)

        self.ui_kumite.btn_start.clicked.connect(self.ui_kumite.start_timer)
        self.ui_kumite.btn_pause.clicked.connect(self.ui_kumite.reset_timer)
        self.ui_kumite.btn_reset.clicked.connect(self.ui_kumite.reset_all)

        self.ui_kumite.plus2sec.clicked.connect(self.ui_kumite.upTime)
        self.ui_kumite.minus2sec.clicked.connect(self.ui_kumite.downTime)

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
        # В главном меню кнопку Загрузки файла Excel
        self.btn_select_file.clicked.connect(self.select_file)

    # Выпадающее меню в окне Кумите с выбором видов соревнований
    def choiseCompitition_Kumite(self):
        if self.ui_kumite.Frame_Header.combo.currentText() == "Главное меню":
            self.showKumiteMenu()
            # self.showDialogWindow("kumite - Главное меню")
        elif self.ui_kumite.Frame_Header.combo.currentText() == "Ката отбороч.":
            self.showDialogWindowKumiteToKataQual()
            # self.showDialogWindow("kumite - Ката отбороч.")
        elif self.ui_kumite.Frame_Header.combo.currentText() == "Ката финал":
            self.showDialogWindowKumiteToKataFinal()
            # self.showDialogWindow("kumite - Ката финал")

    # Выпадающее меню в окне Ката по флажкам с выбором видов соревнований
    def choiseCompitition_kataQual(self):
        if self.ui_kataQual.Frame_Header.combo.currentText() == "Главное меню":
            self.showKataQualMenu()
            # self.showDialogWindow("kataQual - Главное меню")
        elif self.ui_kataQual.Frame_Header.combo.currentText() == "Ката финал":
            self.showDialogWindowKataQualToKataFinal()
            # self.showDialogWindow("kataQual - Ката финал")
        elif self.ui_kataQual.Frame_Header.combo.currentText() == "Кумите":
            self.showDialogWindowKataQualToKumite()
            # self.showDialogWindow("kataQual - Кумите")

    # Выпадающее меню в окне Ката финал с выбором видов соревнований
    def choiseCompitition_kataFinal(self):
        if self.ui_kataFinal.Frame_Header.combo.currentText() == "Главное меню":
            self.showKataFinalMenu()
            # self.showDialogWindow("kataQual - Главное меню")
        elif self.ui_kataFinal.Frame_Header.combo.currentText() == "Ката отбороч.":
            self.showDialogWindowKataFinalToKataQual()
            # self.showDialogWindow("kataQual - Кумите")
        elif self.ui_kataFinal.Frame_Header.combo.currentText() == "Кумите":
            self.showDialogWindowKataFinalToKumite()
            # self.showDialogWindow("kataQual - Ката финал")

    # Метод, очищающий все словари, списки, множества со спортсменами, импортированными их Excel
    # (применяется, если выбран неверный лист. старые данные удаляются)
    def clearDataMember(self):
        self.TempSet = set()
        self.df_Single_list = []
        self.individ_dict = {}
        self.team_dict = {}
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

    # Метод, описывающий процесс выбора файла Excel и импорта данных из файла
    def select_file(self):
        try:
            self.combo.clear()
            self.file, _ = QFileDialog.getOpenFileName(self, 'Открыть файл со сводными списками в формате *xlsx', './',
                                                       "Excel (*.xlsx)")
            self.filename = str(self.file.split('/')[len(self.file.split('/')) - 1])
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 10pt;")
            self.status_file.setText('Файл обрабатывается')
            self.xl = pd.ExcelFile(self.file)

            if len(self.xl.sheet_names) > 1:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 10pt;")
                self.status_file.setText(f'В файле  <b>{self.filename}</b> несколько листов, выберите нужный')
                self.combo.show()
                self.combo.addItems(self.xl.sheet_names)

            else:
                self.combo.hide()
                self.user_choise = 0
                self.data_processing()
        except:
            if self.sportsmans_ages_dict != {}:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 10pt;")
                self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')
                return
            else:
                return

    def userChoise(self):
        self.user_choise_list = self.xl.sheet_names
        self.user_choise = self.user_choise_list.index(self.combo.currentText())
        self.data_processing()

    def data_processing(self):
        self.filename = str(self.file.split('/')[len(self.file.split('/')) - 1])

        if self.file:
            # if len(self.TempSet) > 0:
            #     self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 10pt;")
            #     self.status_file.setText('Выбран неверный файл или лист.'
            #                              '\nПродолжают использоваться, ранее загруженные данные')
            #     return
            try:
                self.sheet1 = None
                self.sheet1 = pd.read_excel(self.file, sheet_name=self.xl.sheet_names[self.user_choise])
                cols2skip = [4, 5, 6, 7]
                cols = [i for i in range(len(self.sheet1.columns) - 2) if i not in cols2skip]
                k = []
                for z in range(10, len(self.sheet1.columns) + 4):
                    k.append('a' + str(z))
                self.sheet = pd.read_excel(self.file, sheet_name=self.xl.sheet_names[self.user_choise],
                                           usecols=cols, header=None, names=k)
                kat_name = set(self.sheet.columns) - {'a10', 'a11', 'a12', 'a13'}
                self.list_kat_name = list(sorted(kat_name))
                self.df_Single_names = []
                self.df_Single_list = []
                self.df_Group_names = []
                self.df_Group_list = []
                self.TempSet = set()
                self.df_Single_list = []
                self.individ_dict = {}
                self.team_dict = {}
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

                # Определяем строчку, с которой начинается таблица
                check_list_dementieva = ['м', 'юн-ры', 'д', 'ж', 'юн-ки']
                check_list_yutkin = ['мальчики', 'юноши', 'юниоры', 'мужчины', 'девочки', 'девушки', 'юниорки', 'женщины']
                value_list = self.sheet['a14'].values.tolist()
                value_set = set(value_list)
                if value_list[0] in check_list_yutkin:
                    self.file_yutkin()
                else:
                    for x in value_set:
                        if x in check_list_dementieva:
                            self.countRowTab = self.sheet.loc[self.sheet['a14'] == x].index[0]
                            self.file_dementieva()
                            break
                self.ui_kumite.Form2.setFixedSize(900, 900)
            except:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 10pt;")
                self.status_file.setText('Выбран неверный файл или лист')
                self.clearDataMember()
                self.ui_kumite.Form2.setFixedSize(995, 500)

    def file_dementieva(self):
        for k_n in self.list_kat_name:
            # ЛИЧНЫЕ СОРЕВНОВАНИЯ
            # Поиск строк со значением "*" в столбце "k_n"
            #           (Поиск всех смортсменов, у которых в категории (столбце "k_n") поставлена ЗВЕЗДОЧКА "*")
            df2 = self.sheet.loc[self.sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]

            # Создание словаря из найденых спортсменов
            df_Temp_Single_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                           'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

            self.df_Single_names.append(k_n)
            self.df_Group_names.append(k_n)
            self.df_Single_list.append(df_Temp_Single_list)
        ################################################################

        self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 10pt;")
        self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')

        # ОПРЕДЕЛЕНИЕ ТИПОВ СЛОВОРЕЙ В ЗАГРУЖЕННОМ ФАЙЛЕ     ############################################
        type_set = set(self.sheet.iloc[self.countRowTab-2].values.tolist()) | set(self.sheet.iloc[self.countRowTab].values.tolist())\
                   | set(self.sheet.iloc[self.countRowTab+1].values.tolist())

        if 'личн' in type_set:                                          # ЛИЧНЫЕ СОРЕВНОВАНИЯ
            self.individ_dict = self.calc_dict(self.countRowTab-2, 'личн')
        if 'личн' not in type_set:                                      # ЛИЧНЫЕ СОРЕВНОВАНИЯ
            self.individ_dict = {}
        if 'КОМ' in type_set:                                           # КОМАНДНЫЕ СОРЕВНОВАНИЯ
            self.team_dict = self.calc_dict(self.countRowTab-2, 'КОМ')
        if 'КОМ' not in type_set:                                       # КОМАНДНЫЕ СОРЕВНОВАНИЯ
            self.team_dict = {}
        if 'кумите' in type_set:                                        # КУМИТЕ
            self.kumite_dict = self.calc_dict(self.countRowTab+1, 'кумите')
        if 'кумите' not in type_set:                                    # КУМИТЕ
            self.kumite_dict = {}
        if 'ката' in type_set:                                          # КАТА
            self.kata_dict = self.calc_dict(self.countRowTab+1, 'ката')
        if 'ката' not in type_set:                                      # КАТА
            self.kata_dict = {}
        if 'м' in type_set:                                             # М
            self.male_label_dict1 = self.calc_dict(self.countRowTab, 'м')
            self.male_label_dict |= self.male_label_dict1
        if 'м' not in type_set:                                         # М
            self.male_label_dict1 = {}
        if 'юн-ры' in type_set:                                         # М
            self.male_label_dict1 = self.calc_dict(self.countRowTab, 'юн-ры')
            self.male_label_dict |= self.male_label_dict1
        if 'юн-ры' not in type_set:                                     # М
            self.male_label_dict1 = {}
        if 'ж' in type_set:                                             # Ж
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'ж')
            self.female_label_dict |= self.female_label_dict1
        if 'ж' not in type_set:                                         # Ж
            self.female_label_dict1 = {}
        if 'д' in type_set:                                             # Ж
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'д')
            self.female_label_dict |= self.female_label_dict1
        if 'д' not in type_set:                                         # Ж
            self.female_label_dict1 = {}
        if 'юн-ки' in type_set:                                         # Ж
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'юн-ки')
            self.female_label_dict |= self.female_label_dict1
        if 'юн-ки' not in type_set:                                     # Ж
            self.female_label_dict1 = {}

        # ЛИЧНЫЕ СОРЕВНОВАНИЯ           ############################################
        # КОМАНДНЫЕ СОРЕВНОВАНИЯ        ############################################
        # КУМИТЕ                        ############################################
        # КАТА                          ############################################
        # М                             ############################################
        # # Ж                           ############################################
        # # Ж                           ############################################
        # ВСЕ ВОЗРАСТА  ############################################
        self.sportsmans_ages_dict = self.sheet.iloc[self.countRowTab-1].to_dict()
        list(map(self.sportsmans_ages_dict.__delitem__,
                 filter(self.sportsmans_ages_dict.__contains__, ('a10', 'a11', 'a12', 'a13'))))

        # М ВСЕ ВОЗРАСТА  ############################################
        self.male_sportsmans_ages_dict = self.sportsmans_ages_dict.copy()
        for g in set(self.female_label_dict):
            if g in self.male_sportsmans_ages_dict:
                self.male_sportsmans_ages_dict.pop(g)

        # Ж ВСЕ ВОЗРАСТА  ############################################
        self.female_sportsmans_ages_dict = self.sportsmans_ages_dict.copy()
        for g in set(self.male_label_dict):
            if g in self.female_sportsmans_ages_dict:
                self.female_sportsmans_ages_dict.pop(g)

        # КАТА М личн   ############################################
        self.individ_kata_male_dict = self.kata_dict.copy()
        for g in (set(self.female_label_dict) | set(self.team_dict)):
            if g in self.individ_kata_male_dict:
                self.individ_kata_male_dict.pop(g)

        # КАТА Ж личн   ############################################
        self.individ_kata_female_dict = self.kata_dict.copy()
        for g in (set(self.male_label_dict) | set(self.team_dict)):
            if g in self.individ_kata_female_dict:
                self.individ_kata_female_dict.pop(g)

        # КУМИТЕ М личн ############################################
        self.individ_kumite_male_dict = self.kumite_dict.copy()
        for g in (set(self.female_label_dict) | set(self.team_dict)):
            if g in self.individ_kumite_male_dict:
                self.individ_kumite_male_dict.pop(g)

        # КУМИТЕ Ж личн ############################################
        self.individ_kumite_female_dict = self.kumite_dict.copy()
        for g in (set(self.male_label_dict) | set(self.team_dict)):
            if g in self.individ_kumite_female_dict:
                self.individ_kumite_female_dict.pop(g)

        # КАТА груп     ############################################
        self.team_kata = self.team_dict.copy()
        for g in set(self.kumite_dict):
            if g in self.team_kata:
                self.team_kata.pop(g)

        # КУМИТЕ ком   ############################################
        self.team_kumite = self.team_dict.copy()
        for g in set(self.team_kata):
            if g in self.team_kumite:
                self.team_kumite.pop(g)
        self.individ_kata_dict = dict((i, self.individ_dict[i]) for i in self.individ_dict
                                      if i not in list(self.kumite_dict.keys()))

        # конструктор для matchName ############################################
        self.matchName_male_dict1 = self.male_sportsmans_ages_dict.copy()
        self.matchName_funk(self.matchName_male_dict1, "М")
        self.matchName_female_dict1 = self.female_sportsmans_ages_dict.copy()
        self.matchName_funk(self.matchName_female_dict1, "Ж")
        self.matchName = (self.matchName_male_dict1 | self.matchName_female_dict1).copy()

    def file_yutkin(self):
        for k_n in self.list_kat_name:
            # ЛИЧНЫЕ СОРЕВНОВАНИЯ
            # Поиск строк со значением "*" в столбце "k_n"
            #           (Поиск всех смортсменов, у которых в категории (столбце "k_n") поставлена ЗВЕЗДОЧКА "*")
            df2 = self.sheet.loc[self.sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]
            # Создание словаря из найденых спортсменов
            df_Temp_Single_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                           'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

            # КОМАНДНЫЕ СОРЕВНОВАНИЯ
            # Если в столбце "k_n" пустой словарь, то осуществляется поиск строк со значением "ком1, ком2 и тд"
            #                                               (Поиск всех смортсменов в командных соревнованиях)
            if df_Temp_Single_list == {}:
                df2 = self.sheet.loc[self.sheet[k_n] == 'ком1', ['a10', 'a11', 'a12', 'a13']]
                df_Temp1_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                df2 = self.sheet.loc[self.sheet[k_n] == 'ком2', ['a10', 'a11', 'a12', 'a13']]
                df_Temp2_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                df2 = self.sheet.loc[self.sheet[k_n] == 'ком3', ['a10', 'a11', 'a12', 'a13']]
                df_Temp3_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                df2 = self.sheet.loc[self.sheet[k_n] == 'ком4', ['a10', 'a11', 'a12', 'a13']]
                df_Temp4_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                df2 = self.sheet.loc[self.sheet[k_n] == 'ком5', ['a10', 'a11', 'a12', 'a13']]
                df_Temp5_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                df_Temp1_Group_list = df_Temp1_Group_list | df_Temp2_Group_list | \
                                      df_Temp3_Group_list | df_Temp4_Group_list | df_Temp5_Group_list
                self.df_Group_list.append(df_Temp1_Group_list)
            self.df_Single_names.append(k_n)
            self.df_Group_names.append(k_n)
            self.df_Single_list.append(df_Temp_Single_list)
        ################################################################

        self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 10pt;")
        self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')

        self.individ_kata_dict = self.calc_dict(3, 'один')  # КАТА ЛИЧН
        self.individ_kumite_dict = self.calc_dict(3, 'личн')  # КУМИТЕ ЛИЧН
        self.team_kata_dict = self.calc_dict(3, 'груп')  # КАТА ГРУП
        self.team_kumite_dict = self.calc_dict(3, 'ком')  # ККУМИТЕ КОМ
        self.male_label_dict = self.calc_dict(7, 'м')  # М
        self.female_label_dict = self.calc_dict(7, 'ж')  # Ж

        # ВСЕ ВОЗРАСТА  ############################################
        self.sportsmans_ages_dict = self.sheet.iloc[4].to_dict()
        list(map(self.sportsmans_ages_dict.__delitem__,
                 filter(self.sportsmans_ages_dict.__contains__, ('a10', 'a11', 'a12', 'a13'))))

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
        self.matchName_dict1 = self.sheet.iloc[0].to_dict()
        list(map(self.matchName_dict1.__delitem__,
                 filter(self.matchName_dict1.__contains__, ('a10', 'a11', 'a12', 'a13'))))
        self.matchName_dict2 = self.sheet.iloc[4].to_dict()
        list(map(self.matchName_dict2.__delitem__,
                 filter(self.matchName_dict2.__contains__, ('a10', 'a11', 'a12', 'a13'))))
        list1 = [self.matchName_dict1, self.matchName_dict2]
        keylist = list1[0].keys()
        self.matchName = dict((k, str.capitalize(' '.join(list(map(lambda d: d[k], list1))))) for k in keylist)

        # М ВСЕ ВОЗРАСТА  ############################################
        self.male_sportsmans_ages_dict = self.sportsmans_ages_dict.copy()
        for g in set(self.female_label_dict):
            if g in self.male_sportsmans_ages_dict:
                self.male_sportsmans_ages_dict.pop(g)


    def matchName_funk(self, matchName_sex_dict, sex):
        if sex == "М":
            value_1 = "Мальчики"
            value_2 = "Юноши"
            value_3 = "Юниоры"
            value_4 = "Мужчины"
        elif sex == "Ж":
            value_1 = "Девочки"
            value_2 = "Девушки"
            value_3 = "Юниорки"
            value_4 = "Женщины"
        age_checklist_1 = ['6 лет', '6-7 лет', '7 лет', '7-8 лет', '8 лет', '8-9 лет', '8-11 лет', '9 лет', '9-10 лет',
                           '10 лет', '10-11 лет', '11 лет', '11-12 лет', '12 лет', '12-13 лет', '12-15 лет', '13 лет',
                           '13-14 лет']
        age_checklist_2 = ['14 лет', '14-15 лет', '14-17 лет', '14-20 лет', '15 лет', '15-16 лет', '16 лет',
                           '16-17 лет', '16-20 лет', '17 лет', '17-18 лет']
        age_checklist_3 = ['18 лет', '19 лет', '20 лет', '18-20 лет']
        age_checklist_4 = ['с 16 лет', 'с 18 лет', 'с 21 года', '21-30 лет', '21-39 лет', '30-39 лет', '40+',
                           '40-49 лет', '50+', '50-60 лет']
        for key, value in matchName_sex_dict.items():
            if value in age_checklist_1:
                matchName_sex_dict[key] = value_1 + " " + value
            elif value in age_checklist_2:
                matchName_sex_dict[key] = value_2 + " " + value
            elif value in age_checklist_3:
                matchName_sex_dict[key] = value_3 + " " + value
            elif value in age_checklist_4:
                matchName_sex_dict[key] = value_4 + " " + value

    def calc_dict(self, rowNum, colName):
        colNum = self.sheet.loc[[rowNum]].where(self.sheet == colName).dropna(how='all').dropna(axis=1)
        sss = []
        for i in range(1, len(colNum.columns.tolist()) + 1):
            sss.append(colName)
        self.colNum_dict = dict(zip(colNum.columns.tolist(), sss))
        return self.colNum_dict

    def useExportDataKataQualMale(self):
        someDict = self.female_label_dict
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
        someDict = self.male_label_dict
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
        someDict = self.female_label_dict
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
        someDict = self.male_label_dict
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
        self.ui_kataQual.clearKataData()
        self.TempSet.clear()
        self.TempSet = sorted(list(set(dict_KataOrKumite) - set(someDict)))
        comboBox_age.setEnabled(True)
        comboBox_age.clear()
        age_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 10pt;")
        name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
        name_white_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 10pt;")
        comboBox_name_red_1.setEnabled(False)
        comboBox_name_red_1.clear()
        comboBox_name_white_1.setEnabled(False)
        comboBox_name_white_1.clear()
        comboBox_age.addItems([self.sportsmans_ages_dict[x] for x in self.TempSet])

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
            jj = self.ui_kataQual.matchName1
        elif name == self.ui_kataQual.name_white_1:
            n = self.ui_kataQual.comboBox_age.currentText()
            jj = self.ui_kataQual.matchName1
        elif name == self.ui_kataFinal.name_red_1:
            n = self.ui_kataFinal.comboBox_age.currentText()
            jj = self.ui_kataFinal.matchName1
        elif name == self.ui_kataFinal.name_white_1:
            n = self.ui_kataFinal.comboBox_age.currentText()
            jj = self.ui_kataFinal.matchName1
        a2 = {k: v for k, v in
              # zip(sorted(list(self.TempSet)), sorted([self.sportsmans_ages_dict[x] for x in self.TempSet]))}
              zip((self.TempSet), [self.sportsmans_ages_dict[x] for x in self.TempSet])}
        self.x = list(self.sportsmans_ages_dict.keys()).index(list(a2.keys())[list(a2.values()).index(n)])
        if self.tatamiName == "":
            jj.setText('Татами №#, ' + self.matchName[list(self.matchName.keys())[self.x]])
        else:
            jj.setText(self.tatamiName + ', ' + self.matchName[list(self.matchName.keys())[self.x]])
        name.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 10pt;")
        comboBox_name.addItems(sorted(self.df_Single_list[self.x]))
        comboBox_name.setEnabled(True)

    def setLabelRed(self):
        name = self.df_Single_list[self.x].get(self.ui_kataQual.comboBox_name_red_1.currentText())
        # это конструктор имя, состоящий из Фамилии и первого символа Имя
        self.ui_kataQual.lineEdit_name_red_1.setText(''.join([name.replace('a12', '').split('a13')[0],
                                                              ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
        self.ui_kataQual.lineEdit_region_red_1.setText(name.split('a11')[1])

    def setLabelRedkataFinal(self):
        name = self.df_Single_list[self.x].get(self.ui_kataFinal.comboBox_name_red_1.currentText())
        # это конструктор имя, состоящий из Фамилии и первого символа Имя
        self.ui_kataFinal.lineEdit_name_red_1.setText(
            ''.join([name.replace('a12', '').split('a13')[0], ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
        self.ui_kataFinal.lineEdit_region_red_1.setText(name.split('a11')[1])

    def setLabelWhite(self):
        name = str(self.df_Single_list[self.x].get(self.ui_kataQual.comboBox_name_white_1.currentText()))
        self.ui_kataQual.lineEdit_name_white_1.setText(''.join([name.replace('a12', '').split('a13')[0],
                                                                ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
        self.ui_kataQual.lineEdit_region_white_1.setText(name.split('a11')[1])

    def calcTabKata_Reset(self):
        # sender = self.sender()
        # if sender == self.ui_kataQual.btn_showData:
        #     ui_kata = self.ui_kataQual
        # elif sender == self.ui_kataFinal.btn_showData:
        #     ui_kata = self.ui_kataFinal
        self.TempSet |= sorted(self.individ_kata_dict.values())  # добавляем в пустой список все столбцы что
        if self.tatamiName != "":
            self.ui_kataQual.matchName1.setText(self.tatamiName + ', Возраст')
        else:
            self.ui_kataQual.matchName1.setText('Татами №#, Возраст')

    def kata_matchName(self):
        sender = self.sender()
        if sender == self.ui_kataQual.btn_showData:
            ui_kata = self.ui_kataQual
        elif sender == self.ui_kataFinal.btn_showData:
            ui_kata = self.ui_kataFinal
        try:
            if len(ui_kata.matchName1.text().split(', ')) > 1:
                self.tatamiName = ui_kata.matchName1.text().split(', ')[0]
                if ui_kata.matchName1.text() == \
                        self.tatamiName + ', ' + self.matchName[list(self.matchName.keys())[self.x]]:
                    ui_kata.matchName1.setText(self.tatamiName +
                                               ', ' + self.matchName[list(self.matchName.keys())[self.x]])
            else:
                ui_kata.matchName1.setText(self.matchName[list(self.matchName.keys())[self.x]])
        except:
            pass

    def kumite_matchName(self):
        sender = self.sender()
        if sender == self.ui_kumite.btn_showData:
            ui_kumite = self.ui_kumite
        if ui_kumite.matchName11.text() != "Татами №#" and ui_kumite.matchName11.text() != self.tatamiName:
            self.tatamiName = ui_kumite.matchName11.text()

    def showKataQualWin(self):
        self.closeAllWin()
        self.ui_kataQual.openSecondWin()
        self.ui_kataQual.show()
        self.close()
        if self.sportsmans_ages_dict == {}:
            self.ui_kataQual.frame_sportsmans.hide()
        else:
            self.ui_kataQual.frame_sportsmans.show()
        if self.tatamiName != "":
            self.ui_kataQual.matchName1.setText(self.tatamiName + ", Возраст")
        self.ui_kataQual.setMatchName()

    def showKataFinalWin(self):
        self.closeAllWin()
        self.ui_kataFinal.openSecondWin()
        self.ui_kataFinal.show()

        self.close()
        if self.sportsmans_ages_dict == {}:
            self.ui_kataFinal.frame_sportsmans.hide()
        else:
            self.ui_kataFinal.frame_sportsmans.show()
        if self.tatamiName != "":
            self.ui_kataFinal.matchName1.setText(self.tatamiName + ", Возраст")
        self.ui_kataFinal.setMatchName()

    def showKumiteWin(self):
        self.ui_kataFinal.clearKataData()
        self.ui_kataQual.NewCategory()
        self.ui_kumite.clearKumiteData()

        self.closeAllWin()
        self.ui_kumite.openSecondWinKumite()
        self.ui_kumite.show()
        self.close()
        if self.tatamiName != "":
            self.ui_kumite.matchName11.setText(self.tatamiName)
        self.ui_kumite.setMatchName()

    def closeAllWin(self):
        self.ui_kumite.closeSecondWinKumite()
        self.ui_kumite.close()
        self.ui_kataQual.closeSecondWin()
        self.ui_kataQual.close()
        self.ui_kataFinal.closeSecondWin()
        self.ui_kataFinal.close()
        self.ui_KataQualToKataFinal.close()
        self.ui_KataFinalToKataQual.close()
        self.ui_KataFinalToKumite.close()
        self.ui_KataQualToKumite.close()
        self.ui_KumiteToKataQual.close()
        self.ui_KumiteToKataFinal.close()
        self.ui_KataQualMenu.close()
        self.ui_KataFinalMenu.close()
        self.ui_KumiteMenu.close()
        self.KumiteWindowsClose.close()
        self.KataQualWindowsClose.close()
        self.KataFinalWindowsClose.close()

    def showDialogWindow(self):
        sender = self.sender()
        if sender == self.ui_kataQual.KumiteButton:
            self.ui_KataQualMenu.close()
            self.ui_KataQualToKataFinal.close()
            self.ui_KataQualToKumite.show()
        elif sender == self.ui_kataQual.KataFinalButton:
            self.ui_KataQualMenu.close()
            self.ui_KataQualToKumite.close()
            self.ui_KataQualToKataFinal.show()
        elif sender == self.ui_kataQual.MenuButton:
            self.ui_KataQualToKumite.close()
            self.ui_KataQualToKataFinal.close()
            self.ui_KataQualMenu.show()
        elif sender == self.ui_kataFinal.KataQualButton:
            self.ui_KataFinalMenu.close()
            self.ui_KataFinalToKumite.close()
            self.ui_KataFinalToKataQual.show()
        elif sender == self.ui_kataFinal.KumiteButton:
            self.ui_KataFinalMenu.close()
            self.ui_KataFinalToKataQual.close()
            self.ui_KataFinalToKumite.show()
        elif sender == self.ui_kataFinal.MenuButton:
            self.ui_KataFinalToKataQual.close()
            self.ui_KataFinalToKumite.close()
            self.ui_KataFinalMenu.show()

    def showDialogWindowKataQualToKumite(self):
        self.ui_KataQualMenu.close()
        self.ui_KataQualToKataFinal.close()
        self.ui_KataQualToKumite.show()

    def showDialogWindowKataQualToKataFinal(self):
        self.ui_KataQualMenu.close()
        self.ui_KataQualToKumite.close()
        self.ui_KataQualToKataFinal.show()

    def showDialogWindowKataFinalToKataQual(self):
        self.ui_KataFinalMenu.close()
        self.ui_KataFinalToKumite.close()
        self.ui_KataFinalToKataQual.show()

    def showDialogWindowKumiteToKataQual(self):
        self.ui_KumiteMenu.close()
        self.ui_KumiteToKataFinal.close()
        self.ui_KumiteToKataQual.show()

    def showDialogWindowKataFinalToKumite(self):
        self.ui_KataFinalMenu.close()
        self.ui_KataFinalToKataQual.close()
        self.ui_KataFinalToKumite.show()

    def showDialogWindowKumiteToKataFinal(self):
        self.ui_KumiteMenu.close()
        self.ui_KumiteToKataQual.close()
        self.ui_KumiteToKataFinal.show()

    def showKataQualMenu(self):
        self.ui_KataQualToKumite.close()
        self.ui_KataQualToKataFinal.close()
        self.ui_KataQualMenu.show()

    def showKataFinalMenu(self):
        self.ui_KataFinalToKataQual.close()
        self.ui_KataFinalToKumite.close()
        self.ui_KataFinalMenu.show()

    def showKumiteMenu(self):
        self.ui_KumiteToKataQual.close()
        self.ui_KumiteToKataFinal.close()
        self.ui_KumiteMenu.show()

    def showMainMenu(self):
        self.closeAllWin()
        self.show()


class dialogWindow_Ui(object):
    def setupUi_dialog(self, Dialog):
        self.btn_style_3 = """
            QPushButton {
                border: 2px solid #3e6ae1;
                color: #3e6ae1;
                background-color: none;
                font-family: Gotham-Light;
                font-size: 15px;
                }
            QPushButton:hover {
                border: 3px solid white;
                background-color: #3e6ae1;
                color: white;                }
            QPushButton:pressed {
                border: 1px solid white;
                background-color: #FAF9F9;
                color: black;
                }
            """

        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 120)
        Dialog.setStyleSheet("background-color: white;")
        self.Ui_Form0 = Ui_Form0()

        self.btn_OK = QtWidgets.QPushButton("OK", Dialog)
        self.btn_OK.setGeometry(QtCore.QRect(95, 70, 100, 32))
        self.btn_OK.setStyleSheet(self.btn_style_3)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(30)
        self.btn_OK.setFont(font)

        self.btn_CANCEL = QtWidgets.QPushButton("CANCEL", Dialog)
        self.btn_CANCEL.setGeometry(QtCore.QRect(205, 70, 100, 32))
        self.btn_CANCEL.setStyleSheet(self.btn_style_3)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(30)
        self.btn_CANCEL.setFont(font)

        self.btn_CANCEL.clicked.connect(Dialog.close)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 15, 400, 25))
        self.label.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(0, 40, 400, 20))
        self.label2.setStyleSheet("font-family: Gotham-Light; font-size: 12px;")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label2.setText(_translate("Dialog", "TextLabel"))


class KumiteWindowsClose(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Закрыть окно \"<b>Кумите</b>\"?")
        self.label2.setText("Откроется \"<b>Главное меню</b>\"")
        self.setWindowTitle(" ")


class KataQualWindowsClose(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Закрыть окно \"<b>КАТА ГО ХАКУ</b>\"?")
        self.label2.setText("Откроется \"<b>Главное меню</b>\"")
        self.setWindowTitle(" ")


class KataFinalWindowsClose(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Закрыть окно \"<b>КАТА ФИНАЛ</b>\"?")
        self.label2.setText("Откроется \"<b>Главное меню</b>\"")
        self.setWindowTitle(" ")


class KataQualToKumite(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Кумите</b>\"?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")


class KataQualMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")


class KataFinalToKataQual(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката по флажкам</b>\"?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")


class KataQualToKataFinal(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката финал</b>\"?")
        self.label2.setText("Окно \"<b>Ката по флажкам</b>\" закроется")
        self.setWindowTitle(" ")


class KataFinalToKumite(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Кумите</b>\"?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")


class KataFinalMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Ката финал</b>\" закроется")
        self.setWindowTitle(" ")


class KumiteToKataFinal(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката финал</b>\"?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")


class KumiteToKataQual(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_dialog(self)
        self.label.setText("Открыть окно \"<b>Ката по флажкам</b>\"?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")


class KumiteMenu(QWidget, dialogWindow_Ui):
    def __init__(self):
        super().__init__()
        self.ui_kumite = KumiteMainWindow_Ui()
        self.setupUi_dialog(self)
        self.label.setText("Открыть Главное меню?")
        self.label2.setText("Окно \"<b>Кумите</b>\" закроется")
        self.setWindowTitle(" ")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/Images/icon.ico'))
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Light.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Medium.ttf")
    QtGui.QFontDatabase.addApplicationFont(":/Fonts/Gotham-Bold.ttf")
    ui0 = MenuWindow()
    ui0.setWindowIcon(QtGui.QIcon(':/Images/icon.ico'))
    ui0.show()
    sys.exit(app.exec_())
