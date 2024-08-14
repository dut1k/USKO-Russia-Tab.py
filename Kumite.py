from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider, QHBoxLayout
from PyQt5.QtMultimedia import QSound
from datetime import datetime, timedelta
import styleCSS as css


class RoundedLabel(QtWidgets.QLabel):
    """Класс для создания круглых иконок флагов регионов"""
    def __init__(self, parent=None):
        super(RoundedLabel, self).__init__(parent)
        self.setScaledContents(True)

    def setPixmap(self, pixmap):
        # Create a rounded mask
        mask = QtGui.QPixmap(pixmap.size())
        mask.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        clip_path = QtGui.QPainterPath()
        clip_path.addRoundedRect(QtCore.QRectF(mask.rect()), 40, 40)
        painter.setClipPath(clip_path)
        painter.drawPixmap(0, 0, pixmap)

        painter.end()

        super(RoundedLabel, self).setPixmap(mask)


class KumiteSWindow_Ui(object):
    def __init__(self):
        self.font_b_60 = css.font_b_60
        self.font_m_60 = css.font_m_60
        self.font_m_100 = css.font_m_100
        self.font_m_530 = css.font_m_530
        self.font_l_150 = css.font_l_150
        self.font_l_190 = css.font_l_190
        self.font_b_250 = css.font_b_250

        self.coo_frame_red2_std = QtCore.QRect(40, 200, 880, 800)
        self.coo_frame_white2_std = QtCore.QRect(1000, 200, 880, 800)
        self.coo_frame_win = QtCore.QRect(40, 220, 1840, 800)
        self.coo_screen_std = QtCore.QRect(0, 120, 1920, 900)
        self.coo_screen_red_std = QtCore.QRect(40, 0, 1840, 400)
        self.coo_screen_white_std = QtCore.QRect(40, 450, 1840, 400)
        self.coo_screen_win = QtCore.QRect(40, 150, 1840, 400)
        self.coo_screen_frm_win = QtCore.QRect(0, 0, 1840, 400)
        self.coo_label_name_red = QtCore.QRect(0, 0, 900, 80)
        self.coo_label_name_white = QtCore.QRect(940, 0, 900, 80)
        self.coo_label_name_red_flag = QtCore.QRect(80, 0, 820, 80)
        self.coo_label_name_white_flag = QtCore.QRect(940, 0, 820, 80)

    def setupUi2(self, Form):
        Form.setObjectName("Form22")
        Form.setEnabled(True)
        Form.setFixedSize(1920, 1080)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color: white;")
        Form.setWindowIcon(QtGui.QIcon(':/Images/Empty.png'))

        self.matchName21 = QtWidgets.QLabel(Form)
        # self.matchName22 = QtWidgets.QLabel(Form)
        self.lcd2 = QtWidgets.QLCDNumber(Form)
        # self.line2 = QtWidgets.QFrame(Form)

        self.frame_sportsman = QtWidgets.QFrame(Form)
        self.label_name_white_2 = QtWidgets.QLabel(self.frame_sportsman)
        self.label_name_red_2 = QtWidgets.QLabel(self.frame_sportsman)

        self.frame_red2 = QtWidgets.QFrame(Form)
        self.label_score21 = QtWidgets.QLabel(self.frame_red2)
        self.background_red21 = QtWidgets.QFrame(self.frame_red2)
        self.frame_background_red22_red2 = QtWidgets.QFrame(self.frame_red2)
        self.background_red22 = QtWidgets.QFrame(self.frame_background_red22_red2)

        self.frame_hm_red = QtWidgets.QFrame(self.frame_background_red22_red2)
        self.label_kum_hmr0 = QtWidgets.QLabel(self.frame_hm_red)
        self.label_kum_hmr1 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r1 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r2 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r3 = QtWidgets.QLabel(self.frame_hm_red)

        self.frame_j_red = QtWidgets.QFrame(self.frame_background_red22_red2)
        self.label_kum_jr0 = QtWidgets.QLabel(self.frame_j_red)
        self.label_kum_jr1 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r1 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r2 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r3 = QtWidgets.QLabel(self.frame_j_red)

        self.frame_white2 = QtWidgets.QFrame(Form)
        self.label_score22 = QtWidgets.QLabel(self.frame_white2)
        self.background_white21 = QtWidgets.QFrame(self.frame_white2)
        self.frame_background_white22_white2 = QtWidgets.QFrame(self.frame_white2)
        self.background_white22 = QtWidgets.QFrame(self.frame_background_white22_white2)

        self.frame_hm_white = QtWidgets.QFrame(self.frame_background_white22_white2)
        self.label_kum_hmw0 = QtWidgets.QLabel(self.frame_hm_white)
        self.label_kum_hmw1 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w1 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w2 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w3 = QtWidgets.QLabel(self.frame_hm_white)

        self.frame_j_white = QtWidgets.QFrame(self.frame_background_white22_white2)
        self.label_kum_jw0 = QtWidgets.QLabel(self.frame_j_white)
        self.label_kum_jw1 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w1 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w2 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w3 = QtWidgets.QLabel(self.frame_j_white)

        self.matchName21.setGeometry(QtCore.QRect(20, 10, 1880, 100))
        self.matchName21.setFont(self.font_m_100)
        self.matchName21.setStyleSheet("color: grey;")
        self.matchName21.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName21.setObjectName("matchName21")

        # self.matchName22.setGeometry(QtCore.QRect(1170, 10, 730, 140))
        # self.matchName22.setStyleSheet("font-family: Gotham-Medium; font-size: 90px; color: grey;")
        # self.matchName22.setAlignment(QtCore.Qt.AlignCenter)
        # self.matchName22.setObjectName("matchName22")

        self.label_winner = QtWidgets.QLabel(Form)
        self.label_winner.hide()
        self.label_winner.setGeometry(QtCore.QRect(0, 0, 1920, 150))
        self.label_winner.setFont(self.font_l_150)
        self.label_winner.setStyleSheet("background-color: white;")
        self.label_winner.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label_winner.setObjectName("label_winner")

        # self.lcd2.setGeometry(QtCore.QRect(580, 150, 760, 280))
        self.lcd2.setGeometry(QtCore.QRect(580, 275, 760, 280))
        self.lcd2.setStyleSheet("background-color: None; border: None")

        # self.line2.setGeometry(QtCore.QRect(957, 580, 6, 460))
        # self.line2.setLineWidth(1)
        # self.line2.setMidLineWidth(6)
        # self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line2.setObjectName("line")


        self.label_score22.setGeometry(QtCore.QRect(380, 0, 500, 420))
        self.label_score22.setFont(self.font_m_530)
        self.label_score22.setStyleSheet("background-color: none;")
        self.label_score22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score22.setObjectName("label_score2")

        # self.frame_red2.setGeometry(QtCore.QRect(40, 150, 880, 850))
        self.frame_red2.setStyleSheet("background-color: None; ")
        self.frame_red2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red2.setObjectName("frame_red2")

        self.label_score21.setGeometry(QtCore.QRect(0, 0, 500, 420))
        self.label_score21.setFont(self.font_m_530)
        self.label_score21.setStyleSheet("background-color: none; color:white;")
        self.label_score21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score21.setObjectName("label_score1")

        self.background_red21.setGeometry(QtCore.QRect(0, 0, 500, 450))
        self.background_red21.setStyleSheet("background-color: rgb(255, 95, 95); border-top-left-radius: 15px;"
                                            "border-top-right-radius: 15px; border: 2px solid grey")
        self.background_red21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red21.setObjectName("background_red21")

        self.frame_background_red22_red2.setGeometry(QtCore.QRect(0, 430, 880, 350))
        self.frame_background_red22_red2.setStyleSheet("background-color: none;")

        self.background_red22.setGeometry(QtCore.QRect(0, 0, 880, 350))
        self.background_red22.setStyleSheet("background-color: white; border-radius: 15px;"
                                            "border: 2px solid grey")
        self.background_red22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red22.setObjectName("background_red22")

        self.frame_sportsman.setGeometry(QtCore.QRect(40, 120, 1840, 80))
        self.frame_sportsman.setStyleSheet("background-color: none;")

        self.label_name_white_2.setGeometry(self.coo_label_name_white)
        self.label_name_white_2.setFont(self.font_m_60)
        self.label_name_white_2.setStyleSheet("background-color: none; color: grey; align-self: flex-end;")
        self.label_name_white_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label_name_white_2.setObjectName("label_name_white_2")

        self.label_name_red_2.setGeometry(self.coo_label_name_red)
        self.label_name_red_2.setFont(self.font_m_60)
        self.label_name_red_2.setStyleSheet("background-color: none; color: grey;")
        self.label_name_red_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.label_name_red_2.setObjectName("label_name_white_2")

        self.flag_white = QtWidgets.QLabel(self.frame_sportsman)
        self.flag_red = QtWidgets.QLabel(self.frame_sportsman)
        self.flag_white.hide()
        self.flag_red.hide()

        # self.icon_white = QtWidgets.QLabel(self.flag_white)
        # self.icon_red = QtWidgets.QLabel(self.flag_red)
        ########################
        self.icon_white = RoundedLabel(self.flag_white)
        self.icon_red = RoundedLabel(self.flag_red)
        ########################
        self.icon_white_frame = QtWidgets.QLabel(self.flag_white)
        self.icon_red_frame = QtWidgets.QLabel(self.flag_red)


        self.img_empty = QtGui.QPixmap(":/Images/Empty.png")
        self.img_white = QtGui.QPixmap(":/Images/icon_regions/flags/01_Adygea.svg")
        self.img_curcle = QtGui.QPixmap(":/Images/icon_regions/flags/00_Curcle.svg")
        self.img_red = QtGui.QPixmap(":/Images/icon_regions/flags/22_Altai_Krai.svg")

        # self.img_white = self.img_white.scaled(80, 80)
        # self.img_red = self.img_red.scaled(80, 80)
        # self.img_white = self.img_white.scaledToHeight(80)
        # self.img_red = self.img_red.scaledToHeight(78)

        self.flag_white.setGeometry(QtCore.QRect(1760, 0, 80, 80))
        self.flag_white.setObjectName("flag_white")
        self.flag_red.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.flag_red.setObjectName("flag_red")

        self.icon_white.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.icon_white.setObjectName("icon_white")
        self.icon_white.setPixmap(self.img_white)

        self.icon_white_frame.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.icon_white_frame.setObjectName("icon_white_frame")
        self.icon_white_frame.setPixmap(self.img_curcle)

        self.icon_red.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.icon_red.setObjectName("icon_red")
        self.icon_red.setPixmap(self.img_red)

        self.icon_red_frame.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.icon_red_frame.setObjectName("icon_red_frame")
        self.icon_red_frame.setPixmap(self.img_curcle)

        self.frame_hm_red.setGeometry(QtCore.QRect(0, 5, 880, 170))
        self.frame_hm_red.setStyleSheet("background-color: None;")
        self.frame_hm_red.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_hm_red.setObjectName("frame_hm_red")

        self.label_kum_hmr0.setGeometry(QtCore.QRect(400, 0, 480, 100))
        self.label_kum_hmr0.setFont(self.font_m_100)
        # self.label_kum_hmr0.setStyleSheet("background-color: None; color: grey;")
        self.label_kum_hmr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr0.setObjectName("label_kum_hmr0")

        self.label_kum_hmr1.setGeometry(QtCore.QRect(0, 0, 400, 170))
        self.label_kum_hmr1.setFont(self.font_l_190)
        self.label_kum_hmr1.setStyleSheet("background-color: None; color: grey;")
        self.label_kum_hmr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr1.setObjectName("label_kum_hmr1")

        self.hm_r1.setGeometry(QtCore.QRect(475, 93, 60, 60))
        self.hm_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r1.setObjectName("hm_r1")

        self.hm_r2.setGeometry(QtCore.QRect(610, 93, 60, 60))
        self.hm_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r2.setObjectName("hm_r2")

        self.hm_r3.setGeometry(QtCore.QRect(745, 93, 60, 60))
        self.hm_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r3.setObjectName("hm_r3")

        self.frame_j_red.setGeometry(QtCore.QRect(0, 170, 880, 170))
        self.frame_j_red.setStyleSheet("background-color: None;")
        self.frame_j_red.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_j_red.setObjectName("frame_j_red")

        self.label_kum_jr0.setGeometry(QtCore.QRect(400, 0, 480, 100))
        self.label_kum_jr0.setFont(self.font_m_100)
        # self.label_kum_jr0.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_jr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr0.setObjectName("label_kum_jr0")

        self.label_kum_jr1.setGeometry(QtCore.QRect(0, 0, 400, 170))
        self.label_kum_jr1.setFont(self.font_l_190)
        self.label_kum_jr1.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_jr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr1.setObjectName("label_kum_jr1")

        self.j_r1.setGeometry(QtCore.QRect(475, 93, 60, 60))
        self.j_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r1.setObjectName("j_r1")

        self.j_r2.setGeometry(QtCore.QRect(610, 93, 60, 60))
        self.j_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r2.setObjectName("j_r2")

        self.j_r3.setGeometry(QtCore.QRect(745, 93, 60, 60))
        self.j_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r3.setObjectName("j_r3")

        # self.frame_white2.setGeometry(QtCore.QRect(1000, 150, 880, 850))
        self.frame_white2.setStyleSheet("background-color: None;")
        self.frame_white2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white2.setObjectName("frame_white2")

        self.background_white21.setGeometry(QtCore.QRect(380, 0, 500, 450))
        self.background_white21.setStyleSheet("background-color: None; border-top-left-radius: 15px;"
                                              "border-top-right-radius: 15px; border: 2px solid grey;")
        self.background_white21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white21.setObjectName("background_white21")

        self.frame_background_white22_white2.setGeometry(QtCore.QRect(0, 430, 880, 350))
        self.frame_background_white22_white2.setStyleSheet("background-color: none;")

        self.background_white22.setGeometry(QtCore.QRect(0, 0, 880, 350))
        self.background_white22.setStyleSheet("background-color: white; border-radius: 15px;"
                                              "border: 2px solid grey")
        self.background_white22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white22.setObjectName("background_white22")

        self.frame_hm_white.setGeometry(QtCore.QRect(0, 5, 880, 170))
        self.frame_hm_white.setStyleSheet("background-color: None;")
        self.frame_hm_white.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_hm_white.setObjectName("frame_hm_white")

        self.label_kum_hmw0.setGeometry(QtCore.QRect(400, 0, 480, 100))
        self.label_kum_hmw0.setFont(self.font_m_100)
        # self.label_kum_hmw0.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_hmw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw0.setObjectName("label_kum_hmw0")

        self.label_kum_hmw1.setGeometry(QtCore.QRect(0, 0, 400, 170))
        self.label_kum_hmw1.setFont(self.font_l_190)
        self.label_kum_hmw1.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_hmw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw1.setObjectName("label_kum_hmw1")

        self.hm_w1.setGeometry(QtCore.QRect(475, 93, 60, 60))
        self.hm_w1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w1.setObjectName("hm_w1")

        self.hm_w2.setGeometry(QtCore.QRect(610, 93, 60, 60))
        self.hm_w2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w2.setObjectName("hm_w2")

        self.hm_w3.setGeometry(QtCore.QRect(745, 93, 60, 60))
        self.hm_w3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w3.setObjectName("hm_w3")

        self.frame_j_white.setGeometry(QtCore.QRect(0, 170, 880, 170))
        self.frame_j_white.setStyleSheet("background-color: None;")
        self.frame_j_white.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_j_white.setObjectName("frame_j_white")

        self.label_kum_jw0.setGeometry(QtCore.QRect(400, 0, 480, 100))
        self.label_kum_jw0.setFont(self.font_m_100)
        # self.label_kum_jw0.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_jw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw0.setObjectName("label_kum_jw0")

        self.label_kum_jw1.setGeometry(QtCore.QRect(0, 0, 400, 170))
        self.label_kum_jw1.setFont(self.font_l_190)
        self.label_kum_jw1.setStyleSheet("background-color: None;  color: grey;")
        self.label_kum_jw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw1.setObjectName("label_kum_jw1")

        self.j_w1.setGeometry(QtCore.QRect(475, 93, 60, 60))
        self.j_w1.setStyleSheet("border-radius: 30px; border: 4px solid black;")
        self.j_w1.setObjectName("j_w1")

        self.j_w2.setGeometry(QtCore.QRect(610, 93, 60, 60))
        self.j_w2.setStyleSheet("border-radius: 30px; border: 4px solid black;")
        self.j_w2.setObjectName("j_w2")

        self.j_w3.setGeometry(QtCore.QRect(745, 93, 60, 60))
        self.j_w3.setStyleSheet("border-radius: 30px; border: 4px solid black;")
        self.j_w3.setObjectName("j_w3")

        # Экран для отображения ФИО спортсменов
        self.sportsman_screen = QtWidgets.QFrame(Form)
        self.screen_frame_white = QtWidgets.QFrame(self.sportsman_screen)
        self.screen_background_white_1 = QtWidgets.QFrame(self.screen_frame_white)
        self.screen_background_white_2 = QtWidgets.QFrame(self.screen_frame_white)
        self.screen_label_name_white = QtWidgets.QLabel(self.screen_frame_white)
        self.screen_label_region_white = QtWidgets.QLabel(self.screen_frame_white)

        self.screen_frame_red = QtWidgets.QFrame(self.sportsman_screen)
        self.screen_background_red_1 = QtWidgets.QFrame(self.screen_frame_red)
        self.screen_background_red_2 = QtWidgets.QFrame(self.screen_frame_red)
        self.screen_label_name_red = QtWidgets.QLabel(self.screen_frame_red)
        self.screen_label_region_red = QtWidgets.QLabel(self.screen_frame_red)

        self.sportsman_screen.setGeometry(QtCore.QRect(0, 120, 1920, 900))
        self.sportsman_screen.setStyleSheet("background-color: white;")
        self.sportsman_screen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sportsman_screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sportsman_screen.setObjectName("sportsman_screen")

        self.screen_frame_white.setGeometry(self.coo_screen_white_std)
        self.screen_frame_white.setStyleSheet("background-color: None;")
        self.screen_frame_white.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_frame_white.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_frame_white.setObjectName("screen_frame_white")

        self.screen_background_white_1.setGeometry(QtCore.QRect(0, 0, 1840, 280))
        self.screen_background_white_1.setStyleSheet("background-color: None; border-top-left-radius: 15px;"
                                                     "border-top-right-radius: 15px; border: 2px solid grey")
        self.screen_background_white_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_background_white_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_background_white_1.setObjectName("screen_background_white_1")

        self.screen_background_white_2.setGeometry(QtCore.QRect(0, 250, 1840, 150))
        self.screen_background_white_2.setStyleSheet("background-color: white; border-radius: 15px;"
                                                     "border: 2px solid grey")
        self.screen_background_white_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_background_white_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_background_white_2.setObjectName("screen_background_white_2")

        self.screen_label_name_white.setGeometry(QtCore.QRect(20, 0, 1800, 250))
        self.screen_label_name_white.setFont(self.font_b_250)
        self.screen_label_name_white.setStyleSheet("background-color: none;")
        self.screen_label_name_white.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label_name_white.setObjectName("screen_label_name_white")

        self.screen_label_region_white.setGeometry(QtCore.QRect(20, 250, 1800, 150))
        self.screen_label_region_white.setFont(self.font_l_150)
        self.screen_label_region_white.setStyleSheet("background-color: none;")
        self.screen_label_region_white.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label_region_white.setObjectName("screen_label_region_white")

        self.screen_frame_red.setGeometry(self.coo_screen_red_std)
        self.screen_frame_red.setStyleSheet("background-color: None; ")
        self.screen_frame_red.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_frame_red.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_frame_red.setObjectName("screen_frame_red")

        self.screen_background_red_1.setGeometry(QtCore.QRect(0, 0, 1840, 280))
        self.screen_background_red_1.setStyleSheet("background-color: rgb(255, 95, 95); border-top-left-radius: 15px;"
                                                   "border-top-right-radius: 15px; border: 2px solid grey")
        self.screen_background_red_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_background_red_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_background_red_1.setObjectName("screen_background_red_1")

        self.screen_background_red_2.setGeometry(QtCore.QRect(0, 250, 1840, 150))
        self.screen_background_red_2.setStyleSheet("background-color: white; border-radius: 15px;"
                                                   "border: 2px solid grey")
        self.screen_background_red_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_background_red_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_background_red_2.setObjectName("screen_background_red_2")

        self.screen_label_name_red.setGeometry(QtCore.QRect(20, 0, 1800, 250))
        self.screen_label_name_red.setFont(self.font_b_250)
        self.screen_label_name_red.setStyleSheet("background-color: none; color: white;")
        self.screen_label_name_red.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label_name_red.setObjectName("screen_label_name_red")

        self.screen_label_region_red.setGeometry(QtCore.QRect(20, 250, 1800, 150))
        self.screen_label_region_red.setFont(self.font_l_150)
        self.screen_label_region_red.setStyleSheet("background-color: none;")
        self.screen_label_region_red.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label_region_red.setObjectName("screen_label_region_red")

        self.sportsman_screen.hide()

        # self.line2.raise_()
        self.lcd2.raise_()

        self.frame_red2.raise_()
        self.label_kum_hmr0.raise_()
        self.label_kum_jr0.raise_()
        self.label_kum_hmw0.raise_()
        self.label_kum_jw0.raise_()

        self.frame_j_red.raise_()
        self.label_score21.raise_()
        self.frame_hm_red.raise_()

        self.hm_r1.raise_()
        self.hm_r2.raise_()
        self.hm_r3.raise_()
        self.j_r1.raise_()
        self.j_r2.raise_()
        self.j_r3.raise_()

        self.hm_w1.raise_()
        self.hm_w2.raise_()
        self.hm_w3.raise_()
        self.j_w1.raise_()
        self.j_w2.raise_()
        self.j_w3.raise_()
        self.label_kum_jw1.raise_()
        self.label_kum_hmw1.raise_()
        self.label_kum_jr1.raise_()
        self.label_kum_hmr1.raise_()

        self.sportsman_screen.raise_()
        self.screen_frame_white.raise_()
        self.screen_background_white_1.raise_()
        self.screen_background_white_2.raise_()
        self.screen_label_name_white.raise_()
        self.screen_label_region_white.raise_()
        self.screen_background_red_1.raise_()
        self.screen_background_red_2.raise_()
        self.screen_label_name_red.raise_()
        self.screen_label_region_red.raise_()
        self.label_winner.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " "))
        self.label_kum_hmr0.setText(_translate("Form", None))
        self.label_kum_hmr1.setText(_translate("Form", "H/M"))
        self.label_score21.setText(_translate("Form", "0"))
        self.label_kum_jr0.setText(_translate("Form", None))
        self.label_kum_jr1.setText(_translate("Form", "J"))
        self.label_kum_hmw0.setText(_translate("Form", None))
        self.label_kum_hmw1.setText(_translate("Form", "H/M"))
        self.label_score22.setText(_translate("Form", "0"))
        self.label_kum_jw0.setText(_translate("Form", None))
        self.label_kum_jw1.setText(_translate("Form", "J"))
        self.matchName21.setText(_translate("Form", "Татами №#, Возраст"))
        # self.matchName22.setText(_translate("Form", "Возраст"))
        self.label_winner.setText(_translate("Form", "ПОБЕДИТЕЛЬ"))
        self.label_name_white_2.setText(_translate("Form", ""))
        self.label_name_red_2.setText(_translate("Form", ""))


class KumiteSecondWindow(QWidget, KumiteSWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)


class Frame_Header(QWidget):
    def __init__(self, parent):
        super(Frame_Header, self).__init__()
        self.parent = parent

        self.btn_style_header = css.btn_style_header

        self.font_l_13 = QtGui.QFont()
        self.font_l_13.setFamily("Gotham-Light")
        self.font_l_13.setPixelSize(13)

        self.font_l_22 = QtGui.QFont()
        self.font_l_22.setFamily("Gotham-Light")
        self.font_l_22.setPixelSize(22)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.frame_title = QtWidgets.QFrame(self)
        self.frame_title.setStyleSheet("border-top: 1px solid gray; border-bottom: none; border-left: 1px solid gray;"
                                       "border-right: none;")
        self.frame_title.setFixedSize(690, 31)

        self.pixmap = QtGui.QPixmap(':/Images/icon_30px.ico')
        self.pixmap2 = self.pixmap.scaled(16, 16, QtCore.Qt.KeepAspectRatio)
        self.pixmap_label = QLabel(self.frame_title)
        self.pixmap_label.setGeometry(QtCore.QRect(8, 0, 30, 31))
        self.pixmap_label.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.pixmap_label.setPixmap(self.pixmap2)

        self.label_windowsTitle = QLabel("Кумите. Судейское окно", self.frame_title)
        self.label_windowsTitle.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.label_windowsTitle.move(30, 9)

        self.frame_combo = QtWidgets.QFrame(self)
        self.frame_combo.setGeometry(QtCore.QRect(0, 0, 153, 31))

        self.frame_combo_border = QtWidgets.QFrame(self.frame_combo)
        self.frame_combo_border.setStyleSheet("background-color: grey;")
        self.frame_combo_border.setGeometry(QtCore.QRect(0, 0, 200, 1))

        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.combo.setGeometry(0, 4, 147, 24)
        self.combo.addItems(["Главное меню", "Ката отбороч.", "Ката финал"])
        self.combo.setFont(self.font_l_13)

        self.frame_btn = QtWidgets.QFrame(self)
        self.frame_btn.setFixedSize(51, 31)
        self.frame_btn.setStyleSheet("border-top: 1px solid gray; border-bottom: none; border-left: none;"
                                     "border-right: 1px solid gray;")

        self.btn_showMinimized = QtWidgets.QPushButton("_", self.frame_btn)
        self.btn_showMinimized.setGeometry(QtCore.QRect(0, 4, 24, 24))
        self.btn_showMinimized.setStyleSheet(self.btn_style_header)
        self.btn_showMinimized.setFont(self.font_l_13)
        self.btn_showMinimized.clicked.connect(self.btn_showMinimized_clicked)

        self.btn_closeWin = QtWidgets.QPushButton("×", self.frame_btn)
        self.btn_closeWin.setStyleSheet(self.btn_style_header)
        self.btn_closeWin.setFont(self.font_l_22)
        self.btn_closeWin.setGeometry(QtCore.QRect(23, 4, 24, 24))

        self.layout.addWidget(self.frame_title)
        self.layout.addWidget(self.frame_combo)
        self.layout.addWidget(self.frame_btn)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(Frame_Header, self).resizeEvent(QResizeEvent)
        self.label_windowsTitle.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_showMinimized_clicked(self):
        self.parent.showMinimized()


class KumiteMainWindow_Ui(QWidget):
    def __init__(self):
        super(KumiteMainWindow_Ui, self).__init__()
        self.flags_dict = None
        QWidget.setWindowTitle(self, "Кумите. Судейское окно")

        self.Form2 = QtWidgets.QFrame(self)
        # self.Form2.setFixedSize(900, 500)
        self.Form2.setStyleSheet("background-color: white;")

        self.frame_matchName = QtWidgets.QFrame(self.Form2)
        self.label_matchName1 = QtWidgets.QLabel('<b>Заголовок</b>', self.frame_matchName)
        self.matchName11 = QtWidgets.QLineEdit("Татами №#", self.frame_matchName)
        self.matchName12 = QtWidgets.QLineEdit("Возраст", self.frame_matchName)
        self.btn_NewCategory = QtWidgets.QPushButton("НОВАЯ\nКАТЕГОРИЯ", self.frame_matchName)
        self.btn_showData = QtWidgets.QPushButton("ПОКАЗАТЬ\nНА ЭКРАНЕ", self.frame_matchName)

        self.control_panel = QtWidgets.QFrame(self.Form2)
        self.lcd1 = QtWidgets.QLCDNumber(self.control_panel)
        self.btn_reset = QtWidgets.QPushButton("НОВЫЙ БОЙ", self.control_panel)
        self.btn_pause = QtWidgets.QPushButton("ОБНУЛИТЬ ТАЙМЕР", self.control_panel)
        self.btn_start = QtWidgets.QPushButton("► START", self.control_panel)
        self.plus2sec = QtWidgets.QPushButton("+2 сек", self.control_panel)
        self.minus2sec = QtWidgets.QPushButton("-2 сек", self.control_panel)

        self.frame_timeRound = QtWidgets.QFrame(self.control_panel)
        self.frame_timeRound2 = QtWidgets.QFrame(self.frame_timeRound)
        self.round_time = QtWidgets.QLabel("Время раунда", self.frame_timeRound)
        self.label_1min = QtWidgets.QLabel("1 мин", self.frame_timeRound)
        self.label_15min = QtWidgets.QLabel("1,5 мин", self.frame_timeRound)
        self.label_2min = QtWidgets.QLabel("2 мин", self.frame_timeRound)
        self.label_3min = QtWidgets.QLabel("3 мин", self.frame_timeRound)
        self.label_5min = QtWidgets.QLabel("5 мин", self.frame_timeRound)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.frame_timeRound)

        self.frame_red1 = QtWidgets.QFrame(self.Form2)
        self.label_score11 = QtWidgets.QLabel("0", self.frame_red1)
        self.score_red_0 = QtWidgets.QRadioButton("0", self.frame_red1)
        self.score_red_1 = QtWidgets.QRadioButton("1", self.frame_red1)
        self.score_red_2 = QtWidgets.QRadioButton("2", self.frame_red1)
        self.score_red_3 = QtWidgets.QRadioButton("3", self.frame_red1)
        self.score_red_4 = QtWidgets.QRadioButton("4", self.frame_red1)
        self.score_red_5 = QtWidgets.QRadioButton("5", self.frame_red1)
        self.score_red_6 = QtWidgets.QRadioButton("6", self.frame_red1)
        self.horizon_line_red = QtWidgets.QFrame(self.frame_red1)

        self.frame_white1 = QtWidgets.QFrame(self.Form2)
        self.label_score12 = QtWidgets.QLabel("0", self.frame_white1)
        self.score_white_0 = QtWidgets.QRadioButton("0", self.frame_white1)
        self.score_white_1 = QtWidgets.QRadioButton("1", self.frame_white1)
        self.score_white_2 = QtWidgets.QRadioButton("2", self.frame_white1)
        self.score_white_3 = QtWidgets.QRadioButton("3", self.frame_white1)
        self.score_white_4 = QtWidgets.QRadioButton("4", self.frame_white1)
        self.score_white_5 = QtWidgets.QRadioButton("5", self.frame_white1)
        self.score_white_6 = QtWidgets.QRadioButton("6", self.frame_white1)
        self.horizon_line_white = QtWidgets.QFrame(self.frame_white1)

        self.winnerFrame = QtWidgets.QFrame(self.Form2)
        self.winnerRed = QtWidgets.QRadioButton("Победил АКА", self.winnerFrame)
        self.winnerWhite = QtWidgets.QRadioButton("Победил СИРО", self.winnerFrame)
        # self.temp_index = False

        self.frame_rh = QtWidgets.QFrame(self.frame_red1)
        self.h_red0 = QtWidgets.QLabel("H \nM", self.frame_rh)
        self.h_red1 = QtWidgets.QRadioButton("Keikoku", self.frame_rh)
        self.h_red2 = QtWidgets.QRadioButton("Chui", self.frame_rh)
        self.h_red3 = QtWidgets.QRadioButton("Hansoku", self.frame_rh)
        self.h_red4 = QtWidgets.QRadioButton("Off", self.frame_rh)
        self.frame_rj = QtWidgets.QFrame(self.frame_red1)
        self.j_red0 = QtWidgets.QLabel("J", self.frame_rj)
        self.j_red1 = QtWidgets.QRadioButton("Keikoku", self.frame_rj)
        self.j_red2 = QtWidgets.QRadioButton("Chui", self.frame_rj)
        self.j_red3 = QtWidgets.QRadioButton("Hansoku", self.frame_rj)
        self.j_red4 = QtWidgets.QRadioButton("Off", self.frame_rj)
        self.frame_wh = QtWidgets.QFrame(self.frame_white1)
        self.h_white0 = QtWidgets.QLabel("H \nM", self.frame_wh)
        self.h_white1 = QtWidgets.QRadioButton("Keikoku", self.frame_wh)
        self.h_white2 = QtWidgets.QRadioButton("Chui", self.frame_wh)
        self.h_white3 = QtWidgets.QRadioButton("Hansoku", self.frame_wh)
        self.h_white4 = QtWidgets.QRadioButton("Off", self.frame_wh)
        self.frame_wj = QtWidgets.QFrame(self.frame_white1)
        self.j_white0 = QtWidgets.QLabel("J", self.frame_wj)
        self.j_white1 = QtWidgets.QRadioButton("Keikoku", self.frame_wj)
        self.j_white2 = QtWidgets.QRadioButton("Chui", self.frame_wj)
        self.j_white3 = QtWidgets.QRadioButton("Hansoku", self.frame_wj)
        self.j_white4 = QtWidgets.QRadioButton("Off", self.frame_wj)

        self.frame_sportsmans = QtWidgets.QFrame(self.Form2)

        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.pers_com_lbl = QtWidgets.QLabel("/", self.frame_sportsmans)
        self.pers_lbl = QtWidgets.QLabel("Личные", self.frame_sportsmans)
        self.com_lbl = QtWidgets.QLabel("Командные", self.frame_sportsmans)
        self.pers_com_qbx = QtWidgets.QCheckBox(self.frame_sportsmans)
        self.male = QtWidgets.QRadioButton("М", self.frame_sex)
        self.female = QtWidgets.QRadioButton("Ж", self.frame_sex)
        self.sex_1 = QtWidgets.QLabel("Пол", self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel("Возраст", self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.comboBox_name_white_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)
        self.name_white_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)

        self.frm_spman_red = QtWidgets.QFrame(self.Form2)
        self.frm_spman_white = QtWidgets.QFrame(self.Form2)

        self.btn_show_screen = QtWidgets.QPushButton("Показать\nэкран ФИО", self.Form2)

        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(self.frm_spman_red,
                                                       placeholderText="АКА. Введите имя спортсмена")
        self.le_comboBox_name_red_1 = QtWidgets.QComboBox(self.frm_spman_red)
        # self.lineEdit_region_red_1 = QtWidgets.QLineEdit(self.frm_spman_red, placeholderText="АКА. Введите регион")
        self.lineEdit_region_red_1 = QtWidgets.QComboBox(self.frm_spman_red)
        self.label_name_red_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.frm_spman_red)
        self.label_region_red_1 = QtWidgets.QLabel("регион", self.frm_spman_red)

        self.lineEdit_name_white_1 = QtWidgets.QLineEdit(self.frm_spman_white,
                                                         placeholderText="СИРО. Введите имя спортсмена")
        self.le_comboBox_name_white_1 = QtWidgets.QComboBox(self.frm_spman_white)
        # self.lineEdit_region_white_1 = QtWidgets.QLineEdit(self.frm_spman_white, placeholderText="СИРО. Введите регион")
        self.lineEdit_region_white_1 = QtWidgets.QComboBox(self.frm_spman_white)
        self.label_name_white_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.frm_spman_white)
        self.label_region_white_1 = QtWidgets.QLabel("регион", self.frm_spman_white)

        self.frame_pyatnov = QtWidgets.QFrame(self.Form2)

        self.pyatnov_label = QtWidgets.QLabel("Выберите пару", self.frame_pyatnov)
        self.pyatnov_name = QtWidgets.QComboBox(self.frame_pyatnov)

        self.pers_com_qbx_style_1 = css.pers_com_qbx_style_1

        self.btn_style_1 = css.btn_style_1

        self.btn_style_2 = css.btn_style_2

        self.combo_style_2 = css.combo_style_2

        self.LEdit_style_1 = css.LEdit_style_1
        """
            QLineEdit {
                border-bottom: 1px solid grey;
                background-color: #FAF9F9;
                color: #555B6E;
                font-size: 20px;
                font-family: Gotham-Light;
                }
            QLineEdit:hover {
                border-bottom: 2px solid #3e6ae1;
                background-color: #fdfdfd;
                color: black;
                }      
        """

        self.LEdit_style_2 = """
            QLineEdit {
                background-color: grey;
                color: #555B6E;
                font-size: 20px;
                font-family: Gotham-Light;
                }
            QLineEdit:hover {
                background-color: #fdfdfd;
                color: black;
                }

        """

        self.Radio_style_1 = """
        QRadioButton {
            border: none;
            border-bottom: 2px solid white;
            font-family: Gotham-Light;
            font-size: 20px;
            background-color: none;
        }
        QRadioButton::indicator
        {
            width: 10px;
            height: 10px;
        }
        QRadioButton::indicator::unchecked
        {
           image: url(:/Images/radiobutton_unchecked.png);
        }
        QRadioButton::indicator:unchecked:hover
        {
            image: url(:/Images/radiobutton_unchecked_hover.png);
        }
        QRadioButton::indicator:unchecked:pressed
        {
            image: url(:/Images/radiobutton_unchecked_pressed.png);
        }
        QRadioButton::indicator::checked 
        {
            image: url(:/Images/radiobutton_checked.png);
        }
        QRadioButton::indicator:checked:hover 
        {
            image: url(:/Images/radiobutton_checked_hover.png);
        }
        QRadioButton::indicator:checked:pressed 
        {
            image: url(:/Images/radiobutton_checked_pressed.png);
        }
        QRadioButton:checked {
            border-bottom: 2px solid #3e6ae1;
        }
        """

        self.Radio_style_2 = """
        QRadioButton {
            border: none;
            border-bottom: 2px solid white;
            font-family: Gotham-Light;
            font-size: 20px;
            background-color: none;
        }
        QRadioButton::indicator
        {
            width: 10px;
            height: 10px;
        }
        QRadioButton::indicator::unchecked
        {
           image: url(:/Images/radiobutton_unchecked.png);
        }
        QRadioButton::indicator:unchecked:hover
        {
            image: url(:/Images/radiobutton_unchecked_hover.png);
        }
        QRadioButton::indicator:unchecked:pressed
        {
            image: url(:/Images/radiobutton_unchecked_pressed.png);
        }
        QRadioButton::indicator::checked 
        {
            image: url(:/Images/radiobutton_checked.png);
        }
        QRadioButton::indicator:checked:hover 
        {
            image: url(:/Images/radiobutton_checked_hover.png);
        }
        QRadioButton::indicator:checked:pressed 
        {
            image: url(:/Images/radiobutton_checked_pressed.png);
        }
        QRadioButton:checked {
            border-bottom: 2px solid #FF4546; 
        }
        """

        self.LEdit_style_2 = """
            QLineEdit {
                border: none;
                border-radius: none;
                border-bottom: 1px solid grey;
                background-color: white;
                color: #555B6E;
                }
            QLineEdit:hover {
                border-bottom: 2px solid #3e6ae1;
                background-color: #fdfdfd;
                color: black;
                }
        """

        self.font_l_10 = css.font_l_10
        self.font_l_12 = css.font_l_12
        self.font_l_13 = css.font_l_13
        self.font_m_13 = css.font_m_13
        self.font_b_13 = css.font_b_13
        self.font_l_16 = css.font_l_16
        self.font_m_16 = css.font_m_16
        self.font_l_20 = css.font_l_20
        self.font_m_20 = css.font_m_20
        self.font_m_33 = css.font_m_33
        self.font_l_40 = css.font_l_40
        self.font_l_46 = css.font_l_46

        self.frame_bottom = QtWidgets.QFrame(self.Form2)
        self.frame_bottom1 = QtWidgets.QFrame(self.Form2)
        self.frame_bottom2 = QtWidgets.QFrame(self.Form2)
        self.frame_bottom3 = QtWidgets.QFrame(self.Form2)
        self.frame_left = QtWidgets.QFrame(self.Form2)
        self.frame_right = QtWidgets.QFrame(self.Form2)

        self.frame_bottom.setGeometry(QtCore.QRect(0, 559, 900, 1))
        self.frame_bottom.setStyleSheet("background-color: grey;")
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_bottom1.setGeometry(QtCore.QRect(25, 559, 850, 1))
        self.frame_bottom1.setStyleSheet("background-color: grey;")
        self.frame_bottom1.setObjectName("frame_bottom1")
        self.frame_bottom2.setGeometry(QtCore.QRect(0, 609, 900, 1))
        self.frame_bottom2.setStyleSheet("background-color: grey;")
        self.frame_bottom2.setObjectName("frame_bottom")
        self.frame_bottom3.setGeometry(QtCore.QRect(0, 669, 900, 1))
        self.frame_bottom3.setStyleSheet("background-color: grey;")
        self.frame_bottom3.setObjectName("frame_bottom1")
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 1, 669))
        self.frame_left.setStyleSheet("background-color: grey;")
        self.frame_left.setObjectName("frame_left")
        self.frame_right.setGeometry(QtCore.QRect(899, 0, 1, 669))
        self.frame_right.setStyleSheet("background-color: grey;")
        self.frame_right.setObjectName("frame_right")

        self.frame_matchName.setGeometry(QtCore.QRect(0, 0, 900, 70))
        self.frame_matchName.setStyleSheet("background-color: none; border: none;")

        self.btn_showData.setGeometry(QtCore.QRect(50, 10, 120, 50))
        self.btn_showData.setStyleSheet(self.btn_style_2)
        self.btn_showData.setFont(self.font_m_13)
        self.btn_showData.setObjectName("btn_showData")
        self.btn_showData.setToolTip('Отобразить на Большом экране ФИО, номер татами и категорию')

        self.btn_NewCategory.setGeometry(QtCore.QRect(730, 10, 120, 50))
        self.btn_NewCategory.setStyleSheet(self.btn_style_2)
        self.btn_NewCategory.setFont(self.font_m_13)
        self.btn_NewCategory.setObjectName("btn_NewCategory")

        self.label_matchName1.setGeometry(QtCore.QRect(210, 0, 480, 25))
        self.label_matchName1.setFont(self.font_l_20)
        self.label_matchName1.setStyleSheet("color: black;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.matchName11.setGeometry(QtCore.QRect(210, 25, 150, 30))
        self.matchName11.setStyleSheet(self.LEdit_style_1)
        self.matchName11.setFont(self.font_l_20)
        self.matchName11.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.matchName11.setObjectName("matchName11")

        self.matchName12.setGeometry(QtCore.QRect(370, 25, 320, 30))
        self.matchName12.setStyleSheet(self.LEdit_style_1)
        self.matchName12.setFont(self.font_l_20)
        self.matchName12.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.matchName12.setObjectName("matchName12")

        grey_style_btn_plus = """
            QPushButton {
                border: 1px solid #7AFFC2;
                border-radius: 9px;
                color: black;
                background-color: #7AFFC2;
                font-family: Gotham-Medium;
                }
            QPushButton:hover {
                border: 1px solid #EB6D59;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #EB6D59, stop: 1 #EB6D59);
                color: white;
                font-family: Gotham-Medium;
                }    
            QPushButton:pressed {
                border: 1px solid #3e6ae1;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #3e6ae1, stop: 1 #3e6ae1);
                color: white;
                font-family: Gotham-Medium;
                }
            QPushButton:flat {
                border: none;
                }
        """

        grey_style_btn_minus = """
            QPushButton {
                border: 1px solid #FFDC7D;
                border-radius: 9px;
                color: black;
                background-color: #FFDC7D;
                font-family: Gotham-Medium;
                }
            QPushButton:hover {
                border: 1px solid #EB6D59;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #EB6D59, stop: 1 #EB6D59);
                color: white;
                font-family: Gotham-Medium;
                }
            QPushButton:pressed {
                border: 1px solid #5876E0;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #5876E0, stop: 1 #5876E0);
                color: white;
                font-family: Gotham-Medium;
                }
            QPushButton:flat {
                border: none;
                }
        """

        self.winnerFrame.setGeometry(QtCore.QRect(135, 140, 610, 25))
        self.winnerFrame.setStyleSheet("background-color: none; ")

        # self.b3.setGeometry(QtCore.QRect(200, 0, 165, 25))

        self.winnerRed.setGeometry(QtCore.QRect(445, 0, 165, 25))
        self.winnerRed.setStyleSheet(self.Radio_style_2)
        self.winnerRed.setObjectName("winnerRed")

        self.winnerWhite.setGeometry(QtCore.QRect(0, 0, 180, 25))
        self.winnerWhite.setStyleSheet(self.Radio_style_1)
        self.winnerWhite.setObjectName("winnerWhite")

        self.frame_red1.setGeometry(QtCore.QRect(460, 140, 415, 270))
        # self.frame_red1.setStyleSheet("background-color: none; border-radius: 15px;  border: 1px solid #FF4546")
        self.frame_red1.setStyleSheet("border-left: 1px solid #FF4546")
        self.frame_red1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red1.setObjectName("frame_red")

        self.label_score11.setGeometry(QtCore.QRect(150, 15, 100, 120))
        self.label_score11.setStyleSheet("background-color: None; border: none;"
                                         "font-family: Gotham-Light; font-size: 135px;")
        self.label_score11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score11.setObjectName("label_score1")

        # self.score_red_0.setGeometry(QtCore.QRect(10, 8, 40, 25))
        self.score_red_0.setGeometry(QtCore.QRect(10, 135, 40, 25))
        self.score_red_0.setStyleSheet(self.Radio_style_2)
        self.score_red_0.setChecked(True)
        self.score_red_0.setObjectName("score_red_0")

        # self.score_red_1.setGeometry(QtCore.QRect(10, 41, 40, 25))
        self.score_red_1.setGeometry(QtCore.QRect(70, 135, 40, 25))
        self.score_red_1.setStyleSheet(self.Radio_style_2)
        self.score_red_1.setObjectName("score_red_1")

        # self.score_red_2.setGeometry(QtCore.QRect(10, 74, 40, 25))
        self.score_red_2.setGeometry(QtCore.QRect(130, 135, 40, 25))
        self.score_red_2.setStyleSheet(self.Radio_style_2)
        self.score_red_2.setObjectName("score_red_2")

        # self.score_red_3.setGeometry(QtCore.QRect(10, 107, 40, 25))
        self.score_red_3.setGeometry(QtCore.QRect(190, 135, 40, 25))
        self.score_red_3.setStyleSheet(self.Radio_style_2)
        self.score_red_3.setObjectName("score_red_3")

        # self.score_red_4.setGeometry(QtCore.QRect(10, 140, 40, 25))
        self.score_red_4.setGeometry(QtCore.QRect(250, 135, 40, 25))
        self.score_red_4.setStyleSheet(self.Radio_style_2)
        self.score_red_4.setObjectName("score_red_4")

        # self.score_red_5.setGeometry(QtCore.QRect(10, 173, 40, 25))
        self.score_red_5.setGeometry(QtCore.QRect(310, 135, 40, 25))
        self.score_red_5.setStyleSheet(self.Radio_style_2)
        self.score_red_5.setObjectName("score_red_5")

        # self.score_red_6.setGeometry(QtCore.QRect(10, 135, 40, 25))
        self.score_red_6.setGeometry(QtCore.QRect(370, 135, 40, 25))
        self.score_red_6.setStyleSheet(self.Radio_style_2)
        self.score_red_6.setObjectName("score_red_6")

        self.horizon_line_red.setGeometry(QtCore.QRect(10, 165, 395, 1))
        self.horizon_line_red.setStyleSheet("background-color: #FF4546;")

        self.frame_white1.setGeometry(QtCore.QRect(25, 140, 415, 270))
        # self.frame_white1.setStyleSheet("background-color: none; border-radius: 15px; border: 1px solid grey;")
        self.frame_white1.setStyleSheet("border-left: 1px solid grey")
        self.frame_white1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white1.setObjectName("frame_white1")

        self.label_score12.setGeometry(QtCore.QRect(150, 15, 100, 120))
        self.label_score12.setStyleSheet("background-color: None; border: none; font-family: Gotham-Light;"
                                         "font-size: 135px;")
        self.label_score12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score12.setObjectName("label_score2")

        self.control_panel.setGeometry(QtCore.QRect(0, 70, 900, 70))
        self.control_panel.setStyleSheet("background-color: none;")
        self.control_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_panel.setObjectName("control_panel")

        self.frame_timeRound.setGeometry(QtCore.QRect(10, 8, 189, 54))
        self.frame_timeRound.setStyleSheet("background-color: none;")
        self.frame_timeRound.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_timeRound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_timeRound.setObjectName("frame_timeRound")

        self.frame_timeRound2.setGeometry(QtCore.QRect(0, 0, 189, 54))
        self.frame_timeRound2.setStyleSheet("background-color: none; ")
        self.frame_timeRound2.setObjectName("frame_timeRound2")

        self.round_time.setGeometry(QtCore.QRect(0, 0, 189, 20))
        self.round_time.setStyleSheet("font-family: Gotham-Medium; font-size: 15px;")
        self.round_time.setAlignment(QtCore.Qt.AlignCenter)
        self.round_time.setObjectName("round_time")
        self.round_time.setToolTip('Кликай или вращай колёсико мышки')

        self.slider.setGeometry(QtCore.QRect(15, 25, 160, 15))
        self.slider.setTickInterval(1)
        self.slider.setRange(1, 5)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setValue(3)

        self.label_1min.setGeometry(QtCore.QRect(2, 40, 35, 14))
        self.label_1min.setFont(self.font_l_10)
        self.label_1min.setObjectName("label_1min")

        self.label_15min.setGeometry(QtCore.QRect(35, 40, 45, 14))
        self.label_15min.setFont(self.font_l_10)
        self.label_15min.setObjectName("label_15min")

        self.label_2min.setGeometry(QtCore.QRect(80, 40, 40, 14))
        self.label_2min.setFont(self.font_l_10)
        self.label_2min.setObjectName("label_2min")

        self.label_3min.setGeometry(QtCore.QRect(120, 40, 35, 14))
        self.label_3min.setFont(self.font_l_10)
        self.label_3min.setObjectName("label_3min")

        self.label_5min.setGeometry(QtCore.QRect(155, 40, 34, 14))
        self.label_5min.setFont(self.font_l_10)
        self.label_5min.setObjectName("label_5min")

        self.lcd1.setGeometry(QtCore.QRect(350, 5, 180, 60))
        self.lcd1.setStyleSheet("background-color: None; border: None")

        self.plus2sec.setGeometry(QtCore.QRect(520, 10, 40, 18))
        self.plus2sec.setStyleSheet(grey_style_btn_plus)
        self.plus2sec.setObjectName("plus2sec")

        self.minus2sec.setGeometry(QtCore.QRect(520, 40, 40, 18))
        self.minus2sec.setStyleSheet(grey_style_btn_minus)
        self.minus2sec.setObjectName("minus2sec")

        self.btn_reset.setGeometry(QtCore.QRect(580, 15, 120, 40))
        self.btn_reset.setStyleSheet(self.btn_style_1)
        self.btn_reset.setFont(self.font_m_13)
        self.btn_reset.setToolTip('Сбросить всё')
        self.btn_reset.setObjectName("btn_reset")

        self.btn_pause.setGeometry(QtCore.QRect(725, 20, 150, 30))
        self.btn_pause.setStyleSheet(self.btn_style_1)
        self.btn_pause.setFont(self.font_m_13)
        self.btn_pause.setToolTip('Сбросить только секундомер')
        self.btn_pause.setObjectName("btn_pause")

        self.btn_start.setGeometry(QtCore.QRect(230, 10, 115, 50))
        self.btn_start.setStyleSheet(self.btn_style_1)
        self.btn_start.setFont(self.font_m_16)
        self.btn_start.setObjectName("btn_start")

        self.score_white_0.setGeometry(QtCore.QRect(10, 135, 40, 25))
        self.score_white_0.setChecked(True)
        self.score_white_0.setStyleSheet(self.Radio_style_1)
        self.score_white_0.setObjectName("score_white_0")

        self.score_white_1.setGeometry(QtCore.QRect(70, 135, 40, 25))
        self.score_white_1.setStyleSheet(self.Radio_style_1)
        self.score_white_1.setObjectName("score_white_1")

        self.score_white_2.setGeometry(QtCore.QRect(130, 135, 40, 25))
        self.score_white_2.setStyleSheet(self.Radio_style_1)
        self.score_white_2.setObjectName("score_white_2")

        self.score_white_3.setGeometry(QtCore.QRect(190, 135, 40, 25))
        self.score_white_3.setStyleSheet(self.Radio_style_1)
        self.score_white_3.setObjectName("score_white_3")

        self.score_white_4.setGeometry(QtCore.QRect(250, 135, 40, 25))
        self.score_white_4.setStyleSheet(self.Radio_style_1)
        self.score_white_4.setObjectName("score_white_4")

        self.score_white_5.setGeometry(QtCore.QRect(310, 135, 40, 25))
        self.score_white_5.setStyleSheet(self.Radio_style_1)
        self.score_white_5.setObjectName("score_white_5")

        self.score_white_6.setGeometry(QtCore.QRect(370, 135, 40, 25))
        self.score_white_6.setStyleSheet(self.Radio_style_1)
        self.score_white_6.setObjectName("score_white_6")

        self.horizon_line_white.setGeometry(QtCore.QRect(10, 165, 395, 1))
        self.horizon_line_white.setStyleSheet("background-color: grey;")

        self.frame_rh.setGeometry(QtCore.QRect(5, 175, 405, 40))
        self.frame_rh.setStyleSheet("border: none")
        self.frame_rh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rh.setObjectName("frame_rh")

        self.h_red0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.h_red0.setFont(self.font_l_20)
        self.h_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_red0.setObjectName("h_red0")

        self.h_red1.setGeometry(QtCore.QRect(35, 5, 100, 25))
        self.h_red1.setStyleSheet(self.Radio_style_2)
        self.h_red1.setObjectName("h_red1")

        self.h_red2.setGeometry(QtCore.QRect(145, 5, 65, 25))
        self.h_red2.setStyleSheet(self.Radio_style_2)
        self.h_red2.setObjectName("h_red2")

        self.h_red3.setGeometry(QtCore.QRect(225, 5, 105, 25))
        self.h_red3.setStyleSheet(self.Radio_style_2)
        self.h_red3.setObjectName("h_red3")

        self.h_red4.setGeometry(QtCore.QRect(345, 5, 55, 25))
        self.h_red4.setStyleSheet(self.Radio_style_2)
        self.h_red4.setChecked(True)
        self.h_red4.setObjectName("h_red4")

        self.frame_rj.setGeometry(QtCore.QRect(5, 225, 405, 40))
        self.frame_rj.setStyleSheet("border: none")
        self.frame_rj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rj.setObjectName("frame_rj")

        self.j_red0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.j_red0.setFont(self.font_l_40)
        self.j_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_red0.setObjectName("j_red0")

        self.j_red1.setGeometry(QtCore.QRect(35, 5, 100, 25))
        self.j_red1.setStyleSheet(self.Radio_style_2)
        self.j_red1.setObjectName("j_red1")

        self.j_red2.setGeometry(QtCore.QRect(145, 5, 65, 25))
        self.j_red2.setStyleSheet(self.Radio_style_2)
        self.j_red2.setObjectName("j_red2")

        self.j_red3.setGeometry(QtCore.QRect(225, 5, 105, 25))
        self.j_red3.setStyleSheet(self.Radio_style_2)
        self.j_red3.setObjectName("j_red3")

        self.j_red4.setGeometry(QtCore.QRect(345, 5, 55, 25))
        self.j_red4.setStyleSheet(self.Radio_style_2)
        self.j_red4.setChecked(True)
        self.j_red4.setObjectName("j_red4")

        self.frame_wh.setGeometry(QtCore.QRect(5, 175, 405, 40))
        self.frame_wh.setStyleSheet("border-color: None;")
        self.frame_wh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wh.setObjectName("frame_wh")

        self.h_white0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.h_white0.setFont(self.font_l_20)
        self.h_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_white0.setObjectName("h_white0")

        self.h_white1.setGeometry(QtCore.QRect(35, 5, 100, 25))
        self.h_white1.setStyleSheet(self.Radio_style_1)
        self.h_white1.setObjectName("h_white1")

        self.h_white2.setGeometry(QtCore.QRect(145, 5, 65, 25))
        self.h_white2.setStyleSheet(self.Radio_style_1)
        self.h_white2.setObjectName("h_white2")

        self.h_white3.setGeometry(QtCore.QRect(225, 5, 105, 25))
        self.h_white3.setStyleSheet(self.Radio_style_1)
        self.h_white3.setObjectName("h_white3")

        self.h_white4.setGeometry(QtCore.QRect(345, 5, 55, 25))
        self.h_white4.setStyleSheet(self.Radio_style_1)
        self.h_white4.setChecked(True)
        self.h_white4.setObjectName("h_white4")

        self.frame_wj.setGeometry(QtCore.QRect(5, 225, 405, 40))
        self.frame_wj.setStyleSheet("border-color: None;")
        self.frame_wj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wj.setObjectName("frame_wj")

        self.j_white0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.j_white0.setFont(self.font_l_40)
        self.j_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_white0.setObjectName("j_white0")

        self.j_white1.setGeometry(QtCore.QRect(35, 5, 100, 25))
        self.j_white1.setStyleSheet(self.Radio_style_1)
        self.j_white1.setObjectName("j_white1")

        self.j_white2.setGeometry(QtCore.QRect(145, 5, 65, 25))
        self.j_white2.setStyleSheet(self.Radio_style_1)
        self.j_white2.setObjectName("j_white2")

        self.j_white3.setGeometry(QtCore.QRect(225, 5, 105, 25))
        self.j_white3.setStyleSheet(self.Radio_style_1)
        self.j_white3.setObjectName("j_white3")

        self.j_white4.setGeometry(QtCore.QRect(345, 5, 55, 25))
        self.j_white4.setStyleSheet(self.Radio_style_1)
        self.j_white4.setChecked(True)
        self.j_white4.setObjectName("j_white4")

        # --------------------------------------

        self.btn_show_screen.setGeometry(QtCore.QRect(405, 475, 90, 50))
        self.btn_show_screen.setStyleSheet(self.btn_style_1)
        self.btn_show_screen.setFont(self.font_m_13)
        self.btn_show_screen.setObjectName("btn_show_screen")
        self.btn_show_screen.setToolTip('Отобразить экран со спортсменами поверх экрана с очками')

        self.frm_spman_white.setGeometry(QtCore.QRect(0, 420, 450, 140))
        self.frm_spman_white.setStyleSheet("background-color: None;")
        self.frm_spman_white.setObjectName("frm_spman_white")

        self.label_name_white_1.setGeometry(QtCore.QRect(50, 0, 350, 40))
        self.label_name_white_1.setFont(self.font_m_33)
        self.label_name_white_1.setStyleSheet("color: grey; border: none;")
        self.label_name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_white_1.setObjectName("label_name_white_1")

        self.label_region_white_1.setGeometry(QtCore.QRect(100, 40, 250, 20))
        self.label_region_white_1.setFont(self.font_m_13)
        self.label_region_white_1.setStyleSheet("color: grey; border: none;")
        self.label_region_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_white_1.setObjectName("label_region_white_1")

        self.lineEdit_name_white_1.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.lineEdit_name_white_1.setStyleSheet(self.LEdit_style_1)
        self.lineEdit_name_white_1.setFont(self.font_l_20)
        self.lineEdit_name_white_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_white_1.setObjectName("lineEdit_name_white_1")

        self.le_comboBox_name_white_1.hide()
        self.le_comboBox_name_white_1.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.le_comboBox_name_white_1.setStyleSheet(self.combo_style_2)
        self.le_comboBox_name_white_1.setFont(self.font_l_13)
        self.le_comboBox_name_white_1.setObjectName("le_comboBox_name_white_1")

        self.lineEdit_region_white_1.setGeometry(QtCore.QRect(75, 100, 300, 30))
        self.lineEdit_region_white_1.setStyleSheet(self.combo_style_2)
        self.lineEdit_region_white_1.setFont(self.font_l_13)
        self.lineEdit_region_white_1.setObjectName("lineEdit_region_white_1")

        self.frm_spman_red.setGeometry(QtCore.QRect(450, 420, 450, 140))
        self.frm_spman_red.setStyleSheet("background-color: None;")
        self.frm_spman_red.setObjectName("frm_spman_red")

        self.label_name_red_1.setGeometry(QtCore.QRect(50, 0, 350, 40))
        self.label_name_red_1.setFont(self.font_m_33)
        self.label_name_red_1.setStyleSheet("color: grey; border: none;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(100, 40, 250, 20))
        self.label_region_red_1.setFont(self.font_m_13)
        self.label_region_red_1.setStyleSheet("color: grey; border: none;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.lineEdit_name_red_1.setStyleSheet(self.LEdit_style_1)
        self.lineEdit_name_red_1.setFont(self.font_l_20)
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.le_comboBox_name_red_1.hide()
        self.le_comboBox_name_red_1.setGeometry(QtCore.QRect(50, 60, 350, 30))
        self.le_comboBox_name_red_1.setStyleSheet(self.combo_style_2)
        self.le_comboBox_name_red_1.setFont(self.font_l_13)
        self.le_comboBox_name_red_1.setObjectName("le_comboBox_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(75, 100, 300, 30))
        self.lineEdit_region_red_1.setStyleSheet(self.combo_style_2)
        self.lineEdit_region_red_1.setFont(self.font_l_13)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        #################### ЕСЛИ ЗАГРУЖЕН СВОДНЫЙ СПИСОК
        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 565, 900, 105))
        self.frame_sportsmans.setStyleSheet("background-color: None;")
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.pers_com_lbl.setGeometry(QtCore.QRect(178, 0, 7, 13))
        self.pers_com_lbl.setFont(self.font_b_13)
        self.pers_com_lbl.setStyleSheet("color: black;")
        self.pers_com_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pers_com_lbl.setObjectName("pers_com_lbl")

        self.pers_lbl.setGeometry(QtCore.QRect(97, 0, 80, 13))
        self.pers_lbl.setFont(self.font_b_13)
        self.pers_lbl.setStyleSheet("color: black;")
        self.pers_lbl.setAlignment(QtCore.Qt.AlignRight)
        self.pers_lbl.setObjectName("pers_lbl")

        self.com_lbl.setGeometry(QtCore.QRect(186, 0, 80, 13))
        self.com_lbl.setFont(self.font_l_13)
        self.com_lbl.setStyleSheet("color: grey;")
        self.com_lbl.setAlignment(QtCore.Qt.AlignLeft)
        self.com_lbl.setObjectName("com_lbl")

        self.pers_com_qbx.setGeometry(QtCore.QRect(155, 20, 50, 25))
        self.pers_com_qbx.setStyleSheet(self.pers_com_qbx_style_1)
        self.pers_com_qbx.setObjectName("pers_com_lbl")

        self.frame_sex.setGeometry(QtCore.QRect(270, 20, 151, 25))
        self.frame_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sex.setObjectName("frame_sex")

        self.male.setGeometry(QtCore.QRect(20, 0, 40, 25))
        self.male.setFont(self.font_m_20)
        self.male.setObjectName("male")

        self.female.setGeometry(QtCore.QRect(90, 0, 40, 25))
        self.female.setFont(self.font_m_20)
        self.female.setObjectName("female")

        self.sex_1.setGeometry(QtCore.QRect(330, 0, 50, 13))
        self.sex_1.setFont(self.font_b_13)
        self.sex_1.setStyleSheet("color: black;")
        self.sex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_1.setObjectName("sex_1")

        self.age_1.setGeometry(QtCore.QRect(490, 0, 110, 13))
        self.age_1.setFont(self.font_l_13)
        self.age_1.setStyleSheet("color: grey;")
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(490, 20, 110, 22))
        self.comboBox_age.setFont(self.font_l_13)
        self.comboBox_age.setObjectName("comboBox_age")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(470, 70, 390, 25))
        self.comboBox_name_red_1.setFont(self.font_l_12)
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.comboBox_name_white_1.setEnabled(False)
        self.comboBox_name_white_1.setGeometry(QtCore.QRect(40, 70, 390, 25))
        self.comboBox_name_white_1.setFont(self.font_l_12)
        self.comboBox_name_white_1.setObjectName("comboBox_name_white_1")

        self.name_red_1.setGeometry(QtCore.QRect(470, 50, 390, 16))
        self.name_red_1.setFont(self.font_l_13)
        self.name_red_1.setStyleSheet("color: grey;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.name_white_1.setGeometry(QtCore.QRect(40, 50, 390, 16))
        self.name_white_1.setFont(self.font_l_13)
        self.name_white_1.setStyleSheet("color: grey;")
        self.name_white_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_white_1.setObjectName("name_white_1")

        # --------------------------------------

        # --------------------------------------

        self.frame_pyatnov.setGeometry(QtCore.QRect(0, 560, 900, 50))
        self.frame_pyatnov.setStyleSheet("background-color: None;")
        self.frame_pyatnov.setObjectName("frame_pyatnov")

        self.pyatnov_name.setEnabled(False)
        self.pyatnov_name.setGeometry(QtCore.QRect(270, 12, 500, 25))
        self.pyatnov_name.setStyleSheet(self.combo_style_2)
        self.pyatnov_name.setFont(self.font_l_16)
        self.pyatnov_name.setObjectName("pyatnov_name")

        self.pyatnov_label.setGeometry(QtCore.QRect(150, 12, 110, 25))
        self.pyatnov_label.setFont(self.font_l_13)
        self.pyatnov_label.setStyleSheet("color: grey;")
        self.pyatnov_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pyatnov_label.setObjectName("pyatnov_label")

        QtCore.QMetaObject.connectSlotsByName(self.Form2)

        self.KumiteSecondWindow = KumiteSecondWindow()
        self.KumiteSWindow_Ui = KumiteSWindow_Ui()

        self.lcd1.setNumDigits(5)
        self.KumiteSecondWindow.lcd2.setNumDigits(5)
        self.timeRound()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.sound_gong1 = QSound(":/Audio/gong1.wav")
        self.sound_gong2 = QSound(":/Audio/gong2.wav")
        self.slider.valueChanged.connect(self.timeRound)

        self.Frame_Header = Frame_Header(self)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(self.Frame_Header)
        self.layout2.addWidget(self.Form2, 1)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint)

    def calc_display_moveCoord(self, display_coord_x1, display_coord_y1, display_width, display_height,
                               display_coord_x1_secW, display_coord_y1_secW):


        self.KumiteSecondWindow.move(display_coord_x1_secW, display_coord_y1_secW)
        self.KumiteSecondWindow.show()
        self.show()
        coord_x1 = display_coord_x1 + (display_width - self.size().width()) // 2
        coord_y1 = display_coord_y1 + (display_height - self.size().height()) // 2
        self.move(coord_x1, coord_y1)
        print('________________________ calc_display_moveCoord', display_coord_x1, display_coord_y1, display_width,
              display_height, display_coord_x1_secW, display_coord_y1_secW, self.size().width(), self.size().height())

    def closeSecondWin(self):
        self.show_screen()
        self.KumiteSecondWindow.close()
        self.close()

    def timeRound(self):
        if self.slider.value() == 1:
            self.lcd1.display('01:00')
            self.KumiteSecondWindow.lcd2.display('01:00')
            self.datetime = datetime.strptime(str('01:00'), '%M:%S')
            self.tics = self.datetime
            self.label_1min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 2:
            self.lcd1.display('01:30')
            self.KumiteSecondWindow.lcd2.display('01:30')
            self.datetime = datetime.strptime(str('01:30'), '%M:%S')
            self.tics = self.datetime
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 3:
            self.lcd1.display('02:00')
            self.KumiteSecondWindow.lcd2.display('02:00')
            self.datetime = datetime.strptime(str('02:00'), '%M:%S')
            self.tics = self.datetime
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 4:
            self.lcd1.display('03:00')
            self.KumiteSecondWindow.lcd2.display('03:00')
            self.datetime = datetime.strptime(str('03:00'), '%M:%S')
            self.tics = self.datetime
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 5:
            self.lcd1.display('05:00')
            self.KumiteSecondWindow.lcd2.display('05:00')
            self.datetime = datetime.strptime(str('05:00'), '%M:%S')
            self.tics = self.datetime
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Medium;")

    def upTime(self):
        self.show_screen()
        if datetime.strptime(str('00:00'), '%M:%S') <= self.tics < self.datetime:
            if self.btn_start.text() == '▇ STOP':
                self.tics += timedelta(seconds=1)
                self.lcd1.display(str(self.tics).split()[1])
                self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            elif self.btn_start.text() == '► START':
                self.tics += timedelta(seconds=2)
                self.lcd1.display(str(self.tics).split()[1])
                self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            else:
                pass
        if self.btn_start.text() == 'Раунд\nзавершен':
            self.tics += timedelta(seconds=2)
            self.lcd1.display(str(self.tics).split()[1])
            self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            self.btn_start.setText('► START')

    def downTime(self):
        self.show_screen()
        if datetime.strptime(str('00:00'), '%M:%S') < self.tics <= self.datetime:
            if self.btn_start.text() == '▇ STOP':
                self.tics -= timedelta(seconds=1)
                self.lcd1.display(str(self.tics).split()[1])
                self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            elif self.btn_start.text() == '► START':
                self.tics -= timedelta(seconds=2)
                self.lcd1.display(str(self.tics).split()[1])
                self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            else:
                pass
        if self.tics > self.datetime:
            self.tics -= timedelta(seconds=2)
            self.lcd1.display(str(self.tics).split()[1])
            self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            self.btn_start.setText('► START')

    def update_time(self):
        self.show_screen()
        self.timer.start(1000)
        self.tics -= timedelta(seconds=1)
        self.lcd1.display(str(self.tics).split()[1])
        self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])

        if self.tics == datetime.strptime(str('00:30'), '%M:%S'):
            self.sound_gong1.play()

        if self.tics <= datetime.strptime(str('00:00'), '%M:%S'):
            self.tics = datetime.strptime(str('00:00'), '%M:%S')
            self.sound_gong2.play()
            self.timer.stop()
            self.btn_start.setText('Раунд\nзавершен')
            self.lcd1.display(str(self.tics).split()[1])
            self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])

    def start_timer(self):
        self.show_screen()
        if self.btn_start.text() == '► START':
            self.btn_start.setText('▇ STOP')
            self.timer.start(1000)
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            self.btn_pause.setFont(self.font_m_13)
            self.btn_reset.setFont(self.font_m_13)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)
        else:
            self.timer.stop()
            self.btn_start.setText('► START')
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            self.btn_pause.setFont(self.font_m_13)
            self.btn_reset.setFont(self.font_m_13)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)

    def reset_timer(self):
        self.show_screen()
        if self.btn_start.text() != '► START':
            self.btn_pause.setText('Останови бой')
            self.btn_pause.setStyleSheet("color: red")
            self.btn_pause.setToolTip('Сперва нужно остановить бой')
        else:
            self.timeRound()
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            self.btn_pause.setFont(self.font_m_13)
            self.btn_reset.setFont(self.font_m_13)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)
            self.btn_pause.setToolTip('Сбросить только секундомер')
            self.btn_reset.setToolTip('Сбросить всё')

    def clearKumiteData(self):
        self.show_screen()
        if self.btn_start.text() != '► START':
            self.btn_reset.setText('Останови бой')
            self.btn_reset.setStyleSheet("color: red")
            self.btn_pause.setToolTip('Сперва нужно остановить бой')
        else:
            self.reset_all()
            self.btn_pause.setToolTip('Сбросить только секундомер')
            self.btn_reset.setToolTip('Сбросить всё')

    def NewCategory(self):
        self.comboBox_age.clear()
        self.comboBox_name_red_1.clear()
        self.comboBox_name_white_1.clear()
        self.comboBox_age.setEnabled(False)
        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_white_1.setEnabled(False)
        self.male.setAutoExclusive(False)
        self.female.setAutoExclusive(False)
        self.male.setChecked(False)
        self.female.setChecked(False)
        self.male.setAutoExclusive(True)
        self.female.setAutoExclusive(True)

        self.name_red_1.setFont(self.font_l_13)
        self.name_red_1.setStyleSheet("color: grey;")
        self.name_white_1.setFont(self.font_l_13)
        self.name_white_1.setStyleSheet("color: grey;")
        self.age_1.setFont(self.font_l_13)
        self.age_1.setStyleSheet("color: grey;")

        self.matchName12.setText('Возраст')
        if len(self.KumiteSecondWindow.matchName21.text().split(', ')) > 1:
            self.KumiteSecondWindow.matchName21.setText(self.KumiteSecondWindow.matchName21.text().split(', ')[0])

    def resetSportsmanFramePosition(self):
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)

        self.KumiteSecondWindow.sportsman_screen.setGeometry(self.KumiteSWindow_Ui.coo_screen_std)
        self.KumiteSecondWindow.screen_frame_red.setGeometry(self.KumiteSWindow_Ui.coo_screen_red_std)
        self.KumiteSecondWindow.screen_frame_white.setGeometry(self.KumiteSWindow_Ui.coo_screen_white_std)

        self.KumiteSecondWindow.frame_red2.setGeometry(self.KumiteSWindow_Ui.coo_frame_red2_std)
        self.KumiteSecondWindow.frame_background_red22_red2.setGeometry(QtCore.QRect(0, 430, 880, 350))
        self.KumiteSecondWindow.label_score21.setGeometry(QtCore.QRect(0, 0, 500, 420))
        self.KumiteSecondWindow.background_red21.setGeometry(QtCore.QRect(0, 0, 500, 450))

        self.KumiteSecondWindow.frame_white2.setGeometry(self.KumiteSWindow_Ui.coo_frame_white2_std)
        self.KumiteSecondWindow.frame_background_white22_white2.setGeometry(QtCore.QRect(0, 430, 880, 350))
        self.KumiteSecondWindow.label_score22.setGeometry(QtCore.QRect(380, 0, 500, 420))
        self.KumiteSecondWindow.background_white21.setGeometry(QtCore.QRect(380, 0, 500, 450))

        self.KumiteSecondWindow.lcd2.show()
        self.KumiteSecondWindow.frame_white2.show()
        self.KumiteSecondWindow.label_winner.hide()
        self.KumiteSecondWindow.frame_red2.show()
        self.KumiteSecondWindow.sportsman_screen.hide()
        self.KumiteSecondWindow.screen_frame_white.show()
        self.KumiteSecondWindow.screen_frame_red.show()
        self.show_screen()


    def reset_all(self, flags_dict=''):
        if flags_dict:
            self.flags_dict = flags_dict
        self.timer.stop()
        self.timeRound()
        self.j_red4.clicked.connect(self.penaltyButton_jr4)
        self.h_white4.clicked.connect(self.penaltyButton_hmw4)
        self.j_white4.clicked.connect(self.penaltyButton_jw4)

        self.KumiteSecondWindow.label_name_white_2.setGeometry(self.KumiteSecondWindow.coo_label_name_white)
        self.KumiteSecondWindow.label_name_red_2.setGeometry(self.KumiteSecondWindow.coo_label_name_red)
        self.KumiteSecondWindow.flag_red.hide()
        self.KumiteSecondWindow.flag_white.hide()

        self.resetSportsmanFramePosition()

        self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
        self.btn_reset.setText('НОВЫЙ БОЙ')
        self.btn_pause.setFont(self.font_m_13)
        self.btn_reset.setFont(self.font_m_13)
        self.btn_pause.setStyleSheet(self.btn_style_1)
        self.btn_reset.setStyleSheet(self.btn_style_1)
        self.label_score11.setText('0')
        self.KumiteSecondWindow.label_score21.setText('0')
        self.label_score12.setText('0')
        self.KumiteSecondWindow.label_score22.setText('0')
        self.KumiteSecondWindow.label_name_white_2.clear()
        self.KumiteSecondWindow.label_name_red_2.clear()

        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_region_red_1.setText("регион")
        self.label_name_white_1.setText("ФАМИЛИЯ")
        self.label_region_white_1.setText("регион")
        self.lineEdit_name_red_1.clear()
        self.lineEdit_name_white_1.clear()
        self.comboBox_name_red_1.clear()
        try:
            self.lineEdit_region_red_1.lineEdit().clear()
            self.lineEdit_region_white_1.lineEdit().clear()
        except:
            self.lineEdit_region_red_1.clear()
            self.lineEdit_region_white_1.clear()
        self.score_red_0.setChecked(True)
        self.score_white_0.setChecked(True)

        self.h_red4.setChecked(True)
        self.j_red4.setChecked(True)
        self.h_white4.setChecked(True)
        self.j_white4.setChecked(True)
        self.setStyleButton(self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                            self.KumiteSecondWindow.hm_r3)
        self.KumiteSecondWindow.label_kum_hmr0.setText(None)
        self.setStyleButton(self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                            self.KumiteSecondWindow.j_r3)
        self.KumiteSecondWindow.label_kum_jr0.setText(None)
        self.setStyleButton(self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                            self.KumiteSecondWindow.hm_w3)
        self.KumiteSecondWindow.label_kum_hmw0.setText(None)
        self.setStyleButton(self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                            self.KumiteSecondWindow.j_w3)
        self.KumiteSecondWindow.label_kum_jw0.setText(None)

    def setWinner(self):
        self.show_screen()
        radio = self.sender()
        if radio.isChecked():
            if radio.text() == "Победил АКА":
                self.KumiteSecondWindow.frame_red2.setGeometry(self.KumiteSWindow_Ui.coo_frame_win)
                self.KumiteSecondWindow.label_score21.setGeometry(QtCore.QRect(300, 360, 380, 420))
                self.KumiteSecondWindow.background_red21.setGeometry(QtCore.QRect(300, 360, 380, 420))
                self.KumiteSecondWindow.frame_background_red22_red2.setGeometry(QtCore.QRect(660, 430, 880, 350))
                self.KumiteSecondWindow.lcd2.hide()
                self.KumiteSecondWindow.label_winner.show()

                self.KumiteSecondWindow.frame_red2.show()
                self.KumiteSecondWindow.frame_white2.hide()
                self.winnerWhite.setChecked(False)

                self.KumiteSecondWindow.sportsman_screen.show()
                self.KumiteSecondWindow.screen_frame_red.show()
                self.KumiteSecondWindow.screen_frame_white.hide()
                self.KumiteSecondWindow.sportsman_screen.setGeometry(self.KumiteSWindow_Ui.coo_screen_win)
                self.KumiteSecondWindow.screen_frame_red.setGeometry(self.KumiteSWindow_Ui.coo_screen_frm_win)

            elif radio.text() == "Победил СИРО":
                self.KumiteSecondWindow.frame_white2.setGeometry(self.KumiteSWindow_Ui.coo_frame_win)
                self.KumiteSecondWindow.label_score22.setGeometry(QtCore.QRect(300, 360, 380, 420))
                self.KumiteSecondWindow.background_white21.setGeometry(QtCore.QRect(300, 360, 380, 420))
                self.KumiteSecondWindow.frame_background_white22_white2.setGeometry(QtCore.QRect(660, 430, 880, 350))
                self.KumiteSecondWindow.lcd2.hide()
                self.KumiteSecondWindow.label_winner.show()

                self.KumiteSecondWindow.frame_white2.show()
                self.KumiteSecondWindow.frame_red2.hide()
                self.winnerRed.setChecked(False)

                self.KumiteSecondWindow.sportsman_screen.show()
                self.KumiteSecondWindow.screen_frame_white.show()
                self.KumiteSecondWindow.screen_frame_red.hide()
                self.KumiteSecondWindow.sportsman_screen.setGeometry(self.KumiteSWindow_Ui.coo_screen_win)
                self.KumiteSecondWindow.screen_frame_white.setGeometry(self.KumiteSWindow_Ui.coo_screen_frm_win)

    def onClickedR(self):
        radio = self.sender()
        if radio.isChecked():
            self.label_score11.setText(radio.text())
            self.KumiteSecondWindow.label_score21.setText(radio.text())

    def onClickedW(self):
        radio = self.sender()
        if radio.isChecked():
            self.label_score12.setText(radio.text())
            self.KumiteSecondWindow.label_score22.setText(radio.text())

    def penaltyButton_hmr1(self):
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                                self.KumiteSecondWindow.hm_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr2(self):
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                                self.KumiteSecondWindow.hm_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr3(self):
        # self.show_screen()
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                                self.KumiteSecondWindow.hm_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr4(self):
        # self.show_screen()
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                                self.KumiteSecondWindow.hm_r3)
            self.KumiteSecondWindow.label_kum_hmr0.setText(None)

    def penaltyButton_jr1(self):
        # self.show_screen()
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                                self.KumiteSecondWindow.j_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr2(self):
        # self.show_screen()
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                                self.KumiteSecondWindow.j_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr3(self):
        # self.show_screen()
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                                self.KumiteSecondWindow.j_r3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr4(self):
        # self.show_screen()
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                                self.KumiteSecondWindow.j_r3)
            self.KumiteSecondWindow.label_kum_jr0.setText(None)

    def penaltyButton_hmw1(self):
        # self.show_screen()
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                                self.KumiteSecondWindow.hm_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw2(self):
        # self.show_screen()
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                                self.KumiteSecondWindow.hm_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw3(self):
        # self.show_screen()
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                                self.KumiteSecondWindow.hm_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw4(self):
        # self.show_screen()
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                                self.KumiteSecondWindow.hm_w3)
            self.KumiteSecondWindow.label_kum_hmw0.setText(None)

    def penaltyButton_jw1(self):
        # self.show_screen()
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                                self.KumiteSecondWindow.j_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw2(self):
        # self.show_screen()
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                                self.KumiteSecondWindow.j_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw3(self):
        # self.show_screen()
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                                self.KumiteSecondWindow.j_w3,
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;',
                                'background-color: black; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw4(self):
        # self.show_screen()
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                                self.KumiteSecondWindow.j_w3)
            self.KumiteSecondWindow.label_kum_jw0.setText(None)

    def setStyleButton(self, rad_S1, rad_S2, rad_S3,
                       rad_S1_FontSize='border-radius: 30px; border: 4px solid grey;',
                       rad_S2_FontSize='border-radius: 30px; border: 4px solid grey;',
                       rad_S3_FontSize='border-radius: 30px; border: 4px solid grey;'):
        rad_S1.setStyleSheet(rad_S1_FontSize)
        rad_S2.setStyleSheet(rad_S2_FontSize)
        rad_S3.setStyleSheet(rad_S3_FontSize)

    def setRegionsFlags(self, region_white, region_red):
        try:
            region_white = region_white.split(' - ком')[0].replace(" ", "").lower()
            region_red = region_red.split(' - ком')[0].replace(" ", "").lower()

            if region_white in self.flags_dict.keys() and region_red in self.flags_dict.keys():
                self.KumiteSecondWindow.label_name_white_2.setGeometry(self.KumiteSecondWindow.coo_label_name_white_flag)
                self.KumiteSecondWindow.label_name_red_2.setGeometry(self.KumiteSecondWindow.coo_label_name_red_flag)
                self.KumiteSecondWindow.flag_white.show()
                self.KumiteSecondWindow.flag_red.show()

                img_white = QtGui.QPixmap(f":/Images/icon_regions/flags/{self.flags_dict[region_white]}.svg")
                img_red = QtGui.QPixmap(f":/Images/icon_regions/flags/{self.flags_dict[region_red]}.svg")
                self.KumiteSecondWindow.icon_white.setPixmap(img_white)
                self.KumiteSecondWindow.icon_red.setPixmap(img_red)
            else:
                self.KumiteSecondWindow.label_name_white_2.setGeometry(self.KumiteSecondWindow.coo_label_name_white)
                self.KumiteSecondWindow.label_name_red_2.setGeometry(self.KumiteSecondWindow.coo_label_name_red)
                self.KumiteSecondWindow.flag_red.hide()
                self.KumiteSecondWindow.flag_white.hide()

        except Exception as e:
            print('setRegionsFlags   ', e)

    def setMatchName(self):
        try:
            firstWindowMatchName1 = self.matchName11.fontMetrics().boundingRect(self.matchName11.text()).width()
            firstWindowMatchName2 = self.matchName12.fontMetrics().boundingRect(self.matchName12.text()).width()
            firstWindowMatchName = firstWindowMatchName1 + firstWindowMatchName2
            if firstWindowMatchName > 356:
                n = "font-family: Gotham-Medium; font-size: " \
                    + str(int(17.8 * (1880 / firstWindowMatchName))) + "px; color: grey;"
                self.KumiteSecondWindow.matchName21.setStyleSheet(n)
            else:
                self.KumiteSecondWindow.matchName21.setStyleSheet(
                    "font-family: Gotham-Medium; font-size: 100px; color: grey;")
            self.KumiteSecondWindow.matchName21.setText(self.matchName11.text() + ", " + self.matchName12.text())
        except Exception as e:
            print('setMatchName   ', e)

    def setSportsmanName(self):
        try:
            self.setMatchName()
            lrwhi = self.lineEdit_region_white_1.currentText()
            lrred = self.lineEdit_region_red_1.currentText()
            self.setRegionsFlags(lrwhi, lrred)

            self.label_name_red_1.setText(self.lineEdit_name_red_1.text())
            self.label_region_red_1.setText(lrred)
            self.KumiteSecondWindow.label_name_red_2.setText(self.lineEdit_name_red_1.text())
            self.KumiteSecondWindow.screen_label_name_red.setText(self.lineEdit_name_red_1.text())
            self.KumiteSecondWindow.screen_label_region_red.setText(lrred)
            self.label_name_white_1.setText(self.lineEdit_name_white_1.text())
            self.label_region_white_1.setText(lrwhi)
            self.KumiteSecondWindow.label_name_white_2.setText(self.lineEdit_name_white_1.text())
            self.KumiteSecondWindow.screen_label_name_white.setText(self.lineEdit_name_white_1.text())
            self.KumiteSecondWindow.screen_label_region_white.setText(lrwhi)

            self.resetSportsmanFramePosition()

            first_window_name_red = self.label_name_red_1.fontMetrics().boundingRect(
                self.label_name_red_1.text()).width()
            screen_window_name_red = first_window_name_red
            first_window_region_red = self.label_region_red_1.fontMetrics().boundingRect(
                self.label_region_red_1.text()).width()

            first_window_name_white = self.label_name_white_1.fontMetrics().boundingRect(
                self.label_name_white_1.text()).width()
            screen_window_name_white = first_window_name_white
            first_window_region_white = self.label_region_white_1.fontMetrics().boundingRect(
                self.label_region_white_1.text()).width()

            if self.KumiteSecondWindow.flag_red.isVisible():
                first_window_name_length = 0.95
            else:
                first_window_name_length = 1

            if max(first_window_name_white, first_window_name_red) > 237*2:
                max_value = max(first_window_name_white, first_window_name_red)

                custom_font = QtGui.QFont()
                custom_font.setFamily("Gotham-Medium")
                custom_font.setPixelSize(int(300/(4.167/2) * (198 / max_value) * first_window_name_length))
                self.KumiteSecondWindow.label_name_white_2.setFont(custom_font)
                self.KumiteSecondWindow.label_name_red_2.setFont(custom_font)

            else:
                self.KumiteSecondWindow.label_name_white_2.setFont(self.KumiteSecondWindow.font_m_60)
                self.KumiteSecondWindow.label_name_red_2.setFont(self.KumiteSecondWindow.font_m_60)

            if max(screen_window_name_white, screen_window_name_red) > 237:
                max_value = max(screen_window_name_white, screen_window_name_red)

                custom_font = QtGui.QFont()
                custom_font.setFamily("Gotham-Medium")
                custom_font.setPixelSize(int(300 * (198 / max_value)))
                self.KumiteSecondWindow.screen_label_name_white.setFont(custom_font)
                self.KumiteSecondWindow.screen_label_name_red.setFont(custom_font)

            else:
                self.KumiteSecondWindow.screen_label_name_white.setFont(self.KumiteSecondWindow.font_b_250)
                self.KumiteSecondWindow.screen_label_name_red.setFont(self.KumiteSecondWindow.font_b_250)

            if max(first_window_region_white, first_window_region_red) > 93:
                max_value = max(first_window_region_white, first_window_region_red)

                custom_font = QtGui.QFont()
                custom_font.setFamily("Gotham-Light")
                custom_font.setPixelSize(int(150 * (155 / max_value)))
                self.KumiteSecondWindow.screen_label_region_white.setFont(custom_font)
                self.KumiteSecondWindow.screen_label_region_red.setFont(custom_font)
            else:
                self.KumiteSecondWindow.screen_label_region_white.setFont(self.KumiteSecondWindow.font_l_150)
                self.KumiteSecondWindow.screen_label_region_red.setFont(self.KumiteSecondWindow.font_l_150)
        except Exception as e:
            print('kum setSportsmanName:', e)

    def show_screen(self, force_hide=1):
        try:
            if self.btn_show_screen.text() == 'Показать\nэкран ФИО' and not force_hide:
                self.setSportsmanName()
                self.resetSportsmanFramePosition()
                self.KumiteSecondWindow.sportsman_screen.show()
                self.btn_show_screen.setText('Скрыть\nэкран ФИО')
                self.btn_show_screen.setStyleSheet("color: red")
                self.btn_show_screen.setToolTip('Скрыть экран с ФИО, отобразится экран с очками')
            else:
                self.KumiteSecondWindow.sportsman_screen.hide()
                self.btn_show_screen.setText('Показать\nэкран ФИО')
                self.btn_show_screen.setStyleSheet(self.btn_style_1)
                self.btn_show_screen.setToolTip('Отобразить экран со спортсменами поверх экрана с очками')
        except Exception as e:
            print('kum show_screen:', e)


class dialogWindow_Ui(object):
    def setupUi_dialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 150, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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
