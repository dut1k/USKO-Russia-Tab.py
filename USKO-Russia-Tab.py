from typing import Tuple

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QComboBox
import pandas as pd
# import numpy as np
from screeninfo import get_monitors
from Kata_final import KataMainWindow_Ui, KataSecondWindow  # KataSecondWindow
from Kata_qual import KataQual_MainWindow_Ui  # KataQual_SecondWindow
from Kumite import KumiteMainWindow_Ui  # KumiteSecondWindow
import styleCSS as css
import re
import datetime
import resources
from os import listdir
# from openpyxl import load_workbook
import win32com.client
# import xlwings as xw
import threading
import pythoncom
import os


# Класс для записи в потоке данных в файл excel
# class Worker(QObject):
class Worker(QThread):
    finished = pyqtSignal(QtCore.QVariant)

    def __init__(self, result):
        super().__init__()
        self.result = result

    def run(self):
        try:
            # print('              check_to_change_interface', self.result)
            self.finished.emit(self.result)
            # Закрываем поток
            self.quit()
            self.deleteLater()

        except Exception as e:
            print('_______Exception check_to_change_interface:', e)
            self.finished.emit(str(e))


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
        self.frame_logo = QtWidgets.QFrame(Form0)
        self.logo_USKOrus = QtGui.QPixmap(":/Images/emblem_usko.png")
        self.logo_VBErus = QtGui.QPixmap(":/Images/emblem_vbe_rus.png")
        self.logo_VBEmos = QtGui.QPixmap(":/Images/emblem_vbe_msk.png")
        self.label_logo_USKOrus = QtWidgets.QLabel(self.frame_logo)
        self.label_logo_VBErus = QtWidgets.QLabel(self.frame_logo)
        self.label_logo_VBEmos = QtWidgets.QLabel(self.frame_logo)
        self.sponsored_by = QtWidgets.QLabel(self.frame_logo)
        self.legend = QtWidgets.QLabel(Form0)

        self.btn_style_1 = css.btn_style_1
        self.btn_style_2 = css.btn_style_2
        self.font_l_12 = css.font_l_12
        self.font_l_15 = css.font_l_15
        self.font_m_15 = css.font_m_15
        self.font_l_20 = css.font_l_20
        self.font_m_35 = css.font_m_35

        # для придания стиля выпадающему списку во всех случаях использую этот способ,
        # помещаю combo_box в прозрачный frame
        self.frame_combo.setGeometry(QtCore.QRect(60, 90, 240, 24))
        self.frame_combo.setStyleSheet("background-color: none;")
        self.frame_combo.setObjectName("frame_combo")

        self.combo.setGeometry(QtCore.QRect(0, 0, 240, 24))
        self.combo.hide()
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(12)
        self.combo.setFont(font)
        self.combo.setObjectName("combo")

        # назначаем переменные, необходимые для импортирования списков участников из Excel
        self.file = str()
        self.user_choice = str()
        self.user_choice_list = list()
        self.xl = str()
        self.x = int()

        # создаем кнопки в Главном меню
        self.btn_select_file.setGeometry(QtCore.QRect(60, 50, 240, 30))
        self.btn_select_file.setToolTip('Можно загрузить файл со сводными списками в Excel')
        self.btn_select_file.setStyleSheet(self.btn_style_2)
        self.btn_select_file.setFont(self.font_m_15)
        self.btn_select_file.setObjectName("btn_select_file")

        self.btn_Kata_qual.setGeometry(QtCore.QRect(100, 350, 350, 50))
        self.btn_Kata_qual.setStyleSheet(self.btn_style_1)
        self.btn_Kata_qual.setFont(self.font_m_35)
        self.btn_Kata_qual.setObjectName("btn_Kata_qual")

        self.btn_Kata_final.setGeometry(QtCore.QRect(100, 410, 350, 50))
        self.btn_Kata_final.setStyleSheet(self.btn_style_1)
        self.btn_Kata_final.setFont(self.font_m_35)
        self.btn_Kata_final.setObjectName("btn_Kata_final")

        self.btn_Kumite.setGeometry(QtCore.QRect(500, 350, 200, 50))
        self.btn_Kumite.setStyleSheet(self.btn_style_1)
        self.btn_Kumite.setFont(self.font_m_35)
        self.btn_Kumite.setObjectName("btn_Kumite")

        self.status_file.setGeometry(QtCore.QRect(60, 20, 780, 30))
        self.status_file.setStyleSheet("color: grey;")
        self.status_file.setFont(self.font_l_12)
        self.status_file.setObjectName("status_file")

        self.frame_logo.setGeometry(QtCore.QRect(330, 50, 570, 300))
        self.frame_logo.setStyleSheet("background-color: none;")
        self.frame_logo.setObjectName("frame_logo")

        self.label_logo_USKOrus.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.label_logo_USKOrus.setObjectName("label_logo_USKOrus")
        self.label_logo_USKOrus.setPixmap(self.logo_USKOrus)

        self.label_logo_VBErus.setGeometry(QtCore.QRect(180, 0, 150, 150))
        self.label_logo_VBErus.setObjectName("label_logo_VBErus")
        self.label_logo_VBErus.setPixmap(self.logo_VBErus)

        self.label_logo_VBEmos.setGeometry(QtCore.QRect(360, 0, 150, 150))
        self.label_logo_VBEmos.setObjectName("label_logo_VBEmos")
        self.label_logo_VBEmos.setPixmap(self.logo_VBEmos)

        self.sponsored_by.setGeometry(QtCore.QRect(0, 150, 510, 55))  # justify
        self.sponsored_by.setStyleSheet("font-family: Gotham-Light; text-align: right; color: black; font-size: 15px;")
        self.sponsored_by.setAlignment(QtCore.Qt.AlignCenter)
        self.sponsored_by.setObjectName("sponsored_by")

        self.legend.setGeometry(QtCore.QRect(0, 480, 900, 10))
        self.legend.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10px;")
        self.legend.setAlignment(QtCore.Qt.AlignCenter)
        self.legend.setObjectName("legend")

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
        self.sponsored_by.setText(_translate("self.frame_logo", "При поддержке Президента РФСОО «Федерация восточного\n"
                                                                "боевого единоборства Сётокан города Москвы» "
                                                                "Латкина А.И."))
        year = datetime.date.today().year
        self.legend.setText(_translate("Form0", f"Программа «Электронное табло USKO RUSSIA». {year} год"))


class MenuWindow(QWidget, Ui_Form0):
    def __init__(self):
        super().__init__()

        self.setupUi0(self)
        # Определяем размеры мониторов
        self.display_coord_x1_secW = 'undefined'
        for m in get_monitors():
            self.list_monitor = str(m).split(', ')
            self.calc_monitor_coord()
        if self.display_coord_x1_secW == 'undefined':
            self.display_coord_x1_secW = self.display_coord_x1
            self.display_width_secW = self.display_width
            self.display_coord_y1_secW = self.display_coord_y1
            self.display_height_secW = self.display_height

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
        self.sportsmans_in_teams_dict = {}
        self.teams_pairs = {}
        self.cur_men_pair_num = None  # Номер строки пары спортсменов

        self.matchName = {}

        self.category_label = ""

        self.sportsmen_dict = {}
        self.region_dict = {}

        self.df_Single_names = []
        self.df_Group_names = []
        self.df_Group_list = []
        self.df_Group_list_only_group = []

        self.sportsmen_list = None  # Для списка Пятнова
        self.pyatnov_winner = None
        self.loaded_file_data_type = None
        self.sheet_name_aka_shiro = ''  # Название листа Aka+Shiro
        self.sheet_name_final = ''  # Название листа Финал
        self.sheet_name_referee = ''  # Название листа Протокол арбитра

        # Флаги, какой тип файла Пятнова был подгружен
        self.flag_pyatnov_kata_single = False  # Ката личное
        self.flag_pyatnov_kata_team = False  # Ката групповое
        self.flag_pyatnov_kumite_single = False  # Кумите личное
        self.flag_pyatnov_kumite_team = False  # Кумите групповое

        # Данные для записи протокола Кумите Пятнов
        self.dict_paytnov_kumite_winner = {
            'siro': {'score': list(), 'hm_j': list(), 'result': 0},
            'aka': {'score': list(), 'hm_j': list(), 'result': 0},
        }
        self.data_to_write_in_paytnov_referee_protocol = [[], []]  # Обработанные данные, записываемы в Excel

        self.btn_Kata_qual.clicked.connect(self.showKataQualWin)
        self.btn_Kata_final.clicked.connect(self.showKataFinalWin)
        self.btn_Kumite.clicked.connect(self.showKumiteWin)

        self.combo.activated[str].connect(self.userChoice)

        self.KumiteWindowsClose = KumiteWindowsClose()  # ДИА.окно КУМИТЕ закрытие окна
        self.KataQualWindowsClose = KataQualWindowsClose()  # ДИА.окно КАТА ОТБОРОЧ. закрытие окна
        self.KataFinalWindowsClose = KataFinalWindowsClose()  # ДИА.окно КАТА ФИНАЛ закрытие окна
        self.ui_kataQual = KataQual_MainWindow_Ui()  # Окно с КАТА по флажкам
        # self.ui_kataQualSecondWindow = KataQual_SecondWindow()
        self.ui_kataFinal = KataMainWindow_Ui()  # Окно с КАТА финал (по балам)
        self.ui_kataFinalSecondWindow = KataSecondWindow()
        self.ui_kumite = KumiteMainWindow_Ui()  # Окно КУМИТЕ
        # self.ui_kumiteSecondWindow = KumiteSecondWindow()
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
        self.KumiteWindowsClose.btn_OK.clicked.connect(self.ui_kumite.reset_all)
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
        self.ui_kataQual.btn_clearData.clicked.connect(self.clearData)
        self.ui_kataQual.btn_NewCategory.clicked.connect(self.clearData)

        # Кнопка очистки данных в Кумите, очищает ФИО и Регион с экрана телевизора
        self.ui_kumite.btn_NewCategory.clicked.connect(self.clearData)

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
        self.ui_KumiteMenu.btn_OK.clicked.connect(lambda: self.ui_kumite.reset_all(self.flags_dict))
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.ui_kumite.NewCategory)
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.showMainMenu)
        ########   в окне КУМИТЕ кнопка КАТА отб.
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(lambda: self.ui_kumite.reset_all(self.flags_dict))
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.ui_kumite.NewCategory)
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.showKataQualWin)
        ########   в окне КУМИТЕ кнопка КАТА ФИНАЛ
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(lambda: self.ui_kumite.reset_all(self.flags_dict))
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.ui_kumite.NewCategory)
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.showKataFinalWin)

        # Все окна операторов (кроме главного меню) имею кастомную панель с кнопками свернуть, закрыть.
        # выпадающий список (Frame_Header.combo) - выбор программы,
        # в которую можно перейти, тут перечислены такие методы
        self.ui_kataQual.Frame_Header.combo.activated[str].connect(self.choiceCompetition_kataQual)
        self.ui_kataFinal.Frame_Header.combo.activated[str].connect(self.choiceCompetition_kataFinal)
        self.ui_kumite.Frame_Header.combo.activated[str].connect(self.choiceCompetition_Kumite)

        # Кнопки и списки из окна Ката по флажкам,
        # отображаются только в случае, если загружен список участников из Excel

        # Кнопки (QRadioButton) "Мужчины" и "Женщины" - первый этап соритровки списков
        self.ui_kataQual.pers_com_qbx.clicked.connect(self.pers_com_qbxKataQual)
        self.ui_kataQual.male.clicked.connect(lambda: self.useExportDataKataQual(
            load_date=self.individ_kata_male_dict))
        self.ui_kataQual.female.clicked.connect(lambda: self.useExportDataKataQual(
            load_date=self.individ_kata_female_dict))
        # Выбор списка участников по возрасту, выбранная возрастная категория передается в comboBox_name
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansRed)
        self.ui_kataQual.comboBox_age.activated[str].connect(self.calcTabKataSpotrsmansWhite)
        # Из списка участников выбирается спортсмент для красных и для белых
        self.ui_kataQual.comboBox_name_red_1.activated[str].connect(self.setLabelRed)
        self.ui_kataQual.comboBox_name_white_1.activated[str].connect(self.setLabelWhite)
        # В окне Ката по флажкам кнопка "Показать на экране"
        self.ui_kataQual.btn_showData.clicked.connect(self.setSportsmanName)
        # Обновляем название категории на мониторе при изменении в окне на ПК
        self.ui_kataQual.matchName1.editingFinished.connect(self.ui_kataQual.setMatchName)
        # В окне Ката по флажкам кнопка "Поделил Ака/Сиро"
        self.ui_kataQual.winnerRed.toggled.connect(self.set_winner)
        self.ui_kataQual.winnerWhite.toggled.connect(self.set_winner)

        # В окне Ката финала нажата кнопка "Рассчитать"
        self.ui_kataFinal.Calc_Button.clicked.connect(self.set_winner)
        self.ui_kataFinal.Clear_Button.clicked.connect(self.clearData)
        # Кнопки и списки из окна Ката финал, принцип, как в Ката по флажкам
        self.ui_kataFinal.pers_com_qbx.clicked.connect(self.pers_com_qbxKataFinal)
        self.ui_kataFinal.male.clicked.connect(lambda: self.useExportDataKataFinal(
            load_date=self.individ_kata_male_dict))
        self.ui_kataFinal.female.clicked.connect(lambda: self.useExportDataKataFinal(
            load_date=self.individ_kata_female_dict))
        self.ui_kataFinal.comboBox_age.activated[str].connect(self.calcTabKataFinalSpotrsmansRed)
        self.ui_kataFinal.comboBox_name_red_1.activated[str].connect(self.setLabelRedKataFinal)

        # Кнопки и списки из окна Кумите, принцип, как в Ката по флажкам
        # Кнопка (QCheckBox) "Личн./Ком." - подгружаем личный или командрый список
        self.ui_kumite.pers_com_qbx.clicked.connect(self.pers_com_qbxKumite)
        self.ui_kumite.male.clicked.connect(lambda: self.useExportDataKumite(
            load_date=self.individ_kumite_male_dict))
        self.ui_kumite.female.clicked.connect(lambda: self.useExportDataKumite(
            load_date=self.individ_kumite_female_dict))
        self.ui_kumite.comboBox_age.activated[str].connect(self.calcTab_kumite)
        self.ui_kumite.comboBox_name_red_1.activated[str].connect(self.setLabelRedKumite)
        self.ui_kumite.comboBox_name_white_1.activated[str].connect(self.setLabelWhiteKumite)

        # В окне Ката по флажкам кнопка "Показать на экране"
        self.ui_kataFinal.btn_showData.clicked.connect(self.setSportsmanName)
        # Обновляем название категории на мониторе при изменении в окне на ПК
        self.ui_kataFinal.matchName1.editingFinished.connect(self.ui_kataFinal.setMatchName)
        # В окне Кумите кнопка "Показать на экране"
        self.ui_kumite.btn_showData.clicked.connect(self.setSportsmanName)
        # Обновляем название категории на мониторе при изменении в окне на ПК
        self.ui_kumite.matchName12.editingFinished.connect(self.ui_kumite.setMatchName)
        # Коннекторы для кнопок в окне Кумите
        self.ui_kumite.winnerRed.clicked.connect(self.set_winner)
        self.ui_kumite.winnerWhite.clicked.connect(self.set_winner)

        self.ui_kumite.btn_start.clicked.connect(self.ui_kumite.start_timer)
        self.ui_kumite.btn_pause.clicked.connect(self.ui_kumite.reset_timer)
        self.ui_kumite.btn_reset.clicked.connect(self.clearData)

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
        self.ui_kumite.h_red2.toggled.connect(self.ui_kumite.penaltyButton_hmr2)
        self.ui_kumite.h_red3.toggled.connect(self.ui_kumite.penaltyButton_hmr3)
        self.ui_kumite.h_red4.toggled.connect(self.ui_kumite.penaltyButton_hmr4)

        self.ui_kumite.j_red1.toggled.connect(self.ui_kumite.penaltyButton_jr1)
        self.ui_kumite.j_red2.toggled.connect(self.ui_kumite.penaltyButton_jr2)
        self.ui_kumite.j_red3.toggled.connect(self.ui_kumite.penaltyButton_jr3)
        self.ui_kumite.j_red4.toggled.connect(self.ui_kumite.penaltyButton_jr4)

        self.ui_kumite.h_white1.toggled.connect(self.ui_kumite.penaltyButton_hmw1)
        self.ui_kumite.h_white2.toggled.connect(self.ui_kumite.penaltyButton_hmw2)
        self.ui_kumite.h_white3.toggled.connect(self.ui_kumite.penaltyButton_hmw3)
        self.ui_kumite.h_white4.toggled.connect(self.ui_kumite.penaltyButton_hmw4)

        self.ui_kumite.j_white1.toggled.connect(self.ui_kumite.penaltyButton_jw1)
        self.ui_kumite.j_white2.toggled.connect(self.ui_kumite.penaltyButton_jw2)
        self.ui_kumite.j_white3.toggled.connect(self.ui_kumite.penaltyButton_jw3)
        self.ui_kumite.j_white4.toggled.connect(self.ui_kumite.penaltyButton_jw4)

        self.ui_kumite.btn_show_screen.clicked.connect(self.setSportsmanName)

        self.ui_kumite.pyatnov_perebivka_btn.clicked.connect(self.ui_kumite.perebivka_disabled)

        self.ui_kumite.le_comboBox_name_white_1.activated[str].connect(self.setLabel)
        self.ui_kumite.le_comboBox_name_red_1.activated[str].connect(self.setLabel)
        self.ui_kumite.pyatnov_name.activated[str].connect(self.setLabel)
        self.ui_kumite.pyatnov_pair_name.activated[str].connect(self.setLabel)
        self.ui_kataQual.pyatnov_name.activated[str].connect(self.setLabel)
        self.ui_kataFinal.pyatnov_name.activated[str].connect(self.setLabel)

        #  Кумите Пятнов данные для протокола
        self.ui_kumite.score_red_0.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_5.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_red_6.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_0.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_5.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.score_white_6.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_red1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_red2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_red3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_red4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_red1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_red2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_red3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_red4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_white1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_white2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_white3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.h_white4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_white1.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_white2.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_white3.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        self.ui_kumite.j_white4.toggled.connect(self.get_data_for_paytnov_kumite_winner)
        ######################################
        # В главном меню кнопку Загрузки файла Excel
        self.btn_select_file.clicked.connect(self.select_file)

        # self.ui_kataQual.frame_pyatnov.hide()
        # self.ui_kataFinal.frame_pyatnov.hide()
        # self.ui_kumite.frame_pyatnov.hide()

        self.show_withOut_load_file_interface()

        ######################################
        # СПИСОК КАТА
        self.kata_list = [
            "Хэйан Сёдан", "Хэйан Нидан", "Хэйан Сандан", "Хэйан Йондан", "Хэйан Годан", "Тэкки Сёдан", "Бассай - Дай",
            "Канку - Дай", "Дзиён", "Энпи", "Хангетцу", "Годзюсихо - Сё", "Канку Сё", "Дзютэ", "Бассай Сё", "Унсу",
            "Нидзюсихо", "Соотин", "Мэйкьё", "Годзюсихо - Дай", "Ганкаку", "Чинтэ", "Ванкан"
        ]

        ###############################################################################################################
        # ИКОНКИ РЕГИОНОВ
        # Все флаги https://ru.wikipedia.org/wiki/%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8
        # Все гербы https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D1%80%D0%B1%D1%8B_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8

        # Полный список регионов
        self.flags_set = \
            ['АДЫГЕЯ Республика', 'БАШКОРТОСТАН Республика', 'КОМИ Республика', 'ТАТАРСТАН Республика',
             'Республика тыва', 'УДМУРТСКАЯ Республика', 'ЧУВАШСКАЯ Республика', 'АЛТАЙСКИЙ край', 'КРАСНОДАРСКИЙ край',
             'КРАСНОЯРСКИЙ край', 'ПРИМОРСКИЙ край', 'СТАВРОПОЛЬСКИЙ край', 'АСТРАХАНСКАЯ область', 'БРЯНСКАЯ область',
             'ВЛАДИМИРСКАЯ область', 'ВОЛОГОДСКАЯ область', 'ВОРОНЕЖСКАЯ область', 'ИВАНОВСКАЯ область',
             'ИРКУТСКАЯ область', 'КАМЧАТСКИЙ край', 'КОСТРОМСКАЯ область', 'ЛЕНИНГРАДСКАЯ область',
             'МОСКОВСКАЯ область', 'НИЖЕГОРОДСКАЯ область', 'НОВОСИБИРСКАЯ область', 'ОМСКАЯ область',
             'ОРЕНБУРГСКАЯ область', 'ПЕНЗЕНСКАЯ область', 'ПЕРМСКИЙ край', 'РОСТОВСКАЯ область', 'РЯЗАНСКАЯ область',
             'САМАРСКАЯ область', 'САРАТОВСКАЯ область', 'СМОЛЕНСКАЯ область', 'ТВЕРСКАЯ область', 'ТУЛЬСКАЯ область',
             'МОСКВА', 'САНКТ-ПЕТЕРБУРГ', 'ДОНЕЦКАЯ НАРОДНАЯ Республика', 'КРЫМ Республика', 'ЯМАЛО-НЕНЕЦКИЙ АО']
        self.flags_set.sort()
        self.flags_dict = {
            'адыгеяреспублика': '01',
            'республикаадыгея': '01',
            'башкортостанреспублика': '02',
            'республикабашкортостан': '02',
            'республикабурятия': '03',
            'республикаалтай': '04',
            'республикадагестан': '05',
            'республикаингушетия': '06',
            'кабардино-балкарскаяреспублика': '07',
            'республикакалмыкия': '08',
            'карачаево-черкесскаяреспублика': '09',
            'республикакарелия': '10',
            'республикакоми': '11',
            'комиреспублика': '11',
            'республикамарийэл': '12',
            'республикамордовия': '13',
            'республикасаха': '14',
            'якутия': '14',
            'республикасевернаяосетия': '15',
            'алания': '15',
            'республикататарстан': '16',
            'татарстанреспублика': '16',
            'республикатыва': '17',
            'удмуртскаяреспублика': '18',
            'республикахакасия': '19',
            'чувашскаяреспублика': '21',
            'алтайскийкрай': '22',
            'краснодарскийкрай': '23',
            'красноярскийкрай': '24',
            'приморскийкрай': '25',
            'ставропольскийкрай': '26',
            'хабаровскийкрай': '27',
            'амурскаяобласть': '28',
            'архангельскаяобласть': '29',
            'астраханскаяобласть': '30',
            'белгородскаяобласть': '31',
            'брянскаяобласть': '32',
            'владимирскаяобласть': '33',
            'волгоградскаяобласть': '34',
            'вологодскаяобласть': '35',
            'воронежскаяобласть': '36',
            'ивановскаяобласть': '37',
            'иркутскаяобласть': '38',
            'калининградскаяобласть': '39',
            'калужскаяобласть': '40',
            'камчатскийкрай': '41',
            'кемеровскаяобласть': '42',
            'кировскаяобласть': '43',
            'костромскаяобласть': '44',
            'курганскаяобласть': '45',
            'курскаяобласть': '46',
            'ленинградскаяобласть': '47',
            'липецкаяобласть': '48',
            'магаданскаяобласть': '49',
            'московскаяобласть': '50',
            'мурманскаяобласть': '51',
            'нижегородскаяобласть': '52',
            'новгородскаяобласть': '53',
            'новосибирскаяобласть': '54',
            'омскаяобласть': '55',
            'оренбургскаяобласть': '56',
            'орловскаяобласть': '57',
            'пензенскаяобласть': '58',
            'пермскийкрай': '59',
            'псковскаяобласть': '60',
            'ростовскаяобласть': '61',
            'рязанскаяобласть': '62',
            'самарскаяобласть': '63',
            'саратовскаяобласть': '64',
            'сахалинскаяобласть': '65',
            'свердловскаяобласть': '66',
            'смоленскаяобласть': '67',
            'тамбовскаяобласть': '68',
            'тверскаяобласть': '69',
            'томскаяобласть': '70',
            'тульскаяобласть': '71',
            'тюменскаяобласть': '72',
            'ульяновскаяобласть': '73',
            'челябинскаяобласть': '74',
            'Забайкальскийкрай': '75',
            'ярославскаяобласть': '76',
            'москва': '77',
            'санкт-петербург': '78',
            'еврейскаяавтономнаяобласть': '79',
            'донецкаянароднаяреспублика': '80',
            'луганскаянароднаяреспублика': '81',
            'республикакрым': '82',
            'крымреспублика': '82',
            'ненецкийавтономныйокруг': '83',
            'херсонскаяобласть': '84',
            'запорожскаяобласть': '85',
            'ханты-мансийскийавтономныйокруг—Югра': '86',
            'чукотскийавтономныйокруг': '87',
            'ямало-ненецкийавтономныйокруг': '89',
            'ямало-ненецкийао': '89',
            'севастополь': '92',
            'чеченскаяреспублика': '95',
            'байконур': '94',
            'харьковскаяобласть': '188',
        }

        self.font_l_13 = css.font_l_13
        self.font_b_13 = css.font_b_13
        self.font_l_16 = css.font_l_16

    # Выпадающее меню в окне Кумите с выбором видов соревнований
    def choiceCompetition_Kumite(self):
        try:
            if self.loaded_file_data_type == 'file_pyatnov':
                self.check_to_wopf()
            if self.ui_kumite.Frame_Header.combo.currentText() == "Главное меню":
                self.showKumiteMenu()
            elif self.ui_kumite.Frame_Header.combo.currentText() == "Ката отбороч.":
                self.showDialogWindowKumiteToKataQual()
            elif self.ui_kumite.Frame_Header.combo.currentText() == "Ката финал":
                self.showDialogWindowKumiteToKataFinal()
        except Exception as e:
            print('_______Exception choiceCompetition_Kumite:', e)

    # Выпадающее меню в окне Ката по флажкам с выбором видов соревнований
    def choiceCompetition_kataQual(self):
        try:
            if self.loaded_file_data_type == 'file_pyatnov':
                self.check_to_wopf()
            if self.ui_kataQual.Frame_Header.combo.currentText() == "Главное меню":
                self.showKataQualMenu()
            elif self.ui_kataQual.Frame_Header.combo.currentText() == "Ката финал":
                self.showDialogWindowKataQualToKataFinal()
            elif self.ui_kataQual.Frame_Header.combo.currentText() == "Кумите":
                self.showDialogWindowKataQualToKumite()
        except Exception as e:
            print('_______Exception choiceCompetition_kataQual:', e)

    # Выпадающее меню в окне Ката финал с выбором видов соревнований
    def choiceCompetition_kataFinal(self):
        try:
            if self.loaded_file_data_type == 'file_pyatnov':
                self.check_to_wopf()
            if self.ui_kataFinal.Frame_Header.combo.currentText() == "Главное меню":
                self.showKataFinalMenu()
            elif self.ui_kataFinal.Frame_Header.combo.currentText() == "Ката отбороч.":
                self.showDialogWindowKataFinalToKataQual()
            elif self.ui_kataFinal.Frame_Header.combo.currentText() == "Кумите":
                self.showDialogWindowKataFinalToKumite()
        except Exception as e:
            print('_______Exception choiceCompetition_kataFinal:', e)

    # Метод, очищающий все словари, списки, множества со спортсменами, импортированными их Excel
    # (применяется, если выбран неверный лист. Старые данные удаляются)
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
        self.sportsmans_in_teams_dict = {}
        self.matchName_dict = {}
        self.df_Single_names = []
        self.df_Group_names = []
        self.df_Group_list = []
        self.df_Group_list_only_group = []
        self.teams_pairs = {}
        self.cur_men_pair_num = None  # Номер строки пары спортсменов
        # Данные для записи протокола Кумите Пятнов
        self.dict_paytnov_kumite_winner = {
            'siro': {'score': list(), 'hm_j': list(), 'result': None},
            'aka': {'score': list(), 'hm_j': list(), 'result': None},
        }

        self.ui_kataQual.frame_pyatnov.hide()
        self.ui_kataFinal.frame_pyatnov.hide()
        self.ui_kumite.frame_pyatnov.hide()

    # Метод, описывающий процесс выбора файла Excel и импорта данных из файла
    def select_file(self):
        try:
            self.combo.clear()

            self.btn_Kumite.setEnabled(True)
            self.btn_Kata_qual.setEnabled(True)
            self.btn_Kata_final.setEnabled(True)

            self.ui_kataQual.frame_pyatnov.hide()
            self.ui_kataFinal.frame_pyatnov.hide()
            self.ui_kumite.frame_pyatnov.hide()

            self.loaded_file_data_type = None

            self.file, _ = QFileDialog.getOpenFileName(self,
                                                       'Открыть файл со сводными списками в формате *xlsx, *xlsm', './',
                                                       "Excel (*.xlsx *.xlsm)")
            self.filename = str(self.file.split('/')[len(self.file.split('/')) - 1])
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 12px;")
            self.status_file.setText('Файл обрабатывается')
            self.xl = pd.ExcelFile(self.file)
            sheet_lst = self.xl.sheet_names
            pyatnov_lst = ['Aka+Shiro', 'team_rec', 'Жеребьевка']
            pyatnov_check = [value for value in sheet_lst if value in pyatnov_lst]
            # print(f"Values in both lists: \n{pyatnov_check}")
            # print(self.xl.sheet_names)
            # print(str(self.file))

            sheets11 = self.xl.book.worksheets

            setka_num = 1000

            sheets11_list = []
            for sheet in sheets11:
                if sheet.sheet_state == 'visible':

                    sh_t = sheet.title
                    # print('********     ', sh_t, '  -  ', sheet.sheet_state, ' ___', sh_t.find('ПФ_и_ ФИНАЛ_КАТА'), ' ___', sh_t.find('ФИНАЛ_КАТА'))
                    sheets11_list.append(sh_t)
                    if not sh_t.find('СЕТКА ('):
                        sh_t_lst_index = sh_t.find('_') if sh_t.find('_') >= 0 else sh_t.find(')')
                        setka_num = int(sh_t[7:sh_t_lst_index]) if sh_t[7:sh_t_lst_index].isdigit() else 1000
                    if not sh_t.find('Aka+Shiro'):
                        self.sheet_name_aka_shiro = sh_t
                    if sh_t.find('ФИНАЛ') >= 0:
                        self.sheet_name_final = sh_t

                else:
                    pass
                    # print('________     ', sheet.title, '  -  ', sheet.sheet_state)

            self.xl.close()

            # Разблокировка интерфейса Кумите
            self.blockedKumiteFrame(False)

            # Проверка, загруженный файл по шаблону Пятнова
            if len(pyatnov_check) == len(pyatnov_lst):

                self.pyatnov_flag()

                self.user_choice = 0
                self.pyatnov_processing()
                self.combo.hide()
                # print(222)
            # Прочие шаблоны - нужно выбрать лист соревнований
            elif len(self.xl.sheet_names) > 1:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 12px;")
                self.status_file.setText(f'В файле  <b>{self.filename}</b> несколько листов, выберите нужный')
                self.combo.show()
                self.combo.addItems(self.xl.sheet_names)


            else:
                self.combo.hide()
                self.user_choice = 0
                self.data_processing()
        except Exception as e:
            if self.sportsmans_ages_dict != {}:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 12px;")
                self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')
                self.show_with_load_file_interface()
                return
            else:
                if str(e) == '':
                    e = 'Файл не выбран'
                self.loaded_file_data_type = None
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
                self.status_file.setText(f'<b>Ошибка:</b> select_file - {e}')
                print(f'select_file <b>Ошибка:</b> select_file - {e}')
                self.show_withOut_load_file_interface()
                return

    def show_withOut_load_file_interface(self):
        self.ui_kumite.Form2.setFixedSize(900, 560)
        self.ui_kumite.frame_bottom.show()
        self.ui_kumite.frame_bottom.move(0, 559)
        self.ui_kumite.frame_bottom1.hide()
        self.ui_kumite.frame_bottom3.hide()

        self.ui_kataQual.frame_pyatnov.hide()
        self.ui_kataFinal.frame_pyatnov.hide()
        self.ui_kumite.frame_pyatnov.hide()

        self.ui_kataQual.frame_sportsmans.hide()
        self.ui_kataFinal.frame_sportsmans.hide()
        self.ui_kumite.frame_sportsmans.hide()

        self.frame_header_combo_enabled()

        self.ui_kataQual.lineEdit_name_red_1.setEnabled(True)
        self.ui_kataQual.lineEdit_region_red_1.setEnabled(True)
        self.ui_kataQual.lineEdit_name_white_1.setEnabled(True)
        self.ui_kataQual.lineEdit_region_white_1.setEnabled(True)

        self.ui_kataFinal.lineEdit_name_red_1.setEnabled(True)
        self.ui_kataFinal.lineEdit_region_red_1.setEnabled(True)
        print('show_withOut_load_file_interface')

    def show_with_load_file_interface(self):
        # Файл Юткина
        self.ui_kumite.Form2.setFixedSize(900, 670)
        self.ui_kumite.frame_bottom1.show()
        self.ui_kumite.frame_bottom3.show()
        self.ui_kumite.frame_bottom.hide()

        self.ui_kataQual.frame_pyatnov.hide()
        self.ui_kataFinal.frame_pyatnov.hide()
        self.ui_kumite.frame_pyatnov.hide()

        self.ui_kataQual.frame_sportsmans.show()
        self.ui_kataFinal.frame_sportsmans.show()
        self.ui_kumite.frame_sportsmans.show()

        self.frame_header_combo_enabled()

        self.ui_kataQual.lineEdit_name_red_1.setEnabled(True)
        self.ui_kataQual.lineEdit_region_red_1.setEnabled(True)
        self.ui_kataQual.lineEdit_name_white_1.setEnabled(True)
        self.ui_kataQual.lineEdit_region_white_1.setEnabled(True)

        self.ui_kataFinal.lineEdit_name_red_1.setEnabled(True)
        self.ui_kataFinal.lineEdit_region_red_1.setEnabled(True)

        self.ui_kumite.reset_all(self.flags_dict)
        print('    show_with_load_file_interface')
        print('self.df_Group_list_only_group')
        print(self.df_Group_list_only_group)

    def frame_header_combo_enabled(self):
        # Отображаем все пункты в выпадающем списке Главное меню-Ката-Кумите
        self.ui_kataQual.Frame_Header.combo.model().item(1).setEnabled(True)
        self.ui_kataQual.Frame_Header.combo.model().item(2).setEnabled(True)
        self.ui_kataFinal.Frame_Header.combo.model().item(1).setEnabled(True)
        self.ui_kataFinal.Frame_Header.combo.model().item(2).setEnabled(True)
        self.ui_kumite.Frame_Header.combo.model().item(1).setEnabled(True)
        self.ui_kumite.Frame_Header.combo.model().item(2).setEnabled(True)

    def frame_header_combo_disabled(self):
        # Скрытие все пункты кроме "Главное меню" в выпадающем списке Главное меню-Ката-Кумите
        self.ui_kataQual.Frame_Header.combo.model().item(1).setEnabled(False)
        self.ui_kataQual.Frame_Header.combo.model().item(2).setEnabled(False)
        self.ui_kataFinal.Frame_Header.combo.model().item(1).setEnabled(False)
        self.ui_kataFinal.Frame_Header.combo.model().item(2).setEnabled(False)
        self.ui_kumite.Frame_Header.combo.model().item(1).setEnabled(False)
        self.ui_kumite.Frame_Header.combo.model().item(2).setEnabled(False)

    def show_pyatnov_kata_interface(self):
        self.btn_Kumite.setEnabled(False)
        self.btn_Kata_qual.setEnabled(True)
        self.btn_Kata_final.setEnabled(True)

        self.ui_kataQual.frame_pyatnov.show()
        self.ui_kataFinal.frame_pyatnov.show()
        self.ui_kumite.frame_pyatnov.hide()

        self.ui_kataQual.frame_sportsmans.hide()
        self.ui_kataFinal.frame_sportsmans.hide()
        self.ui_kumite.frame_sportsmans.hide()

        self.ui_kumite.Form2.setFixedSize(900, 610)
        self.ui_kumite.frame_bottom1.hide()
        self.ui_kumite.frame_bottom3.hide()
        self.ui_kumite.frame_bottom.show()
        self.ui_kumite.frame_bottom.move(0, 609)

        self.ui_kataQual.Frame_Header.combo.model().item(2).setEnabled(False)
        self.ui_kataFinal.Frame_Header.combo.model().item(2).setEnabled(False)

        self.ui_kataQual.lineEdit_name_red_1.show()
        self.ui_kataQual.lineEdit_region_red_1.show()
        self.ui_kataQual.lineEdit_name_white_1.show()
        self.ui_kataQual.lineEdit_region_white_1.show()

        self.ui_kataQual.lineEdit_name_red_1.setEnabled(False)
        self.ui_kataQual.lineEdit_region_red_1.setEnabled(False)
        self.ui_kataQual.lineEdit_name_white_1.setEnabled(False)
        self.ui_kataQual.lineEdit_region_white_1.setEnabled(False)

        self.ui_kataFinal.lineEdit_name_red_1.setEnabled(False)
        self.ui_kataFinal.lineEdit_region_red_1.setEnabled(False)

    def show_pyatnov_kumite_interface(self, team=False):
        self.btn_Kumite.setEnabled(True)
        self.btn_Kata_qual.setEnabled(False)
        self.btn_Kata_final.setEnabled(False)

        self.ui_kataQual.frame_pyatnov.hide()
        self.ui_kataFinal.frame_pyatnov.hide()
        self.ui_kumite.frame_pyatnov.show()

        self.ui_kataQual.frame_sportsmans.hide()
        self.ui_kataFinal.frame_sportsmans.hide()
        self.ui_kumite.frame_sportsmans.hide()

        self.ui_kumite.Form2.setFixedSize(900, 610)
        self.ui_kumite.frame_pyatnov.setGeometry(QtCore.QRect(0, 560, 900, 50))
        self.ui_kumite.frame_bottom1.show()
        self.ui_kumite.frame_bottom.hide()

        self.ui_kumite.Frame_Header.combo.model().item(1).setEnabled(False)
        self.ui_kumite.Frame_Header.combo.model().item(2).setEnabled(False)

        self.ui_kumite.btn_NewCategory.hide()

        if team:
            self.ui_kumite.Form2.setFixedSize(900, 648)
            self.ui_kumite.frame_pyatnov.setGeometry(QtCore.QRect(0, 560, 900, 88))
            self.ui_kumite.frame_bottom.show()
            self.ui_kumite.frame_bottom.move(0, 647)

            self.ui_kumite.pyatnov_label.setText('Выбор команд')
            self.ui_kumite.btn_show_screen.setGeometry(QtCore.QRect(405, 475, 90, 35))

            self.ui_kumite.lineEdit_region_white_1.hide()
            self.ui_kumite.lineEdit_region_red_1.hide()

            self.ui_kumite.pyatnov_pair_label.show()
            self.ui_kumite.pyatnov_pair_name.show()
        else:
            self.ui_kumite.pyatnov_label.setText('Выберите пару')
            self.ui_kumite.btn_show_screen.setGeometry(QtCore.QRect(405, 475, 90, 50))

            self.ui_kumite.lineEdit_region_white_1.show()
            self.ui_kumite.lineEdit_region_red_1.show()

            self.ui_kumite.pyatnov_pair_label.hide()
            self.ui_kumite.pyatnov_pair_name.hide()

    def userChoice(self):
        self.user_choice_list = self.xl.sheet_names
        self.user_choice = self.user_choice_list.index(self.combo.currentText())
        self.data_processing()

    def pyatnov_processing(self):
        # Обработка excel
        sheets11 = self.xl.book.worksheets
        setka_num = 1000
        aka_shiro = None

        sheet_lst = []
        for sheet in sheets11:
            sh_t = sheet.title
            if sheet.sheet_state == 'visible':
                sheet_lst.append(sh_t)
                if not sh_t.find('СЕТКА ('):
                    sh_t_lst_index = sh_t.find('_') if sh_t.find('_') >= 0 else sh_t.find(')')
                    setka_num = int(sh_t[7:sh_t_lst_index]) if sh_t[7:sh_t_lst_index].isdigit() else 1000
                if not sh_t.find('Aka+Shiro'):
                    aka_shiro = sh_t
                if sh_t.find('ФИНАЛ') >= 0:
                    sheet_name_final = sh_t
                if sh_t.find('Прот_арб') >= 0:
                    self.sheet_name_referee = sh_t
        self.xl.close()
        # Создание списков
        if not aka_shiro:
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 12px;")
            self.status_file.setText(
                f'Данные не загружены. Тип файла определен (Пятнов), но не найден лист <b>aka_shiro</b>')
            self.clearDataMember()
            self.show_withOut_load_file_interface()
            return print('aka_shiro: Лист не найден')
        self.filename = str(self.file.split('/')[len(self.file.split('/')) - 1])
        is_semi_final = [False, False]  # [Полуфинал, Финал]

        if self.file:
            try:
                self.clearDataMember()

                competition_data = pd.read_excel(self.file, sheet_name='Жеребьевка', usecols='I:L',
                                                 header=8, nrows=3, names=['I', 'J', 'K', 'L'])
                # Проверка наличия данных о категории
                if competition_data['I'][0] != 'дисциплина':
                    raise 'Выбран неверный файл или лист'
                comp_type = competition_data['K'][0]

                qual_sportsman_cnt = 0  # Номер последней пары в отборочных
                final_sportsman_cnt = 3
                if comp_type == 'ката':
                    for sheet_name in sheet_lst:
                        if not sheet_name.find('ПФ_и_ ФИНАЛ_КАТА'):
                            final_sportsman_cnt = 7
                        elif not sheet_name.find('ФИНАЛ_КАТА'):
                            final_sportsman_cnt = 3

                qual_sportsman_cnt = 32 - final_sportsman_cnt if setka_num < 64 else 64 - final_sportsman_cnt

                # Название категории и для кумите КОМ список спортсменов в командах
                self.category_label = ""
                self.sportsmans_in_teams_dict = {}
                if competition_data['L'][0] in ('КОМ.', 'груп.'):
                    if competition_data['L'][0] == 'КОМ.':
                        self.pyatnov_flag(f4=True)
                        self.category_label = 'КОМАНДНЫЕ. '
                        # Список спортменов в командах
                        self.sportsmans_in_teams_dict = pd.read_excel(self.file, sheet_name='Жеребьевка', header=8,
                                                                      nrows=64, usecols=[1, 6], index_col=0,
                                                                      names=['team', 'names'])
                        self.sportsmans_in_teams_dict.dropna(axis=0, how='all', inplace=True)
                        self.sportsmans_in_teams_dict = self.sportsmans_in_teams_dict.to_dict()
                        self.sportsmans_in_teams_dict = self.sportsmans_in_teams_dict['names']
                        for i in self.sportsmans_in_teams_dict:
                            self.sportsmans_in_teams_dict[i] = self.sportsmans_in_teams_dict[i].split('\n')

                        referee_protocol = pd.read_excel(self.file, sheet_name='Прот_арб', header=0,
                        usecols=[0, 1, 2,
                                   3, 4, 5, 6, 7,
                                   8,
                                   9,
                                   10, 11, 12, 13, 14,
                                   15, 17
                                 ],
                        names=[
                        '1_siro_num', '2_siro_sportsman', '3_siro_region',
                        '4_siro_rating_1', '5_siro_rating_2', '6_siro_rating_3', '7_siro_rating_4', '8_siro_rating_5',
                        '9_siro_score',
                        '10_aka_score',
                        '11_aka_rating_1', '12_aka_rating_2', '13_aka_rating_3', '14_aka_rating_4', '15_aka_rating_5',
                        '17_aka_sportsman', '18_aka_num'
                        ]
                                                         )
                        use11cols = [0, 1, 2,
                                   3, 4, 5, 6, 7,
                                   8,
                                   9,
                                   10, 11, 12, 13, 14,
                                   10, 15, 17]
                        use22cols = [1, 2, 3,
                                   4, 5, 6, 7, 8,
                                   9,
                                   10,
                                   11, 12, 13, 14, 15,
                                   12, 16, 18]
                        name11s=[
                        '1_siro_num', '2_siro_sportsman', '3_siro_region',
                        '4_siro_rating_1', '5_siro_rating_2', '6_siro_rating_3', '7_siro_rating_4', '8_siro_rating_5',
                        '9_siro_score',
                        '10_aka_score',
                        '11_aka_rating_1', '12_aka_rating_2', '13_aka_rating_3', '14_aka_rating_4', '15_aka_rating_5',
                        '16_aka_region', '17_aka_sportsman', '18_aka_num'
                        ]

                        referee_protocol = referee_protocol.fillna('')
                        # print('referee_protocol', len(referee_protocol))
                        # print(referee_protocol.loc[77])
                        # # Удаляем выступивших, запрещаем выбор - делаем серым или просто удаляем из списка
                        # self.sportsmen_list = \
                        #     self.sportsmen_list.query(
                        #         'score_siro == score_aka or (score_siro.isna() and score_aka.isna())')

                        t_name_dict = referee_protocol.iloc[21::53, [0, 2, 10]].to_dict()

                        # Список пар участвующих (pairs)
                        pairs_1 = referee_protocol.iloc[24::53, [0, 1, 15, 8, 9]].to_dict()
                        pairs_2 = referee_protocol.iloc[26::53, [0, 1, 15, 8, 9]].to_dict()
                        pairs_3 = referee_protocol.iloc[28::53, [0, 1, 15, 8, 9]].to_dict()
                        perebivka = referee_protocol.iloc[37::53, [0, 1, 15, 8, 9]].to_dict()

                        # print('pairs_1')
                        # print(pairs_1)
                        #
                        # print('pairs_2')
                        # print(pairs_2)
                        #
                        # print('pairs_3')
                        # print(pairs_3)
                        #
                        # print('perebivka')
                        # print(perebivka)

                        self.teams_pairs = dict()
                        self.cur_men_pair_num = None  # Номер строки пары спортсменов
                        for key in pairs_2['1_siro_num'].keys():
                            team_siro = t_name_dict['3_siro_region'][key - 5]
                            team_aka = t_name_dict['11_aka_rating_1'][key - 5]

                            if team_siro == '' and team_aka == '':
                                continue

                            team_siro_short = team_siro
                            team_aka_short = team_aka

                            if len(team_siro.split(' ')) > 1:
                                team_siro_short = team_siro.split(' ')[0] + ' ком ' + team_siro.split(' ком ')[1]
                            if len(team_aka.split(' ')) > 1:
                                team_aka_short = team_aka.split(' ')[0] + ' ком ' + team_aka.split(' ком ')[1]

                            tmp_teams_name = team_siro_short + ' - ' + team_aka_short
                            siro_man_1 = pairs_1['2_siro_sportsman'][key - 2]
                            siro_man_2 = pairs_2['2_siro_sportsman'][key]
                            siro_man_3 = pairs_3['2_siro_sportsman'][key + 2]
                            siro_perebivka = perebivka['2_siro_sportsman'][key + 11]
                            aka_man_1 = pairs_1['17_aka_sportsman'][key - 2]
                            aka_man_2 = pairs_2['17_aka_sportsman'][key]
                            aka_man_3 = pairs_3['17_aka_sportsman'][key + 2]
                            aka_perebivka = perebivka['17_aka_sportsman'][key + 11]

                            siro_short_man_1, siro_short_man_2, siro_short_man_3 = ['', '', '']
                            aka_short_man_1, aka_short_man_2, aka_short_man_3 = ['', '', '']
                            men_pair_1, men_pair_2, men_pair_3 = ['', '', '']
                            # Для проведенных выступлений блокируем (0) возможность выбора строки из выпадающего меню
                            complete_pair_1, complete_pair_2, complete_pair_3 = [1, 1, 1]
                            # Пары спортсменов для перебивки
                            siro_short_perebivka, aka_short_perebivka = ['', '']
                            perebivka_tmp = ''
                            complete_perebivka = 1

                            if len(siro_man_1.split(' ')) > 1:
                                siro_short_man_1 = siro_man_1.split(' ')[0] + ' ' + siro_man_1.split(' ')[1][0] + '.'
                            if len(siro_man_2.split(' ')) > 1:
                                siro_short_man_2 = siro_man_2.split(' ')[0] + ' ' + siro_man_2.split(' ')[1][0] + '.'
                            if len(siro_man_3.split(' ')) > 1:
                                siro_short_man_3 = siro_man_3.split(' ')[0] + ' ' + siro_man_3.split(' ')[1][0] + '.'
                            if len(siro_perebivka.split(' ')) > 1:
                                siro_short_perebivka = (
                                        siro_perebivka.split(' ')[0] + ' ' + siro_perebivka.split(' ')[1][0] + '.')


                            if len(aka_man_1.split(' ')) > 1:
                                aka_short_man_1 = aka_man_1.split(' ')[0] + ' ' + aka_man_1.split(' ')[1][0] + '.'
                            if len(aka_man_2.split(' ')) > 1:
                                aka_short_man_2 = aka_man_2.split(' ')[0] + ' ' + aka_man_2.split(' ')[1][0] + '.'
                            if len(aka_man_3.split(' ')) > 1:
                                aka_short_man_3 = aka_man_3.split(' ')[0] + ' ' + aka_man_3.split(' ')[1][0] + '.'
                            if len(aka_perebivka.split(' ')) > 1:
                                aka_short_perebivka = (
                                        aka_perebivka.split(' ')[0] + ' ' + aka_perebivka.split(' ')[1][0] + '.')

                            if siro_man_1 != '' or aka_man_1 != '':
                                men_pair_1 = f"{siro_short_man_1} -  {aka_short_man_1}"
                            if siro_man_2 != '' or aka_man_2 != '':
                                men_pair_2 = f"{siro_short_man_2} -  {aka_short_man_2}"
                            if siro_man_3 != '' or aka_man_3 != '':
                                men_pair_3 = f"{siro_short_man_3} -  {aka_short_man_3}"
                            if siro_perebivka != '' or aka_perebivka != '':
                                perebivka_tmp = f"{siro_short_perebivka} -  {aka_short_perebivka}"

                            # Для проведенных выступлений блокируем возможность выбора строки из выпадающего меню
                            if pairs_1['9_siro_score'][key - 2] or  pairs_1['10_aka_score'][key - 2]:
                                complete_pair_1 = 0
                            if pairs_2['9_siro_score'][key] or  pairs_2['10_aka_score'][key]:
                                complete_pair_2 = 0
                            if pairs_3['9_siro_score'][key + 2] or  pairs_3['10_aka_score'][key + 2]:
                                complete_pair_3 = 0

                            # Для проведенных выступлений блокируем возможность выбора строки из выпадающего меню
                            if perebivka['9_siro_score'][key + 11] or  perebivka['10_aka_score'][key + 11]:
                                complete_perebivka = 0

                            #Если все бои завершены и нет перебивки - не добавляем команду
                            if complete_pair_1==complete_pair_2==complete_pair_3==0 and not (complete_perebivka==1 and perebivka_tmp):
                                continue
                            self.teams_pairs[tmp_teams_name] = {
                                'team_siro': team_siro,
                                'team_aka': team_aka,
                                'siro_man_1': siro_man_1,
                                'siro_man_2': siro_man_2,
                                'siro_man_3': siro_man_3,
                                'siro_short_man_1': siro_short_man_1,
                                'siro_short_man_2': siro_short_man_2,
                                'siro_short_man_3': siro_short_man_3,
                                'aka_man_1': aka_man_1,
                                'aka_man_2': aka_man_2,
                                'aka_man_3': aka_man_3,
                                'aka_short_man_1': aka_short_man_1,
                                'aka_short_man_2': aka_short_man_2,
                                'aka_short_man_3': aka_short_man_3,
                                'men_pair_1': men_pair_1,
                                'men_pair_2': men_pair_2,
                                'men_pair_3': men_pair_3,
                                'row_num_1': key,
                                'row_num_2': key+2,
                                'row_num_3': key+4,
                                'complete_pair_1': complete_pair_1,
                                'complete_pair_2': complete_pair_2,
                                'complete_pair_3': complete_pair_3,

                                'siro_short_perebivka': siro_short_perebivka,
                                'aka_perebivka': aka_perebivka,
                                'aka_short_perebivka': aka_short_perebivka,
                                'perebivka_tmp': perebivka_tmp,
                                'row_num_perebivka': key+13,
                                'complete_perebivka': complete_perebivka,
                            }
                    else:
                        self.category_label = 'ГРУППА. '
                        self.pyatnov_flag(f2=True)
                else:
                    if comp_type == 'ката':
                        self.pyatnov_flag(f1=True)
                    else:
                        self.pyatnov_flag(f3=True)
                self.category_label = f"{self.category_label}{competition_data['K'][1]}{competition_data['J'][2]}"
                pd.options.display.max_columns = None
                # Создаём датасет из данных на листе Aka+Shiro
                self.sportsmen_list = pd.read_excel(self.file, sheet_name=aka_shiro, usecols=[1, 2, 8, 9, 10],
                                                    header=9, names=['duet', 'siro', 'score_siro', 'score_aka', 'aka'])
                # добавляем столбец с номером строки, куда будем записывать очки победителей
                self.sportsmen_list['row_num'] = self.sportsmen_list.index + 12
                # Удаляем каждую втору строчку (это пустая строка с подочками 4, 0, 3, 1, 2
                self.sportsmen_list = self.sportsmen_list.iloc[::2, :]
                self.sportsmen_list = self.sportsmen_list.query(f'duet < {qual_sportsman_cnt}')
                self.sportsmen_list = self.sportsmen_list.iloc[:, [5, 1, 4, 2, 3]]
                # Обнуляем индексы
                self.sportsmen_list = self.sportsmen_list.reset_index(drop=True)
                # Удаляем пустые строки
                self.sportsmen_list.dropna(axis=0, how='all', inplace=True)
                # Удаляем строки, где нет ФИО сиро или ака
                self.sportsmen_list.dropna(axis=0, subset=["siro", "aka"], inplace=True)
                # Оставляем строки только для пар, где, или результат 0-0, или другой одинаковый (1-1, 2-2 и тд)
                self.sportsmen_list = \
                    self.sportsmen_list.query('score_siro == score_aka or (score_siro.isna() and score_aka.isna())')

                # Регионы спортсменов
                self.region_dict = pd.read_excel(self.file, sheet_name='Жеребьевка', usecols=[1, 4, 6], header=8,
                                                 names=['name', 'region', 'team_list'])
                self.region_dict.dropna(axis=0, how='all', inplace=True)

                # Если датасет пустой, значит остались только финальные сетки
                if not len(self.sportsmen_list):

                    if comp_type == 'ката':
                        # Если полуфинал и финал
                        if sheet_name_final.find('ПФ') >= 0:
                            is_semi_final = [True, False]
                            # Создаём датасет из данных на листе ФИНАЛ
                            self.sportsmen_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=8,
                                                                usecols=[1, 3], header=5, names=['name', 'kata'])
                            self.sportsmen_list['row_num'] = self.sportsmen_list.index + 7
                            self.sportsmen_list['ttl_cnt_sp'] = len(self.sportsmen_list.query(f'name.notna()'))
                            self.sportsmen_list = self.sportsmen_list.query(f'name.notna() and kata.isna()')
                            self.sportsmen_list = self.sportsmen_list.iloc[:, [2, 0, 1, 3]]

                            # Проверяем есть ли переигровка в полуфинале
                            self.rematch_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=2,
                                                              usecols=[1, 3], header=14, names=['name', 'kata'])
                            self.rematch_list['row_num'] = self.rematch_list.index + 16
                            self.rematch_list = self.rematch_list.query(f'name.notna() and kata.isna()')
                            self.rematch_list = self.rematch_list.iloc[:, [2, 0, 1]]

                            self.sportsmen_list = pd.concat([self.sportsmen_list, self.rematch_list], sort=False)

                            # Если все полуфиналы отыграны смотрим на финалы
                            if not len(self.sportsmen_list):
                                is_semi_final = [False, True]
                                self.sportsmen_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=4,
                                                                    usecols=[1, 3], header=24, names=['name', 'kata'])
                                self.sportsmen_list['row_num'] = self.sportsmen_list.index + 26
                                self.sportsmen_list['ttl_cnt_sp'] = len(self.sportsmen_list.query(f'name.notna()'))
                                self.sportsmen_list = self.sportsmen_list.query(f'name.notna() and kata.isna()')
                                self.sportsmen_list = self.sportsmen_list.iloc[:, [2, 0, 1, 3]]

                                # Проверяем есть ли переигровка в финале
                                self.rematch_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=2,
                                                                  usecols=[1, 3], header=29, names=['name', 'kata'])
                                self.rematch_list['row_num'] = self.rematch_list.index + 31
                                self.rematch_list = self.rematch_list.query(f'name.notna() and kata.isna()')
                                self.rematch_list = self.rematch_list.iloc[:, [2, 0, 1]]
                        else:
                            is_semi_final = [False, True]
                            self.sportsmen_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=4,
                                                                usecols=[1, 3], header=5,
                                                                names=['name', 'kata'])
                            self.sportsmen_list['row_num'] = self.sportsmen_list.index + 7
                            self.sportsmen_list['ttl_cnt_sp'] = len(self.sportsmen_list.query(f'name.notna()'))
                            self.sportsmen_list = self.sportsmen_list.query(f'name.notna() and kata.isna()')
                            self.sportsmen_list = self.sportsmen_list.iloc[:, [2, 0, 1, 3]]

                            # Проверяем есть ли переигровка в финале
                            self.rematch_list = pd.read_excel(self.file, sheet_name=sheet_name_final, nrows=2,
                                                              usecols=[1, 3], header=11, names=['name', 'kata'])
                            self.rematch_list['row_num'] = self.rematch_list.index + 13
                            self.rematch_list = self.rematch_list.query(f'name.notna() and kata.isna()')
                            self.rematch_list = self.rematch_list.iloc[:, [2, 0, 1]]

                        # Если список не пуст, то добавляем сокращённые имена и регионы
                        if len(self.sportsmen_list):
                            self.sportsmen_list['name_short'] = \
                                self.sportsmen_list['name'].str.split(' ', expand=True)[0] + ' ' + \
                                self.sportsmen_list['name'].str.split(' ', expand=True)[1].str[0] + '.'

                            self.region_dict.rename(columns={'name': 'name1'}, inplace=True)
                            self.sportsmen_list = pd.merge(self.sportsmen_list, self.region_dict[['name1', 'region']],
                                                           left_on='name', right_on='name1', how='left')

                            self.sportsmen_list.drop('name1', axis=1, inplace=True)
                            self.sportsmen_list.rename(columns={'region': 'region_aka'}, inplace=True)

                            self.sportsmen_dict = self.sportsmen_list.to_dict()

                    elif comp_type == 'кумите':
                        # Создаём датасет из данных на листе Aka+Shiro
                        self.sportsmen_list = pd.read_excel(self.file, sheet_name=aka_shiro, usecols=[1, 2, 8, 9, 10],
                                                            header=9,
                                                            names=['duet', 'siro', 'score_siro', 'score_aka', 'aka'])
                        # добавляем столбец с номером строки, куда будем записывать очки победителей
                        self.sportsmen_list['row_num'] = self.sportsmen_list.index + 12

                        # Удаляем каждую втору строчку (это пустая строка с подочками 4, 0, 3, 1, 2
                        self.sportsmen_list = self.sportsmen_list.iloc[::2, :]
                        self.sportsmen_list = self.sportsmen_list.query(f'duet >= {qual_sportsman_cnt}')
                        self.sportsmen_list = self.sportsmen_list.iloc[:, [5, 1, 4, 2, 3]]
                        # Обнуляем индексы
                        self.sportsmen_list = self.sportsmen_list.reset_index(drop=True)

                        # Удаляем пустые строки
                        self.sportsmen_list.dropna(axis=0, how='all', inplace=True)
                        # Удаляем строки, где нет ФИО сиро или ака
                        self.sportsmen_list.dropna(axis=0, subset=["siro", "aka"], inplace=True)
                        # Оставляем строки только для пар, где, или результат 0-0, или другой одинаковый (1-1, 2-2 и тд)
                        self.sportsmen_list = \
                            self.sportsmen_list.query(
                                'score_siro == score_aka or (score_siro.isna() and score_aka.isna())')

                if len(self.sportsmen_list):
                    if is_semi_final == [False, False]:
                        # Добавляем столбцы с ФИО, кратким ФИО и пара спортсменов
                        if self.sportsmans_in_teams_dict:
                            team_num_siro = list(self.sportsmen_list['siro'].str.split(' - ком ', expand=True))[-1]
                            self.sportsmen_list['siro_short'] = \
                                self.sportsmen_list['siro'].str.split(' ', expand=True)[0] + ' ком ' + \
                                self.sportsmen_list['siro'].str.split(' - ком ', expand=True)[team_num_siro]

                            team_num_aka = list(self.sportsmen_list['aka'].str.split(' - ком ', expand=True))[-1]
                            self.sportsmen_list['aka_short'] = \
                                self.sportsmen_list['aka'].str.split(' ', expand=True)[0] + ' ком ' + \
                                self.sportsmen_list['aka'].str.split(' - ком ', expand=True)[team_num_aka]

                            self.sportsmen_list['combo_box'] = \
                                self.sportsmen_list['siro_short'] + ' - ' + self.sportsmen_list['aka_short']


                        else:
                            self.sportsmen_list['siro_short'] = \
                                self.sportsmen_list['siro'].str.split(' ', expand=True)[0] + ' ' + \
                                self.sportsmen_list['siro'].str.split(' ', expand=True)[1].str[0] + '.'

                            self.sportsmen_list['aka_short'] = \
                                self.sportsmen_list['aka'].str.split(' ', expand=True)[0] + ' ' + \
                                self.sportsmen_list['aka'].str.split(' ', expand=True)[1].str[0] + '.'

                            self.sportsmen_list['combo_box'] = \
                                self.sportsmen_list['siro_short'] + ' - ' + self.sportsmen_list['aka_short']
                        # Добавляем регион участников
                        if self.sportsmans_in_teams_dict:
                            self.sportsmen_list['region_siro'] = self.sportsmen_list['siro']
                            self.sportsmen_list['region_aka'] = self.sportsmen_list['aka']
                        else:
                            self.sportsmen_list = pd.merge(self.sportsmen_list, self.region_dict[['name', 'region']],
                                                           left_on='siro',
                                                           right_on='name', how='left')

                            self.sportsmen_list.drop('name', axis=1, inplace=True)
                            self.sportsmen_list.rename(columns={'region': 'region_siro'}, inplace=True)
                            self.sportsmen_list = pd.merge(self.sportsmen_list, self.region_dict[['name', 'region']],
                                                           left_on='aka', right_on='name', how='left')
                            self.sportsmen_list.drop('name', axis=1, inplace=True)
                            self.sportsmen_list.rename(columns={"region": "region_aka"}, inplace=True)

                        pd.options.display.max_columns = None

                    elif is_semi_final in [[False, True], [True, False]]:
                        self.sportsmen_list['combo_box'] = \
                            self.sportsmen_list['name'] + ' - ' + self.sportsmen_list['region_aka']

                    self.sportsmen_dict = self.sportsmen_list.to_dict()
                else:
                    self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 12px;")
                    self.status_file.setText(f'Файл  <b>{self.filename}</b> отработан. Данные не загружены')
                    self.loaded_file_data_type = 'file_pyatnov'
                    return 'file was completed'

                if comp_type == 'ката':
                    self.show_pyatnov_kata_interface()
                    self.ui_kumite.matchName12.setText(self.category_label)

                    if self.tatamiName == "":
                        self.ui_kataQual.matchName1.setText('Татами №#, ' + self.category_label)
                        self.ui_kataFinal.matchName1.setText('Татами №#, ' + self.category_label)
                    else:
                        self.ui_kataQual.matchName1.setText(self.tatamiName + ', ' + self.category_label)
                        self.ui_kataFinal.matchName1.setText(self.tatamiName + ', ' + self.category_label)

                    if is_semi_final == [False, False]:
                        self.ui_kataQual.pyatnov_name.clear()
                        self.ui_kataQual.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kataQual.pyatnov_name.setEnabled(True)

                        self.btn_Kata_qual.setEnabled(True)
                        self.btn_Kata_final.setEnabled(False)

                    elif is_semi_final in [[True, False], [False, True]]:

                        self.ui_kataQual.frame_pyatnov.hide()

                        self.ui_kataFinal.pyatnov_name.clear()
                        self.ui_kataFinal.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kataFinal.pyatnov_name.setEnabled(True)

                        # Список ката
                        self.ui_kataFinal.pyatnov_kata_name.clear()
                        self.ui_kataFinal.pyatnov_kata_name.addItems(self.kata_list)
                        self.ui_kataFinal.pyatnov_kata_name.setEnabled(True)
                        self.ui_kataFinal.pyatnov_kata_name.activated[str].connect(self.setLabel)

                        self.btn_Kata_qual.setEnabled(False)
                        self.btn_Kata_final.setEnabled(True)

                elif comp_type == 'кумите':
                    self.ui_kumite.lineEdit_name_white_1.setEnabled(False)
                    self.ui_kumite.lineEdit_region_white_1.setEnabled(False)
                    self.ui_kumite.lineEdit_name_red_1.setEnabled(False)
                    self.ui_kumite.lineEdit_region_red_1.setEnabled(False)

                    if self.flag_pyatnov_kumite_single:
                        self.show_pyatnov_kumite_interface(team=False)
                        self.ui_kumite.pyatnov_name.clear()
                        self.ui_kumite.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kumite.pyatnov_name.setEnabled(True)
                        self.ui_kumite.matchName12.setText(self.category_label)
                    elif self.flag_pyatnov_kumite_team:
                        self.show_pyatnov_kumite_interface(team=True)
                        self.ui_kumite.pyatnov_name.clear()
                        self.ui_kumite.pyatnov_name.addItem('Выберите команды...')
                        self.ui_kumite.pyatnov_name.addItems(self.teams_pairs.keys())
                        self.ui_kumite.pyatnov_name.setEnabled(True)
                        self.ui_kumite.matchName12.setText(self.category_label)

                self.status_file.setStyleSheet("color: rgb(0, 178, 80);")
                self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')
                self.loaded_file_data_type = 'file_pyatnov'

                # Скрываем все пункты из выпадающего списка Главное меню - Ката - Кумите
                self.frame_header_combo_disabled()

                threading.current_thread().main_thread_completion_status = True
                # Если был последний бой в отборочных Ката, то открываем окно Ката финал
                if comp_type == 'ката' and is_semi_final in [[True, False],
                                                             [False, True]] and self.ui_kataQual.isVisible():
                    threading.current_thread().main_thread_completion_status = 'self.showKataFinalWin()'
                    return 'self.showKataFinalWin()'

            except Exception as e:
                print('_______Exception pyatnov_processing:', e)
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 12px;")
                self.status_file.setText(f'Выбран неверный файл или лист: <b>{str(e)}</b>')
                self.clearDataMember()
                self.show_withOut_load_file_interface()

    def data_processing(self):
        self.filename = str(self.file.split('/')[len(self.file.split('/')) - 1])

        if self.file:
            try:
                self.sheet1 = None
                self.sheet1 = pd.read_excel(self.file, sheet_name=self.xl.sheet_names[self.user_choice])
                cols2skip = [4, 5, 6, 7]
                cols = [i for i in range(len(self.sheet1.columns) - 2) if i not in cols2skip]
                k = []
                for z in range(10, len(self.sheet1.columns) + 4):
                    k.append('a' + str(z))
                self.sheet = pd.read_excel(self.file, sheet_name=self.xl.sheet_names[self.user_choice],
                                           usecols=cols, header=None, names=k)

                for i in range(len(self.sheet.columns) - 1, 9, -1):
                    try:
                        if pd.isnull(self.sheet.iloc[4, i]):
                            self.sheet.drop(self.sheet.columns[[i]], axis=1, inplace=True)
                    except Exception as e:
                        print('_______Exception data_processing1:', e)

                kat_name = set(self.sheet.columns) - {'a10', 'a11', 'a12', 'a13'}
                self.list_kat_name = list(sorted(kat_name))

                self.clearDataMember()

                # Определяем строчку, с которой начинается таблица
                check_list_dementieva = ['м', 'юн-ры', 'д', 'ж', 'юн-ки']
                check_list_yutkin = ['мальчики', 'юноши', 'юниоры', 'мужчины', 'девочки', 'девушки', 'юниорки',
                                     'женщины']
                value_list = self.sheet['a14'].values.tolist()
                value_set = set(value_list)
                if value_list[0] in check_list_yutkin:
                    self.file_yutkin()
                    self.show_with_load_file_interface()
                    return
                else:
                    for x in value_set:
                        if x in check_list_dementieva:
                            self.countRowTab = self.sheet.loc[self.sheet['a14'] == x].index[0]
                            self.file_dementieva()
                            self.show_with_load_file_interface()
                            break
                # # Для окна Кумите, если загружен список отображается область с выбором категории
                # self.ui_kumite.Form2.setFixedSize(900, 750)
                # self.ui_kumite.frame_bottom1.show()
                # self.ui_kumite.frame_bottom.hide()
            except Exception as e:
                self.status_file.setStyleSheet("font-family: Gotham-Light; color: red; font-size: 12px;")
                print('_______Exception data_processing2:', e)
                self.status_file.setText(f'Выбран неверный файл или лист {e}')
                self.clearDataMember()
                self.show_withOut_load_file_interface()

    def file_dementieva(self):
        # print('file_dementieva')
        # print(self.list_kat_name)
        # for k_n in self.list_kat_name:
        #     # ЛИЧНЫЕ СОРЕВНОВАНИЯ
        #     # Поиск строк со значением "*" в столбце "k_n"
        #     #           (Поиск всех смортсменов, у которых в категории (столбце "k_n") поставлена ЗВЕЗДОЧКА "*")
        #     df2 = self.sheet.loc[self.sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]
        #
        #     # Создание словаря из найденых спортсменов
        #     df_Temp_Single_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
        #                                    'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))
        #
        #     # КОМАНДНЫЕ СОРЕВНОВАНИЯ
        #     # ------------
        #
        #     self.df_Single_names.append(k_n)
        #     self.df_Group_names.append(k_n)
        #     self.df_Single_list.append(df_Temp_Single_list)
        ################################################################
        # print(self.df_Single_list)
        # for i in self.df_Single_list:
        #     print(i)
        #     print('      ', type(i))

        self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 12px;")
        self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')

        # ОПРЕДЕЛЕНИЕ ТИПОВ СЛОВОРЕЙ В ЗАГРУЖЕННОМ ФАЙЛЕ     ############################################
        type_set = set(self.sheet.iloc[self.countRowTab - 2].values.tolist()) | set(
            self.sheet.iloc[self.countRowTab].values.tolist()) \
                   | set(self.sheet.iloc[self.countRowTab + 1].values.tolist())
        # ЛИЧНЫЕ СОРЕВНОВАНИЯ
        if 'личн' in type_set:
            self.individ_dict = self.calc_dict(self.countRowTab - 2, 'личн')
        else:
            self.individ_dict = {}
        # КОМАНДНЫЕ СОРЕВНОВАНИЯ
        if 'КОМ' in type_set:
            self.team_dict = self.calc_dict(self.countRowTab - 2, 'КОМ')
        else:
            self.team_dict = {}
        # КУМИТЕ
        if 'кумите' in type_set:
            self.kumite_dict = self.calc_dict(self.countRowTab + 1, 'кумите')
        else:
            self.kumite_dict = {}
        # КАТА
        if 'ката' in type_set:
            self.kata_dict = self.calc_dict(self.countRowTab + 1, 'ката')
        else:
            self.kata_dict = {}
        # М
        if 'м' in type_set:
            self.male_label_dict1 = self.calc_dict(self.countRowTab, 'м')
            self.male_label_dict |= self.male_label_dict1
        else:
            self.male_label_dict1 = {}
        # М
        if 'юн-ры' in type_set:
            self.male_label_dict1 = self.calc_dict(self.countRowTab, 'юн-ры')
            self.male_label_dict |= self.male_label_dict1
        else:
            self.male_label_dict1 = {}
        # Ж
        if 'ж' in type_set:
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'ж')
            self.female_label_dict |= self.female_label_dict1
        else:
            self.female_label_dict1 = {}
        # Ж
        if 'д' in type_set:
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'д')
            self.female_label_dict |= self.female_label_dict1
        else:
            self.female_label_dict1 = {}
        if 'юн-ки' in type_set:  # Ж
            self.female_label_dict1 = self.calc_dict(self.countRowTab, 'юн-ки')
            self.female_label_dict |= self.female_label_dict1
        else:
            self.female_label_dict1 = {}

        # ЛИЧНЫЕ СОРЕВНОВАНИЯ           ############################################
        # КОМАНДНЫЕ СОРЕВНОВАНИЯ        ############################################
        # КУМИТЕ                        ############################################
        # КАТА                          ############################################
        # М                             ############################################
        # # Ж                           ############################################
        # # Ж                           ############################################
        # ВСЕ ВОЗРАСТА  ############################################
        self.sportsmans_ages_dict = self.sheet.iloc[self.countRowTab - 1].to_dict()
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

        ############ Ката М/Ж КОМ   #################################
        self.team_kata_male_dict = self.team_dict.copy()
        self.team_kata_female_dict = self.team_dict.copy()
        for g in self.team_dict.keys():
            if g in (set(self.team_kumite) | set(self.male_label_dict)):
                self.team_kata_female_dict.pop(g)
            if g in (set(self.team_kumite) | set(self.female_label_dict)):
                self.team_kata_male_dict.pop(g)

        ############ Кумите М/Ж КОМ #################################
        self.team_kumite_male_dict = self.team_dict.copy()
        self.team_kumite_female_dict = self.team_dict.copy()
        for g in self.team_dict.keys():
            if g in (set(self.team_kata) | set(self.male_label_dict)):
                self.team_kumite_female_dict.pop(g)
            if g in (set(self.team_kumite) | set(self.female_label_dict)):
                self.team_kumite_male_dict.pop(g)

        # конструктор для matchName ############################################
        self.matchName_male_dict1 = self.male_sportsmans_ages_dict.copy()
        self.matchName_funk(self.matchName_male_dict1, "М")
        self.matchName_female_dict1 = self.female_sportsmans_ages_dict.copy()
        self.matchName_funk(self.matchName_female_dict1, "Ж")
        self.matchName = (self.matchName_male_dict1 | self.matchName_female_dict1).copy()
        self.matchName = dict(sorted(self.matchName.items()))

        self.loaded_file_data_type = 'file_dementieva'

        # print(self.team_dict)
        # print(self.team_dict.keys())
        # print(self.team_kumite_male_dict.keys())
        # print(self.team_kumite_female_dict.keys())
        # print(self.individ_kumite_male_dict)
        # print(self.individ_kumite_female_dict)
        # print(self.team_kumite_male_dict)
        # print(self.team_kumite_female_dict)

        for k_n in self.list_kat_name:
            # ЛИЧНЫЕ СОРЕВНОВАНИЯ
            # Поиск строк со значением "*" в столбце "k_n"
            #           (Поиск всех смортсменов, у которых в категории (столбце "k_n") поставлена ЗВЕЗДОЧКА "*")
            df2 = self.sheet.loc[self.sheet[k_n] == '*', ['a10', 'a11', 'a12', 'a13']]

            # Создание словаря из найденых спортсменов
            df_Temp_Single_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                           'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

            # КОМАНДНЫЕ СОРЕВНОВАНИЯ
            # ------------
            if k_n in self.team_dict.keys():
                self.df_Group_list.append(df_Temp_Single_list)
                self.df_Single_list.append({})

                self.df_Group_list_only_group.append(dict(zip(df2.a11, '')))
            else:
                self.df_Single_list.append(df_Temp_Single_list)
                self.df_Group_list.append({})
                self.df_Group_list_only_group.append({})

            self.df_Single_names.append(k_n)
            self.df_Group_names.append(k_n)

        # for i in self.df_Single_list:
        #     print(i)
        # for i in self.df_Group_list:
        #     print('      ', i)

    def file_yutkin(self):
        # print('file_yutkin')
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
                df2 = self.sheet.loc[
                    self.sheet[k_n].isin(
                        ['ком1', 'ком2', 'ком3', 'ком4', 'ком5', 'ком 1', 'ком 2', 'ком 3', 'ком 4', 'ком 5']
                    ), ['a10', 'a11', 'a12', 'a13', k_n]]
                df_Temp1_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))
                # print(df2)

                self.df_Group_list.append(df_Temp1_Group_list)
                self.df_Group_list_only_group.append(dict(zip(df2.a11 + ' - ' + df2[k_n], df2[k_n])))
                # print(dict(zip(df2.a11 + ' - ' + df2[k_n], '--')))
            else:
                self.df_Group_list.append({})
                self.df_Group_list_only_group.append({})

            self.df_Single_names.append(k_n)
            self.df_Group_names.append(k_n)
            self.df_Single_list.append(df_Temp_Single_list)
        ################################################################
        # print('self.df_Group_list_only_group')
        # print(self.df_Group_list_only_group)
        # print('self.df_Group_list')
        # print(self.df_Group_list)

        self.status_file.setStyleSheet("font-family: Gotham-Light; color: rgb(0, 178, 80); font-size: 12px;")
        self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')

        self.individ_kata_dict = self.calc_dict(3, 'один')  # КАТА ЛИЧН
        self.individ_kumite_dict = self.calc_dict(3, 'личн')  # КУМИТЕ ЛИЧН
        self.team_kata_dict = self.calc_dict(3, 'груп')  # КАТА ГРУП
        self.team_kumite_dict = self.calc_dict(3, 'ком')  # КУМИТЕ КОМ
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

        ############ Ката М КОМ   #################################
        self.team_kata_male_dict = self.team_kata_dict.copy()
        for g in set(self.female_label_dict):
            if g in self.team_kata_male_dict:
                self.team_kata_male_dict.pop(g)

        ############ Ката Ж КОМ   #################################
        self.team_kata_female_dict = self.team_kata_dict.copy()
        for g in set(self.male_label_dict):
            if g in self.team_kata_female_dict:
                self.team_kata_female_dict.pop(g)

        ############ Кумите М КОМ #################################
        self.team_kumite_male_dict = self.team_kumite_dict.copy()
        for g in set(self.female_label_dict):
            if g in self.team_kumite_male_dict:
                self.team_kumite_male_dict.pop(g)

        ############ Кумите Ж КОМ #################################
        self.team_kumite_female_dict = self.team_kumite_dict.copy()
        for g in set(self.male_label_dict):
            if g in self.team_kumite_female_dict:
                self.team_kumite_female_dict.pop(g)

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
        self.matchName = dict(sorted(self.matchName.items()))

        # М ВСЕ ВОЗРАСТА  ############################################
        self.male_sportsmans_ages_dict = self.sportsmans_ages_dict.copy()
        for g in set(self.female_label_dict):
            if g in self.male_sportsmans_ages_dict:
                self.male_sportsmans_ages_dict.pop(g)

        self.loaded_file_data_type = 'file_yutkin'

    def matchName_funk(self, matchName_sex_dict, sex):
        if sex == "М":
            value_1 = "Мальчики"
            value_2 = "Юноши"
            value_3 = "Юниоры"
            value_4 = "Мужчины"
        else:
            value_1 = "Девочки"
            value_2 = "Девушки"
            value_3 = "Юниорки"
            value_4 = "Женщины"
        # age_checklist_1 = ['6 лет', '6-7 лет', '7 лет', '7-8 лет', '8 лет', '8-9 лет', '8-11 лет', '9 лет', '9-10 лет',
        #                    '10 лет', '10-11 лет', '11 лет', '11-12 лет', '12 лет', '12-13 лет', '12-15 лет', '13 лет',
        #                    '13-14 лет']
        # age_checklist_2 = ['14 лет', '14-15 лет', '14-17 лет', '14-20 лет', '15 лет', '15-16 лет', '16 лет',
        #                    '16-17 лет', '16-20 лет', '17 лет', '17-18 лет']
        # age_checklist_3 = ['18 лет', '19 лет', '20 лет', '18-20 лет']
        # age_checklist_4 = ['с 16 лет', 'с 18 лет', 'с 21 года', '21-30 лет', '21-39 лет', '30-39 лет', '40+',
        #                    '40-49 лет', '50+', '50-60 лет']
        # for key, value in matchName_sex_dict.items():
        #     if value in age_checklist_1:
        #         matchName_sex_dict[key] = value_1 + " " + value
        #     elif value in age_checklist_2:
        #         matchName_sex_dict[key] = value_2 + " " + value
        #     elif value in age_checklist_3:
        #         matchName_sex_dict[key] = value_3 + " " + value
        #     elif value in age_checklist_4:
        #         matchName_sex_dict[key] = value_4 + " " + value

        for key, value in matchName_sex_dict.items():
            ages = re.findall(r'\d+', value)
            age = [int(i) for i in ages][0]
            if age < 14:
                matchName_sex_dict[key] = value_1 + " " + value
            elif age <= 18:
                matchName_sex_dict[key] = value_2 + " " + value
            elif age <= 20:
                matchName_sex_dict[key] = value_3 + " " + value
            elif age > 20:
                matchName_sex_dict[key] = value_4 + " " + value
            # if value in age_checklist_1:
            #     matchName_sex_dict[key] = value_1 + " " + value
            # elif value in age_checklist_2:
            #     matchName_sex_dict[key] = value_2 + " " + value
            # elif value in age_checklist_3:
            #     matchName_sex_dict[key] = value_3 + " " + value
            # elif value in age_checklist_4:
            #     matchName_sex_dict[key] = value_4 + " " + value

    def calc_dict(self, rowNum, colName):
        colNum = self.sheet.loc[[rowNum]].where(self.sheet == colName).dropna(how='all').dropna(axis=1)
        sss = []
        for i in range(1, len(colNum.columns.tolist()) + 1):
            sss.append(colName)
        self.colNum_dict = dict(zip(colNum.columns.tolist(), sss))
        return self.colNum_dict

    def pers_com_qbxKataQual(self):
        try:
            pers_com_qbx = self.ui_kataQual.pers_com_qbx
            # print(pers_com_qbx.isChecked(), self.ui_kataQual.male.isChecked())
            if not pers_com_qbx.isChecked():
                self.ui_kataQual.pers_lbl.setFont(self.font_b_13)
                self.ui_kataQual.pers_lbl.setStyleSheet("color: black;")
                self.ui_kataQual.com_lbl.setFont(self.font_l_13)
                self.ui_kataQual.com_lbl.setStyleSheet("color: grey;")

                self.ui_kataQual.male.clicked.connect(
                    lambda: self.useExportDataKataQual(load_date=self.individ_kata_male_dict))
                self.ui_kataQual.female.clicked.connect(
                    lambda: self.useExportDataKataQual(load_date=self.individ_kata_female_dict))
                if self.ui_kataQual.male.isChecked():
                    self.useExportDataKataQual(load_date=self.individ_kata_male_dict)
                elif self.ui_kataQual.female.isChecked():
                    self.useExportDataKataQual(load_date=self.individ_kata_female_dict)
                else:
                    self.ui_kataQual.male.setChecked(True)
                    self.useExportDataKataQual(load_date=self.individ_kata_male_dict)
            else:
                self.ui_kataQual.com_lbl.setFont(self.font_b_13)
                self.ui_kataQual.com_lbl.setStyleSheet("color: black;")
                self.ui_kataQual.pers_lbl.setFont(self.font_l_13)
                self.ui_kataQual.pers_lbl.setStyleSheet("color: grey;")

                self.ui_kataQual.male.clicked.connect(
                    lambda: self.useExportDataKataQual(load_date=self.team_kata_male_dict))
                self.ui_kataQual.female.clicked.connect(
                    lambda: self.useExportDataKataQual(load_date=self.team_kata_female_dict))
                if self.ui_kataQual.male.isChecked():
                    self.useExportDataKataQual(load_date=self.team_kata_male_dict)
                elif self.ui_kataQual.female.isChecked():
                    self.useExportDataKataQual(load_date=self.team_kata_female_dict)
                else:
                    self.ui_kataQual.male.setChecked(True)
                    self.useExportDataKataQual(load_date=self.team_kata_male_dict)
        except Exception as e:
            print(e)

    def useExportDataKataQual(self, load_date):
        # print('useExportDataKataQual')
        dict_KataOrKumite = load_date
        comboBox_age = self.ui_kataQual.comboBox_age
        age_1 = self.ui_kataQual.age_1
        name_red_1 = self.ui_kataQual.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                                   name_white_1, comboBox_name_red_1, comboBox_name_white_1)

    # def useExportDataKataQualMale(self):
    #     dict_KataOrKumite = self.individ_kata_male_dict
    #     comboBox_age = self.ui_kataQual.comboBox_age
    #     age_1 = self.ui_kataQual.age_1
    #     name_red_1 = self.ui_kataQual.name_red_1
    #     name_white_1 = self.ui_kataQual.name_white_1
    #     comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
    #     comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
    #     self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
    #                                name_white_1, comboBox_name_red_1, comboBox_name_white_1)
    #
    # def useExportDataKataQualFemale(self):
    #     dict_KataOrKumite = self.individ_kata_female_dict
    #     comboBox_age = self.ui_kataQual.comboBox_age
    #     age_1 = self.ui_kataQual.age_1
    #     name_red_1 = self.ui_kataQual.name_red_1
    #     name_white_1 = self.ui_kataQual.name_white_1
    #     comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
    #     comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
    #     self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
    #                                name_white_1, comboBox_name_red_1, comboBox_name_white_1)

    # def useExportDataKataFinalMale(self):
    #     dict_KataOrKumite = self.individ_kata_male_dict
    #     comboBox_age = self.ui_kataFinal.comboBox_age
    #     age_1 = self.ui_kataFinal.age_1
    #     name_red_1 = self.ui_kataFinal.name_red_1
    #     name_white_1 = self.ui_kataQual.name_white_1
    #     comboBox_name_red_1 = self.ui_kataFinal.comboBox_name_red_1
    #     comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
    #     self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
    #                                name_white_1, comboBox_name_red_1, comboBox_name_white_1)
    #
    # def useExportDataKataFinalFemale(self):
    #     dict_KataOrKumite = self.individ_kata_female_dict
    #     comboBox_age = self.ui_kataFinal.comboBox_age
    #     age_1 = self.ui_kataFinal.age_1
    #     name_red_1 = self.ui_kataFinal.name_red_1
    #     name_white_1 = self.ui_kataQual.name_white_1
    #     comboBox_name_red_1 = self.ui_kataFinal.comboBox_name_red_1
    #     comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
    #     self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
    #                                name_white_1, comboBox_name_red_1, comboBox_name_white_1)
    def pers_com_qbxKataFinal(self):
        pers_com_qbx = self.ui_kataFinal.pers_com_qbx
        if not pers_com_qbx.isChecked():
            self.ui_kataFinal.pers_lbl.setFont(self.font_b_13)
            self.ui_kataFinal.pers_lbl.setStyleSheet("color: black;")
            self.ui_kataFinal.com_lbl.setFont(self.font_l_13)
            self.ui_kataFinal.com_lbl.setStyleSheet("color: grey;")

            self.ui_kataFinal.male.clicked.connect(
                lambda: self.useExportDataKataFinal(load_date=self.individ_kata_male_dict))
            self.ui_kataFinal.female.clicked.connect(
                lambda: self.useExportDataKataFinal(load_date=self.individ_kata_female_dict))
            if self.ui_kataFinal.male.isChecked():
                self.useExportDataKataFinal(load_date=self.individ_kata_male_dict)
            elif self.ui_kataFinal.female.isChecked():
                self.useExportDataKataFinal(load_date=self.individ_kata_female_dict)
            else:
                self.ui_kataFinal.male.setChecked(True)
                self.useExportDataKataFinal(load_date=self.individ_kata_male_dict)
        else:
            self.ui_kataFinal.com_lbl.setFont(self.font_b_13)
            self.ui_kataFinal.com_lbl.setStyleSheet("color: black;")
            self.ui_kataFinal.pers_lbl.setFont(self.font_l_13)
            self.ui_kataFinal.pers_lbl.setStyleSheet("color: grey;")

            self.ui_kataFinal.male.clicked.connect(
                lambda: self.useExportDataKataFinal(load_date=self.team_kata_male_dict))
            self.ui_kataFinal.female.clicked.connect(
                lambda: self.useExportDataKataFinal(load_date=self.team_kata_female_dict))
            if self.ui_kataFinal.male.isChecked():
                self.useExportDataKataFinal(load_date=self.team_kata_male_dict)
            elif self.ui_kataFinal.female.isChecked():
                self.useExportDataKataFinal(load_date=self.team_kata_female_dict)
            else:
                self.ui_kataFinal.male.setChecked(True)
                self.useExportDataKataFinal(load_date=self.team_kata_male_dict)

    def useExportDataKataFinal(self, load_date):
        dict_KataOrKumite = load_date
        comboBox_age = self.ui_kataFinal.comboBox_age
        age_1 = self.ui_kataFinal.age_1
        name_red_1 = self.ui_kataFinal.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataFinal.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                                   name_white_1, comboBox_name_red_1, comboBox_name_white_1)

    def pers_com_qbxKumite(self):
        pers_com_qbx = self.ui_kumite.pers_com_qbx
        if not pers_com_qbx.isChecked():
            self.ui_kumite.pers_lbl.setFont(self.font_b_13)
            self.ui_kumite.pers_lbl.setStyleSheet("color: black;")
            self.ui_kumite.com_lbl.setFont(self.font_l_13)
            self.ui_kumite.com_lbl.setStyleSheet("color: grey;")

            self.ui_kumite.male.clicked.connect(
                lambda: self.useExportDataKumite(load_date=self.individ_kumite_male_dict))
            self.ui_kumite.female.clicked.connect(
                lambda: self.useExportDataKumite(load_date=self.individ_kumite_female_dict))
            if self.ui_kumite.male.isChecked():
                self.useExportDataKumite(load_date=self.individ_kumite_male_dict)
            elif self.ui_kumite.female.isChecked():
                self.useExportDataKumite(load_date=self.individ_kumite_female_dict)
            else:
                self.ui_kumite.male.setChecked(True)
                self.useExportDataKumite(load_date=self.individ_kumite_male_dict)
        else:
            self.ui_kumite.com_lbl.setFont(self.font_b_13)
            self.ui_kumite.com_lbl.setStyleSheet("color: black;")
            self.ui_kumite.pers_lbl.setFont(self.font_l_13)
            self.ui_kumite.pers_lbl.setStyleSheet("color: grey;")

            self.ui_kumite.male.clicked.connect(
                lambda: self.useExportDataKumite(load_date=self.team_kumite_male_dict))
            self.ui_kumite.female.clicked.connect(
                lambda: self.useExportDataKumite(load_date=self.team_kumite_female_dict))
            if self.ui_kumite.male.isChecked():
                self.useExportDataKumite(load_date=self.team_kumite_male_dict)
            elif self.ui_kumite.female.isChecked():
                self.useExportDataKumite(load_date=self.team_kumite_female_dict)
            else:
                self.ui_kumite.male.setChecked(True)
                self.useExportDataKumite(load_date=self.team_kumite_male_dict)

    def useExportDataKumite(self, load_date):
        dict_KataOrKumite = load_date
        comboBox_age = self.ui_kumite.comboBox_age
        age_1 = self.ui_kumite.age_1
        name_red_1 = self.ui_kumite.name_red_1
        name_white_1 = self.ui_kumite.name_white_1
        comboBox_name_red_1 = self.ui_kumite.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kumite.comboBox_name_white_1
        self.calcTabKumiteSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1, name_white_1,
                                     comboBox_name_red_1, comboBox_name_white_1)
        # print(load_date)

    def calcTabKumiteSpotrsmans(self, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                                name_white_1, comboBox_name_red_1, comboBox_name_white_1):
        self.TempSet.clear()
        self.TempSet = sorted(list(set(dict_KataOrKumite)))
        comboBox_age.setEnabled(True)
        comboBox_age.clear()
        age_1.setFont(self.font_b_13)
        age_1.setStyleSheet("color: black;")
        name_red_1.setFont(self.font_l_13)
        name_red_1.setStyleSheet("color: grey;")
        name_white_1.setFont(self.font_l_13)
        name_white_1.setStyleSheet("color: grey;")
        comboBox_name_red_1.setEnabled(False)
        comboBox_name_red_1.clear()
        comboBox_name_white_1.setEnabled(False)
        comboBox_name_white_1.clear()
        comboBox_age.addItems([self.sportsmans_ages_dict[x] for x in self.TempSet])

    def calcTabKataSpotrsmans(self, dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                              name_white_1, comboBox_name_red_1, comboBox_name_white_1):
        self.ui_kataQual.clearKataData()
        self.ui_kataFinal.clearKataData()
        self.TempSet.clear()
        self.TempSet = sorted(list(set(dict_KataOrKumite)))
        comboBox_age.setEnabled(True)
        comboBox_age.clear()
        age_1.setFont(self.font_b_13)
        age_1.setStyleSheet("color: black;")
        name_red_1.setFont(self.font_l_13)
        name_red_1.setStyleSheet("color: grey;")
        name_white_1.setFont(self.font_l_13)
        name_white_1.setStyleSheet("color: grey;")
        comboBox_name_red_1.setEnabled(False)
        comboBox_name_red_1.clear()
        comboBox_name_white_1.setEnabled(False)
        comboBox_name_white_1.clear()
        comboBox_age.addItems([self.sportsmans_ages_dict[x] for x in self.TempSet])

    def calcTabKataFinalSpotrsmansRed(self):
        self.calcTab(self.ui_kataFinal.name_red_1,
                     self.ui_kataFinal.comboBox_name_red_1,
                     self.ui_kataFinal.pers_com_qbx)

    def calcTabKataSpotrsmansRed(self):
        self.calcTab(self.ui_kataQual.name_red_1,
                     self.ui_kataQual.comboBox_name_red_1,
                     self.ui_kataQual.pers_com_qbx)

    def calcTabKataSpotrsmansWhite(self):
        self.calcTab(self.ui_kataQual.name_white_1,
                     self.ui_kataQual.comboBox_name_white_1,
                     self.ui_kataQual.pers_com_qbx)

    def calcTab_kumite(self):
        name_r = self.ui_kumite.name_red_1
        name_w = self.ui_kumite.name_white_1
        comboBox_name_r = self.ui_kumite.comboBox_name_red_1
        comboBox_name_w = self.ui_kumite.comboBox_name_white_1
        comboBox_name_r.clear()
        comboBox_name_w.clear()

        n = self.ui_kumite.comboBox_age.currentText()
        jj = self.ui_kumite.matchName12

        a2 = {k: v for k, v in
              zip((self.TempSet), [self.sportsmans_ages_dict[x] for x in self.TempSet])}
        self.x = list(self.sportsmans_ages_dict.keys()).index(list(a2.keys())[list(a2.values()).index(n)])
        pers_com_qbx = self.ui_kumite.pers_com_qbx
        group_pref = ''

        if not pers_com_qbx.isChecked():
            df_list = sorted(self.df_Single_list[self.x])
        else:
            df_list = sorted(self.df_Group_list[self.x])
            group_pref = "КОМАНДНЫЕ "
        jj.setText(f"{group_pref}{self.matchName[list(self.matchName.keys())[self.x]]}")

        name_r.setFont(self.font_b_13)
        name_r.setStyleSheet("color: black;")
        name_w.setFont(self.font_b_13)
        name_w.setStyleSheet("color: black;")

        comboBox_name_r.addItems(df_list)
        comboBox_name_w.addItems(df_list)
        comboBox_name_r.setEnabled(True)
        comboBox_name_w.setEnabled(True)

    def calcTab(self, name, comboBox_name, pers_com_qbx):
        try:
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
            group_pref = ''

            if not pers_com_qbx.isChecked():
                df_list = sorted(self.df_Single_list[self.x])
            else:
                df_list = sorted(self.df_Group_list[self.x])
                df_list = sorted(self.df_Group_list_only_group[self.x])
                group_pref = "ГРУППА  "
            try:
                if self.tatamiName == "":
                    jj.setText(f"Татами №#, {group_pref}{self.matchName[list(self.matchName.keys())[self.x]]}")
                else:
                    jj.setText(f"{self.tatamiName}, {group_pref}{self.matchName[list(self.matchName.keys())[self.x]]}")
            except Exception as e:
                print('_______Exception calcTab1:', e)
                if self.tatamiName == "":
                    jj.setText('Татами №#, ')
                else:
                    jj.setText(self.tatamiName)
            name.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 12px;")
            # comboBox_name.addItems(sorted(self.df_Single_list[self.x]))
            comboBox_name.addItems(df_list)
            comboBox_name.setEnabled(True)
        except Exception as e:
            print('_______Exception calcTab2:', e)

    def setLabel(self):
        try:
            sender = self.sender()

            is_sender_paytnov = sender == self.ui_kumite.pyatnov_name
            is_name_none = self.ui_kumite.pyatnov_name.currentText() in ['Выберите пару...', 'Выберите команды...']
            is_sender_paytnov_pair_name = sender == self.ui_kumite.pyatnov_pair_name
            is_pair_none = self.ui_kumite.pyatnov_pair_name.currentText() in ['Выберите пару...', 'Выберите команды...']

            if (is_sender_paytnov and is_name_none) or (is_sender_paytnov_pair_name and is_pair_none):
                return self.ui_kumite.blocked_Form2.show()

            # Нажали для кумите Выбор региона
            if sender == self.ui_kumite.pyatnov_name:
                self.ui_kumite.le_comboBox_name_white_1.clear()
                self.ui_kumite.le_comboBox_name_red_1.clear()

                # Для личных
                if self.flag_pyatnov_kumite_single:
                    # Выбранное значение команды или спортсмена
                    c_box_choice = self.sportsmen_list[
                        self.sportsmen_list['combo_box'] == self.ui_kumite.pyatnov_name.currentText()]
                    self.ui_kumite.lineEdit_name_white_1.setText(c_box_choice['siro_short'].values[0])
                    self.ui_kumite.lineEdit_name_white_1.setEnabled(False)
                    self.ui_kumite.lineEdit_name_red_1.setText(c_box_choice['aka_short'].values[0])
                    self.ui_kumite.lineEdit_name_red_1.setEnabled(False)

                    self.ui_kumite.lineEdit_region_white_1.lineEdit().setText(c_box_choice['region_siro'].values[0])
                    self.ui_kumite.lineEdit_region_white_1.setEnabled(False)
                    self.ui_kumite.lineEdit_region_red_1.lineEdit().setText(c_box_choice['region_aka'].values[0])
                    self.ui_kumite.lineEdit_region_red_1.setEnabled(False)

                    # Разблокировка интерфейса Кумите
                    self.blockedKumiteFrame(False)

                # Для командных. Если всё ок, то весь код выше нужно перетащить сюда
                elif self.flag_pyatnov_kumite_team:
                    # self.ui_kumite.le_comboBox_name_white_1.setEnabled(False)
                    # self.ui_kumite.le_comboBox_name_red_1.setEnabled(False)
                    # self.ui_kumite.le_comboBox_name_white_1.clear()
                    # self.ui_kumite.le_comboBox_name_red_1.clear()

                    print('2 c_box_choice', self.ui_kumite.pyatnov_name.currentText())
                    print('3 c_box_choice', self.teams_pairs.keys())

                    # Выбранное значение команды или спортсмена
                    c_box_choice = self.teams_pairs[self.ui_kumite.pyatnov_name.currentText()]

                    # Находим все пары спортсменов
                    pair_name_list = list()
                    complete_pair_list = list()  # Блокируем завершенные выступления
                    for i in range(3):
                        if c_box_choice[f'men_pair_{i+1}'] != '':
                            pair_name_list.append(c_box_choice[f'men_pair_{i+1}'])
                            complete_pair_list.append(c_box_choice[f'complete_pair_{i+1}'])
                    # Очищаем список спортсменов на экране
                    self.ui_kumite.pyatnov_pair_name.clear()

                    # Выпадающий список выбора пар
                    self.ui_kumite.pyatnov_pair_name.addItem('Выберите пару...')
                    self.ui_kumite.pyatnov_pair_name.addItems(pair_name_list)
                    self.ui_kumite.pyatnov_pair_name.setEnabled(True)

                    # Блокируем завершенные выступления и добавляем префикс - "завершено" к ФИО
                    for i in range(len(complete_pair_list)):
                        self.ui_kumite.pyatnov_pair_name.model().item(i+1).setEnabled(complete_pair_list[i])
                        if not complete_pair_list[i]:
                            self.ui_kumite.pyatnov_pair_name.itemText(i+1)
                            new_pair_name_value = f'заверш. {self.ui_kumite.pyatnov_pair_name.itemText(i+1)}'
                            self.ui_kumite.pyatnov_pair_name.setItemText(i+1, new_pair_name_value)

                    # Поле отображения регионов
                    self.ui_kumite.lineEdit_region_white_1.lineEdit().setText(c_box_choice['team_siro'])
                    self.ui_kumite.lineEdit_region_white_1.setEnabled(False)
                    self.ui_kumite.lineEdit_region_red_1.lineEdit().setText(c_box_choice['team_aka'])
                    self.ui_kumite.lineEdit_region_red_1.setEnabled(False)

                    # Поле отображения ФИО
                    self.ui_kumite.lineEdit_name_white_1.clear()
                    self.ui_kumite.lineEdit_name_red_1.clear()

            elif sender == self.ui_kumite.pyatnov_pair_name:
                self.ui_kumite.le_comboBox_name_white_1.setEnabled(False)
                self.ui_kumite.le_comboBox_name_red_1.setEnabled(False)
                self.ui_kumite.le_comboBox_name_white_1.clear()
                self.ui_kumite.le_comboBox_name_red_1.clear()
                print('1 pyatnov_name', self.ui_kumite.pyatnov_name.currentText())
                print('1 pyatnov_pair_name', self.ui_kumite.pyatnov_pair_name.currentText())

                # Определяем номер строки, для заполнения протокола:
                # Находим пару команд в словаре c_box_choice, у этой пары находим пару спортсменов
                cur_team_pair = self.teams_pairs[self.ui_kumite.pyatnov_name.currentText()]
                cur_men_pair = self.ui_kumite.pyatnov_pair_name.currentText()
                self.cur_men_pair_num = None  # Номер строки пары спортсменов
                siro_man = ''  # ФИО сиро
                aka_man = ''  # ФИО ака

                print('cur_men_pair', cur_men_pair)

                if cur_team_pair['men_pair_1'] == cur_men_pair:
                    self.cur_men_pair_num = cur_team_pair['row_num_1']
                    siro_man = cur_team_pair['siro_short_man_1']
                    aka_man = cur_team_pair['aka_short_man_1']
                elif cur_team_pair['men_pair_2'] == cur_men_pair:
                    self.cur_men_pair_num = cur_team_pair['row_num_2']
                    siro_man = cur_team_pair['siro_short_man_2']
                    aka_man = cur_team_pair['aka_short_man_2']
                elif cur_team_pair['men_pair_3'] == cur_men_pair:
                    self.cur_men_pair_num = cur_team_pair['row_num_3']
                    siro_man = cur_team_pair['siro_short_man_3']
                    aka_man = cur_team_pair['aka_short_man_3']

                # Поле отображения ФИО
                self.ui_kumite.lineEdit_name_white_1.setText(siro_man)
                self.ui_kumite.lineEdit_name_red_1.setText(aka_man)


                # Разблокировка интерфейса Кумите
                self.blockedKumiteFrame(False)




            elif sender == self.ui_kataQual.pyatnov_name:
                value = [i for i in self.sportsmen_dict['combo_box'] if
                         self.sportsmen_dict['combo_box'][i] == self.ui_kataQual.pyatnov_name.currentText()][0]

                self.ui_kataQual.lineEdit_name_red_1.setText(self.sportsmen_dict['aka_short'][value])
                self.ui_kataQual.lineEdit_region_red_1.lineEdit().setText(self.sportsmen_dict['region_aka'][value])
                self.ui_kataQual.lineEdit_name_white_1.setText(self.sportsmen_dict['siro_short'][value])
                self.ui_kataQual.lineEdit_region_white_1.lineEdit().setText(self.sportsmen_dict['region_siro'][value])

            # Нажали для ката финал
            elif sender == self.ui_kataFinal.pyatnov_name:
                value = [i for i in self.sportsmen_dict['combo_box'] if
                         self.sportsmen_dict['combo_box'][i] == self.ui_kataFinal.pyatnov_name.currentText()][0]

                self.ui_kataFinal.lineEdit_name_red_1.setText(self.sportsmen_dict['name'][value])
                self.ui_kataFinal.lineEdit_region_red_1.lineEdit().setText(self.sportsmen_dict['region_aka'][value])

        except Exception as e:
            print('_______Exception setLabel:', e)

    def setLabelRed(self):
        try:
            pers_com_qbx = self.ui_kataQual.pers_com_qbx
            if not pers_com_qbx.isChecked():
                df_list = self.df_Single_list[self.x]
                name = str(df_list.get(self.ui_kataQual.comboBox_name_red_1.currentText()))
                region = name.split('a11')[1]
                name = ''.join([name.replace('a12', '').split('a13')[0],
                                ' ' + name.split('a13')[1].split('a11')[0][0] + '.'])
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataQual.lineEdit_name_red_1.setText(name)
                self.ui_kataQual.lineEdit_region_red_1.lineEdit().setText(region)
            else:
                df_list = self.df_Group_list_only_group[self.x]
                name = self.ui_kataQual.comboBox_name_red_1.currentText().split(' - ком')[0]
                region = str(df_list.get(self.ui_kataQual.comboBox_name_red_1.currentText()))
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataQual.lineEdit_name_red_1.setText(name)
                self.ui_kataQual.lineEdit_region_red_1.lineEdit().setText(region)

        except Exception as e:
            self.show_withOut_load_file_interface()
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
            self.status_file.setText(f'setLabelRed. <b>Ошибка:</b> {e}')
            print(f'setLabelRed. <b>Ошибка:</b> {e}')

    def setLabelRedKataFinal(self):
        try:
            pers_com_qbx = self.ui_kataFinal.pers_com_qbx
            if not pers_com_qbx.isChecked():
                df_list = self.df_Single_list[self.x]
                name = str(df_list.get(self.ui_kataFinal.comboBox_name_red_1.currentText()))
                region = name.split('a11')[1]
                name = ''.join([name.replace('a12', '').split('a13')[0],
                                ' ' + name.split('a13')[1].split('a11')[0][0] + '.'])
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataFinal.lineEdit_name_red_1.setText(name)
                self.ui_kataFinal.lineEdit_region_red_1.lineEdit().setText(region)
            else:
                df_list = self.df_Group_list_only_group[self.x]
                name = self.ui_kataFinal.comboBox_name_red_1.currentText().split(' - ком')[0]
                region = str(df_list.get(self.ui_kataFinal.comboBox_name_red_1.currentText()))
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataFinal.lineEdit_name_red_1.setText(name)
                self.ui_kataFinal.lineEdit_region_red_1.lineEdit().setText(region)

        except Exception as e:
            self.show_withOut_load_file_interface()
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
            self.status_file.setText(f'setLabelRedKataFinal. <b>Ошибка:</b> {e}')
            print(f'setLabelRedKataFinal. <b>Ошибка:</b> {e}')

    def setLabelWhite(self):
        try:
            pers_com_qbx = self.ui_kataQual.pers_com_qbx
            if not pers_com_qbx.isChecked():
                df_list = self.df_Single_list[self.x]
                name = str(df_list.get(self.ui_kataQual.comboBox_name_white_1.currentText()))
                region = name.split('a11')[1]
                name = ''.join([name.replace('a12', '').split('a13')[0],
                                ' ' + name.split('a13')[1].split('a11')[0][0] + '.'])
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataQual.lineEdit_name_white_1.setText(name)
                self.ui_kataQual.lineEdit_region_white_1.lineEdit().setText(region)
            else:
                df_list = self.df_Group_list_only_group[self.x]
                name = self.ui_kataQual.comboBox_name_white_1.currentText().split(' - ком')[0]
                region = str(df_list.get(self.ui_kataQual.comboBox_name_white_1.currentText()))
                # это конструктор имя, состоящий из Фамилии и первого символа Имя
                self.ui_kataQual.lineEdit_name_white_1.setText(name)
                self.ui_kataQual.lineEdit_region_white_1.lineEdit().setText(region)

        except Exception as e:
            self.show_withOut_load_file_interface()
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
            self.status_file.setText(f'setLabelWhite. <b>Ошибка:</b> {e}')
            print(f'setLabelWhite. <b>Ошибка:</b> {e}')

    def setLabelRedKumite(self):
        try:
            pers_com_qbx = self.ui_kumite.pers_com_qbx
            if not pers_com_qbx.isChecked():
                df_list = self.df_Single_list[self.x]
            else:
                df_list = self.df_Group_list[self.x]
            name = df_list.get(self.ui_kumite.comboBox_name_red_1.currentText())
            # это конструктор имя, состоящий из Фамилии и первого символа Имя
            self.ui_kumite.lineEdit_name_red_1.setText(
                ''.join([name.replace('a12', '').split('a13')[0], ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
            # self.ui_kumite.lineEdit_region_red_1.setText(name.split('a11')[1])
            self.ui_kumite.lineEdit_region_red_1.lineEdit().setText(name.split('a11')[1])
        except Exception as e:
            self.show_withOut_load_file_interface()
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
            self.status_file.setText(f'setLabelRedKumite. <b>Ошибка:</b> {e}')
            print(f'setLabelRedKumite. <b>Ошибка:</b> {e}')

    def setLabelWhiteKumite(self):
        try:
            pers_com_qbx = self.ui_kumite.pers_com_qbx
            if not pers_com_qbx.isChecked():
                df_list = self.df_Single_list[self.x]
            else:
                df_list = self.df_Group_list[self.x]
            name = df_list.get(self.ui_kumite.comboBox_name_white_1.currentText())
            # это конструктор имя, состоящий из Фамилии и первого символа Имя
            self.ui_kumite.lineEdit_name_white_1.setText(
                ''.join([name.replace('a12', '').split('a13')[0], ' ' + name.split('a13')[1].split('a11')[0][0] + '.']))
            # self.ui_kumite.lineEdit_region_white_1.setText(name.split('a11')[1])
            self.ui_kumite.lineEdit_region_white_1.lineEdit().setText(name.split('a11')[1])
        except Exception as e:
            self.show_withOut_load_file_interface()
            self.status_file.setStyleSheet("font-family: Gotham-Light; color: #red; font-size: 12px;")
            self.status_file.setText(f'setLabelWhiteKumite. <b>Ошибка:</b> {e}')
            print(f'setLabelWhiteKumite. <b>Ошибка:</b> {e}')

    def calcTabKata_Reset(self):
        if self.loaded_file_data_type == 'file_pyatnov':
            self.check_to_wopf()
        if self.tatamiName != "":
            self.ui_kataQual.matchName1.setText(self.tatamiName + ', Возраст')
        else:
            self.ui_kataQual.matchName1.setText('Татами №#, Возраст')

    def kata_matchName(self):
        sender = self.sender()
        if sender in (self.ui_kataQual.matchName1, self.ui_kataQual.btn_showData):
            ui_kata = self.ui_kataQual
        elif sender in (self.ui_kataFinal.matchName1, self.ui_kataFinal.btn_showData):
            ui_kata = self.ui_kataFinal
        # print('kata_matchName 1', sender, ui_kata)
        try:
            # print('kata_matchName 2')
            if len(ui_kata.matchName1.text().split(', ')) > 1:
                self.tatamiName = ui_kata.matchName1.text().split(', ')[0]
                # print('kata_matchName 2 1')
                # print(f"_{len(self.matchName)}_{ui_kata.matchName1.text()}_")
                # print(f"_{self.tatamiName}_")
                # print(f"_{self.tatamiName + ', ' + self.matchName[list(self.matchName.keys())[self.x]]}_")
                if len(self.matchName) and ui_kata.matchName1.text() == \
                        self.tatamiName + ', ' + self.matchName[list(self.matchName.keys())[self.x]]:
                    # print('kata_matchName 2 1 1')
                    ui_kata.matchName1.setText(self.tatamiName +
                                               ', ' + self.matchName[list(self.matchName.keys())[self.x]])
            else:
                # print('kata_matchName 2 2')
                if len(self.matchName):
                    # print('kata_matchName 2 2 1')
                    ui_kata.matchName1.setText(self.matchName[list(self.matchName.keys())[self.x]])
        except Exception as e:
            print('_______Exception kata_matchName:', e)

    def kumite_matchName(self):
        sender = self.sender()
        if sender in (self.ui_kumite.btn_showData, self.ui_kumite.matchName12):
            ui_kumite = self.ui_kumite
        try:
            # print(111111111111111111)
            # print("ui_kumite.matchName11.text():  ui_kumite.matchName11.text():  self.tatamiName:")
            # print(f"__{ui_kumite.matchName11.text()}__{ui_kumite.matchName11.text()}__{self.tatamiName}__")
            # print(ui_kumite.matchName11.text() != "Татами №#", ui_kumite.matchName11.text() != self.tatamiName)
            if sender == self.ui_kumite.matchName12:
                self.tatamiName = ui_kumite.matchName11.text()
            elif ui_kumite.matchName11.text() != "Татами №#" and ui_kumite.matchName11.text() != self.tatamiName:
                self.tatamiName = ui_kumite.matchName11.text()
        except Exception as e:
            print('_______Exception kumite_matchName:', e)

    def showKataQualWin(self):
        try:
            self.closeAllWin()
            self.ui_kataQual.calc_display_moveCoord(self.display_coord_x1, self.display_coord_y1, self.display_width,
                                                    self.display_height, self.display_coord_x1_secW,
                                                    self.display_coord_y1_secW)
            self.close()

            if self.tatamiName != "":
                if self.category_label:
                    self.ui_kataQual.matchName1.setText(self.tatamiName + ", " + self.category_label)
                else:
                    self.ui_kataQual.matchName1.setText(self.tatamiName + ", Возраст")
            self.ui_kataQual.setMatchName()

            # Заполняем списки регионов в выпадающем списке
            if self.loaded_file_data_type == 'file_pyatnov':
                self.ui_kataQual.lineEdit_name_white_1.setPlaceholderText("СИРО. Имя спортсмена")
                self.ui_kataQual.lineEdit_name_red_1.setPlaceholderText("АКА. Имя спортсмена")
                edit_white = QtWidgets.QLineEdit(self, placeholderText="СИРО. Регион")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="АКА. Регион")
            else:
                self.ui_kataQual.lineEdit_name_white_1.setPlaceholderText("СИРО. Введите имя спортсмена")
                self.ui_kataQual.lineEdit_name_red_1.setPlaceholderText("АКА. Введите имя спортсмена")
                edit_white = QtWidgets.QLineEdit(self, placeholderText="СИРО. Введите регион")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="АКА. Введите регион")

            lineEdit_region_white_1 = self.ui_kataQual.lineEdit_region_white_1
            lineEdit_region_white_1.addItems([''])
            lineEdit_region_white_1.addItems(self.flags_set)

            edit_white.setFont(self.font_l_15)
            edit_white.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit_region_white_1.setLineEdit(edit_white)

            lineEdit_region_red_1 = self.ui_kataQual.lineEdit_region_red_1
            lineEdit_region_red_1.addItems([''])
            lineEdit_region_red_1.addItems(self.flags_set)

            edit_red.setFont(self.font_l_15)
            edit_red.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit_region_red_1.setLineEdit(edit_red)

        except Exception as e:
            print('_______Exception showKataQualWin:\n', e)

    def showKataFinalWin(self):
        try:
            self.closeAllWin()
            self.ui_kataFinal.calc_display_moveCoord(self.display_coord_x1, self.display_coord_y1, self.display_width,
                                                     self.display_height, self.display_coord_x1_secW,
                                                     self.display_coord_y1_secW)
            self.close()
            if self.tatamiName != "":
                if self.category_label:
                    self.ui_kataFinal.matchName1.setText(self.tatamiName + ", " + self.category_label)
                else:
                    self.ui_kataFinal.matchName1.setText(self.tatamiName + ", Возраст")
            self.ui_kataFinal.setMatchName()

            # Заполняем списки регионов в выпадающем списке
            lineEdit_region_red_1 = self.ui_kataFinal.lineEdit_region_red_1
            lineEdit_region_red_1.addItems([''])
            lineEdit_region_red_1.addItems(self.flags_set)
            if self.loaded_file_data_type == 'file_pyatnov':
                self.ui_kataFinal.lineEdit_name_red_1.setPlaceholderText("Имя спортсмена")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="Регион")
            else:
                self.ui_kataFinal.lineEdit_name_red_1.setPlaceholderText("Введите имя спортсмена")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="Введите регион")

            edit_red.setFont(self.font_l_15)
            edit_red.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit_region_red_1.setLineEdit(edit_red)

            # Очищаем данные из полей выбора спортсменов
            self.ui_kataFinal.male.setAutoExclusive(False)
            self.ui_kataFinal.female.setAutoExclusive(False)
            self.ui_kataFinal.male.setChecked(False)
            self.ui_kataFinal.female.setChecked(False)
            self.ui_kataFinal.male.setAutoExclusive(True)
            self.ui_kataFinal.female.setAutoExclusive(True)
            self.ui_kataFinal.age_1.setFont(self.font_l_13)
            self.ui_kataFinal.age_1.setStyleSheet("color: grey;")
            self.ui_kataFinal.comboBox_age.clear()
            self.ui_kataFinal.comboBox_age.setEnabled(False)
            self.ui_kataFinal.name_red_1.setFont(self.font_l_13)
            self.ui_kataFinal.name_red_1.setStyleSheet("color: grey;")
            self.ui_kataFinal.comboBox_name_red_1.clear()
            self.ui_kataFinal.comboBox_name_red_1.setEnabled(False)

        except Exception as e:
            print('_______Exception showKataFinalWin:', e)

    def showKumiteWin(self):
        try:
            self.ui_kataFinal.clearKataData()
            self.ui_kataQual.NewCategory()
            self.ui_kumite.reset_all(self.flags_dict)
            self.closeAllWin()
            self.ui_kumite.calc_display_moveCoord(self.display_coord_x1, self.display_coord_y1, self.display_width,
                                                  self.display_height, self.display_coord_x1_secW,
                                                  self.display_coord_y1_secW)
            self.close()
            if self.tatamiName != "":
                self.ui_kumite.matchName11.setText(self.tatamiName)
            self.ui_kumite.setMatchName()

            # Если командное для Пятнова, то отображаем выпадающий список с ФИО спортсменов команд и скрываем lineEdit
            if self.sportsmans_in_teams_dict:
                if not self.flag_pyatnov_kumite_team:
                    self.ui_kumite.le_comboBox_name_white_1.show()
                    self.ui_kumite.le_comboBox_name_red_1.show()

                    self.ui_kumite.lineEdit_name_white_1.hide()
                    self.ui_kumite.lineEdit_name_red_1.hide()

                    self.ui_kumite.frame_pyatnov_perebivka.hide()

                self.ui_kumite.le_comboBox_name_white_1.setEnabled(False)
                self.ui_kumite.le_comboBox_name_red_1.setEnabled(False)

                placeholder_text_white = 'СИРО. Выберите спортсмена'
                placeholder_text_red = 'АКА. Выберите спортсмена'
                if self.flag_pyatnov_kumite_team:
                    placeholder_text_white = 'СИРО. Выберите пару'
                    placeholder_text_red = 'АКА. Выберите пару'

                le_comboBox_name_white_1 = self.ui_kumite.le_comboBox_name_white_1
                le_comboBox_name_white_1.clear()
                edit_white = QtWidgets.QLineEdit(self, placeholderText=placeholder_text_white)
                edit_white.setFont(self.font_l_15)
                edit_white.setAlignment(QtCore.Qt.AlignCenter)
                le_comboBox_name_white_1.setLineEdit(edit_white)

                le_comboBox_name_red_1 = self.ui_kumite.le_comboBox_name_red_1
                le_comboBox_name_red_1.clear()
                edit_red = QtWidgets.QLineEdit(self, placeholderText=placeholder_text_red)
                edit_red.setFont(self.font_l_15)
                edit_red.setAlignment(QtCore.Qt.AlignCenter)
                le_comboBox_name_red_1.setLineEdit(edit_red)
            else:
                self.ui_kumite.le_comboBox_name_white_1.hide()
                self.ui_kumite.le_comboBox_name_red_1.hide()

                self.ui_kumite.lineEdit_name_white_1.show()
                self.ui_kumite.lineEdit_name_red_1.show()

                self.ui_kumite.frame_pyatnov_perebivka.hide()

            # Заполняем списки регионов в выпадающем списке
            if self.loaded_file_data_type == 'file_pyatnov':
                self.ui_kumite.lineEdit_name_white_1.setPlaceholderText("СИРО. Имя спортсмена")
                self.ui_kumite.lineEdit_name_red_1.setPlaceholderText("АКА. Имя спортсмена")
                edit_white = QtWidgets.QLineEdit(self, placeholderText="СИРО. Регион")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="АКА. Регион")

                self.blockedKumiteFrame()
            else:
                self.ui_kumite.lineEdit_name_white_1.setPlaceholderText("СИРО. Введите имя спортсмена")
                self.ui_kumite.lineEdit_name_red_1.setPlaceholderText("АКА. Введите имя спортсмена")
                edit_white = QtWidgets.QLineEdit(self, placeholderText="СИРО. Введите регион")
                edit_red = QtWidgets.QLineEdit(self, placeholderText="АКА. Введите регион")

                self.blockedKumiteFrame(status=False)

            lineEdit_region_white_1 = self.ui_kumite.lineEdit_region_white_1
            lineEdit_region_white_1.addItems([''])
            lineEdit_region_white_1.addItems(self.flags_set)
            edit_white.setFont(self.font_l_15)
            edit_white.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit_region_white_1.setLineEdit(edit_white)

            lineEdit_region_red_1 = self.ui_kumite.lineEdit_region_red_1
            lineEdit_region_red_1.addItems([''])
            lineEdit_region_red_1.addItems(self.flags_set)
            edit_red.setFont(self.font_l_15)
            edit_red.setAlignment(QtCore.Qt.AlignCenter)
            lineEdit_region_red_1.setLineEdit(edit_red)
        except Exception as e:
            print('_______Exception showKumiteWin:\n', e)

    def blockedKumiteFrame(self, status :bool=True):
        self.ui_kumite.frame_matchName.setDisabled(status)
        self.ui_kumite.control_panel.setDisabled(status)
        self.ui_kumite.frame_red1.setDisabled(status)
        self.ui_kumite.frame_white1.setDisabled(status)
        self.ui_kumite.winnerFrame.setDisabled(status)
        self.ui_kumite.frm_spman_red.setDisabled(status)
        self.ui_kumite.frm_spman_white.setDisabled(status)
        if status:
            self.ui_kumite.blocked_Form2.show()
        else:
            self.ui_kumite.blocked_Form2.hide()


    def closeAllWin(self):
        # print('        closeAllWin 1')
        self.ui_kumite.closeSecondWin()
        self.ui_kataQual.closeSecondWin()
        self.ui_kataFinal.closeSecondWin()
        self.ui_KataQualToKataFinal.close()
        self.ui_KataQualToKumite.close()
        self.ui_KataQualMenu.close()
        self.ui_KataFinalToKataQual.close()
        self.ui_KataFinalToKumite.close()
        self.ui_KataFinalMenu.close()
        self.ui_KumiteToKataQual.close()
        self.ui_KumiteToKataFinal.close()
        self.ui_KumiteMenu.close()
        self.KumiteWindowsClose.close()
        self.KataQualWindowsClose.close()
        self.KataFinalWindowsClose.close()
        # print('        closeAllWin 16')

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

    def calc_monitor_coord(self):
        if self.list_monitor[7] == 'is_primary=True)':
            self.display_coord_x1 = int(self.list_monitor[0].replace('Monitor(x=', ''))
            self.display_width = int(self.list_monitor[2].replace('width=', ''))
            self.display_coord_y1 = int(self.list_monitor[1].replace('y=', ''))
            self.display_height = int(self.list_monitor[3].replace('height=', ''))
        if self.list_monitor[7] == 'is_primary=False)' and self.display_coord_x1_secW == 'undefined':
            self.display_coord_x1_secW = int(self.list_monitor[0].replace('Monitor(x=', ''))
            self.display_width_secW = int(self.list_monitor[2].replace('width=', ''))
            self.display_coord_y1_secW = int(self.list_monitor[1].replace('y=', ''))
            self.display_height_secW = int(self.list_monitor[3].replace('height=', ''))

    def setSportsmanName(self):
        try:
            sender = self.sender()
            if self.loaded_file_data_type == 'file_pyatnov':
                if sender == self.ui_kataQual.btn_showData:
                    self.ui_kataQual.setSportsmanName()
                elif sender == self.ui_kataFinal.btn_showData:
                    self.ui_kataFinal.setSportsmanName()
                elif sender == self.ui_kumite.btn_showData:
                    self.ui_kumite.setSportsmanName()
                    self.ui_kumite.show_screen(force_hide=0)
                elif sender == self.ui_kumite.btn_show_screen:
                    self.ui_kumite.show_screen(force_hide=0)
                self.check_to_wopf()
            else:
                if sender == self.ui_kataQual.btn_showData:
                    # self.kata_matchName()
                    self.ui_kataQual.setSportsmanName()
                elif sender == self.ui_kataFinal.btn_showData:
                    # self.kata_matchName()
                    self.ui_kataFinal.setSportsmanName()
                elif sender == self.ui_kumite.btn_showData:
                    # self.kumite_matchName()
                    self.ui_kumite.setSportsmanName()
                    self.ui_kumite.show_screen(force_hide=0)
                elif sender == self.ui_kumite.btn_show_screen:
                    self.ui_kumite.show_screen(force_hide=0)
        except Exception as e:
            print('_______Exception setSportsmanName:', e)

    def clearData(self):
        try:
            sender = self.sender()
            if sender == self.ui_kataQual.btn_clearData:
                self.ui_kataQual.clearKataData()
            elif sender == self.ui_kataQual.btn_NewCategory:
                self.calcTabKata_Reset()
                self.ui_kataQual.NewCategory()
            elif sender == self.ui_kataFinal.Clear_Button:
                self.ui_kataFinal.clearKataData()
            elif sender == self.ui_kumite.btn_reset:
                if self.loaded_file_data_type == 'file_pyatnov':
                    self.paytnov_prepare_data_to_write_to_protocol()
                    # Если бой остановлен, то блокируем экран, т.к. бой завершен
                    if self.ui_kumite.btn_start.text() == '► START':
                        self.blockedKumiteFrame()
                self.ui_kumite.clearKumiteData()
            elif sender == self.ui_kumite.btn_NewCategory:
                if self.loaded_file_data_type == 'file_pyatnov':
                    self.paytnov_prepare_data_to_write_to_protocol()
                    # Если бой остановлен, то блокируем экран, т.к. бой завершен
                    if self.ui_kumite.btn_start.text() == '► START':
                        self.blockedKumiteFrame()
                self.ui_kumite.reset_all()
                self.ui_kumite.NewCategory()
            if self.loaded_file_data_type == 'file_pyatnov':
                self.check_to_wopf()
        except Exception as e:
            print('_______Exception clearData:', e)

    def set_winner(self):
        try:
            sender = self.sender()
            if sender in (self.ui_kataQual.winnerRed, self.ui_kataQual.winnerWhite):
                if sender == self.ui_kataQual.winnerRed:
                    self.ui_kataQual.setWinnerRed()
                elif sender == self.ui_kataQual.winnerWhite:
                    self.ui_kataQual.setWinnerWhite()

                if self.loaded_file_data_type == 'file_pyatnov':
                    aka_name = self.ui_kataQual.lineEdit_name_red_1.text()
                    siro_name = self.ui_kataQual.lineEdit_name_white_1.text()
                    side = 'siro' if sender == self.ui_kataQual.winnerWhite else 'aka'
                    row_num = siro_name + ' - ' + aka_name
                    row1 = [k for k, v in self.sportsmen_dict['combo_box'].items() if v == row_num][0]
                    row = self.sportsmen_dict['row_num'][row1]
                    col_white, col_red = ["G", "L"]
                    col = col_white if sender == self.ui_kataQual.winnerWhite else col_red
                    cell_coord = f"{col}{row}"
                    self.pyatnov_winner = {'type': 'ui_kataQual', 'side': side, 'cell': cell_coord}
            elif sender == self.ui_kataFinal.Calc_Button:
                self.ui_kataFinal.calcResult()
                if self.loaded_file_data_type == 'file_pyatnov':
                    aka_name = self.ui_kataFinal.label_name_red_1.text()
                    aka_region = self.ui_kataFinal.label_region_red_1.text()
                    # Находим key по имени и региону
                    row1 = [k for k, v in
                            {k: self.sportsmen_dict['name'][k] + str(self.sportsmen_dict['region_aka'][k]) for k in
                             self.sportsmen_dict['name']}.items() if v == aka_name + aka_region][0]

                    kata = self.ui_kataFinal.pyatnov_kata_name.currentText()
                    row = self.sportsmen_dict['row_num'][row1]
                    sp_cnt = self.sportsmen_dict['ttl_cnt_sp'][row1]
                    try:
                        score1 = float(self.ui_kataFinal.lineEdit_referee1.text())
                    except:
                        score1 = 0
                    try:
                        score2 = float(self.ui_kataFinal.lineEdit_referee2.text())
                    except:
                        score2 = 0
                    try:
                        score3 = float(self.ui_kataFinal.lineEdit_referee3.text())
                    except:
                        score3 = 0
                    try:
                        score4 = float(self.ui_kataFinal.lineEdit_referee4.text())
                    except:
                        score4 = 0
                    try:
                        score5 = float(self.ui_kataFinal.lineEdit_referee5.text())
                    except:
                        score5 = 0
                    try:
                        score6 = float(self.ui_kataFinal.lineEdit_referee6.text())
                    except:
                        score6 = 0
                    try:
                        score7 = float(self.ui_kataFinal.lineEdit_referee7.text())
                    except:
                        score7 = 0

                    if self.ui_kataFinal.lineEdit_referee6.text() == '.':
                        score = [
                            kata,
                            score1,
                            score2,
                            score3,
                            score4,
                            score5
                        ]
                        cell_coord = f"D{row}:I{row}"
                    else:
                        score = [
                            kata,
                            score1,
                            score2,
                            score3,
                            score4,
                            score5,
                            score6,
                            score7
                        ]
                        cell_coord = f"D{row}:K{row}"
                    number = [sp_cnt - len(self.sportsmen_dict['row_num']) + 1]
                    number_coord = f"A{row}"
                    self.pyatnov_winner = {'type': 'ui_kataFinal', 'score': score, 'cell': cell_coord, 'number': number,
                                           'number_coord': number_coord}
            elif sender in [self.ui_kumite.winnerRed, self.ui_kumite.winnerWhite]:
                self.ui_kumite.isShowSportsmanName(resetSportsmanFrame=0)
                self.ui_kumite.setWinner()

                if self.loaded_file_data_type == 'file_pyatnov':

                    if self.flag_pyatnov_kumite_team:
                        print('self.cur_men_pair_num', self.cur_men_pair_num)
                        name_white = self.ui_kumite.label_name_white_1.text()
                        region_white = self.ui_kumite.label_region_white_1.text()
                        name_red = self.ui_kumite.label_name_red_1.text()
                        region_red = self.ui_kumite.label_region_red_1.text()
                        ####################################################################
                        #  НИЧЕГО НЕ ДЕЛАЕМ ДЛЯ ЗАПИСИ В ФАЙЛ ПЯТНОВА
                        ####################################################################
                        # print('name_white', name_white, 'region_white', region_white)
                        # print('name_red', name_red, 'region_red', region_red)
                        # print('СОХРАНИТЬ В EXCEL кум командное')
                        # print('dict_paytnov_kumite_winner', self.dict_paytnov_kumite_winner)
                    else:
                        name_white = self.ui_kumite.label_name_white_1.text()
                        region_white = self.ui_kumite.label_region_white_1.text()
                        name_red = self.ui_kumite.label_name_red_1.text()
                        region_red = self.ui_kumite.label_region_red_1.text()
                        print('name_white', name_white, 'region_white', region_white)
                        print('name_red', name_red, 'region_red', region_red)
                        print('СОХРАНИТЬ В EXCEL кум ЛИЧНОЕ')
                    self.pyatnov_winner = {'type': 'ui_kumite'}

        except Exception as e:
            print('_______Exception set_winner:', e)

    def check_to_wopf(self):
        print('___________ check_to_wopf')
        if self.pyatnov_winner is None:
            print('                       self.pyatnov_winner is None')
            return
        try:
            # Записываем данные из переменной, обнуляем переменную и делаем проверку по ней, если она не None,
            # то записываем изменение в excel. Нужно добавить сценарий, на случай, если файл занят.



            if threading.active_count() <= 1:

                if self.flag_pyatnov_kumite_team:
                    # Если кумите команда отображаем заглушку сохранения
                    self.ui_kumite.blocked_Form2.hide()
                    self.ui_kumite.saving_into_kumite_team_Form2.show()

                thread1 = threading.Thread(target=self.write_on_pyatov_file, daemon=True)
                thread1.start()

                # print('hasattr(threading.current_thread()',
                #       hasattr(threading.current_thread(), 'main_thread_completion_status'))
                # print(threading.current_thread().main_thread_completion_status)

            else:
                # print('check_to_wopf threading.activeCount() БОЛЬШЕ 1')
                return

        except Exception as e:
            print('_______Exception check_to_wopf:', e)

    def write_on_pyatov_file(self):
        try:
            sender = self.sender()
            if self.loaded_file_data_type != 'file_pyatnov':
                return
            if self.pyatnov_winner is None:
                return
            excel_file_path = str(self.file)

            if self.pyatnov_winner['type'] == 'ui_kataQual':
                try:
                    excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    workbook = excel.Workbooks.Open(excel_file_path)
                    worksheet = workbook.Worksheets("Aka+Shiro")
                    worksheet.Range(self.pyatnov_winner['cell']).Value = 1
                    workbook.Save()
                    workbook.Close()
                    excel.Quit()

                    self.pyatnov_winner = None
                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

            elif self.pyatnov_winner['type'] == 'ui_kataFinal':
                try:
                    excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    workbook = excel.Workbooks.Open(excel_file_path)
                    worksheet = workbook.Worksheets(self.sheet_name_final)
                    worksheet.Range(self.pyatnov_winner['cell']).Value = self.pyatnov_winner['score']
                    worksheet.Range(self.pyatnov_winner['number_coord']).Value = self.pyatnov_winner['number']
                    workbook.Save()
                    workbook.Close()
                    excel.Quit()

                    self.pyatnov_winner = None
                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

            elif self.pyatnov_winner['type'] == 'ui_kumite':
                print(4, 222, 'ui_kumite')
                try:
                    self.ui_kumite.reset_all()
                    print('ЗАПИСЬ В EXCEL на строке:', self.cur_men_pair_num)
                    print('write_on_pyatov_file data_to_write_in_paytnov_referee_protocol', self.data_to_write_in_paytnov_referee_protocol)
                    excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    workbook = excel.Workbooks.Open(excel_file_path)
                    worksheet = workbook.Worksheets(self.sheet_name_referee)

                    # Determine the range to write data
                    start_row = self.cur_men_pair_num
                    start_col = 4

                    # Записываем данные для siro
                    for row_idx, row in enumerate(self.data_to_write_in_paytnov_referee_protocol, start=start_row):
                        for col_idx, value in enumerate(row, start=start_col):
                            worksheet.Cells(row_idx, col_idx).Value = value

                    workbook.Save()
                    workbook.Close()
                    excel.Quit()
                    print('ЗАПИСАНО В EXCEL ')

                    self.pyatnov_winner = None

                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

                self.ui_kumite.blocked_Form2.hide()

                # Если кумите команда закрываем заглушку сохранения
                if self.flag_pyatnov_kumite_team:
                    self.ui_kumite.saving_into_kumite_team_Form2.hide()
                    self.ui_kumite.blocked_Form2.show()

            else:
                return
            print(' 1 write_on_pyatov_file')
            result = self.pyatnov_processing()
            print(' 2 write_on_pyatov_file')
            if self.flag_pyatnov_kata_single or self.flag_pyatnov_kata_team:

                self.worker = Worker(result=result)
                self.worker.finished.connect(self.kata_qual_last_fight)
                self.worker.start()

                print(' 5 write_on_pyatov_file')

        except Exception as e:
            print('_______Exception write_on_pyatov_file:', e)

    def kata_qual_last_fight(self, result):
        # Проверка, нужно ли переключать интерфейс при записи в Excel(например из Ката отб в Ката финал)
        try:
            # print('           ___ kata_qual_last_fight', result)
            # Если был последний бой в отборочных Ката, то открываем окно Ката финал
            if result == 'self.showKataFinalWin()':
                self.showKataFinalWin()
        except Exception as e:
            print('_______Exception kata_qual_last_fight:', e)

    def pyatnov_flag(self, f1:bool=False, f2:bool=False, f3:bool=False, f4:bool=False):
        # Обновляем значение флага, в соответствии с тем, какой тип файла был загружен
        self.flag_pyatnov_kata_single = f1
        self.flag_pyatnov_kata_team = f2
        self.flag_pyatnov_kumite_single = f3
        self.flag_pyatnov_kumite_team = f4

    def get_data_for_paytnov_kumite_winner(self):
        # Записываем данные о течении боя
        try:
            sender = self.sender()
            # Если подключённый файл не Пятнова, ничего не делаем
            if self.loaded_file_data_type != 'file_pyatnov' or not sender.isChecked():
                return False
            # Если нажаты кнопку "обнуления", значит удаляем последнее добавленное значение
            if sender in (self.ui_kumite.score_white_0, self.ui_kumite.score_red_0,
                          self.ui_kumite.h_white4, self.ui_kumite.j_white4,
                          self.ui_kumite.h_red4, self.ui_kumite.j_red4):
                if sender == self.ui_kumite.score_white_0:
                    self.dict_paytnov_kumite_winner['siro']['score'] = list()
                elif sender == self.ui_kumite.score_red_0:
                    self.dict_paytnov_kumite_winner['aka']['score'] = list()
                elif sender == self.ui_kumite.h_white4:
                    self.paytnov_reset_hm_j('hm', self.dict_paytnov_kumite_winner['siro']['hm_j'], sender.text())
                    # self.dict_paytnov_kumite_winner['siro']['hm'] = list()
                elif sender == self.ui_kumite.j_white4:
                    self.paytnov_reset_hm_j('j', self.dict_paytnov_kumite_winner['siro']['hm_j'], sender.text())
                    # self.dict_paytnov_kumite_winner['siro']['j'] = list()
                elif sender == self.ui_kumite.h_red4:
                    self.paytnov_reset_hm_j('hm', self.dict_paytnov_kumite_winner['aka']['hm_j'], sender.text())
                    # self.dict_paytnov_kumite_winner['aka']['hm'] = list()
                elif sender == self.ui_kumite.j_red4:
                    self.paytnov_reset_hm_j('j', self.dict_paytnov_kumite_winner['aka']['hm_j'], sender.text())
                    # self.dict_paytnov_kumite_winner['aka']['j'] = list()
                return True


            # Проверяем, что нет повторов или меньших очков в списке данных протокола.
            # В таком случае из списка удаляем всё, что стоит дальше
            # self.paytnov_drop_repeated_score

            # СИРО
            if sender in (self.ui_kumite.score_white_1, self.ui_kumite.score_white_2, self.ui_kumite.score_white_3,
                            self.ui_kumite.score_white_4, self.ui_kumite.score_white_5, self.ui_kumite.score_white_6):
                self.dict_paytnov_kumite_winner['siro']['score'] = self.paytnov_drop_repeated_score(
                    'num',
                    self.dict_paytnov_kumite_winner['siro']['score'],
                    sender.text()
                )
                return True

            elif sender in (self.ui_kumite.h_white1, self.ui_kumite.h_white2, self.ui_kumite.h_white3):
                self.dict_paytnov_kumite_winner['siro']['hm_j'] = self.paytnov_drop_repeated_score(
                    'hm',
                    self.dict_paytnov_kumite_winner['siro']['hm_j'],
                    sender.text()
                )
                return True

            elif sender in (self.ui_kumite.j_white1, self.ui_kumite.j_white2, self.ui_kumite.j_white3):
                self.dict_paytnov_kumite_winner['siro']['hm_j'] = self.paytnov_drop_repeated_score(
                    'j',
                    self.dict_paytnov_kumite_winner['siro']['hm_j'],
                    sender.text()
                )
                return True

            # АКА
            elif sender in (self.ui_kumite.score_red_1, self.ui_kumite.score_red_2, self.ui_kumite.score_red_3,
                            self.ui_kumite.score_red_4, self.ui_kumite.score_red_5, self.ui_kumite.score_red_6):
                self.dict_paytnov_kumite_winner['aka']['score'] = self.paytnov_drop_repeated_score(
                    'num',
                    self.dict_paytnov_kumite_winner['aka']['score'],
                    sender.text()
                )
                return True

            elif sender in (self.ui_kumite.h_red1, self.ui_kumite.h_red2, self.ui_kumite.h_red3):
                self.dict_paytnov_kumite_winner['aka']['hm_j'] = self.paytnov_drop_repeated_score(
                    'hm',
                    self.dict_paytnov_kumite_winner['aka']['hm_j'],
                    sender.text()
                )
                return True

            elif sender in (self.ui_kumite.j_red1, self.ui_kumite.j_red2, self.ui_kumite.j_red3):
                self.dict_paytnov_kumite_winner['aka']['hm_j'] = self.paytnov_drop_repeated_score(
                    'j',
                    self.dict_paytnov_kumite_winner['aka']['hm_j'],
                    sender.text()
                )
                return True

        except Exception as e:
            print('_______Exception get_data_for_paytnov_kumite_winner:', e)

    def paytnov_prepare_data_to_write_to_protocol(self):
        # Обрадатываем данные для запими данных в проктокол агрибтра
        try:
            self.data_to_write_in_paytnov_referee_protocol = [[], []]
            # Заносим запись о победителе в словарь протокола
            if self.ui_kumite.winnerWhite.isChecked():
                self.dict_paytnov_kumite_winner['siro']['result'] = 1
                self.dict_paytnov_kumite_winner['aka']['result'] = 0
            elif self.ui_kumite.winnerRed.isChecked():
                self.dict_paytnov_kumite_winner['siro']['result'] = 0
                self.dict_paytnov_kumite_winner['aka']['result'] = 1
            else:
                self.dict_paytnov_kumite_winner['siro']['result'] = 0
                self.dict_paytnov_kumite_winner['aka']['result'] = 0

            def score_convert(lst: list) -> list:
                # Функция конвертирует цифры в кружки для записи в протокол
                score = {1: '○', 2: '●'}
                if len(lst) > 1:
                    new_lst = [0 for _ in lst]
                    new_lst[0] = lst[0]
                    for i in range(1, len(lst)):
                        new_lst[i] = lst[i] - lst[i - 1]
                    lst = new_lst
                if len(lst):
                    new_lst = list()
                    for x in lst:
                        new_lst.append(score[x] if x < 3 else score[2])
                    lst = new_lst
                # Если длина списка не 5, добавляем пустоты, т.к. мы записываем данные дня 5 ячеек
                if len(lst) < 5:
                    for i in range(len(lst), 5):
                        lst.append('')
                else:
                    lst = lst[:5]
                return lst

            def hm_j_convert(lst: list) -> list:
                # Функция конвертации нарушений в аббревиатуру
                hm_j = {'hm_Keikoku': 'K', 'hm_Chui': 'HC', 'hm_Hansoku': 'H',
                        'j_Keikoku': 'JK', 'j_Chui': 'JС', 'j_Hansoku': 'JH'}

                if len(lst):
                    lst = [hm_j[x] for x in lst if x in hm_j.keys()]
                # Если длина списка не 5, добавляем пустоты, т.к. мы записываем данные дня 5 ячеек
                if len(lst) < 5:
                    for i in range(len(lst), 5):
                        lst.append('')
                else:
                    lst = lst[:5]
                return lst

            def result_convert(siro_result: int, aka_result: int) -> tuple[str, str]:
                # Функция конвертирует результат в кружок, квадрат или крест
                result = {(1, 0):('□', '×'), (0, 1):('×', '□'), (0, 0):('△', '△')}

                return result[siro_result, aka_result]

            # Преобразовываем данные для записи в файл
            siro_score = self.dict_paytnov_kumite_winner['siro']['score']
            siro_score = [int(x) for x in siro_score if x]

            self.dict_paytnov_kumite_winner['siro']['score'] = score_convert(siro_score)

            self.dict_paytnov_kumite_winner['siro']['hm_j'] = hm_j_convert(
                self.dict_paytnov_kumite_winner['siro']['hm_j'])

            siro_result = self.dict_paytnov_kumite_winner['siro']['result']

            aka_score = self.dict_paytnov_kumite_winner['aka']['score']
            aka_score = [int(x) for x in aka_score if x]

            self.dict_paytnov_kumite_winner['aka']['score'] = score_convert(aka_score)

            self.dict_paytnov_kumite_winner['aka']['hm_j'] = hm_j_convert(
                self.dict_paytnov_kumite_winner['aka']['hm_j'])

            aka_result = self.dict_paytnov_kumite_winner['aka']['result']

            self.dict_paytnov_kumite_winner['siro']['result'], self.dict_paytnov_kumite_winner['aka']['result'] = (
                result_convert(siro_result, aka_result))

            self.data_to_write_in_paytnov_referee_protocol = [[], []]

            self.data_to_write_in_paytnov_referee_protocol[0].extend(self.dict_paytnov_kumite_winner['siro']['score'])
            self.data_to_write_in_paytnov_referee_protocol[0].append(self.dict_paytnov_kumite_winner['siro']['result'])
            self.data_to_write_in_paytnov_referee_protocol[0].append(self.dict_paytnov_kumite_winner['aka']['result'])
            self.data_to_write_in_paytnov_referee_protocol[0].extend(self.dict_paytnov_kumite_winner['aka']['score'])

            self.data_to_write_in_paytnov_referee_protocol[1].extend(self.dict_paytnov_kumite_winner['siro']['hm_j'])
            self.data_to_write_in_paytnov_referee_protocol[1].append('')
            self.data_to_write_in_paytnov_referee_protocol[1].append('')
            self.data_to_write_in_paytnov_referee_protocol[1].extend(self.dict_paytnov_kumite_winner['aka']['hm_j'])
        except Exception as e:
            print('_______Exception paytnov_prepare_data_to_write_to_protocol:', e)

    def paytnov_drop_repeated_score(self, lst_type: str, lst: list, score: str) -> list:
        # Удаляем повторяющиеся значения очков. Такое может быть если захотели вернуть прежнее значение
        # lst_type - типы списка (числовые -score и текстовые - hm, j)
        try:
            # Для числовых значений
            if lst_type == 'num':
                # Если список был пуст - возвращаем список с одним значением
                if not len(lst):
                    return [score]

                # Конвертируем всё в числа
                int_lst = [int(x) for x in lst if x]
                score = int(score)

                # Создаём список значений с большими или такими же числами, как score
                # и определяем нахождение самого первого значения
                position_of_max_val = list()
                for num, val in enumerate(int_lst):
                    if val >= score:
                        position_of_max_val.append(num)

                # Если в списке было найдено равное или больше число, отправляем новый список
                if len(position_of_max_val):
                    if position_of_max_val[0] == 0:
                        return [score]
                    int_lst = int_lst[:position_of_max_val[0]]
                    int_lst.append(score)
                    return int_lst
                else:
                    int_lst.append(score)
                    return int_lst
            else:
                score = f'{lst_type}_{score}'

                # Если список был пуст - возвращаем список с одним значением
                if not len(lst):
                    return [score]

                # Добавляем пустое значение, куда потенциально может встать score
                lst.append('')

                # Словари с очками
                dct = {
                    f'{lst_type}_Keikoku': 1,
                    f'{lst_type}_Chui': 2,
                    f'{lst_type}_Hansoku': 3,
                }
                dct_reverse = {
                    1: f'{lst_type}_Keikoku',
                    2: f'{lst_type}_Chui',
                    3: f'{lst_type}_Hansoku',
                }

                # Конвертируем всё в числа
                int_lst = list()
                for x in range(len(lst)):
                    if lst[x] in dct.keys():
                        int_lst.append(dct[lst[x]])
                        lst[x] = ''

                # Создаём список значений с большими или такими же числами, как score
                # и определяем нахождение самого первого значения
                position_of_max_val = list()
                for num, val in enumerate(int_lst):
                    if val >= dct[score]:
                        position_of_max_val.append(num)

                # Если в списке было найдено равное или больше число, отправляем новый список
                if len(position_of_max_val):
                    if position_of_max_val[0] == 0:
                        int_lst = list()
                    else:
                        int_lst = int_lst[:position_of_max_val[0]]

                # Проходим по списку int_lst и добавляем сконвертированное в текст значение в lst
                if len(int_lst):
                    for i in range(len(int_lst)):
                        for j in range(len(lst)):
                            if lst[j] == '':
                                lst[j] = dct_reverse[int_lst[i]]
                                break
                # Нет других очков hm кроме score. Добавляем score в первую пустую позицию и возвращаем список
                else:
                    for x in range(len(lst)):
                        if lst[x] == '':
                            lst[x] = score
                            return lst

                # Если остались пустые значения, удаляем их
                lst = list(filter(None, lst))
                lst.append(score)
                return lst

        except Exception as e:
            print('_______Exception paytnov_drop_repeated_score:', e)

    def paytnov_reset_hm_j(self, lst_type: str, lst: list, score: str) -> list:
        # Обнуляем hm_j если нажали на ноль штрафов
        # lst_type - типы списка (числовые -score и текстовые - hm, j)
        try:
            # Если список был пуст - возвращаем список с одним значением
            if not len(lst):
                return ['']

            # Словари с очками
            dct = {
                f'{lst_type}_Keikoku': 1,
                f'{lst_type}_Chui': 2,
                f'{lst_type}_Hansoku': 3,
            }

            # Удаляем все значения lst_type из списка и "двигаем" другие штрафы, если есть
            for x in range(len(lst)):
                if lst[x] in dct.keys():
                    lst[x] = ''

            # Если остались пустые значения, удаляем их
            lst = list(filter(None, lst))

            return lst
        except Exception as e:
            print('_______Exception paytnov_reset_hm_j:', e)


class dialogWindow_Ui(object):
    def __init__(self):
        self.font_l_12 = css.font_l_12
        self.font_l_15 = css.font_l_15
        self.font_l_20 = css.font_l_20
        self.btn_style_1 = css.btn_style_1

    def setupUi_dialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 120)
        Dialog.setStyleSheet("background-color: white;")
        self.Ui_Form0 = Ui_Form0()

        self.btn_OK = QtWidgets.QPushButton("OK", Dialog)
        self.btn_OK.setGeometry(QtCore.QRect(95, 70, 100, 32))
        self.btn_OK.setStyleSheet(self.btn_style_1)
        self.btn_OK.setFont(self.font_l_15)

        self.btn_CANCEL = QtWidgets.QPushButton("CANCEL", Dialog)
        self.btn_CANCEL.setGeometry(QtCore.QRect(205, 70, 100, 32))
        self.btn_CANCEL.setStyleSheet(self.btn_style_1)
        self.btn_CANCEL.setFont(self.font_l_15)

        self.btn_CANCEL.clicked.connect(Dialog.close)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 15, 400, 25))
        self.label.setFont(self.font_l_20)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(0, 40, 400, 20))
        self.label2.setFont(self.font_l_12)
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
