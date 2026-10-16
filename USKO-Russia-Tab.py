import sys

# Дочерний сервер не загружает Qt, Excel, ресурсы табло и окна судейства.
# Та же точка входа используется в собранном exe без отдельной консоли Windows.
if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "--usko-server-worker":
    from server_worker import run_worker
    sys.exit(run_worker(sys.argv[2:]))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtSvg import QSvgRenderer
# from PyQt5.QtCore.QProcess import sender
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
from openpyxl import Workbook, load_workbook
import win32com.client
# import xlwings as xw
import threading
import pythoncom
import os
import sys
import json
import websocket  # websocket-client
import requests
import base64
from program_download import DOWNLOAD_URL, DOWNLOAD_QR_PNG
from contextlib import contextmanager


# Класс для записи в потоке данных в файл excel
# class Worker(QObject):
class Worker(QThread):
    finished = pyqtSignal(QtCore.QVariant)

    def __init__(self, result):
        super().__init__()
        self.result = result

    def run(self):
        try:
            self.finished.emit(self.result)
            # Закрываем поток
            self.quit()
            self.deleteLater()

        except Exception as e:
            print('_______Exception check_to_change_interface:', e)
            self.finished.emit(str(e))


class Ui_Form0(object):
    def __init__(self):
        self.year = '2026-10-11'
        self.program_release_number = 'rev-006'

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
        self.btn_settings = QtWidgets.QPushButton(Form0)
        self.frame_combo = QtWidgets.QFrame(Form0)
        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.frame_logo = QtWidgets.QFrame(Form0)
        self.logo_USKOrus = QtGui.QPixmap(":/Images/emblem_usko.png")
        self.logo_VBErus = QtGui.QPixmap(":/Images/emblem_vbe_rus.png")
        self.logo_JKA = QtGui.QPixmap(":/Images/icon.ico")
        self.label_logo_USKOrus = QtWidgets.QLabel(self.frame_logo)
        self.label_logo_VBErus = QtWidgets.QLabel(self.frame_logo)
        self.label_logo_JKA = QtWidgets.QLabel(self.frame_logo)
        self.sponsored_by = QtWidgets.QLabel(self.frame_logo)
        self.legend = QtWidgets.QLabel(Form0)
        self.frame_overlay_status = QtWidgets.QFrame(Form0)
        self.overlay_status_label = QtWidgets.QLabel(self.frame_overlay_status)
        self.img_overlay_offline = QtGui.QPixmap(":/Images/overlay_offline.svg")
        self.img_overlay_online = QtGui.QPixmap(":/Images/overlay_online.svg")
        self.img_overlay_no_data = QtGui.QPixmap(":/Images/overlay_no_data.svg")
        self.label_img_overlay_offline = QtWidgets.QLabel(self.frame_overlay_status)
        self.label_img_overlay_online = QtWidgets.QLabel(self.frame_overlay_status)
        self.label_img_overlay_no_data = QtWidgets.QLabel(self.frame_overlay_status)

        self.frame_sportsmans_load_status = QtWidgets.QFrame(Form0)
        self.img_sportsmans_not_loaded = QtGui.QPixmap(":/Images/sportsmans_not_loaded.svg")
        self.img_spotrsmans_uploaded = QtGui.QPixmap(":/Images/spotrsmans_uploaded.svg")
        self.label_img_sportsmans_not_loaded = QtWidgets.QLabel(self.frame_sportsmans_load_status)
        self.label_img_spotrsmans_uploaded = QtWidgets.QLabel(self.frame_sportsmans_load_status)

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

        # Готовый QR показывается без HTTP и генерации при запуске: недоступность
        # Google не должна задерживать открытие меню или работу секретаря.
        self.download_qr = QtWidgets.QLabel(Form0)
        self.download_qr.setGeometry(QtCore.QRect(106, 130, 147, 147))
        self.download_qr.setObjectName('download_qr')
        self.download_qr.setAccessibleName('QR-код для скачивания актуальной версии программы')
        self.download_qr.setToolTip('Наведите камеру телефона: таблица со ссылкой на скачивание программы')
        qr_pixmap = QtGui.QPixmap()
        qr_pixmap.loadFromData(base64.b64decode(DOWNLOAD_QR_PNG), 'PNG')
        # 49 модулей с белыми полями × 3 пикселя: границы остаются чёткими.
        self.download_qr.setPixmap(qr_pixmap.scaled(147, 147, QtCore.Qt.KeepAspectRatio,
                                                  QtCore.Qt.FastTransformation))
        self.download_link = QtWidgets.QLabel(Form0)
        self.download_link.setGeometry(QtCore.QRect(60, 277, 240, 32))
        self.download_link.setObjectName('download_link')
        self.download_link.setAlignment(QtCore.Qt.AlignCenter)
        self.download_link.setStyleSheet('font-family: Gotham-Light; font-size: 13px; color: grey;')
        self.download_link.setText(f'<a href="{DOWNLOAD_URL}">Скачать программу</a><br>Актуальная версия')
        self.download_link.setOpenExternalLinks(True)
        self.download_link.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.main_instruction_link = QtWidgets.QLabel(Form0)
        self.main_instruction_link.setGeometry(QtCore.QRect(60, 313, 240, 24))
        self.main_instruction_link.setObjectName('main_instruction_link')
        self.main_instruction_link.setAlignment(QtCore.Qt.AlignCenter)
        self.main_instruction_link.setStyleSheet('font-family: Gotham-Light; font-size: 13px;')
        self.main_instruction_link.setText(
            '<a href="https://docs.google.com/document/d/'
            '15DOfeDC1w3KRnIniRTZ2F0rWOWWCaNN3n5OrbMsGwP4/edit?tab=t.0">Инструкция по программе</a>')
        self.main_instruction_link.setOpenExternalLinks(True)
        self.main_instruction_link.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.main_instruction_link.setToolTip('Открыть инструкцию по работе с табло в браузере')

        self.status_file.setGeometry(QtCore.QRect(60, 20, 780, 30))
        self.status_file.setStyleSheet("color: grey;")
        self.status_file.setFont(self.font_l_12)
        self.status_file.setObjectName("status_file")

        # Кнопка «настройки» (шестерёнка)
        self.btn_settings.setGeometry(QtCore.QRect(840, 20, 30, 30))
        self.btn_settings.setText("⚙")
        self.btn_settings.setToolTip("Режим работы и подключение к трансляции")
        self.btn_settings.setObjectName("btn_settings")

        # Круглая шестерёнка с реакцией на hover/press
        self.btn_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet("""
            QPushButton#btn_settings {
                background-color: transparent;
                border: none;
                font-size: 18px;
                border-radius: 15px;      /* круг при 30x30 */
            }
            QPushButton#btn_settings:hover {
                background-color: rgba(0, 0, 0, 0.06);
            }
            QPushButton#btn_settings:pressed {
                background-color: rgba(0, 0, 0, 0.15);
            }
        """)

        self.frame_logo.setGeometry(QtCore.QRect(330, 50, 570, 300))
        self.frame_logo.setStyleSheet("background-color: none;")
        self.frame_logo.setObjectName("frame_logo")

        self.label_logo_USKOrus.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.label_logo_USKOrus.setObjectName("label_logo_USKOrus")
        self.label_logo_USKOrus.setPixmap(self.logo_USKOrus)

        self.label_logo_VBErus.setGeometry(QtCore.QRect(180, 0, 150, 150))
        self.label_logo_VBErus.setObjectName("label_logo_VBErus")
        self.label_logo_VBErus.setPixmap(self.logo_VBErus)

        self.label_logo_JKA.setGeometry(QtCore.QRect(360, 0, 150, 150))
        self.label_logo_JKA.setObjectName("label_logo_JKA")
        # Вписываем логотип в область 150×150, сохраняя пропорции.
        self.label_logo_JKA.setPixmap(
            self.logo_JKA.scaled(
                self.label_logo_JKA.size(),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation,
            )
        )
        self.label_logo_JKA.setAlignment(QtCore.Qt.AlignCenter)

        self.sponsored_by.setGeometry(QtCore.QRect(0, 150, 510, 85))  # justify
        self.sponsored_by.setStyleSheet("font-family: Gotham-Light; text-align: right; color: black; font-size: 15px;")
        self.sponsored_by.setAlignment(QtCore.Qt.AlignCenter)
        self.sponsored_by.setObjectName("sponsored_by")

        self.legend.setGeometry(QtCore.QRect(0, 480, 900, 10))
        self.legend.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10px;")
        self.legend.setAlignment(QtCore.Qt.AlignCenter)
        self.legend.setObjectName("legend")

        self.frame_overlay_status.setGeometry(QtCore.QRect(0, 465, 900, 10))
        self.frame_overlay_status.setStyleSheet("background-color: none;")
        self.frame_overlay_status.setObjectName("overlay_status_label")

        self.label_img_overlay_offline.setGeometry(QtCore.QRect(5, 0, 10, 10))
        self.label_img_overlay_offline.setObjectName("label_img_overlay_offline")
        self.label_img_overlay_offline.setPixmap(self.img_overlay_offline)

        self.label_img_overlay_online.setGeometry(QtCore.QRect(5, 0, 10, 10))
        self.label_img_overlay_online.setObjectName("label_img_overlay_online")
        self.label_img_overlay_online.setPixmap(self.img_overlay_online)

        self.label_img_overlay_no_data.setGeometry(QtCore.QRect(5, 0, 15, 10))
        self.label_img_overlay_no_data.setObjectName("label_img_overlay_no_data")
        self.label_img_overlay_no_data.setPixmap(self.img_overlay_no_data)

        self.overlay_status_label.setGeometry(QtCore.QRect(20, 0, 880, 10))
        self.overlay_status_label.setStyleSheet("font-family: Gotham-Light; color: grey; font-size: 10px;")
        self.overlay_status_label.setAlignment(QtCore.Qt.AlignLeft)
        self.overlay_status_label.setObjectName("overlay_status_label")

        self.frame_sportsmans_load_status.setGeometry(QtCore.QRect(885, 5, 15, 10))
        self.frame_sportsmans_load_status.setStyleSheet("background-color: none;")
        self.frame_sportsmans_load_status.setObjectName("frame_sportsmans_load_status")

        self.label_img_sportsmans_not_loaded.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_sportsmans_not_loaded.setObjectName("label_img_sportsmans_not_loaded")
        self.label_img_sportsmans_not_loaded.setPixmap(self.img_sportsmans_not_loaded)

        self.label_img_spotrsmans_uploaded.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.label_img_spotrsmans_uploaded.setObjectName("label_img_spotrsmans_uploaded")
        self.label_img_spotrsmans_uploaded.setPixmap(self.img_spotrsmans_uploaded)

        self.label_img_spotrsmans_uploaded.hide()

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
        self.sponsored_by.setText(
            _translate(
                "self.frame_logo",
                "При поддержке президента Общероссийской\nфизкультурно-спортивной общественной организации\n«Объединённая организация сётокан каратэ-до России»\nЛаткина А. И."
            )
        )
        # year = datetime.date.today().year
        self.legend.setText(_translate("Form0",
                                       f"Программа «Электронное табло USKO RUSSIA». {self.year} год. "
                                       f"Версия {self.program_release_number}"))

# Сбор настроек на всех листах файла
def backup_all_page_setups(workbook):
    setups = {}
    for sheet in workbook.Worksheets:
        setups[sheet.Name] = backup_page_setup(sheet)
        print(f'    backup_all_page_setups:{sheet.Name}', setups[sheet.Name])
    return setups

# Для сохранения файла Пятнова нужно считать настройки форматирования листа
def backup_page_setup(worksheet):
    try:
        ps = worksheet.PageSetup
        return {
            'PrintArea': worksheet.Range(ps.PrintArea).Address if ps.PrintArea else None,
            'PrintTitleRows': worksheet.Rows(ps.PrintTitleRows).Address if ps.PrintTitleRows else None,
            'PrintTitleColumns': worksheet.Columns(ps.PrintTitleColumns).Address if ps.PrintTitleColumns else None,
            'LeftMargin': ps.LeftMargin,
            'RightMargin': ps.RightMargin,
            'TopMargin': ps.TopMargin,
            'BottomMargin': ps.BottomMargin,
            'HeaderMargin': ps.HeaderMargin,
            'FooterMargin': ps.FooterMargin,
            'Orientation': ps.Orientation,
            'Zoom': ps.Zoom,
            'FitToPagesWide': ps.FitToPagesWide,
            'FitToPagesTall': ps.FitToPagesTall,
            'CenterHorizontally': ps.CenterHorizontally,
            'CenterVertically': ps.CenterVertically,
            'PaperSize': ps.PaperSize,
            'HPageBreaks': [brk.Location.Address for brk in worksheet.HPageBreaks],
            'VPageBreaks': [brk.Location.Address for brk in worksheet.VPageBreaks],
        }
    except Exception as e:
        print('   ! Exception ____backup_page_setup', str(e))
        return {}

# В файле пятнова проходим по каждому листу и восстанавливаем настройки листов
def restore_all_page_setups(workbook, setups):
    for sheet in workbook.Worksheets:
        if sheet.Name in setups:
            restore_page_setup(sheet, setups[sheet.Name])

# Для сохранения файла Пятнова восстанавливаем форматирование перед сохранением
def restore_page_setup(worksheet, setup):
    try:
        ps = worksheet.PageSetup

        if setup.get('PrintArea'):
            ps.PrintArea = worksheet.Range(setup['PrintArea']).Address
        else:
            ps.PrintArea = ""

        if setup.get('PrintTitleRows'):
            ps.PrintTitleRows = worksheet.Rows(setup['PrintTitleRows']).Address
        else:
            ps.PrintTitleRows = ""

        if setup.get('PrintTitleColumns'):
            ps.PrintTitleColumns = worksheet.Columns(setup['PrintTitleColumns']).Address
        else:
            ps.PrintTitleColumns = ""

        ps.LeftMargin = setup['LeftMargin']
        ps.RightMargin = setup['RightMargin']
        ps.TopMargin = setup['TopMargin']
        ps.BottomMargin = setup['BottomMargin']
        ps.HeaderMargin = setup['HeaderMargin']
        ps.FooterMargin = setup['FooterMargin']
        ps.Orientation = setup['Orientation']
        ps.Zoom = setup['Zoom']
        ps.FitToPagesWide = setup['FitToPagesWide']
        ps.FitToPagesTall = setup['FitToPagesTall']
        ps.CenterHorizontally = setup['CenterHorizontally']
        ps.CenterVertically = setup['CenterVertically']
        ps.PaperSize = setup['PaperSize']

        # Разрывы
        for i in reversed(range(worksheet.HPageBreaks.Count)):
            worksheet.HPageBreaks(i + 1).Delete()
        for i in reversed(range(worksheet.VPageBreaks.Count)):
            worksheet.VPageBreaks(i + 1).Delete()

        for addr in setup.get('HPageBreaks', []):
            worksheet.HPageBreaks.Add(Before=worksheet.Range(addr))
        for addr in setup.get('VPageBreaks', []):
            worksheet.VPageBreaks.Add(Before=worksheet.Range(addr))
    except Exception as e:
        print('   ! Exception restore_page_setup', str(e))


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
        self.data_to_write_in_paytnov_referee_protocol = [[], [], []]  # Обработанные данные, записываемы в Excel

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
        # --- WebSocket: онлайн-обновление оценок в Ката финал ---
        try:
            for le in (
                self.ui_kataFinal.lineEdit_referee1,
                self.ui_kataFinal.lineEdit_referee2,
                self.ui_kataFinal.lineEdit_referee3,
                self.ui_kataFinal.lineEdit_referee4,
                self.ui_kataFinal.lineEdit_referee5,
                self.ui_kataFinal.lineEdit_referee6,
                self.ui_kataFinal.lineEdit_referee7,
            ):
                le.textChanged.connect(self.on_kata_final_scores_changed)
        except Exception as e:
            print("WS: cannot connect kata_final score signals:", e)

        self.ui_kataFinalSecondWindow = KataSecondWindow()
        self.ui_kumite = KumiteMainWindow_Ui()  # Окно КУМИТЕ

        self.combo_placeholder_choice = 'Выбор'

        # Поиск внутри выпадающих списков спортсменов.
        # Не трогаем comboBox_age, регионы и верхнее меню, чтобы не было конфликтов.
        for combo_box in (
            self.ui_kataQual.comboBox_name_red_1,
            self.ui_kataQual.comboBox_name_white_1,
            self.ui_kataFinal.comboBox_name_red_1,
            self.ui_kumite.comboBox_name_red_1,
            self.ui_kumite.comboBox_name_white_1,
        ):
            self.make_searchable_combo(combo_box)


        self.USKO_PC = css.USKO_PC

        # ---- Настройки сервера трансляции ----
        self.server_ip = None
        self.server_port = None
        self.server_config_path = None
        self.has_server_info = False  # Подгружена валидная инфа для коннекта к серверу оверлея
        self.is_overlay_connected = False  # Есть соединение с сервером оверлея
        self.overlay_seq = 0


        # Кнопка "шестерёнка"
        self.btn_settings.clicked.connect(self.open_settings_dialog)

        # Попытка найти usko-server.txt рядом с exe
        self.load_server_config_default()

        self.tatamiName = f'Татами №{self.USKO_PC}' if self.USKO_PC != '#' else ''

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
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.update_kumite_overlay)
        self.ui_KumiteMenu.btn_OK.clicked.connect(self.showMainMenu)
        ########   в окне КУМИТЕ кнопка КАТА отб.
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(lambda: self.ui_kumite.reset_all(self.flags_dict))
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.ui_kumite.NewCategory)
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.update_kumite_overlay)
        self.ui_KumiteToKataQual.btn_OK.clicked.connect(self.showKataQualWin)
        ########   в окне КУМИТЕ кнопка КАТА ФИНАЛ
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(lambda: self.ui_kumite.reset_all(self.flags_dict))
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.ui_kumite.NewCategory)
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.update_kumite_overlay)
        self.ui_KumiteToKataFinal.btn_OK.clicked.connect(self.showKataFinalWin)

        self.ui_KataQualMenu.btn_OK.clicked.connect(self.clear_kata_qual_searchable_combos)
        self.ui_KataQualToKumite.btn_OK.clicked.connect(self.clear_kata_qual_searchable_combos)
        self.ui_KataQualToKataFinal.btn_OK.clicked.connect(self.clear_kata_qual_searchable_combos)

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

        # Ката по флажкам → после пересчёта участников обновляем оверлей
        self.ui_kataQual.comboBox_age.activated[str].connect(
            lambda *_: self.update_kata_qual_overlay()
        )
        # Ката финал → после выбора возраста обновляем оверлей (final=False, т.к. ещё не нажали "Рассчитать")
        self.ui_kataFinal.comboBox_age.activated[str].connect(
            lambda *_: self.update_kata_final_overlay(final=False)
        )
        # Кумите → после выбора возраста обновляем оверлей
        self.ui_kumite.comboBox_age.activated[str].connect(
            lambda *_: self.update_kumite_overlay()
        )

        # В окне Ката по флажкам кнопка "Показать на экране"
        self.ui_kataFinal.btn_showData.clicked.connect(self.setSportsmanName)
        # Обновляем название категории на мониторе при изменении в окне на ПК
        self.ui_kataFinal.matchName1.editingFinished.connect(self.ui_kataFinal.setMatchName)
        # В окне Кумите кнопка "Показать на экране"
        self.ui_kumite.btn_showData.clicked.connect(self.setSportsmanName)
        # Обновляем название категории на мониторе при изменении в окне на ПК
        self.ui_kumite.matchName12.editingFinished.connect(self.ui_kumite.setMatchName)

        # обновляем оверлей КАТА по флажкам — когда пользователь руками поменял строку категории
        self.ui_kataQual.matchName1.editingFinished.connect(self.update_kata_qual_overlay)
        # обновляем оверлей КАТА финал — обновляем оверлей при ручном изменении
        self.ui_kataFinal.matchName1.editingFinished.connect(
            lambda: self.update_kata_final_overlay(final=False)
        )
        # обновляем оверлей КУМИТЕ — ручное изменение строки категории
        self.ui_kumite.matchName12.editingFinished.connect(self.update_kumite_overlay)

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

        self.ui_kumite.btn_start.clicked.connect(self.update_kumite_overlay)
        self.ui_kumite.btn_pause.clicked.connect(self.update_kumite_dynamic_overlay)
        # self.ui_kumite.btn_reset.clicked.connect(self.update_kumite_dynamic_overlay)  #Уже используем в clearData
        self.ui_kumite.plus2sec.clicked.connect(self.update_kumite_dynamic_overlay)
        self.ui_kumite.minus2sec.clicked.connect(self.update_kumite_dynamic_overlay)

        # Обновление позиций экранов по нажатию кнопки
        self.ui_kataQual.btn_refresh_display_position.clicked.connect(lambda: self.refresh_display_position_clicked('ui_kataQual'))
        self.ui_kataFinal.btn_refresh_display_position.clicked.connect(lambda: self.refresh_display_position_clicked('ui_kataFinal'))
        self.ui_kumite.btn_refresh_display_position.clicked.connect(lambda: self.refresh_display_position_clicked('ui_kumite'))

        # --- WS / Overlay: каждую секунду обновляем таймер в оверлее ---
        try:
            self.ui_kumite.timer.timeout.connect(self.tick_update_kumite_dynamic_overlay)
        except Exception as e:
            print("WS: cannot connect kumite timer to overlay:", e)

        # --- WS / Overlay: обновление состояния при изменении очков и штрафов ---
        for rb in (
            self.ui_kumite.score_red_0,    self.ui_kumite.score_white_0,
            self.ui_kumite.score_red_1,    self.ui_kumite.score_white_1,
            self.ui_kumite.score_red_2,    self.ui_kumite.score_white_2,
            self.ui_kumite.score_red_3,    self.ui_kumite.score_white_3,
            self.ui_kumite.score_red_4,    self.ui_kumite.score_white_4,
            self.ui_kumite.score_red_5,    self.ui_kumite.score_white_5,
            self.ui_kumite.score_red_6,    self.ui_kumite.score_white_6,
            self.ui_kumite.h_red1,         self.ui_kumite.h_white1,
            self.ui_kumite.h_red2,         self.ui_kumite.h_white2,
            self.ui_kumite.h_red3,         self.ui_kumite.h_white3,
            self.ui_kumite.h_red4,         self.ui_kumite.h_white4,
            self.ui_kumite.j_red1,         self.ui_kumite.j_white1,
            self.ui_kumite.j_red2,         self.ui_kumite.j_white2,
            self.ui_kumite.j_red3,         self.ui_kumite.j_white3,
            self.ui_kumite.j_red4,         self.ui_kumite.j_white4,
        ):
            rb.toggled.connect(self.kumite_toggled_hmj_overlay)

        self.ui_kumite.btn_show_screen.clicked.connect(self.setSportsmanName)

        self.ui_kumite.pyatnov_perebivka_qbx.clicked.connect(self.paytnov_perebivka)
        self.ui_kumite.pyatnov_perebivka_btn.clicked.connect(self.paytnov_perebivka)
        self.ui_kumite.perebivka_siro.activated[str].connect(self.setLabel)
        self.ui_kumite.perebivka_aka.activated[str].connect(self.setLabel)

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

        self.overlay_kumite_state = {}  # Сохраняем последнее изменение боя кумите (отправляем вместе с тиками)
        self.reset_kumite_overlay_state()
        # Флаг, что не нужно отправлять в оверлей нажатия QRadioButton пока едёт сброс (кнопка новый бой)
        self._overlay_suppress = False

        # В самом начале работы приложения — сбросить оверлей (ничего не идёт)
        try:
            self.send_overlay_idle()
        except Exception as e:
            print("overlay idle on start error:", e)

    # Блокируем сигнал для отправки в оверлей кумите, пока очищаем интерфейс для нового боя
    @contextmanager
    def suppress_overlay(self):
        old = self._overlay_suppress
        self._overlay_suppress = True
        try:
            yield
        finally:
            self._overlay_suppress = old

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

    # Метод, очищающий все данные, импортированными их Excel (применяется, если выбран неверный лист. Старые данные удаляются)
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
        # self.cur_men_pair_num = None  # Номер строки пары спортсменов
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

            sheets11 = self.xl.book.worksheets

            setka_num = 1000

            sheets11_list = []
            for sheet in sheets11:
                if sheet.sheet_state == 'visible':

                    sh_t = sheet.title
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
                self.show_withOut_load_file_interface()
                return

    # Интерфейс без выбранных файлов (нет выбора пар спортсменов)
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

        self.sportsmans_load_status_frame(is_loaded=False)

    # Интерфейс с выбранным файлом (с выбором пар спортсменов)
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

        # Финал использует готовые SVG из того же справочника регионов.
        self.ui_kataFinal.flags_dict = self.flags_dict

        self.sportsmans_load_status_frame()

    # Обновление позиции мониторов по нажатию кнопки
    def refresh_display_position_clicked(self, sender):

        if sender == 'ui_kumite':
            sender = self.ui_kumite
        elif sender == 'ui_kataQual':
            sender = self.ui_kataQual
        elif sender == 'ui_kataFinal':
            sender = self.ui_kataFinal
        else:
            return

        # 1. заново получаем список мониторов
        monitors = get_monitors()

        # 2. сбрасываем координаты
        self.display_coord_x1 = None
        self.display_coord_y1 = None
        self.display_width = None
        self.display_height = None

        self.display_coord_x1_secW = None
        self.display_coord_y1_secW = None
        self.display_width_secW = None
        self.display_height_secW = None

        # 3. перерасчитываем
        for monitor in monitors:
            if monitor.is_primary:
                self.display_coord_x1 = monitor.x
                self.display_coord_y1 = monitor.y
                self.display_width = monitor.width
                self.display_height = monitor.height
            else:
                self.display_coord_x1_secW = monitor.x
                self.display_coord_y1_secW = monitor.y
                self.display_width_secW = monitor.width
                self.display_height_secW = monitor.height

        # 4. если найден основной монитор — центрируем
        if self.display_coord_x1 is not None:
            sender.calc_display_moveCoord(
                self.display_coord_x1,
                self.display_coord_y1,
                self.display_width,
                self.display_height,
                self.display_coord_x1_secW or self.display_coord_x1,
                self.display_coord_y1_secW or self.display_coord_y1
            )

    def _post_overlay_async(self, url, payload, is_tick=False):
        try:
            r = requests.post(url, json=payload, timeout=(1, 2))
            r.raise_for_status()

            self.overlay_status_frame(
                txt="",
                tool_tip="",
                is_online="online"
            )
            self.is_overlay_connected = True

        except Exception as e:
            self.overlay_status_frame(
                txt="WS: overlay недоступен",
                tool_tip=str(e),
                is_online="offline"
            )

            if not is_tick:
                self.is_overlay_connected = False

    # Делаем возможность поиска в списках спортсменов
    def make_searchable_combo(self, combo_box, placeholder="Начните вводить для поиска"):
        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

        combo_box.lineEdit().setPlaceholderText(placeholder)
        combo_box.lineEdit().setAlignment(QtCore.Qt.AlignCenter)

        completer = QtWidgets.QCompleter(combo_box.model(), combo_box)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        combo_box.setCompleter(completer)

        def select_completed_text(text):
            index = combo_box.findText(text)
            if index >= 0:
                combo_box.setCurrentIndex(index)
                combo_box.activated[str].emit(text)

        completer.activated[str].connect(select_completed_text)

    # Заполняем возраст с первым disabled-пунктом "Выбор"
    def fill_age_combo_with_placeholder(self, combo_box, values):
        combo_box.clear()
        combo_box.addItem(self.combo_placeholder_choice)
        combo_box.addItems(values)
        combo_box.setCurrentIndex(0)

        first_item = combo_box.model().item(0)
        if first_item:
            first_item.setEnabled(False)

    # Очищаем searchable combo, чтобы показывался плейсхолдер, а не первая ФИО
    def reset_searchable_combo(self, combo_box):
        combo_box.clear()
        combo_box.setCurrentIndex(-1)

        if combo_box.isEditable() and combo_box.lineEdit():
            combo_box.lineEdit().clear()

    # После заполнения ФИО оставляем поле пустым с плейсхолдером
    def fill_searchable_combo(self, combo_box, values):
        combo_box.clear()
        combo_box.addItems(values)
        combo_box.setCurrentIndex(-1)

        if combo_box.isEditable() and combo_box.lineEdit():
            combo_box.lineEdit().clear()

    # Сбрасываем выбранное ФИО, но НЕ очищаем список значений
    def clear_searchable_combo_selection(self, combo_box):
        combo_box.setCurrentIndex(-1)

        if combo_box.isEditable() and combo_box.lineEdit():
            combo_box.lineEdit().clear()

    def clear_kata_qual_searchable_combos(self):
        self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_red_1)
        self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_white_1)

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

    def pyatnov_processing(self, is_kum_team_clear_name=True):
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
                                   15, 17,
                                 23, 24, 25, 26, 27
                                 ],
                        names=[
                        '1_siro_num', '2_siro_sportsman', '3_siro_region',
                        '4_siro_rating_1', '5_siro_rating_2', '6_siro_rating_3', '7_siro_rating_4', '8_siro_rating_5',
                        '9_siro_score',
                        '10_aka_score',
                        '11_aka_rating_1', '12_aka_rating_2', '13_aka_rating_3', '14_aka_rating_4', '15_aka_rating_5',
                        '17_aka_sportsman', '18_aka_num',
                        '19_perebivka_1', '20_perebivka_2', '21_perebivka_3', '22_perebivka_4', '23_perebivka_5',
                        ]
                                                         )

                        referee_protocol = referee_protocol.fillna('')

                        t_name_dict = referee_protocol.iloc[21::53, [0, 2, 10]].to_dict()

                        # Список пар участвующих (pairs)
                        pairs_1 = referee_protocol.iloc[24::53, [0, 1, 15, 8, 9]].to_dict()
                        pairs_2 = referee_protocol.iloc[26::53, [0, 1, 15, 8, 9]].to_dict()
                        pairs_3 = referee_protocol.iloc[28::53, [0, 1, 15, 8, 9]].to_dict()
                        team_result = referee_protocol.iloc[34::53, [8, 9]].to_dict()
                        perebivka = referee_protocol.iloc[37::53, [0, 1, 15, 8, 9]].to_dict()
                        perebivka_siro_raw = referee_protocol.iloc[25::53, [17, 18, 19, 20, 21]].to_dict()
                        perebivka_aka_raw = referee_protocol.iloc[24::53, [17, 18, 19, 20, 21]].to_dict()

                        self.teams_pairs = dict()
                        # self.cur_men_pair_num = None  # Номер строки пары спортсменов
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
                            siro_perebivka_raw_1 = perebivka_siro_raw['19_perebivka_1'][key - 1]
                            siro_perebivka_raw_2 = perebivka_siro_raw['20_perebivka_2'][key - 1]
                            siro_perebivka_raw_3 = perebivka_siro_raw['21_perebivka_3'][key - 1]
                            siro_perebivka_raw_4 = perebivka_siro_raw['22_perebivka_4'][key - 1]
                            siro_perebivka_raw_5 = perebivka_siro_raw['23_perebivka_5'][key - 1]
                            aka_man_1 = pairs_1['17_aka_sportsman'][key - 2]
                            aka_man_2 = pairs_2['17_aka_sportsman'][key]
                            aka_man_3 = pairs_3['17_aka_sportsman'][key + 2]
                            siro_team_result = team_result['9_siro_score'][key + 8]
                            aka_team_result = team_result['10_aka_score'][key + 8]
                            aka_perebivka = perebivka['17_aka_sportsman'][key + 11]
                            aka_perebivka_raw_1 = perebivka_aka_raw['19_perebivka_1'][key - 2]
                            aka_perebivka_raw_2 = perebivka_aka_raw['20_perebivka_2'][key - 2]
                            aka_perebivka_raw_3 = perebivka_aka_raw['21_perebivka_3'][key - 2]
                            aka_perebivka_raw_4 = perebivka_aka_raw['22_perebivka_4'][key - 2]
                            aka_perebivka_raw_5 = perebivka_aka_raw['23_perebivka_5'][key - 2]

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

                            # Обрабатываем ФИО перебивок, добавляем вариант с сокращением имя/отчество
                            (aka_perebivka_short_1, aka_perebivka_short_2, aka_perebivka_short_3,
                             aka_perebivka_short_4, aka_perebivka_short_5) = ['', '', '', '', '']
                            (siro_perebivka_short_1, siro_perebivka_short_2, siro_perebivka_short_3,
                             siro_perebivka_short_4, siro_perebivka_short_5) = ['', '', '', '', '']
                            combo_box_aka_perebivka = list()
                            combo_box_aka_perebivka_short = list()
                            combo_box_siro_perebivka = list()
                            combo_box_siro_perebivka_short = list()
                            if not isinstance(aka_perebivka_raw_1, int) and len(aka_perebivka_raw_1.split(' ')) > 1:
                                aka_perebivka_short_1 = (aka_perebivka_raw_1.split(' ')[0] + ' ' +
                                                         aka_perebivka_raw_1.split(' ')[1][0] + '.')
                                combo_box_aka_perebivka.append(aka_perebivka_raw_1)
                                combo_box_aka_perebivka_short.append(aka_perebivka_short_1)
                            if not isinstance(aka_perebivka_raw_2, int) and len(aka_perebivka_raw_2.split(' ')) > 1:
                                aka_perebivka_short_2 = (aka_perebivka_raw_2.split(' ')[0] + ' ' +
                                                         aka_perebivka_raw_2.split(' ')[1][0] + '.')
                                combo_box_aka_perebivka.append(aka_perebivka_raw_2)
                                combo_box_aka_perebivka_short.append(aka_perebivka_short_2)
                            if not isinstance(aka_perebivka_raw_3, int) and len(aka_perebivka_raw_3.split(' ')) > 1:
                                aka_perebivka_short_3 = (aka_perebivka_raw_3.split(' ')[0] + ' ' +
                                                         aka_perebivka_raw_3.split(' ')[1][0] + '.')
                                combo_box_aka_perebivka.append(aka_perebivka_raw_3)
                                combo_box_aka_perebivka_short.append(aka_perebivka_short_3)
                            if not isinstance(aka_perebivka_raw_4, int) and len(aka_perebivka_raw_4.split(' ')) > 1:
                                aka_perebivka_short_4 = (aka_perebivka_raw_4.split(' ')[0] + ' ' +
                                                         aka_perebivka_raw_4.split(' ')[1][0] + '.')
                                combo_box_aka_perebivka.append(aka_perebivka_raw_4)
                                combo_box_aka_perebivka_short.append(aka_perebivka_short_4)
                            if not isinstance(aka_perebivka_raw_5, int) and len(aka_perebivka_raw_5.split(' ')) > 1:
                                aka_perebivka_short_5 = (aka_perebivka_raw_5.split(' ')[0] + ' ' +
                                                         aka_perebivka_raw_5.split(' ')[1][0] + '.')
                                combo_box_aka_perebivka.append(aka_perebivka_raw_5)
                                combo_box_aka_perebivka_short.append(aka_perebivka_short_5)
                            if not isinstance(siro_perebivka_raw_1, int) and len(siro_perebivka_raw_1.split(' ')) > 1:
                                siro_perebivka_short_1 = (siro_perebivka_raw_1.split(' ')[0] + ' ' +
                                                          siro_perebivka_raw_1.split(' ')[1][0] + '.')
                                combo_box_siro_perebivka.append(siro_perebivka_raw_1)
                                combo_box_siro_perebivka_short.append(siro_perebivka_short_1)
                            if not isinstance(siro_perebivka_raw_2, int) and len(siro_perebivka_raw_2.split(' ')) > 1:
                                siro_perebivka_short_2 = (siro_perebivka_raw_2.split(' ')[0] + ' ' +
                                                          siro_perebivka_raw_2.split(' ')[1][0] + '.')
                                combo_box_siro_perebivka.append(siro_perebivka_raw_2)
                                combo_box_siro_perebivka_short.append(siro_perebivka_short_2)
                            if not isinstance(siro_perebivka_raw_3, int) and len(siro_perebivka_raw_3.split(' ')) > 1:
                                siro_perebivka_short_3 = (siro_perebivka_raw_3.split(' ')[0] + ' ' +
                                                          siro_perebivka_raw_3.split(' ')[1][0] + '.')
                                combo_box_siro_perebivka.append(siro_perebivka_raw_3)
                                combo_box_siro_perebivka_short.append(siro_perebivka_short_3)
                            if not isinstance(siro_perebivka_raw_4, int) and len(siro_perebivka_raw_4.split(' ')) > 1:
                                siro_perebivka_short_4 = (siro_perebivka_raw_4.split(' ')[0] + ' ' +
                                                          siro_perebivka_raw_4.split(' ')[1][0] + '.')
                                combo_box_siro_perebivka.append(siro_perebivka_raw_4)
                                combo_box_siro_perebivka_short.append(siro_perebivka_short_4)
                            if not isinstance(siro_perebivka_raw_5, int) and len(siro_perebivka_raw_5.split(' ')) > 1:
                                siro_perebivka_short_5 = (siro_perebivka_raw_5.split(' ')[0] + ' ' +
                                                          siro_perebivka_raw_5.split(' ')[1][0] + '.')
                                combo_box_siro_perebivka.append(siro_perebivka_raw_5)
                                combo_box_siro_perebivka_short.append(siro_perebivka_short_5)

                            #Если все бои завершены и нет перебивки - не добавляем команду
                            # if (complete_pair_1==complete_pair_2==complete_pair_3==0 and
                            #         not (complete_perebivka==1 and perebivka_tmp)):
                            if siro_team_result and aka_team_result:
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
                                'siro_perebivka_raw_1': siro_perebivka_raw_1,
                                'siro_perebivka_raw_2': siro_perebivka_raw_2,
                                'siro_perebivka_raw_3': siro_perebivka_raw_3,
                                'siro_perebivka_raw_4': siro_perebivka_raw_4,
                                'siro_perebivka_raw_5': siro_perebivka_raw_5,
                                'siro_perebivka_short_1': siro_perebivka_short_1,
                                'siro_perebivka_short_2': siro_perebivka_short_2,
                                'siro_perebivka_short_3': siro_perebivka_short_3,
                                'siro_perebivka_short_4': siro_perebivka_short_4,
                                'siro_perebivka_short_5': siro_perebivka_short_5,
                                'aka_perebivka_raw_1': aka_perebivka_raw_1,
                                'aka_perebivka_raw_2': aka_perebivka_raw_2,
                                'aka_perebivka_raw_3': aka_perebivka_raw_3,
                                'aka_perebivka_raw_4': aka_perebivka_raw_4,
                                'aka_perebivka_raw_5': aka_perebivka_raw_5,
                                'aka_perebivka_short_1': aka_perebivka_short_1,
                                'aka_perebivka_short_2': aka_perebivka_short_2,
                                'aka_perebivka_short_3': aka_perebivka_short_3,
                                'aka_perebivka_short_4': aka_perebivka_short_4,
                                'aka_perebivka_short_5': aka_perebivka_short_5,
                                'combo_box_siro_perebivka': combo_box_siro_perebivka,
                                'combo_box_siro_perebivka_short': combo_box_siro_perebivka_short,
                                'combo_box_aka_perebivka': combo_box_aka_perebivka,
                                'combo_box_aka_perebivka_short': combo_box_aka_perebivka_short,

                                'siro_short_perebivka': siro_short_perebivka,
                                'siro_perebivka': siro_perebivka,
                                'aka_short_perebivka': aka_short_perebivka,
                                'aka_perebivka': aka_perebivka,
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

                zzz = pd.read_excel(self.file, sheet_name=aka_shiro, usecols=list(range(10)), skiprows=10, nrows=5)

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
                        # Удаляем задвоение пробелов в ФИО
                        self.sportsmen_list['siro'] = self.sportsmen_list['siro'].str.replace(r'\s+', ' ', regex=True)
                        self.sportsmen_list['aka'] = self.sportsmen_list['aka'].str.replace(r'\s+', ' ', regex=True)

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
                    self.sportsmans_load_status_frame(is_loaded=False)
                    return 'file was completed'

                if comp_type == 'ката':
                    self.show_pyatnov_kata_interface()
                    self.ui_kumite.matchName12.setText(self.category_label)

                    if self.tatamiName == "":
                        self.ui_kataQual.matchName1.setText(f'Татами №{self.USKO_PC}, ' + self.category_label)
                        self.ui_kataFinal.matchName1.setText(f'Татами №{self.USKO_PC}, ' + self.category_label)
                    else:
                        self.ui_kataQual.matchName1.setText(self.tatamiName + ', ' + self.category_label)
                        self.ui_kataFinal.matchName1.setText(self.tatamiName + ', ' + self.category_label)

                    if is_semi_final == [False, False]:
                        # self.ui_kataQual.pyatnov_name.hidePopup()
                        self.ui_kataQual.pyatnov_name.clear()
                        self.ui_kataQual.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kataQual.pyatnov_name.setEnabled(True)

                        self.btn_Kata_qual.setEnabled(True)
                        self.btn_Kata_final.setEnabled(False)

                    elif is_semi_final in [[True, False], [False, True]]:

                        self.ui_kataQual.frame_pyatnov.hide()

                        # self.ui_kataFinal.pyatnov_name.hidePopup()
                        self.ui_kataFinal.pyatnov_name.clear()
                        self.ui_kataFinal.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kataFinal.pyatnov_name.setEnabled(True)

                        # Список ката
                        # self.ui_kataFinal.pyatnov_name.hidePopup()
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
                        # self.ui_kumite.pyatnov_name.hidePopup()

                        self.ui_kumite.pyatnov_name.clear()
                        self.ui_kumite.pyatnov_name.addItems(self.sportsmen_list['combo_box'].tolist())
                        self.ui_kumite.pyatnov_name.setEnabled(True)
                        self.ui_kumite.matchName12.setText(self.category_label)
                        self.ui_kumite.pyatnov_name.setCurrentIndex(0)
                    elif self.flag_pyatnov_kumite_team:
                        if not is_kum_team_clear_name:
                            pyatnov_name_index = self.ui_kumite.pyatnov_name.currentIndex()
                        self.show_pyatnov_kumite_interface(team=True)
                        # self.ui_kumite.pyatnov_name.hidePopup()
                        self.ui_kumite.pyatnov_name.clear()
                        self.ui_kumite.pyatnov_name.addItem('Выберите команды...')
                        self.ui_kumite.pyatnov_name.addItems(self.teams_pairs.keys())
                        self.ui_kumite.pyatnov_name.setEnabled(True)
                        self.ui_kumite.matchName12.setText(self.category_label)
                        self.ui_kumite.pyatnov_name.setCurrentIndex(0 if is_kum_team_clear_name else pyatnov_name_index)

                self.status_file.setStyleSheet("color: rgb(0, 178, 80);")
                self.status_file.setText(f'Файл  <b>{self.filename}</b> загружен')

                self.sportsmans_load_status_frame(is_loaded=True)

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
                df2 = self.sheet.loc[
                    self.sheet[k_n].isin(
                        ['ком1', 'ком2', 'ком3', 'ком4', 'ком5', 'ком 1', 'ком 2', 'ком 3', 'ком 4', 'ком 5']
                    ), ['a10', 'a11', 'a12', 'a13', k_n]]
                df_Temp1_Group_list = dict(zip(df2.a12 + ' ' + df2.a13 + ' - ' + df2.a11,
                                               'a12' + df2.a12 + 'a13' + df2.a13 + 'a11' + df2.a11))

                self.df_Group_list.append(df_Temp1_Group_list)
                self.df_Group_list_only_group.append(dict(zip(df2.a11 + ' - ' + df2[k_n], df2[k_n])))
            else:
                self.df_Group_list.append({})
                self.df_Group_list_only_group.append({})

            self.df_Single_names.append(k_n)
            self.df_Group_names.append(k_n)
            self.df_Single_list.append(df_Temp_Single_list)
        ################################################################

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
        dict_KataOrKumite = load_date
        comboBox_age = self.ui_kataQual.comboBox_age
        age_1 = self.ui_kataQual.age_1
        name_red_1 = self.ui_kataQual.name_red_1
        name_white_1 = self.ui_kataQual.name_white_1
        comboBox_name_red_1 = self.ui_kataQual.comboBox_name_red_1
        comboBox_name_white_1 = self.ui_kataQual.comboBox_name_white_1
        self.calcTabKataSpotrsmans(dict_KataOrKumite, comboBox_age, age_1, name_red_1,
                                   name_white_1, comboBox_name_red_1, comboBox_name_white_1)

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
        self.reset_searchable_combo(comboBox_name_red_1)

        comboBox_name_white_1.setEnabled(False)
        self.reset_searchable_combo(comboBox_name_white_1)

        self.fill_age_combo_with_placeholder(
            comboBox_age,
            [self.sportsmans_ages_dict[x] for x in self.TempSet]
        )

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
        self.reset_searchable_combo(comboBox_name_red_1)

        comboBox_name_white_1.setEnabled(False)
        self.reset_searchable_combo(comboBox_name_white_1)

        self.fill_age_combo_with_placeholder(
            comboBox_age,
            [self.sportsmans_ages_dict[x] for x in self.TempSet]
        )

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
        if n == self.combo_placeholder_choice:
            return
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

        self.fill_searchable_combo(comboBox_name_r, df_list)
        self.fill_searchable_combo(comboBox_name_w, df_list)
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
            if n == self.combo_placeholder_choice:
                return
            a2 = {k: v for k, v in
                  # zip(sorted(list(self.TempSet)), sorted([self.sportsmans_ages_dict[x] for x in self.TempSet]))}
                  zip((self.TempSet), [self.sportsmans_ages_dict[x] for x in self.TempSet])}
            self.x = list(self.sportsmans_ages_dict.keys()).index(list(a2.keys())[list(a2.values()).index(n)])
            group_pref = ''

            if not pers_com_qbx.isChecked():
                df_list = sorted(self.df_Single_list[self.x])
            else:
                # df_list = sorted(self.df_Group_list[self.x])
                df_list = sorted(self.df_Group_list_only_group[self.x])
                group_pref = "ГРУППА  "
            try:
                if self.tatamiName == "":
                    jj.setText(f"Татами №{self.USKO_PC}, {group_pref}{self.matchName[list(self.matchName.keys())[self.x]]}")
                else:
                    jj.setText(f"{self.tatamiName}, {group_pref}{self.matchName[list(self.matchName.keys())[self.x]]}")
            except Exception as e:
                print('_______Exception calcTab1:', e)
                if self.tatamiName == "":
                    jj.setText(f'Татами №{self.USKO_PC}, ')
                else:
                    jj.setText(self.tatamiName)
            name.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 12px;")
            # comboBox_name.addItems(sorted(self.df_Single_list[self.x]))
            self.fill_searchable_combo(comboBox_name, df_list)
            comboBox_name.setEnabled(True)
        except Exception as e:
            print('_______Exception calcTab2:', e)

    def setLabel(self):
        try:
            sender = self.sender()

            #Отдельно обрабатываем Перебивку Кумите Ком
            if sender == self.ui_kumite.perebivka_siro:
                if not self.ui_kumite.perebivka_siro.currentIndex():
                    return
                return self.ui_kumite.lineEdit_name_red_1.setText(self.ui_kumite.perebivka_siro.currentText())
            elif sender == self.ui_kumite.perebivka_aka:
                if not self.ui_kumite.perebivka_aka.currentIndex():
                    return
                return self.ui_kumite.lineEdit_name_white_1.setText(self.ui_kumite.perebivka_aka.currentText())

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

                    # Панель перебивки и выпадающие списки для перебивки
                    self.ui_kumite.perebivka_frame(btn_disable=False, id_show=False, btn_select=False)
                    self.ui_kumite.perebivka_siro.clear()
                    self.ui_kumite.perebivka_aka.clear()
                    self.ui_kumite.perebivka_siro.addItem('СИРО. Перебивка')
                    self.ui_kumite.perebivka_siro.addItems(c_box_choice['combo_box_siro_perebivka_short'])
                    self.ui_kumite.perebivka_siro.setEnabled(True)
                    self.ui_kumite.perebivka_siro.model().item(0).setEnabled(False)
                    self.ui_kumite.perebivka_aka.addItem('АКА. Перебивка')
                    self.ui_kumite.perebivka_aka.addItems(c_box_choice['combo_box_aka_perebivka_short'])
                    self.ui_kumite.perebivka_aka.setEnabled(True)
                    self.ui_kumite.perebivka_aka.model().item(0).setEnabled(False)

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

                _cur_men_pair_num, siro_man, aka_man = self.cur_team_pair()
                # Если данные для протокола пусты, указываем номер строки
                if self.data_to_write_in_paytnov_referee_protocol == [[], [], []]:
                    self.cur_men_pair_num = _cur_men_pair_num

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

    def cur_team_pair(self) -> tuple[int, str, str]:
        """Определяем пару в командном кумите и номер строки в протоколе"""
        cur_team_pair = self.teams_pairs[self.ui_kumite.pyatnov_name.currentText()]
        cur_men_pair = self.ui_kumite.pyatnov_pair_name.currentText()

        if cur_team_pair['men_pair_1'] == cur_men_pair:
            return cur_team_pair['row_num_1'], cur_team_pair['siro_short_man_1'], cur_team_pair['aka_short_man_1']
        elif cur_team_pair['men_pair_2'] == cur_men_pair:
            return cur_team_pair['row_num_2'], cur_team_pair['siro_short_man_2'], cur_team_pair['aka_short_man_2']
        elif cur_team_pair['men_pair_3'] == cur_men_pair:
            return cur_team_pair['row_num_3'], cur_team_pair['siro_short_man_3'], cur_team_pair['aka_short_man_3']

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
            self.ui_kataQual.matchName1.setText(f'Татами №{self.USKO_PC}, Возраст')
            # self.ui_kataQual.matchName1.setText('Татами №#, Возраст')

    def showKataQualWin(self):
        try:
            self.closeAllWin()
            self.refresh_display_position_clicked('ui_kataQual')
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
            self.refresh_display_position_clicked('ui_kataFinal')
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
            self.reset_searchable_combo(self.ui_kataFinal.comboBox_name_red_1)
            self.ui_kataFinal.comboBox_name_red_1.setEnabled(False)

        except Exception as e:
            print('_______Exception showKataFinalWin:', e)

    def showKumiteWin(self):
        try:
            self.ui_kataFinal.clearKataData()
            self.ui_kataQual.NewCategory()
            self.ui_kumite.reset_all(self.flags_dict)
            self.closeAllWin()
            self.refresh_display_position_clicked('ui_kumite')
            self.close()
            if self.tatamiName != "":
                self.ui_kumite.matchName11.setText(self.tatamiName)
            self.ui_kumite.setMatchName()

            # Если командное для Пятнова, то отображаем выпадающий список с ФИО спортсменов команд и скрываем lineEdit
            if self.sportsmans_in_teams_dict:

                # """
                # Пока ничего не делаем с перебивкой. Нужно пересмортерть источник, где мы берем список ФИО ДЛЯ ПЕРЕБИВКИ,
                # т.к. ФИО выступавшего могут не указать в списке первых трёх спортсменов
                # """
                # self.ui_kumite.frame_pyatnov_perebivka.hide()


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

        self.reset_kumite_overlay_state()

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
        # Оверлей: по желанию можно скрыть табло
        try:
            self.send_overlay_idle()
        except Exception as e:
            print("overlay showMainMenu error:", e)

    def closeEvent(self, event):
        super().closeEvent(event)

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
                    # self.refresh_display_position_clicked('ui_kataQual')
                    self.ui_kataQual.setSportsmanName()
                elif sender == self.ui_kataFinal.btn_showData:
                    # self.refresh_display_position_clicked('ui_kataFinal')
                    self.ui_kataFinal.setSportsmanName()
                elif sender == self.ui_kumite.btn_showData:
                    # self.refresh_display_position_clicked('ui_kumite')
                    self.ui_kumite.setSportsmanName()
                    self.ui_kumite.show_screen(force_hide=0)
                    # Обновляем значение названия татами
                    self.tatamiName = self.ui_kumite.matchName11.text()
                elif sender == self.ui_kumite.btn_show_screen:
                    self.ui_kumite.show_screen(force_hide=0)
                self.check_to_wopf()
            else:
                if sender == self.ui_kataQual.btn_showData:
                    # self.refresh_display_position_clicked('ui_kataQual')
                    self.ui_kataQual.setSportsmanName()
                elif sender == self.ui_kataFinal.btn_showData:
                    # self.refresh_display_position_clicked('ui_kataFinal')
                    self.ui_kataFinal.setSportsmanName()
                elif sender == self.ui_kumite.btn_showData:
                    # self.refresh_display_position_clicked('ui_kumite')
                    self.ui_kumite.setSportsmanName()
                    self.ui_kumite.show_screen(force_hide=0)
                    # Обновляем значение названия татами
                    self.tatamiName = self.ui_kumite.matchName11.text()
                elif sender == self.ui_kumite.btn_show_screen:
                    # self.refresh_display_position_clicked('ui_kumite')
                    self.ui_kumite.show_screen(force_hide=0)

            # --- НОВОЕ: после любого обновления ФИО шлём данные в оверлей ---
            try:
                state = None
                if sender in (self.ui_kumite.btn_showData, self.ui_kumite.btn_show_screen):
                    self.build_kumite_state()
                    self.send_overlay_message(self.overlay_kumite_state)
                elif sender == self.ui_kataQual.btn_showData:
                    state = self.build_kata_qual_state()
                elif sender == self.ui_kataFinal.btn_showData:
                    state = self.build_kata_final_state()

                if state:
                    self.send_overlay_message(state)
            except Exception as e:
                print("overlay error in setSportsmanName:", e)

        except Exception as e:
            print('_______Exception setSportsmanName:', e)

    def clearData(self):
        try:
            sender = self.sender()
            # --- КАТА ОТБОРОЧНЫЕ ---
            if sender == self.ui_kataQual.btn_clearData:
                self.ui_kataQual.clearKataData()
                self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_red_1)
                self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_white_1)

                # Оверлей: очистка бойцов, оставляем только категорию/татами
                try:
                    state = self.build_kata_qual_state()
                    if state:
                        state["aka"]["name"] = ""
                        state["aka"]["region"] = ""
                        state["siro"]["name"] = ""
                        state["siro"]["region"] = ""
                        state.pop("winner_side", None)
                        self.send_overlay_message(state)
                except Exception as e:
                    print("overlay kata_qual clear error:", e)

            elif sender == self.ui_kataQual.btn_NewCategory:
                # self.refresh_display_position_clicked('ui_kataQual')
                self.calcTabKata_Reset()
                self.ui_kataQual.NewCategory()
                self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_red_1)
                self.clear_searchable_combo_selection(self.ui_kataQual.comboBox_name_white_1)

                # Оверлей: новая категория, спортсмены ещё не выбраны
                try:
                    state = self.build_kata_qual_state()
                    if state:
                        state["aka"]["name"] = ""
                        state["aka"]["region"] = ""
                        state["siro"]["name"] = ""
                        state["siro"]["region"] = ""
                        state.pop("winner_side", None)
                        self.send_overlay_message(state)
                except Exception as e:
                    print("overlay kata_qual new_category error:", e)

            # --- КАТА ФИНАЛ ---
            elif sender == self.ui_kataFinal.Clear_Button:
                # self.refresh_display_position_clicked('ui_kataFinal')
                self.ui_kataFinal.clearKataData()
                self.clear_searchable_combo_selection(self.ui_kataFinal.comboBox_name_red_1)

                # Оверлей: очистка оценок и суммы
                try:
                    state = self.build_kata_final_state()
                    if state:
                        for k in state.get("scores", {}):
                            state["scores"][k] = ""
                        state["sum"] = ""
                        state["final"] = False
                        self.send_overlay_message(state)
                except Exception as e:
                    print("overlay kata_final clear error:", e)

            # --- КУМИТЕ
            elif sender == self.ui_kumite.btn_reset:
                self.reset_kumite_overlay_state()
                # self.refresh_display_position_clicked('ui_kumite')
                if self.loaded_file_data_type == 'file_pyatnov':
                    self.paytnov_prepare_data_to_write_to_protocol()
                    # Если бой остановлен, то блокируем экран, т.к. бой завершен
                    if self.ui_kumite.btn_start.text() == '► START':
                        self.blockedKumiteFrame()
                with self.suppress_overlay():
                    self.ui_kumite.clearKumiteData()
                    self.clear_searchable_combo_selection(self.ui_kumite.comboBox_name_red_1)
                    self.clear_searchable_combo_selection(self.ui_kumite.comboBox_name_white_1)
                # >>> обновляем оверлей после сброса боя
                self.update_kumite_overlay()
            elif sender == self.ui_kumite.btn_NewCategory:
                self.reset_kumite_overlay_state()
                # self.refresh_display_position_clicked('ui_kumite')
                if self.loaded_file_data_type == 'file_pyatnov':
                    self.paytnov_prepare_data_to_write_to_protocol()
                    # Если бой остановлен, то блокируем экран, т.к. бой завершен
                    if self.ui_kumite.btn_start.text() == '► START':
                        self.blockedKumiteFrame()
                with self.suppress_overlay():
                    self.ui_kumite.reset_all()
                    self.ui_kumite.NewCategory()
                    self.clear_searchable_combo_selection(self.ui_kumite.comboBox_name_red_1)
                    self.clear_searchable_combo_selection(self.ui_kumite.comboBox_name_white_1)
                # >>> обновляем оверлей после сброса боя
                self.update_kumite_overlay()
            if self.loaded_file_data_type == 'file_pyatnov':
                self.check_to_wopf()
        except Exception as e:
            print('_______Exception clearData:', e)

    def set_winner(self):
        try:
            sender = self.sender()
            if sender in (self.ui_kataQual.winnerRed, self.ui_kataQual.winnerWhite):
                # toggled приходит и при снятии отметки, в том числе до обновления
                # ФИО новой пары. Такое событие не должно объявлять старого победителя
                # или заново подготавливать его результат для протокола Пятнова.
                if not sender.isChecked():
                    return
                # self.refresh_display_position_clicked('ui_kataQual')
                if sender == self.ui_kataQual.winnerRed:
                    self.ui_kataQual.setWinnerRed()
                elif sender == self.ui_kataQual.winnerWhite:
                    self.ui_kataQual.setWinnerWhite()

                if self.loaded_file_data_type == 'file_pyatnov':
                    aka_name = self.ui_kataQual.label_name_red_1.text()
                    siro_name = self.ui_kataQual.label_name_white_1.text()
                    side = 'siro' if sender == self.ui_kataQual.winnerWhite else 'aka'
                    row_num = siro_name + ' - ' + aka_name
                    row1 = [k for k, v in self.sportsmen_dict['combo_box'].items() if v == row_num][0]
                    row = self.sportsmen_dict['row_num'][row1]
                    col_white, col_red = ["G", "L"]
                    col = col_white if sender == self.ui_kataQual.winnerWhite else col_red
                    cell_coord = f"{col}{row}"
                    self.pyatnov_winner = {'type': 'ui_kataQual', 'side': side, 'cell': cell_coord, 'pfs_name':row_num}

                # --- Оверлей: победитель КАТА по флажкам ---
                try:
                    winner_side = "aka" if sender == self.ui_kataQual.winnerRed else "siro"

                    state = self.build_kata_qual_state()
                    state["winner_side"] = winner_side

                    self.send_overlay_message(state)
                except Exception as e:
                    print("overlay kata_qual winner error:", e)

            elif sender == self.ui_kataFinal.Calc_Button:
                # self.refresh_display_position_clicked('ui_kataFinal')
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
                                           'number_coord': number_coord, 'pfs_name': aka_name}

                # --- Оверлей: после расчёта показываем сумму и считаем это финалом ---
                try:
                    state = self.build_kata_final_state()
                    if state:
                        state["final"] = True  # флаг, что сумма финальная
                        self.send_overlay_message(state)
                except Exception as e:
                    print("overlay kata_final calc error:", e)

            elif sender in [self.ui_kumite.winnerRed, self.ui_kumite.winnerWhite]:
                # self.refresh_display_position_clicked('ui_kumite')
                self.ui_kumite.isShowSportsmanName(resetSportsmanFrame=0)
                self.ui_kumite.setWinner()

                if self.loaded_file_data_type == 'file_pyatnov':
                    if self.flag_pyatnov_kumite_team:
                        name_white = self.ui_kumite.label_name_white_1.text()
                        region_white = self.ui_kumite.label_region_white_1.text()
                        name_red = self.ui_kumite.label_name_red_1.text()
                        region_red = self.ui_kumite.label_region_red_1.text()
                        self.pyatnov_winner = {'type': 'ui_kumite', 'pfs_name': f'{name_white} - {name_red}'}

                        # ВРЕМЕННО!!! Если перебивка, данных в pyatnov_winner нет
                        if self.ui_kumite.pyatnov_perebivka_qbx.isChecked():
                            self.pyatnov_winner = None
                    else:
                        siro_name = self.ui_kumite.label_name_white_1.text()
                        region_white = self.ui_kumite.label_region_white_1.text()
                        aka_name = self.ui_kumite.label_name_red_1.text()
                        region_red = self.ui_kumite.label_region_red_1.text()

                        side = 'siro' if sender == self.ui_kumite.winnerWhite.isChecked() else 'aka'
                        row_num = siro_name + ' - ' + aka_name
                        row1 = [k for k, v in self.sportsmen_dict['combo_box'].items() if v == row_num][0]
                        row = self.sportsmen_dict['row_num'][row1]
                        col_white, col_red = ["G", "L"]
                        col = col_white if sender == self.ui_kumite.winnerWhite.isChecked() else col_red

                        cell_coord = f"{col}{row}"
                        self.pyatnov_winner = {
                            'type': 'ui_kumite', 'side': side, 'cell': cell_coord, 'pfs_name': row_num
                        }


                        # if self.loaded_file_data_type == 'file_pyatnov':
                        #
                        #
                        #
                        #     side = 'siro' if sender == self.ui_kumite.winnerWhite.isChecked() else 'aka'
                        #     row_num = siro_name + ' - ' + aka_name
                        #     row1 = [k for k, v in self.sportsmen_dict['combo_box'].items() if v == row_num][0]
                        #     row = self.sportsmen_dict['row_num'][row1]
                        #     col_white, col_red = ["G", "L"]
                        #     col = col_white if sender == self.ui_kumite.winnerWhite.isChecked() else col_red
                        #
                        #     cell_coord = f"{col}{row}"
                        #     self.pyatnov_winner = {'type': 'ui_kumite', 'side': side, 'cell': cell_coord}




                            # aka_name = self.ui_kataQual.lineEdit_name_red_1.text()
                            # siro_name = self.ui_kataQual.lineEdit_name_white_1.text()
                            # side = 'siro' if sender == self.ui_kataQual.winnerWhite else 'aka'
                            # row_num = siro_name + ' - ' + aka_name
                            # row1 = [k for k, v in self.sportsmen_dict['combo_box'].items() if v == row_num][0]
                            # row = self.sportsmen_dict['row_num'][row1]
                            # col_white, col_red = ["G", "L"]
                            # col = col_white if sender == self.ui_kataQual.winnerWhite else col_red
                            # cell_coord = f"{col}{row}"
                            # self.pyatnov_winner = {'type': 'ui_kataQual', 'side': side, 'cell': cell_coord}

                # --- Оверлей: победитель КУМИТЕ ---
                try:
                    winner_side = "aka" if sender == self.ui_kumite.winnerRed else "siro"
                    # В окне Кумите итоговые ФИО лежат в label_name_*_1
                    # winner_name = (
                    #     self.ui_kumite.label_name_red_1.text()
                    #     if winner_side == "aka"
                    #     else self.ui_kumite.label_name_white_1.text()
                    # )

                    self.build_kumite_state()
                    self.overlay_kumite_state["winner_side"] = winner_side
                    self.send_overlay_message(self.overlay_kumite_state)
                except Exception as e:
                    print("overlay kumite winner error:", e)

        except Exception as e:
            print('_______Exception set_winner:', e)

    def check_to_wopf(self):
        print('___________ check_to_wopf')
        print(self.pyatnov_winner)
        if self.pyatnov_winner is None:
            print('                       self.pyatnov_winner is None')
            return
        # ВРЕМЕННО!!! Если перебивка, в протокол не вносим, потом пофиксится
        if self.ui_kumite.pyatnov_perebivka_qbx.isChecked():
            return
        try:
            # Записываем данные из переменной, обнуляем переменную и делаем проверку по ней, если она не None,
            # то записываем изменение в excel. Нужно добавить сценарий, на случай, если файл занят.



            if threading.active_count() <= 1:
                # Статус сохранения файла
                self.paytnov_save_status(need_to_close=False)
                # if self.flag_pyatnov_kumite_team:
                #     self.paytnov_save_status(need_to_close=False)
                #     # Если кумите команда отображаем заглушку сохранения
                #     # self.ui_kumite.blocked_Form2.hide()
                #     # self.ui_kumite.saving_into_kumite_team_Form2.show()
                #     # self.ui_kumite.img_saving_into_kumite_team.start()

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

            # ВРЕМЕННО!!! Если перебивка, в протокол не вносим, потом пофиксится
            if self.ui_kumite.pyatnov_perebivka_qbx.isChecked():
                return

            excel_file_path = str(self.file)

            print('self.pyatnov_winner', self.pyatnov_winner)
            print('  self.sheet_name_aka_shiro', self.sheet_name_aka_shiro)
            print('    excel_file_path', excel_file_path)

            if self.pyatnov_winner['type'] == 'ui_kataQual':
                try:
                    # wb = load_workbook(excel_file_path)
                    # ws = wb[self.sheet_name_aka_shiro]
                    # ws[self.pyatnov_winner['cell']] = 1
                    #
                    # wb.save(excel_file_path)

                    excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    workbook = excel.Workbooks.Open(excel_file_path)
                    worksheet = workbook.Worksheets(self.sheet_name_aka_shiro)

                    # print('self.pyatnov_winner')
                    # print(self.pyatnov_winner)
                    #
                    worksheet.Range(self.pyatnov_winner['cell']).Value = 1
                    workbook.Save()
                    #
                    #
                    #
                    # # 🔁 Восстанавливаем настройки печати
                    # # restore_page_setup(worksheet, saved_setup)
                    # restore_all_page_setups(workbook, saved_setups)
                    #
                    #
                    workbook.Close()
                    excel.Quit()

                    # ############################## ВТОРОЙ ВАРИАНТ НАЧАЛО #####################
                    #     wb = load_workbook(excel_file_path, keep_vba=True)
                    #     ws = wb["Aka+Shiro"]
                    #     ws[self.pyatnov_winner['cell']] = 1
                    #
                    #     wb.save(excel_file_path)
                    # ############################## ВТОРОЙ ВАРИАНТ ОКОНЧАНИЕ #####################

                    # ############################## ТРЕТИЙ ВАРИАНТ НАЧАЛО #####################
                    # excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    # excel.Visible = False
                    # excel.DisplayAlerts = False  # подавляет предупреждения Excel
                    # workbook = excel.Workbooks.Open(excel_file_path)
                    # # worksheet = workbook.Worksheets("Aka+Shiro")
                    # sheet = workbook.Sheets("Aka+Shiro")
                    # print('111 saved_setups')
                    # saved_setups = backup_all_page_setups(workbook)
                    # sheet.Range(self.pyatnov_winner['cell']).Value = 1
                    #
                    # print('222 restore_all_page_setups')
                    # restore_all_page_setups(workbook, saved_setups)
                    # excel.ActiveWindow.View = 2  # обычный режим (Normal View)
                    # sheet.DisplayPageBreaks = False
                    # excel.Calculation = -4135  # ручной расчёт
                    # excel.DisplayAlerts = False
                    # workbook.Save()
                    # workbook.Close()
                    # excel.Quit()
                    # ############################## ТРЕТИЙ ВАРИАНТ ОКОНЧАНИЕ #####################



                    self.pyatnov_winner = None
                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

            elif self.pyatnov_winner['type'] == 'ui_kataFinal':
                try:
                    excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                    workbook = excel.Workbooks.Open(excel_file_path)
                    worksheet = workbook.Worksheets(self.sheet_name_final)

                    # 🔒 Сохраняем параметры печати
                    # saved_setup = backup_page_setup(worksheet)
                    print('saved_setups 1')
                    saved_setups = backup_all_page_setups(workbook)

                    worksheet.Range(self.pyatnov_winner['cell']).Value = self.pyatnov_winner['score']
                    worksheet.Range(self.pyatnov_winner['number_coord']).Value = self.pyatnov_winner['number']

                    # 🔁 Восстанавливаем настройки печати
                    # restore_page_setup(worksheet, saved_setup)
                    restore_all_page_setups(workbook, saved_setups)

                    workbook.Save()
                    workbook.Close()
                    excel.Quit()

                    self.pyatnov_winner = None
                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

            elif self.pyatnov_winner['type'] == 'ui_kumite':
                print('4 222 ui_kumite')
                try:
                    self.ui_kumite.reset_all()
                    # Кумите-команда
                    if self.flag_pyatnov_kumite_team:

                        # Убираем номер строки и выводим в отдельную переменную
                        self.data_to_write_in_paytnov_referee_protocol, self.cur_men_pair_num = (
                            self.data_to_write_in_paytnov_referee_protocol[:-1],
                            self.data_to_write_in_paytnov_referee_protocol[-1]
                        )

                        # Если self.cur_men_pair_num не указан, получаем его
                        if not self.cur_men_pair_num:
                            self.cur_men_pair_num = self.cur_team_pair()
                        self.cur_men_pair_num = self.cur_men_pair_num[0]

                        print('ЗАПИСЬ В EXCEL на строке:', self.cur_men_pair_num)
                        excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                        workbook = excel.Workbooks.Open(excel_file_path)
                        worksheet = workbook.Worksheets(self.sheet_name_referee)

                        start_row = self.cur_men_pair_num
                        start_col = 4

                        # Записываем данные для siro
                        for row_idx, row in enumerate(self.data_to_write_in_paytnov_referee_protocol, start=start_row):
                            for col_idx, value in enumerate(row, start=start_col):
                                worksheet.Cells(row_idx, col_idx).Value = value
                    else:
                        excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
                        workbook = excel.Workbooks.Open(excel_file_path)
                        worksheet = workbook.Worksheets("Aka+Shiro")

                        # 🔒 Сохраняем параметры печати
                        # saved_setup = backup_page_setup(worksheet)
                        print('saved_setups 3')
                        saved_setups = backup_all_page_setups(workbook)

                        worksheet.Range(self.pyatnov_winner['cell']).Value = 1

                    # 🔁 Восстанавливаем настройки печати
                    # restore_page_setup(worksheet, saved_setup)
                    restore_all_page_setups(workbook, saved_setups)

                    workbook.Save()
                    workbook.Close()
                    excel.Quit()
                    print(' ЗАПИСАНО В EXCEL')

                    self.pyatnov_winner = None

                    # self.paytnov_save_status(flag_save=False, need_to_close=False)

                except AttributeError:
                    os.system("taskkill /f /im excel.exe")
                    print("Excel terminated using taskkill")

            else:
                return

            self.paytnov_save_status(flag_save=False, need_to_close=False)

            result = self.pyatnov_processing(is_kum_team_clear_name=False)

            if self.flag_pyatnov_kata_single or self.flag_pyatnov_kata_team:
                self.worker = Worker(result=result)
                self.worker.finished.connect(self.kata_qual_last_fight)
                self.worker.start()

            else:
                self.worker = Worker(result=result)
                self.worker.start()

        except Exception as e:
            print('_______Exception write_on_pyatov_file:', e)

    def kata_qual_last_fight(self, result):
        # Проверка, нужно ли переключать интерфейс при записи в Excel(например из Ката отб в Ката финал)
        try:
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
                elif sender == self.ui_kumite.j_white4:
                    self.paytnov_reset_hm_j('j', self.dict_paytnov_kumite_winner['siro']['hm_j'], sender.text())
                elif sender == self.ui_kumite.h_red4:
                    self.paytnov_reset_hm_j('hm', self.dict_paytnov_kumite_winner['aka']['hm_j'], sender.text())
                elif sender == self.ui_kumite.j_red4:
                    self.paytnov_reset_hm_j('j', self.dict_paytnov_kumite_winner['aka']['hm_j'], sender.text())
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
        # Обрабатываем данные для записи данных в протокол арбитра
        try:
            # ВРЕМЕННО!!! Если не кумите команда или нажата кнопка "перебивка" в протокол не заносим. Пока временно
            if not  self.flag_pyatnov_kumite_team or self.ui_kumite.pyatnov_perebivka_qbx.isChecked():
                return
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

            self.data_to_write_in_paytnov_referee_protocol = [[], [], []]

            self.data_to_write_in_paytnov_referee_protocol[0].extend(self.dict_paytnov_kumite_winner['siro']['score'])
            self.data_to_write_in_paytnov_referee_protocol[0].append(self.dict_paytnov_kumite_winner['siro']['result'])
            self.data_to_write_in_paytnov_referee_protocol[0].append(self.dict_paytnov_kumite_winner['aka']['result'])
            self.data_to_write_in_paytnov_referee_protocol[0].extend(self.dict_paytnov_kumite_winner['aka']['score'])

            self.data_to_write_in_paytnov_referee_protocol[1].extend(self.dict_paytnov_kumite_winner['siro']['hm_j'])
            self.data_to_write_in_paytnov_referee_protocol[1].append('')
            self.data_to_write_in_paytnov_referee_protocol[1].append('')
            self.data_to_write_in_paytnov_referee_protocol[1].extend(self.dict_paytnov_kumite_winner['aka']['hm_j'])

            self.data_to_write_in_paytnov_referee_protocol[2].append(self.cur_team_pair()[0])

            print(self.data_to_write_in_paytnov_referee_protocol)
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

    def paytnov_save_status(self, flag_save: bool = True, need_to_close: bool = True):
        """Метод управляет надписями статуса сохранения файла Пятнова"""
        try:
            # Определяем в каком окне отображать статус
            karateWidgetWindows = self.ui_kumite
            if self.ui_kataQual is not None and self.ui_kataQual.isVisible():
                karateWidgetWindows = self.ui_kataQual
            elif self.ui_kataFinal is not None and self.ui_kataFinal.isVisible():
                karateWidgetWindows = self.ui_kataFinal


            # karateWidgetWindows = self.ui_kumite
            # if sender == 'ui_kataFinal':
            #     karateWidgetWindows = self.ui_kataFinal
            # elif sender == 'ui_kataQual':
            #     karateWidgetWindows = self.ui_kataQual

            # Текущее время
            now_time = datetime.datetime.now().strftime('%H:%M:%S')

            # ФИО кого сохраняем
            if self.pyatnov_winner and 'pfs_name' in self.pyatnov_winner:
                pfs_name = self.pyatnov_winner['pfs_name']
                karateWidgetWindows.pfss_pair_name.setText(pfs_name)

            # Описание статуса
            if flag_save:
                pfs_status = f'{now_time}: Сохранение в файл...'
                karateWidgetWindows.pfss_pair_name.setStyleSheet("color: black;")
                pfss_pixmap = QtGui.QPixmap(':/Images/pfss_pixmap_save.svg')
            else:
                pfs_status = f'{now_time}: Сохранено'
                karateWidgetWindows.pfss_pair_name.setStyleSheet("color: grey;")
                pfss_pixmap = QtGui.QPixmap(':/Images/pfss_pixmap_done.svg')
            pfss_pixmap2 = pfss_pixmap.scaled(16, 16, QtCore.Qt.KeepAspectRatio)
            karateWidgetWindows.pfss_pixmap_label.setPixmap(pfss_pixmap2)
            karateWidgetWindows.pfss_status.setText(pfs_status)

            # Скрыть/отобразить запись
            if need_to_close:
                karateWidgetWindows.frame_paytnov_file_save_status.hide()
            else:
                karateWidgetWindows.frame_paytnov_file_save_status.show()

        except Exception as e:
            print('_______Exception paytnov_save_status:', e)

    def paytnov_perebivka(self):
        """Функция позволяет создать пару для перебивки Кумите команда"""
        try:
            if self.ui_kumite.btn_start.text() != '► START':
                self.ui_kumite.btn_reset.setText('Заверши бой')
                self.ui_kumite.btn_reset.setStyleSheet("color: red")
                self.ui_kumite.pyatnov_perebivka_qbx.setChecked(False)
                return

            # Если нажали не флажок, а надпись, меняем статус флажка(словно нажали флажок)
            sender = self.sender()

            if sender == self.ui_kumite.pyatnov_perebivka_btn:
                self.ui_kumite.perebivka_select(not self.ui_kumite.pyatnov_perebivka_qbx.isChecked())
            elif sender == self.ui_kumite.pyatnov_perebivka_qbx:
                self.ui_kumite.perebivka_select(self.ui_kumite.pyatnov_perebivka_qbx.isChecked())
            self.ui_kumite.perebivka_select_name(self.ui_kumite.pyatnov_perebivka_qbx.isChecked())

            # Разблокировка интерфейса Кумите
            self.blockedKumiteFrame(False)
        except Exception as e:
            print('_______Exception paytnov_perebivka:', e)

    def open_settings_dialog(self):
        """Режим выбирается явно; сервер никогда не запускается при старте табло."""
        try:
            server_window = getattr(self, 'server_window', None)
            server_mode = server_window is not None and server_window.isVisible()
            dlg = ServerSettingsDialog(parent=server_window if server_mode else self)
            dlg.mode_combo.setCurrentIndex(1 if server_mode else 0)

            # Подставим уже использованный файл/значения, если есть
            if self.server_config_path:
                dlg.set_path(self.server_config_path)
                dlg.set_values(self.server_ip, self.server_port)

            if dlg.exec_() == QtWidgets.QDialog.Accepted:
                if dlg.mode_combo.currentIndex() == 1:
                    if not server_mode:
                        from server_console import ServerWindow
                        if server_window is None:
                            self.server_window = ServerWindow(app_version=self.program_release_number)
                            self.server_window.setWindowIcon(self.windowIcon())
                            self.server_window.mode_requested.connect(self.open_settings_dialog)
                        # Показываем новое окно до скрытия меню: Qt не должен
                        # завершить приложение при исчезновении последнего окна.
                        self.server_window.show()
                        self.hide()
                    return
                if server_mode:
                    server_window.request_table_mode(self.show)
                    return
                path = dlg.get_path()
                if path:
                    self.read_server_config(path)
        except Exception as e:
            print("_______Exception open_settings_dialog:", e)

    def load_server_config_default(self):
        """Ищем usko-server.txt в директории exe (или скрипта, если не собран PyInstaller)."""
        try:
            if getattr(sys, "frozen", False):
                base_dir = os.path.dirname(sys.executable)
            else:
                base_dir = os.path.dirname(os.path.abspath(__file__))

            candidate = os.path.join(base_dir, "usko-server.txt")
            if os.path.exists(candidate):
                self.read_server_config(candidate)
            else:
                self.has_server_info = False

                # Для удобства — подсказка в статусе
                self.overlay_status_frame(
                    txt=f"default: usko-server.txt не найден в {base_dir}",
                    tool_tip="",
                    is_online='no_data'
                )

        except Exception as e:
            print("_______Exception load_server_config_default:", e)

    def read_server_config(self, path: str):
        """Читаем SERVER_IP и SERVER_PORT из текстового файла."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            tatami_match = re.search(r'TATAMI_ID\s*=\s*(\d+)', text)
            ip_match = re.search(r'SERVER_IP\s*=\s*["\']([^"\']+)["\']', text)
            port_match = re.search(r'SERVER_PORT\s*=\s*(\d+)', text)

            if not ip_match or not port_match:
                raise ValueError("Файл не содержит корректные SERVER_IP и SERVER_PORT")

            self.server_ip = ip_match.group(1)
            self.server_port = int(port_match.group(1))
            self.server_config_path = path

            # --- TATAMI_ID ---
            if tatami_match:
                self.USKO_PC = int(tatami_match.group(1))
                css.USKO_PC = self.USKO_PC

            self.has_server_info = True

            # Для удобства — подсказка в статусе
            self.overlay_status_frame(
                txt=f"Сервер трансляции: {self.server_ip}:{self.server_port} | Татами {self.USKO_PC}",
                tool_tip=(
                    f"Сервер трансляции: {self.server_ip}:{self.server_port}\n"
                    f"Татами: {self.USKO_PC}\n"
                    f"Файл: {self.server_config_path}"
                ),
                is_online = 'offline'
            )

        except Exception as e:
            print("_______Exception read_server_config:", e)
            self.has_server_info = False
            self.overlay_status_frame(
                txt=f"Exception read_server_config: {e}",
                tool_tip="",
                is_online='no_data'
            )

    def overlay_health_ok(self, set_timeout=0.2) -> bool:
        """
        Проверяет, что сервер оверлея доступен и отвечает 200.
        НИЧЕГО не собирает, никаких payload.
        """
        if not self.server_ip or not self.server_port:
            return False

        url = f"http://{self.server_ip}:{self.server_port}/health"

        try:
            r = requests.get(url, timeout=set_timeout)
            self.is_overlay_connected = True
            return r.status_code == 200
        except Exception as e:
            self.is_overlay_connected = False
            self.overlay_status_frame(
                txt=f"WS: overlay health-check failed: {e}",
                tool_tip=f"WS: overlay health-check failed: {e}",
                is_online='offline'
            )
            return False

    def send_overlay_idle(self):
        if not self.has_server_info: return ''
        """Сбрасываем оверлей: нет активного боя (меню/закрытие)."""
        try:
            tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
        except Exception:
            tatami = f"Татами №{getattr(self, 'USKO_PC', '#')}"

        payload = {
            "mode": "idle",
            "discipline": "",
            "tatami": tatami,
            "category": "",
        }
        self.send_overlay_message(payload)

        # Хелперы для сбора инфы для оверлея ОБС

    def update_kumite_overlay(self):
        if not self.has_server_info: return ''
        try:
            self.build_kumite_state()
            self.send_overlay_message(self.overlay_kumite_state)
        except Exception as e:
            print("update_kumite_overlay error:", e)

    def update_kata_qual_overlay(self):
        if not self.has_server_info: return ''
        try:
            state = self.build_kata_qual_state()
            if state:
                self.send_overlay_message(state)
        except Exception as e:
            print("update_kata_qual_overlay error:", e)

    def update_kata_final_overlay(self, final: bool = False):
        if not self.has_server_info: return ''
        try:
            state = self.build_kata_final_state()
            if state:
                state["final"] = final
                self.send_overlay_message(state)
        except Exception as e:
            print("update_kata_final_overlay error:", e)

    def send_overlay_message(self, payload: dict, is_tick=False):
        if not self.has_server_info:
            return ''

        if not self.server_ip or not self.server_port:
            self.has_server_info = False
            self.overlay_status_frame(
                txt="WS: сервер не настроен (server_ip / server_port пустые)",
                tool_tip="",
                is_online="no_data"
            )
            return ''

        url = f"http://{self.server_ip}:{self.server_port}/api/state"

        self.overlay_seq += 1

        full_payload = {
            "tatami_id": self.USKO_PC,
            "overlay_seq": self.overlay_seq,
            **payload,
        }


        threading.Thread(
            target=self._post_overlay_async,
            args=(url, full_payload, is_tick),
            daemon=True
        ).start()

    # Оверлей - кумите. функцию, которая вернёт только то, что реально меняется во время боя
    # (таймер, счёт, штрафы, категория/татами
    
    def reset_kumite_overlay_state(self):
        self.overlay_kumite_state = {
            "mode": "",
            "discipline": "",
            "tatami": "",
            "category": "",
            "timer": "",
            "aka": {
                "name": "",
                "region": "",
                "region_logo_url": "",
                "score": "",
                "penalties": {
                    "hm": "",  # H/M КРАСНОГО
                    "j": "",   # J КРАСНОГО
                },
            },
            "siro": {
                "name": "",
                "region": "",
                "region_logo_url": "",
                "score": "",
                "penalties": {
                    "hm": "",  # H/M БЕЛОГО
                    "j": "",   # J БЕЛОГО
                },
            },
        }

    def build_kumite_dynamic_state(self, is_tick=False):
        if not self.has_server_info: return {}

        sender = self.sender()
        sender_name = sender.objectName() if sender else ""

        """
        ЛЁГКОЕ состояние боя Кумите для частичных обновлений:
        - таймер
        - счёт
        - штрафы
        - категория/татами
         ОБНОВЛЯЕМ в self.overlay_kumite_state ТОЛЬКО ТО ЧТО ПРИСЛАЛ СЕНДЕР
        """
        try:
            # # Название татами и категории
            # tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
            # category = f'{self.ui_kumite.matchName11.text()}, {self.ui_kumite.matchName12.text()}'

            # --- Таймер ---
            if not sender_name or sender_name in ('minus2sec', 'plus2sec'):
                timer_obj = None
                try:
                    tics = getattr(self.ui_kumite, "tics", None)
                    if tics is not None:
                        mm = tics.minute
                        ss = tics.second
                        remaining_sec = mm * 60 + ss

                        kum_timer = getattr(self.ui_kumite, "timer", None)
                        is_running = bool(kum_timer and kum_timer.isActive())

                        timer_obj = {
                            "remaining_sec": remaining_sec,
                            "status": "running" if is_running else "stopped",
                        }
                except Exception:
                    timer_obj = None
                self.overlay_kumite_state['timer'] = timer_obj

            # --- Очки - СИРО ---
            if 'score_white_' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                if sec is not None:
                    siro_score = sec.label_score22.text()
                else:
                    siro_label = getattr(self.ui_kumite, "label_score12", None)
                    siro_score = siro_label.text() if siro_label else ""
                self.overlay_kumite_state['siro']['score'] = siro_score
            # --- Очки - АКА ---
            if 'score_red_' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                if sec is not None:
                    aka_score = sec.label_score21.text()
                else:
                    aka_label = getattr(self.ui_kumite, "label_score11", None)
                    aka_score = aka_label.text() if aka_label else ""
                self.overlay_kumite_state['aka']['score'] = aka_score


            # --- Штрафы - СИРО ---
            if 'h_white' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                hm = sec.label_kum_hmw0.text() or ""
                self.overlay_kumite_state['siro']['penalties']['hm'] = hm
            if 'j_white' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                j = sec.label_kum_jw0.text() or ""
                self.overlay_kumite_state['siro']['penalties']['j'] = j
            # --- Штрафы - АКА ---
            if 'h_red' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                hm = sec.label_kum_hmr0.text() or ""
                self.overlay_kumite_state['aka']['penalties']['hm'] = hm
            if 'j_red' in sender_name:
                sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
                j = sec.label_kum_jr0.text() or ""
                self.overlay_kumite_state['aka']['penalties']['j'] = j


            # --- Штрафы ---
            # hmr = jr = hmw = jw = ""
            # if sec is not None:
            #     hmr = sec.label_kum_hmr0.text() or ""
            #     jr = sec.label_kum_jr0.text() or ""
            #     hmw = sec.label_kum_hmw0.text() or ""
            #     jw = sec.label_kum_jw0.text() or ""
            
            # # --- Очки ---
            # sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
            # if sec is not None:
            #     aka_score = sec.label_score21.text()
            #     siro_score = sec.label_score22.text()
            # else:
            #     aka_label = getattr(self.ui_kumite, "label_score11", None)
            #     siro_label = getattr(self.ui_kumite, "label_score12", None)
            #     aka_score = aka_label.text() if aka_label else ""
            #     siro_score = siro_label.text() if siro_label else ""

            # # --- Штрафы ---
            # hmr = jr = hmw = jw = ""
            # if sec is not None:
            #     hmr = sec.label_kum_hmr0.text() or ""
            #     jr = sec.label_kum_jr0.text() or ""
            #     hmw = sec.label_kum_hmw0.text() or ""
            #     jw = sec.label_kum_jw0.text() or ""

            # state = {
            #     "mode": "kumite",
            #     "discipline": "КУМИТЕ",
            #     "tatami": tatami,
            #     "category": category,
            #     "timer": timer_obj,
            #     "aka": {
            #         "score": aka_score,
            #         "penalties": {
            #             "hm": hmr,
            #             "j": jr,
            #         },
            #     },
            #     "siro": {
            #         "score": siro_score,
            #         "penalties": {
            #             "hm": hmw,
            #             "j": jw,
            #         },
            #     },
            # }
            # return state
        except Exception as e:
            print("build_kumite_dynamic_state error:", e)
            # return {}

    def tick_update_kumite_dynamic_overlay(self):
        if not self.has_server_info: return ''
        # self.build_kumite_dynamic_state(is_tick=True)
        self.overlay_kumite_state['mode'] = 'kumite'
        self.overlay_kumite_state['discipline'] = 'КУМИТЕ'
        return self.update_kumite_dynamic_overlay(is_tick=True)

    def kumite_toggled_hmj_overlay(self):
        # 1) игнорируем любые переключения, пока идёт reset
        if self._overlay_suppress:
            return

        if self.sender().isChecked():
            self.build_kumite_dynamic_state()
            self.overlay_kumite_state['mode'] = 'kumite'
            self.overlay_kumite_state['discipline'] = 'КУМИТЕ'
            self.send_overlay_message(self.overlay_kumite_state)
            # self.update_kumite_dynamic_overlay()

    def update_kumite_dynamic_overlay(self, is_tick=False, clear_winner=True):
        if not self.has_server_info: return ''
        """
        Отправляет облегчённое (partial) состояние Кумите:
        без ФИО/региона/флагов, только то, что обычно меняется в бою.
        """
        try:
            self.build_kumite_dynamic_state(is_tick=is_tick)
            if clear_winner:
                self.overlay_kumite_state.pop("winner_side", None)
            self.send_overlay_message(self.overlay_kumite_state, is_tick=is_tick)
        except Exception as e:
            print("update_kumite_dynamic_overlay error:", e)

    def build_kumite_state(self):
        """ 
        Собираем текущее состояние боя Кумите для оверлея.
        """
        if not self.has_server_info: return 0
        try:
            # Название татами и категории
            tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
            category = f'{self.ui_kumite.matchName11.text()}, {self.ui_kumite.matchName12.text()}'

            # --- Таймер ---
            timer_obj = None
            try:
                tics = getattr(self.ui_kumite, "tics", None)
                if tics is not None:
                    # tics — это datetime, сохраняем оставшееся время в секундах
                    mm = tics.minute
                    ss = tics.second
                    remaining_sec = mm * 60 + ss

                    kum_timer = getattr(self.ui_kumite, "timer", None)
                    is_running = bool(kum_timer and kum_timer.isActive())

                    timer_obj = {
                        "remaining_sec": remaining_sec,
                        "status": "running" if is_running else "stopped",
                    }
            except Exception:
                timer_obj = None

            # --- Очки ---
            # Счёт во второй форме (той, что на большом экране), там же, где его видят зрители
            sec = getattr(self.ui_kumite, "KumiteSecondWindow", None)
            if sec is not None:
                aka_score = sec.label_score21.text()
                siro_score = sec.label_score22.text()
            else:
                # запасной вариант — из судейского окна
                aka_label = getattr(self.ui_kumite, "label_score11", None)
                siro_label = getattr(self.ui_kumite, "label_score12", None)
                aka_score = aka_label.text() if aka_label else ""
                siro_score = siro_label.text() if siro_label else ""

            # --- Имя / регион ---
            # Берём именно данные, уже показанные на табло, а не текущий выбор в выпадающих списках
            aka_name = self.ui_kumite.label_name_red_1.text()
            aka_region = self.ui_kumite.label_region_red_1.text()

            siro_name = self.ui_kumite.label_name_white_1.text()
            siro_region = self.ui_kumite.label_region_white_1.text()

            # --- Штрафы ---
            hmr = jr = hmw = jw = ""
            if sec is not None:
                hmr = sec.label_kum_hmr0.text() or ""
                jr = sec.label_kum_jr0.text() or ""
                hmw = sec.label_kum_hmw0.text() or ""
                jw = sec.label_kum_jw0.text() or ""

            self.overlay_kumite_state = {
                "mode": "kumite",
                "discipline": "КУМИТЕ",
                "tatami": tatami,
                "category": category,
                "timer": timer_obj,
                "aka": {
                    "name": aka_name,
                    "region": aka_region,
                    "region_logo_url": self.svg_resource_to_data_url(aka_region),
                    "score": aka_score,
                    "penalties": {
                        "hm": hmr,  # H/M КРАСНОГО
                        "j": jr,  # J КРАСНОГО
                    },
                },
                "siro": {
                    "name": siro_name,
                    "region": siro_region,
                    "region_logo_url": self.svg_resource_to_data_url(siro_region),
                    "score": siro_score,
                    "penalties": {
                        "hm": hmw,  # H/M БЕЛОГО
                        "j": jw,  # J БЕЛОГО
                    },
                },
            }

        except Exception as e:
            print("build_kumite_state error:", e)
            self.reset_kumite_overlay_state()

    def build_kata_qual_state(self) -> dict:
        if not self.has_server_info:
            return {}

        try:
            tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
            category = self.ui_kataQual.matchName1.text()

            aka_region = self.ui_kataQual.label_region_red_1.text()
            siro_region = self.ui_kataQual.label_region_white_1.text()

            return {
                "mode": "kata_qual",
                "discipline": "КАТА",
                "tatami": tatami,
                "category": category,
                "aka": {
                    "name": self.ui_kataQual.label_name_red_1.text(),
                    "region": aka_region,
                    "region_logo_url": self.svg_resource_to_data_url(aka_region),
                },
                "siro": {
                    "name": self.ui_kataQual.label_name_white_1.text(),
                    "region": siro_region,
                    "region_logo_url": self.svg_resource_to_data_url(siro_region),
                },
            }

        except Exception as e:
            print("build_kata_qual_state error:", e)
            return {}

    def build_kata_final_scores_state(self) -> dict:
        if not self.has_server_info: return {}
        """
        Облегчённое состояние Ката финал:
        только вид, категория, оценки судей и сумма — без ФИО/флагов.
        """
        try:
            tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
            category = self.ui_kataFinal.matchName1.text()

            ref1 = self.ui_kataFinal.lineEdit_referee1.text()
            ref2 = self.ui_kataFinal.lineEdit_referee2.text()
            ref3 = self.ui_kataFinal.lineEdit_referee3.text()
            ref4 = self.ui_kataFinal.lineEdit_referee4.text()
            ref5 = self.ui_kataFinal.lineEdit_referee5.text()
            ref6 = self.ui_kataFinal.lineEdit_referee6.text()
            ref7 = self.ui_kataFinal.lineEdit_referee7.text()

            # убираем одиночную точку
            ref1 = ref1 if ref1 != '.' else ''
            ref2 = ref2 if ref2 != '.' else ''
            ref3 = ref3 if ref3 != '.' else ''
            ref4 = ref4 if ref4 != '.' else ''
            ref5 = ref5 if ref5 != '.' else ''
            ref6 = ref6 if ref6 != '.' else ''
            ref7 = ref7 if ref7 != '.' else ''

            scores = {
                "ref1": ref1,
                "ref2": ref2,
                "ref3": ref3,
                "ref4": ref4,
                "ref5": ref5,
                "ref6": ref6,
                "ref7": ref7,
            }

            sum_text = self.ui_kataFinal.label_sum.text()

            try:
                float(sum_text)
            except ValueError:
                sum_text = "0.0"

            return {
                "mode": "kata_final",
                "discipline": "КАТА",
                "tatami": tatami,
                "category": category,
                "scores": scores,
                "sum": sum_text,
            }
        except Exception as e:
            print("build_kata_final_scores_state error:", e)
            return {}

    def on_kata_final_scores_changed(self, *_):
        if not self.has_server_info: return ''
        """Каждый раз, когда судья меняет оценку в ката финал — обновляем оверлей."""
        try:
            state = self.build_kata_final_scores_state()
            if state:
                state["final"] = False  # ещё не финальная сумма
                state["partial"] = True  # это патч, а не полный state
                self.send_overlay_message(state)
        except Exception as e:
            print("overlay error in on_kata_final_scores_changed:", e)

    def build_kata_final_state(self) -> dict:
        if not self.has_server_info: return {}
        """
        Состояние окна Ката финал для оверлея:
        - вид соревнований
        - категория / татами
        - ФИО и регион
        - оценки судей
        - сумма (если уже посчитана)
        """
        try:
            tatami = self.tatamiName or f"Татами №{self.USKO_PC}"
            category = self.ui_kataFinal.matchName1.text()

            # ФИО/регион спортсмена
            aka_name = self.ui_kataFinal.label_name_red_1.text()
            aka_region = self.ui_kataFinal.label_region_red_1.text()

            # Оценки судей (как строки, чтобы не ловить формат)
            ref1 = self.ui_kataFinal.lineEdit_referee1.text()
            ref2 = self.ui_kataFinal.lineEdit_referee2.text()
            ref3 = self.ui_kataFinal.lineEdit_referee3.text()
            ref4 = self.ui_kataFinal.lineEdit_referee4.text()
            ref5 = self.ui_kataFinal.lineEdit_referee5.text()
            ref6 = self.ui_kataFinal.lineEdit_referee6.text()
            ref7 = self.ui_kataFinal.lineEdit_referee7.text()
            ref1 = ref1 if ref1 != '.' else ''
            ref2 = ref2 if ref2 != '.' else ''
            ref3 = ref3 if ref3 != '.' else ''
            ref4 = ref4 if ref4 != '.' else ''
            ref5 = ref5 if ref5 != '.' else ''
            ref6 = ref6 if ref6 != '.' else ''
            ref7 = ref7 if ref7 != '.' else ''
            scores = {
                "ref1": ref1,
                "ref2": ref2,
                "ref3": ref3,
                "ref4": ref4,
                "ref5": ref5,
                "ref6": ref6,
                "ref7": ref7,
            }

            # Сумма — то, что сейчас написано в label_sum
            sum_text = self.ui_kataFinal.label_sum.text()

            try:
                float(sum_text)  # Попытка преобразовать в число с плавающей точкой
            except ValueError:
                sum_text = '0.0'

            state = {
                "mode": "kata_final",
                "discipline": "КАТА",
                "tatami": tatami,
                "category": category,
                "aka": {
                    "name": aka_name,
                    "region": aka_region,
                    "region_logo_url": self.svg_resource_to_data_url(aka_region),
                },
                "scores": scores,
                "sum": sum_text,
            }
            return state
        except Exception as e:
            print("build_kata_final_state error:", e)
            return {}

        # Для передачи флага в оверлей

    def svg_resource_to_data_url(self, region_code: str, size: int = 128) -> str:

        region_code = region_code.split(' - ком')[0].replace(" ", "").lower()
        code = self.flags_dict.get(region_code)
        # Отправляем только название файла, а на фронте картинку подставляем
        return f"{code}.svg" if code else ''
        if not code:
            return ""

        resource_path = f":/Images/icon_regions/flags/{code}.svg"

        f = QtCore.QFile(resource_path)
        if not f.open(QtCore.QIODevice.ReadOnly):
            print("Не удалось открыть ресурс:", resource_path)
            return ""

        svg_bytes = bytes(f.readAll())
        f.close()

        renderer = QSvgRenderer(svg_bytes)
        if not renderer.isValid():
            print("SVG невалиден:", resource_path)
            return ""

        image = QtGui.QImage(size, size, QtGui.QImage.Format_ARGB32)
        image.fill(QtCore.Qt.transparent)

        painter = QtGui.QPainter(image)
        renderer.render(painter)
        painter.end()

        ba = QtCore.QByteArray()
        buf = QtCore.QBuffer(ba)
        buf.open(QtCore.QIODevice.WriteOnly)
        image.save(buf, "PNG")
        buf.close()

        b64 = base64.b64encode(bytes(ba)).decode("ascii")
        return f"data:image/png;base64,{b64}"

    def sportsmans_load_status_frame(self, is_loaded : bool = True):
        """Обновляем иконку статуса загрузки Excel списка спортсменов"""
        try:
            if is_loaded:
                self.frame_sportsmans_load_status.setToolTip('Список спортсменов подгружен')
                self.ui_kataQual.frame_sportsmans_load_status.setToolTip('Список спортсменов подгружен')
                self.ui_kataFinal.frame_sportsmans_load_status.setToolTip('Список спортсменов подгружен')
                self.ui_kumite.frame_sportsmans_load_status.setToolTip('Список спортсменов подгружен')

                self.label_img_sportsmans_not_loaded.hide()
                self.label_img_spotrsmans_uploaded.show()
                self.ui_kataQual.label_img_sportsmans_not_loaded.hide()
                self.ui_kataQual.label_img_spotrsmans_uploaded.show()
                self.ui_kataFinal.label_img_sportsmans_not_loaded.hide()
                self.ui_kataFinal.label_img_spotrsmans_uploaded.show()
                self.ui_kumite.label_img_sportsmans_not_loaded.hide()
                self.ui_kumite.label_img_spotrsmans_uploaded.show()
            else:
                self.frame_sportsmans_load_status.setToolTip('Список спортсменов НЕ подгружен')
                self.ui_kataQual.frame_sportsmans_load_status.setToolTip('Список спортсменов НЕ подгружен')
                self.ui_kataFinal.frame_sportsmans_load_status.setToolTip('Список спортсменов НЕ подгружен')
                self.ui_kumite.frame_sportsmans_load_status.setToolTip('Список спортсменов НЕ подгружен')

                self.label_img_sportsmans_not_loaded.show()
                self.label_img_spotrsmans_uploaded.hide()
                self.ui_kataQual.label_img_sportsmans_not_loaded.show()
                self.ui_kataQual.label_img_spotrsmans_uploaded.hide()
                self.ui_kataFinal.label_img_sportsmans_not_loaded.show()
                self.ui_kataFinal.label_img_spotrsmans_uploaded.hide()
                self.ui_kumite.label_img_sportsmans_not_loaded.show()
                self.ui_kumite.label_img_spotrsmans_uploaded.hide()

        except Exception as e:
            print("_______sportsmans_load_status_frame:", e)
            self.has_server_info = False

    def overlay_status_frame(self, txt: str = '', tool_tip: str = '', is_online : str = 'online'):
        """Обновляем статус соединение с оверлеем"""
        try:

            self.overlay_status_label.setText(txt)
            self.frame_overlay_status.setToolTip(tool_tip)
            self.ui_kataQual.frame_overlay_status.setToolTip(tool_tip)
            self.ui_kataFinal.frame_overlay_status.setToolTip(tool_tip)
            self.ui_kumite.frame_overlay_status.setToolTip(tool_tip)

            if is_online == 'online':
                self.label_img_overlay_offline.hide()
                self.label_img_overlay_online.show()
                self.label_img_overlay_no_data.hide()
                self.ui_kataQual.label_img_overlay_offline.hide()
                self.ui_kataQual.label_img_overlay_online.show()
                self.ui_kataQual.label_img_overlay_no_data.hide()
                self.ui_kataFinal.label_img_overlay_offline.hide()
                self.ui_kataFinal.label_img_overlay_online.show()
                self.ui_kataFinal.label_img_overlay_no_data.hide()
                self.ui_kumite.label_img_overlay_offline.hide()
                self.ui_kumite.label_img_overlay_online.show()
                self.ui_kumite.label_img_overlay_no_data.hide()
            elif is_online == 'offline':
                self.label_img_overlay_offline.show()
                self.label_img_overlay_online.hide()
                self.label_img_overlay_no_data.hide()
                self.ui_kataQual.label_img_overlay_offline.show()
                self.ui_kataQual.label_img_overlay_online.hide()
                self.ui_kataQual.label_img_overlay_no_data.hide()
                self.ui_kataFinal.label_img_overlay_offline.show()
                self.ui_kataFinal.label_img_overlay_online.hide()
                self.ui_kataFinal.label_img_overlay_no_data.hide()
                self.ui_kumite.label_img_overlay_offline.show()
                self.ui_kumite.label_img_overlay_online.hide()
                self.ui_kumite.label_img_overlay_no_data.hide()
            elif is_online == 'no_data':
                self.label_img_overlay_offline.hide()
                self.label_img_overlay_online.hide()
                self.label_img_overlay_no_data.show()
                self.ui_kataQual.label_img_overlay_offline.hide()
                self.ui_kataQual.label_img_overlay_online.hide()
                self.ui_kataQual.label_img_overlay_no_data.show()
                self.ui_kataFinal.label_img_overlay_offline.hide()
                self.ui_kataFinal.label_img_overlay_online.hide()
                self.ui_kataFinal.label_img_overlay_no_data.show()
                self.ui_kumite.label_img_overlay_offline.hide()
                self.ui_kumite.label_img_overlay_online.hide()
                self.ui_kumite.label_img_overlay_no_data.show()

        except Exception as e:
            print("_______overlay_status_frame:", e)
            self.has_server_info = False


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


class ServerSettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.font_l_12 = css.font_l_12
        self.font_l_15 = css.font_l_15
        self.btn_style_1 = css.btn_style_1

        self.setObjectName("ServerSettingsDialog")
        self.setFont(css.font_l_15)
        self.setModal(True)
        self.setWindowTitle("Настройки USKO Tab")
        self.setFixedSize(500, 260)
        self.setStyleSheet("background-color: white;")

        # Заголовок
        self.label = QtWidgets.QLabel("Файл настроек сервера (usko-server.txt):", self)
        self.label.setGeometry(QtCore.QRect(20, 15, 460, 20))
        self.label.setFont(self.font_l_15)

        # Поле пути к файлу + кнопка обзора
        self.edt_path = QtWidgets.QLineEdit(self)
        self.edt_path.setGeometry(QtCore.QRect(20, 45, 380, 24))
        self.edt_path.setFont(self.font_l_12)
        self.edt_path.setStyleSheet(css.combo_style_2)

        self.btn_browse = QtWidgets.QPushButton("...", self)
        self.btn_browse.setGeometry(QtCore.QRect(410, 45, 60, 24))
        self.btn_browse.setStyleSheet(self.btn_style_1)
        self.btn_browse.setFont(self.font_l_15)

        # Отображение найденных значений IP/PORT
        self.label_ip = QtWidgets.QLabel("SERVER_IP:", self)
        self.label_ip.setGeometry(QtCore.QRect(20, 85, 90, 20))
        self.label_ip.setFont(self.font_l_12)

        self.edit_ip = QtWidgets.QLineEdit(self)
        self.edit_ip.setGeometry(QtCore.QRect(110, 85, 140, 22))
        self.edit_ip.setFont(self.font_l_12)
        self.edit_ip.setStyleSheet(css.combo_style_2)
        self.edit_ip.setReadOnly(True)

        self.label_port = QtWidgets.QLabel("SERVER_PORT:", self)
        self.label_port.setGeometry(QtCore.QRect(260, 85, 100, 20))
        self.label_port.setFont(self.font_l_12)

        self.edit_port = QtWidgets.QLineEdit(self)
        self.edit_port.setGeometry(QtCore.QRect(360, 85, 80, 22))
        self.edit_port.setFont(self.font_l_12)
        self.edit_port.setStyleSheet(css.combo_style_2)
        self.edit_port.setReadOnly(True)

        # Кнопки OK / Отмена
        self.btn_ok = QtWidgets.QPushButton("OK", self)
        self.btn_ok.setGeometry(QtCore.QRect(190, 125, 100, 32))
        self.btn_ok.setStyleSheet(self.btn_style_1)
        self.btn_ok.setFont(self.font_l_15)

        self.btn_cancel = QtWidgets.QPushButton("Отмена", self)
        self.btn_cancel.setGeometry(QtCore.QRect(300, 125, 100, 32))
        self.btn_cancel.setStyleSheet(self.btn_style_1)
        self.btn_cancel.setFont(self.font_l_15)

        # Сигналы
        self.btn_browse.clicked.connect(self.on_browse)
        self.btn_ok.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)

        # Существующие настройки относятся только к клиенту-табло.
        # Переключатель режима отделён от файла адреса удалённого сервера.
        connection_widgets = [self.label, self.edt_path, self.btn_browse,
                              self.label_ip, self.edit_ip, self.label_port, self.edit_port]
        for widget in connection_widgets + [self.btn_ok, self.btn_cancel]:
            widget.move(widget.x(), widget.y() + 80)
        mode_label = QtWidgets.QLabel("Режим работы:", self)
        mode_label.setGeometry(20, 15, 150, 24)
        mode_label.setFont(css.font_l_15)
        self.mode_combo = QtWidgets.QComboBox(self)
        self.mode_combo.setGeometry(180, 15, 290, 26)
        self.mode_combo.setFont(css.font_l_15)
        self.mode_combo.setStyleSheet(css.combo_style_2)
        self.mode_combo.addItems(["Табло", "Сервер трансляции"])
        hint = QtWidgets.QLabel("Для одновременной работы откройте вторую копию программы.", self)
        hint.setGeometry(20, 50, 460, 25)
        hint.setWordWrap(True)
        hint.setFont(css.font_l_12)
        self.mode_combo.currentIndexChanged.connect(
            lambda index: [widget.setEnabled(index == 0) for widget in connection_widgets])

    def on_browse(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл usko-server.txt",
            "./",
            "Text files (*.txt);;All files (*.*)"
        )
        if path:
            self.edt_path.setText(path)
            # Попробуем заранее достать IP/PORT для отображения
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                ip_match = re.search(r'SERVER_IP\s*=\s*["\']([^"\']+)["\']', text)
                port_match = re.search(r'SERVER_PORT\s*=\s*(\d+)', text)
                self.edit_ip.setText(ip_match.group(1) if ip_match else "")
                self.edit_port.setText(port_match.group(1) if port_match else "")
            except Exception as e:
                print("Exception preview server config:", e)

    def get_path(self) -> str:
        return self.edt_path.text().strip()

    def set_path(self, path: str):
        self.edt_path.setText(path)

    def set_values(self, ip: str, port):
        if ip:
            self.edit_ip.setText(str(ip))
        if port:
            self.edit_port.setText(str(port))


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
