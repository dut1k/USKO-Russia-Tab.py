from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication, QLineEdit, \
    QVBoxLayout, QLCDNumber, QSlider
from PyQt5.QtMultimedia import QSound
from datetime import datetime, timedelta


class KumiteSWindow_Ui(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: white;")
        Form.resize(1920, 1080)

        self.lcd2 = QtWidgets.QLCDNumber(Form)
        self.line2 = QtWidgets.QFrame(Form)
        self.label_score21 = QtWidgets.QLabel(Form)
        self.label_score22 = QtWidgets.QLabel(Form)
        self.frame_red2 = QtWidgets.QFrame(Form)
        self.label_kum_hmr0 = QtWidgets.QLabel(Form)
        self.label_kum_hmr1 = QtWidgets.QLabel(Form)
        self.frame = QtWidgets.QFrame(Form)
        self.label_kum_jr0 = QtWidgets.QLabel(Form)
        self.hm_r1 = QtWidgets.QLabel(self.frame)
        self.hm_r2 = QtWidgets.QLabel(self.frame)
        self.hm_r3 = QtWidgets.QLabel(self.frame)
        self.label_kum_jr1 = QtWidgets.QLabel(Form)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.j_r1 = QtWidgets.QLabel(self.frame_2)
        self.j_r2 = QtWidgets.QLabel(self.frame_2)
        self.j_r3 = QtWidgets.QLabel(self.frame_2)
        self.label_kum_hmw0 = QtWidgets.QLabel(Form)
        self.label_kum_hmw1 = QtWidgets.QLabel(Form)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.hm_w1 = QtWidgets.QLabel(self.frame_3)
        self.hm_w2 = QtWidgets.QLabel(self.frame_3)
        self.hm_w3 = QtWidgets.QLabel(self.frame_3)
        self.label_kum_jw0 = QtWidgets.QLabel(Form)
        self.label_kum_jw1 = QtWidgets.QLabel(Form)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.j_w1 = QtWidgets.QLabel(self.frame_4)
        self.j_w2 = QtWidgets.QLabel(self.frame_4)
        self.j_w3 = QtWidgets.QLabel(self.frame_4)

        self.lcd2.setGeometry(QtCore.QRect(750, 0, 420, 140))
        self.lcd2.setStyleSheet("background-color: None; border: None")

        self.line2.setGeometry(QtCore.QRect(957, 150, 6, 890))
        font = QtGui.QFont()
        font.setKerning(True)
        self.line2.setFont(font)
        self.line2.setLineWidth(1)
        self.line2.setMidLineWidth(6)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line")

        self.label_score21.setGeometry(QtCore.QRect(305, 150, 350, 450))
        self.label_score21.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; color: white; font-size: 530px;")
        self.label_score21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score21.setObjectName("label_score1")

        self.label_score22.setGeometry(QtCore.QRect(1305, 150, 350, 450))
        self.label_score22.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; font-size: 530px; ")
        self.label_score22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score22.setObjectName("label_score2")

        self.frame_red2.setGeometry(QtCore.QRect(40, 150, 880, 850))
        self.frame_red2.setStyleSheet("background-color: rgb(255, 95, 95);")
        self.frame_red2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red2.setObjectName("frame_red")

        self.label_kum_hmr0.setEnabled(True)
        self.label_kum_hmr0.setGeometry(QtCore.QRect(160, 580, 640, 120))
        self.label_kum_hmr0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_hmr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr0.setObjectName("label_kum_hmr0")

        self.label_kum_hmr1.setEnabled(True)
        self.label_kum_hmr1.setGeometry(QtCore.QRect(40, 700, 180, 71))
        self.label_kum_hmr1.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 70px;")
        self.label_kum_hmr1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr1.setObjectName("label_kum_hmr1")

        self.frame.setGeometry(QtCore.QRect(40, 700, 880, 71))
        self.frame.setStyleSheet("background-color: white; border-color: rgb(0, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.hm_r1.setGeometry(QtCore.QRect(195, 5, 60, 60))
        self.hm_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r1.setObjectName("hm_r1")

        self.hm_r2.setGeometry(QtCore.QRect(410, 5, 60, 60))
        self.hm_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r2.setObjectName("hm_r2")

        self.hm_r3.setGeometry(QtCore.QRect(625, 5, 60, 60))
        self.hm_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r3.setObjectName("hm_r3")

        self.label_kum_jr0.setEnabled(True)
        self.label_kum_jr0.setGeometry(QtCore.QRect(160, 770, 640, 120))
        self.label_kum_jr0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_jr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr0.setObjectName("label_kum_jr0")

        self.label_kum_jr1.setGeometry(QtCore.QRect(40, 890, 180, 71))
        self.label_kum_jr1.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 70px;")
        self.label_kum_jr1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr1.setObjectName("label_kum_jr1")

        self.frame_2.setGeometry(QtCore.QRect(40, 890, 880, 71))
        self.frame_2.setStyleSheet("background-color: white")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setObjectName("frame_2")

        self.j_r1.setGeometry(QtCore.QRect(195, 5, 60, 60))
        self.j_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r1.setObjectName("j_r1")

        self.j_r2.setGeometry(QtCore.QRect(410, 5, 60, 60))
        self.j_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r2.setObjectName("j_r2")

        self.j_r3.setGeometry(QtCore.QRect(625, 5, 60, 60))
        self.j_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r3.setObjectName("j_r3")

        self.label_kum_hmw0.setEnabled(True)
        self.label_kum_hmw0.setGeometry(QtCore.QRect(1160, 580, 640, 120))
        self.label_kum_hmw0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_hmw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw0.setObjectName("label_kum_hmw0")

        self.label_kum_hmw1.setEnabled(True)
        self.label_kum_hmw1.setGeometry(QtCore.QRect(1040, 700, 180, 71))
        self.label_kum_hmw1.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 70px;")
        self.label_kum_hmw1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw1.setObjectName("label_kum_hmw1")

        self.frame_3.setGeometry(QtCore.QRect(1040, 700, 880, 71))
        self.frame_3.setStyleSheet("background-color: white")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setObjectName("frame_3")

        self.hm_w1.setGeometry(QtCore.QRect(195, 5, 60, 60))
        self.hm_w1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w1.setObjectName("hm_w1")

        self.hm_w2.setGeometry(QtCore.QRect(410, 5, 60, 60))
        self.hm_w2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w2.setObjectName("hm_w2")

        self.hm_w3.setGeometry(QtCore.QRect(625, 5, 60, 60))
        self.hm_w3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w3.setObjectName("hm_w3")

        self.label_kum_jw0.setEnabled(True)
        self.label_kum_jw0.setGeometry(QtCore.QRect(1040, 770, 880, 120))
        self.label_kum_jw0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_jw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw0.setObjectName("label_kum_jw0")

        self.label_kum_jw1.setEnabled(True)
        self.label_kum_jw1.setGeometry(QtCore.QRect(1040, 890, 180, 71))
        self.label_kum_jw1.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 70px;")
        self.label_kum_jw1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw1.setObjectName("label_kum_jw1")

        self.frame_4.setGeometry(QtCore.QRect(1040, 890, 880, 71))
        self.frame_4.setStyleSheet("background-color: white")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setObjectName("frame_4")

        self.j_w1.setGeometry(QtCore.QRect(195, 5, 60, 60))
        self.j_w1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w1.setObjectName("j_w1")

        self.j_w2.setGeometry(QtCore.QRect(410, 5, 60, 60))
        self.j_w2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w2.setObjectName("j_w2")

        self.j_w3.setGeometry(QtCore.QRect(625, 5, 60, 60))
        self.j_w3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w3.setObjectName("j_w3")

        self.line2.raise_()
        self.lcd2.raise_()

        self.label_kum_hmr0.raise_()
        self.label_kum_jr0.raise_()
        self.label_kum_hmw0.raise_()
        self.label_kum_jw0.raise_()

        self.frame_2.raise_()
        self.label_score21.raise_()
        self.frame.raise_()

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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " "))
        self.label_kum_hmr0.setText(_translate("Form", None))
        self.label_kum_hmr1.setText(_translate("Form", "H M"))
        self.label_score21.setText(_translate("Form", "0"))
        self.label_kum_jr0.setText(_translate("Form", None))
        self.label_kum_jr1.setText(_translate("Form", "J"))
        self.label_kum_hmw0.setText(_translate("Form", None))
        self.label_kum_hmw1.setText(_translate("Form", "H M"))
        self.label_score22.setText(_translate("Form", "0"))
        self.label_kum_jw0.setText(_translate("Form", None))
        self.label_kum_jw1.setText(_translate("Form", "J"))

class KumiteSecondWindow(QWidget, KumiteSWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)


class KumiteMainWindow_Ui(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form")
        Form2.setEnabled(True)
        Form2.setFixedSize(900, 500)
        Form2.setWindowOpacity(1.0)
        Form2.setToolTipDuration(-1)
        Form2.setStatusTip("")
        Form2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MenuButton = QtWidgets.QPushButton(Form2)
        self.MenuButton.setGeometry(QtCore.QRect(765, 5, 110, 20))
        self.MenuButton.setStyleSheet("background-color: rgb(242, 242, 242); "
                                      "font-family: Gotham-Light; font-size: 10pt;")
        self.MenuButton.setObjectName("MenuButton")

        self.KataQualButton = QtWidgets.QPushButton(Form2)
        self.KataQualButton.setGeometry(QtCore.QRect(765, 30, 110, 20))
        self.KataQualButton.setStyleSheet("background-color: rgb(242, 242, 242); "
                                      "font-family: Gotham-Light; font-size: 10pt;")
        self.KataQualButton.setObjectName("KataQualButton")

        self.KataFinalButton = QtWidgets.QPushButton(Form2)
        self.KataFinalButton.setGeometry(QtCore.QRect(765, 55, 110, 20))
        self.KataFinalButton.setStyleSheet("background-color: rgb(242, 242, 242); "
                                      "font-family: Gotham-Light; font-size: 10pt;")
        self.KataFinalButton.setObjectName("KataFinalButton")

        self.lcd1 = QtWidgets.QLCDNumber(Form2)
        self.lcd1.setGeometry(QtCore.QRect(360, 0, 180, 60))

        self.line1 = QtWidgets.QFrame(Form2)
        self.line1.setGeometry(QtCore.QRect(447, 80, 6, 385))
        self.line1.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.line1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line1.setObjectName("line")

        self.frame_red1 = QtWidgets.QFrame(Form2)
        self.frame_red1.setGeometry(QtCore.QRect(475, 80, 400, 240))
        self.frame_red1.setStyleSheet("background-color: rgb(255, 222, 219);")
        self.frame_red1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red1.setObjectName("frame_red")

        self.label_score11 = QtWidgets.QLabel(self.frame_red1)
        self.label_score11.setGeometry(QtCore.QRect(150, 20, 100, 200))
        self.label_score11.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 135px;")
        self.label_score11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score11.setObjectName("label_score1")

        self.score_red_0 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_0.setGeometry(QtCore.QRect(10, 8, 40, 25))
        self.score_red_0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_0.setChecked(True)
        self.score_red_0.setObjectName("score_red_0")

        self.score_red_1 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_1.setGeometry(QtCore.QRect(10, 41, 40, 25))
        self.score_red_1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_1.setObjectName("score_red_1")

        self.score_red_2 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_2.setGeometry(QtCore.QRect(10, 74, 40, 25))
        self.score_red_2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_2.setObjectName("score_red_2")

        self.score_red_3 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_3.setGeometry(QtCore.QRect(10, 107, 40, 25))
        self.score_red_3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_3.setObjectName("score_red_3")

        self.score_red_4 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_4.setGeometry(QtCore.QRect(10, 140, 40, 25))
        self.score_red_4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_4.setObjectName("score_red_4")

        self.score_red_5 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_5.setGeometry(QtCore.QRect(10, 173, 40, 25))
        self.score_red_5.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_5.setObjectName("score_red_5")

        self.score_red_6 = QtWidgets.QRadioButton(self.frame_red1)
        self.score_red_6.setGeometry(QtCore.QRect(10, 206, 40, 25))
        self.score_red_6.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_6.setObjectName("score_red_6")

        self.frame_white1 = QtWidgets.QFrame(Form2)
        self.frame_white1.setGeometry(QtCore.QRect(25, 80, 400, 240))
        self.frame_white1.setStyleSheet("background-color: white")
        self.frame_white1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white1.setObjectName("frame_white")

        self.label_score12 = QtWidgets.QLabel(self.frame_white1)
        self.label_score12.setGeometry(QtCore.QRect(150, 20, 100, 200))
        self.label_score12.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 135px;")
        self.label_score12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score12.setObjectName("label_score2")

        # self.round_time = QtWidgets.QLabel(Form2)
        # self.round_time.setGeometry(QtCore.QRect(40, 0, 105, 20))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.round_time.setFont(font)
        # self.round_time.setAlignment(QtCore.Qt.AlignCenter)
        # self.round_time.setObjectName("round_time")
        #
        # self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, Form2)
        # self.slider.setGeometry(QtCore.QRect(15, 25, 160, 15))
        # self.slider.setTickInterval(1)
        # self.slider.setRange(1, 5)
        # self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        # self.slider.setTickPosition(QSlider.TicksBothSides)
        # self.slider.setSingleStep(1)
        # self.slider.setPageStep(1)
        # self.slider.setValue(3)
        #
        # self.label_1min = QtWidgets.QLabel(Form2)
        # self.label_1min.setGeometry(QtCore.QRect(0, 40, 35, 14))
        # self.label_1min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        # self.label_1min.setObjectName("label_1min")
        #
        # self.label_15min = QtWidgets.QLabel(Form2)
        # self.label_15min.setGeometry(QtCore.QRect(35, 40, 45, 14))
        # self.label_15min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        # self.label_15min.setObjectName("label_15min")
        #
        # self.label_2min = QtWidgets.QLabel(Form2)
        # self.label_2min.setGeometry(QtCore.QRect(80, 40, 40, 14))
        # self.label_2min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        # self.label_2min.setObjectName("label_2min")
        #
        # self.label_3min = QtWidgets.QLabel(Form2)
        # self.label_3min.setGeometry(QtCore.QRect(120, 40, 35, 14))
        # self.label_3min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        # self.label_3min.setObjectName("label_3min")
        #
        # self.label_5min = QtWidgets.QLabel(Form2)
        # self.label_5min.setGeometry(QtCore.QRect(155, 40, 34, 14))
        # self.label_5min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        # self.label_5min.setObjectName("label_5min")

        self.frame_timeRound = QtWidgets.QFrame(Form2)
        self.frame_timeRound.setGeometry(QtCore.QRect(30, 0, 189, 54))
        self.frame_timeRound.setStyleSheet("background-color: none")
        self.frame_timeRound.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_timeRound.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_timeRound.setObjectName("frame_white")

        self.round_time = QtWidgets.QLabel(self.frame_timeRound)
        self.round_time.setGeometry(QtCore.QRect(40, 0, 105, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.round_time.setFont(font)
        self.round_time.setAlignment(QtCore.Qt.AlignCenter)
        self.round_time.setObjectName("round_time")

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.frame_timeRound)
        self.slider.setGeometry(QtCore.QRect(15, 25, 160, 15))
        self.slider.setTickInterval(1)
        self.slider.setRange(1, 5)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setValue(3)

        self.label_1min = QtWidgets.QLabel(self.frame_timeRound)
        self.label_1min.setGeometry(QtCore.QRect(0, 40, 35, 14))
        self.label_1min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_1min.setObjectName("label_1min")

        self.label_15min = QtWidgets.QLabel(self.frame_timeRound)
        self.label_15min.setGeometry(QtCore.QRect(35, 40, 45, 14))
        self.label_15min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_15min.setObjectName("label_15min")

        self.label_2min = QtWidgets.QLabel(self.frame_timeRound)
        self.label_2min.setGeometry(QtCore.QRect(80, 40, 40, 14))
        self.label_2min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_2min.setObjectName("label_2min")

        self.label_3min = QtWidgets.QLabel(self.frame_timeRound)
        self.label_3min.setGeometry(QtCore.QRect(120, 40, 35, 14))
        self.label_3min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_3min.setObjectName("label_3min")

        self.label_5min = QtWidgets.QLabel(self.frame_timeRound)
        self.label_5min.setGeometry(QtCore.QRect(155, 40, 34, 14))
        self.label_5min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_5min.setObjectName("label_5min")


###########################
        self.plus5sec = QtWidgets.QPushButton(Form2)
        # self.plus5sec.setGeometry(QtCore.QRect(190, 13, 40, 17))
        self.plus5sec.setGeometry(QtCore.QRect(470, 65, 40, 17))
        self.plus5sec.setStyleSheet("background-color: 204, 204, 204")
        self.plus5sec.setObjectName("plus5sec")

        self.minus5sec = QtWidgets.QPushButton(Form2)
        # self.minus5sec.setGeometry(QtCore.QRect(190, 33, 40, 17))
        self.minus5sec.setGeometry(QtCore.QRect(390, 65, 40, 17))
        self.minus5sec.setStyleSheet("background-color: 204, 204, 204")
        self.minus5sec.setObjectName("minus5sec")

        self.score_white_0 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_0.setGeometry(QtCore.QRect(10, 8, 40, 25))
        self.score_white_0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_0.setChecked(True)
        self.score_white_0.setObjectName("score_white_0")

        self.score_white_1 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_1.setGeometry(QtCore.QRect(10, 41, 40, 25))
        self.score_white_1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_1.setObjectName("score_white_1")

        self.score_white_2 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_2.setGeometry(QtCore.QRect(10, 74, 40, 25))
        self.score_white_2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_2.setObjectName("score_white_2")

        self.score_white_3 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_3.setGeometry(QtCore.QRect(10, 107, 40, 25))
        self.score_white_3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_3.setObjectName("score_white_3")

        self.score_white_4 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_4.setGeometry(QtCore.QRect(10, 140, 40, 25))
        self.score_white_4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_4.setObjectName("score_white_4")

        self.score_white_5 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_5.setGeometry(QtCore.QRect(10, 173, 40, 25))
        self.score_white_5.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_5.setObjectName("score_white_5")

        self.score_white_6 = QtWidgets.QRadioButton(self.frame_white1)
        self.score_white_6.setGeometry(QtCore.QRect(10, 206, 40, 25))
        self.score_white_6.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_6.setObjectName("score_white_6")

        self.h_red0 = QtWidgets.QLabel(Form2)
        self.h_red0.setGeometry(QtCore.QRect(475, 360, 25, 40))
        self.h_red0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_red0.setObjectName("h_red0")

        self.frame_rh = QtWidgets.QFrame(Form2)
        self.frame_rh.setGeometry(QtCore.QRect(500, 360, 380, 40))
        self.frame_rh.setStyleSheet("border-color: None")
        self.frame_rh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rh.setObjectName("frame_rh")

        self.h_red1 = QtWidgets.QRadioButton(self.frame_rh)
        self.h_red1.setGeometry(QtCore.QRect(10, 5, 110, 25))
        self.h_red1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red1.setObjectName("h_red1")

        self.h_red2 = QtWidgets.QRadioButton(self.frame_rh)
        self.h_red2.setGeometry(QtCore.QRect(120, 5, 80, 25))
        self.h_red2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red2.setObjectName("h_red2")

        self.h_red3 = QtWidgets.QRadioButton(self.frame_rh)
        self.h_red3.setGeometry(QtCore.QRect(200, 5, 110, 25))
        self.h_red3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red3.setObjectName("h_red3")

        self.h_red4 = QtWidgets.QRadioButton(self.frame_rh)
        self.h_red4.setGeometry(QtCore.QRect(320, 5, 60, 25))
        self.h_red4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red4.setChecked(True)
        self.h_red4.setObjectName("h_red4")

        self.j_red0 = QtWidgets.QLabel(Form2)
        self.j_red0.setGeometry(QtCore.QRect(475, 430, 25, 40))
        self.j_red0.setStyleSheet("font-family: Gotham-Light; font-size: 40px;")
        self.j_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_red0.setObjectName("j_red0")

        self.frame_rj = QtWidgets.QFrame(Form2)
        self.frame_rj.setGeometry(QtCore.QRect(500, 430, 380, 40))
        self.frame_rj.setStyleSheet("border-color: None")
        self.frame_rj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rj.setObjectName("frame_rj")

        self.j_red1 = QtWidgets.QRadioButton(self.frame_rj)
        self.j_red1.setGeometry(QtCore.QRect(10, 5, 110, 25))
        self.j_red1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red1.setObjectName("j_red1")

        self.j_red2 = QtWidgets.QRadioButton(self.frame_rj)
        self.j_red2.setGeometry(QtCore.QRect(120, 5, 80, 25))
        self.j_red2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red2.setObjectName("j_red2")

        self.j_red3 = QtWidgets.QRadioButton(self.frame_rj)
        self.j_red3.setGeometry(QtCore.QRect(200, 5, 110, 25))
        self.j_red3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red3.setObjectName("j_red3")

        self.j_red4 = QtWidgets.QRadioButton(self.frame_rj)
        self.j_red4.setGeometry(QtCore.QRect(320, 5, 60, 25))
        self.j_red4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red4.setChecked(True)
        self.j_red4.setObjectName("j_red4")

        self.h_white0 = QtWidgets.QLabel(Form2)
        self.h_white0.setGeometry(QtCore.QRect(25, 360, 25, 40))
        self.h_white0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_white0.setObjectName("h_white0")

        self.frame_wh = QtWidgets.QFrame(Form2)
        self.frame_wh.setGeometry(QtCore.QRect(50, 360, 380, 40))
        self.frame_wh.setStyleSheet("border-color: None")
        self.frame_wh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wh.setObjectName("frame_wh")

        self.h_white1 = QtWidgets.QRadioButton(self.frame_wh)
        self.h_white1.setGeometry(QtCore.QRect(10, 5, 110, 25))
        self.h_white1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white1.setObjectName("h_white1")

        self.h_white2 = QtWidgets.QRadioButton(self.frame_wh)
        self.h_white2.setGeometry(QtCore.QRect(120, 5, 80, 25))
        self.h_white2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white2.setObjectName("h_white2")

        self.h_white3 = QtWidgets.QRadioButton(self.frame_wh)
        self.h_white3.setGeometry(QtCore.QRect(200, 5, 110, 25))
        self.h_white3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white3.setObjectName("h_white3")

        self.h_white4 = QtWidgets.QRadioButton(self.frame_wh)
        self.h_white4.setGeometry(QtCore.QRect(320, 5, 60, 25))
        self.h_white4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white4.setChecked(True)
        self.h_white4.setObjectName("h_white4")

        self.j_white0 = QtWidgets.QLabel(Form2)
        self.j_white0.setGeometry(QtCore.QRect(25, 430, 25, 40))
        self.j_white0.setStyleSheet("font-family: Gotham-Light; font-size: 40px;")
        self.j_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_white0.setObjectName("j_white0")

        self.frame_wj = QtWidgets.QFrame(Form2)
        self.frame_wj.setGeometry(QtCore.QRect(50, 430, 380, 40))
        self.frame_wj.setStyleSheet("border-color: None")
        self.frame_wj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wj.setObjectName("frame_wj")

        self.j_white1 = QtWidgets.QRadioButton(self.frame_wj)
        self.j_white1.setGeometry(QtCore.QRect(10, 5, 110, 25))
        self.j_white1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white1.setObjectName("j_white1")

        self.j_white2 = QtWidgets.QRadioButton(self.frame_wj)
        self.j_white2.setGeometry(QtCore.QRect(120, 5, 80, 25))
        self.j_white2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white2.setObjectName("j_white2")

        self.j_white3 = QtWidgets.QRadioButton(self.frame_wj)
        self.j_white3.setGeometry(QtCore.QRect(200, 5, 110, 25))
        self.j_white3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white3.setObjectName("j_white3")

        self.j_white4 = QtWidgets.QRadioButton(self.frame_wj)
        self.j_white4.setGeometry(QtCore.QRect(320, 5, 60, 25))
        self.j_white4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white4.setChecked(True)
        self.j_white4.setObjectName("j_white4")

        self.pushButton_reset = QtWidgets.QPushButton(Form2)
        self.pushButton_reset.setGeometry(QtCore.QRect(580, 35, 170, 20))
        self.pushButton_reset.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                            "font-family: Gotham-Light; font-size: 8pt;")
        self.pushButton_reset.setObjectName("pushButton_reset")

        self.pushButton_pause = QtWidgets.QPushButton(Form2)
        self.pushButton_pause.setGeometry(QtCore.QRect(580, 5, 170, 25))
        self.pushButton_pause.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                            "font-family: Gotham-Light; font-size: 13pt;")
        self.pushButton_pause.setObjectName("pushButton_pause")

        self.pushButton_start = QtWidgets.QPushButton(Form2)
        self.pushButton_start.setGeometry(QtCore.QRect(240, 10, 115, 40))
        self.pushButton_start.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                            "font-family: Gotham-Light; font-size: 20pt;")
        self.pushButton_start.setObjectName("pushButton_start")

        self.frame_timeRound.raise_()
        self.frame_red1.raise_()
        self.line1.raise_()
        self.frame_white1.raise_()
        self.lcd1.raise_()


        self.minus5sec.raise_()
        self.plus5sec.raise_()
        self.frame_wh.raise_()
        self.frame_rj.raise_()
        self.frame_rh.raise_()
        self.j_red3.raise_()
        self.j_red0.raise_()
        self.j_red2.raise_()
        self.j_red1.raise_()
        self.h_red0.raise_()
        self.h_red2.raise_()
        self.h_red3.raise_()
        self.h_red4.raise_()
        self.h_red1.raise_()
        self.h_white0.raise_()
        self.j_white0.raise_()
        self.j_white2.raise_()
        self.j_white3.raise_()
        self.j_white1.raise_()
        self.h_white2.raise_()
        self.h_white3.raise_()
        self.h_white1.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_pause.raise_()
        self.pushButton_start.raise_()

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Экран для судей. Кумите"))
        self.MenuButton.setText(_translate("Form2", "Главное меню"))
        self.KataQualButton.setText(_translate("Form2", "Ката отбороч."))
        self.KataFinalButton.setText(_translate("Form2", "Ката финал"))

        self.round_time.setText(_translate("Form2", "Время раунда"))
        self.label_1min.setText(_translate("Form2", "1 мин"))
        self.label_15min.setText(_translate("Form2", "1,5 мин"))
        self.label_2min.setText(_translate("Form2", "2 мин"))
        self.label_3min.setText(_translate("Form2", "3 мин"))
        self.label_5min.setText(_translate("Form2", "5 мин"))

        self.plus5sec.setText(_translate("Form2", "+5 сек"))
        self.minus5sec.setText(_translate("Form2", "-5 сек"))

        self.label_score11.setText(_translate("Form2", "0"))
        self.score_red_1.setText(_translate("Form2", "1"))
        self.score_red_2.setText(_translate("Form2", "2"))
        self.score_red_3.setText(_translate("Form2", "3"))
        self.score_red_4.setText(_translate("Form2", "4"))
        self.score_red_5.setText(_translate("Form2", "5"))
        self.score_red_6.setText(_translate("Form2", "6"))
        self.score_red_0.setText(_translate("Form2", "0"))

        self.label_score12.setText(_translate("Form2", "0"))
        self.score_white_4.setText(_translate("Form2", "4"))
        self.score_white_5.setText(_translate("Form2", "5"))
        self.score_white_1.setText(_translate("Form2", "1"))
        self.score_white_2.setText(_translate("Form2", "2"))
        self.score_white_3.setText(_translate("Form2", "3"))
        self.score_white_6.setText(_translate("Form2", "6"))
        self.score_white_0.setText(_translate("Form2", "0"))

        self.j_red0.setText(_translate("Form2", "J"))
        self.j_red1.setText(_translate("Form2", "Keikoku"))
        self.j_red2.setText(_translate("Form2", "Chui"))
        self.j_red3.setText(_translate("Form2", "Hansoku"))
        self.j_red4.setText(_translate("Form2", "Off"))
        self.h_red0.setText(_translate("Form2", "H \nM"))
        self.h_red1.setText(_translate("Form2", "Keikoku"))
        self.h_red2.setText(_translate("Form2", "Chui"))
        self.h_red3.setText(_translate("Form2", "Hansoku"))
        self.h_red4.setText(_translate("Form2", "Off"))

        self.j_white0.setText(_translate("Form2", "J"))
        self.j_white1.setText(_translate("Form2", "Keikoku"))
        self.j_white2.setText(_translate("Form2", "Chui"))
        self.j_white3.setText(_translate("Form2", "Hansoku"))
        self.j_white4.setText(_translate("Form2", "Off"))
        self.h_white0.setText(_translate("Form2", "H \nM"))
        self.h_white1.setText(_translate("Form2", "Keikoku"))
        self.h_white2.setText(_translate("Form2", "Chui"))
        self.h_white3.setText(_translate("Form2", "Hansoku"))
        self.h_white4.setText(_translate("Form2", "Off"))

        self.pushButton_reset.setText(_translate("Form2", "Новый бой (сбросить всё)"))
        self.pushButton_pause.setText(_translate("Form2", "Обнулить таймер"))
        self.pushButton_start.setText(_translate("Form2", "► Start"))


class KumiteMainWindow(QWidget, KumiteMainWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.KumiteSecondWindow = KumiteSecondWindow()
        self.lcd1.setNumDigits(5)
        self.KumiteSecondWindow.lcd2.setNumDigits(5)
        self.timeRound()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.sound_gong1 = QSound(":/audio/gong1.wav")
        self.sound_gong2 = QSound(":/audio/gong2.wav")
        self.slider.valueChanged.connect(self.timeRound)

    def openSecondWinKumite(self):
        self.KumiteSecondWindow.show()

    def closeSecondWinKumite(self):
        self.KumiteSecondWindow.hide()

    def timeRound(self):
        if self.slider.value() == 1:
            self.lcd1.display('01:00')
            self.KumiteSecondWindow.lcd2.display('01:00')
            self.tics = datetime.strptime(str('01:00'), '%M:%S')
            self.label_1min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 2:
            self.lcd1.display('01:30')
            self.KumiteSecondWindow.lcd2.display('01:30')
            self.tics = datetime.strptime(str('01:30'), '%M:%S')
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 3:
            self.lcd1.display('02:00')
            self.KumiteSecondWindow.lcd2.display('02:00')
            self.tics = datetime.strptime(str('02:00'), '%M:%S')
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 4:
            self.lcd1.display('03:00')
            self.KumiteSecondWindow.lcd2.display('03:00')
            self.tics = datetime.strptime(str('03:00'), '%M:%S')
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Medium;")
            self.label_5min.setStyleSheet("font-family: Gotham-Light;")
        elif self.slider.value() == 5:
            self.lcd1.display('05:00')
            self.KumiteSecondWindow.lcd2.display('05:00')
            self.tics = datetime.strptime(str('05:00'), '%M:%S')
            self.label_1min.setStyleSheet("font-family: Gotham-Light;")
            self.label_15min.setStyleSheet("font-family: Gotham-Light;")
            self.label_2min.setStyleSheet("font-family: Gotham-Light;")
            self.label_3min.setStyleSheet("font-family: Gotham-Light;")
            self.label_5min.setStyleSheet("font-family: Gotham-Medium;")

        # if self.radio_timer_2.isChecked():
        #     self.lcd1.display('02:00')
        #     self.KumiteSecondWindow.lcd2.display('02:00')
        #     self.tics = datetime.strptime(str('02:00'), '%M:%S')
        # elif self.radio_timer_5.isChecked():
        #     self.lcd1.display('05:00')
        #     self.KumiteSecondWindow.lcd2.display('05:00')
        #     self.tics = datetime.strptime(str('05:00'), '%M:%S')
        # elif self.radio_timer_1.isChecked():
        #     self.lcd1.display('01:00')
        #     self.KumiteSecondWindow.lcd2.display('01:00')
        #     self.tics = datetime.strptime(str('01:00'), '%M:%S')
        # elif self.radio_timer_6.isChecked():
        #     self.lcd1.display('06:00')
        #     self.KumiteSecondWindow.lcd2.display('06:00')
        #     self.tics = datetime.strptime(str('06:00'), '%M:%S')

    def upTime(self):
        if self.tics != 0:
            self.tics += timedelta(seconds=4)

    def downTime(self):
        if self.tics != 0:
            self.tics -= timedelta(seconds=4)

    def update_time(self):
        self.timer.start(1000)

        if self.tics == datetime.strptime(str('00:00'), '%M:%S'):
            self.timer.stop()
            return

        self.tics -= timedelta(seconds=1)
        self.lcd1.display(str(self.tics).split()[1])
        self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])

        if self.tics == datetime.strptime(str('00:30'), '%M:%S'):
            self.sound_gong1.play()

        if self.tics == datetime.strptime(str('00:00'), '%M:%S'):
            self.sound_gong2.play()
            self.timer.stop()
            self.pushButton_start.setText('Раунд\nзавершен')
            self.pushButton_start.setStyleSheet("background-color: yellow; color: black;"
                                                "font-family: Gotham-Medium; font-size: 12pt;")

    def start_timer(self):
        if self.pushButton_start.text() == '► Start':
            self.pushButton_start.setText('▇ Stop')
            self.timer.start(1000)
            self.pushButton_pause.setText('Обнулить таймер')
            self.pushButton_pause.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 13pt;")
            self.pushButton_reset.setText('Новый бой (сбросить всё)')
            self.pushButton_reset.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 8pt;")
        # elif self.pushButton_start.text() == 'Раунд\nзавершен':
        #     self.pushButton_start.setText('Нажмите кнопку\nНовый бой')
        #     self.pushButton_start.setStyleSheet("background-color: orange; color: black;"
        #                                         "font-family: Gotham-Light; font-size: 10pt;")
        else:
            # self.pushButton_start.text() == '▇ Stop':
            self.timer.stop()
            self.pushButton_start.setText('► Start')
            self.pushButton_pause.setText('Обнулить таймер')
            self.pushButton_pause.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 13pt;")
            self.pushButton_reset.setText('Новый бой (сбросить всё)')
            self.pushButton_reset.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 8pt;")

    def reset_timer(self):
        if self.pushButton_start.text() != '► Start':
            self.pushButton_pause.setText('Останови бой')
            self.pushButton_pause.setStyleSheet("color: red")

        else:
            self.timeRound()
            self.pushButton_pause.setText('Обнулить таймер')
            self.pushButton_pause.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 13pt;")
            self.pushButton_reset.setText('Новый бой (сбросить всё)')
            self.pushButton_reset.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                                "font-family: Gotham-Light; font-size: 8pt;")

    def reset_all(self):
        if self.pushButton_start.text() != '► Start':
            self.pushButton_reset.setText('Останови бой')
            self.pushButton_reset.setStyleSheet("color: red")
        else:
            self.clearKumiteData()

    def clearKumiteData(self):
        self.timer.stop()
        self.timeRound()
        self.j_red4.clicked.connect(self.penaltyButton_jr4)
        self.h_white4.clicked.connect(self.penaltyButton_hmw4)
        self.j_white4.clicked.connect(self.penaltyButton_jw4)

        self.pushButton_pause.setText('Обнулить таймер')
        self.pushButton_pause.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                            "font-family: Gotham-Light; font-size: 13pt;")
        self.pushButton_reset.setText('Новый бой (сбросить всё)')
        self.pushButton_reset.setStyleSheet("background-color: rgb(62, 106, 225); color: white;"
                                            "font-family: Gotham-Light; font-size: 8pt;")
        self.label_score11.setText('0')
        self.KumiteSecondWindow.label_score21.setText('0')
        self.label_score12.setText('0')
        self.KumiteSecondWindow.label_score22.setText('0')
        self.score_red_0.setChecked(True)
        self.score_white_0.setChecked(True)

        self.h_red4.setStyleSheet('color: black;')
        self.j_red4.setStyleSheet('color: black;')
        self.h_white4.setStyleSheet('color: black;')
        self.j_white4.setStyleSheet('color: black;')
        self.h_red4.setChecked(True)
        self.j_red4.setChecked(True)
        self.h_white4.setChecked(True)
        self.j_white4.setChecked(True)
        self.setStyleButton(self.h_red1, self.h_red2, self.h_red3, self.h_red4,
                            self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                            self.KumiteSecondWindow.hm_r3)
        self.KumiteSecondWindow.label_kum_hmr0.setText(None)
        self.setStyleButton(self.j_red1, self.j_red2, self.j_red3, self.j_red4,
                            self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2,
                            self.KumiteSecondWindow.j_r3)
        self.KumiteSecondWindow.label_kum_jr0.setText(None)
        self.setStyleButton(self.h_white1, self.h_white2, self.h_white3, self.h_white4,
                            self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2,
                            self.KumiteSecondWindow.hm_w3)
        self.KumiteSecondWindow.label_kum_hmw0.setText(None)
        self.setStyleButton(self.j_white1, self.j_white2, self.j_white3, self.j_white4,
                            self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2,
                            self.KumiteSecondWindow.j_w3)
        self.KumiteSecondWindow.label_kum_jw0.setText(None)

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
            self.setStyleButton(self.h_red2, self.h_red3, self.h_red4, self.h_red1,
                                self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2, self.KumiteSecondWindow.hm_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr2(self):
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.h_red1, self.h_red3, self.h_red4, self.h_red2,
                                self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2, self.KumiteSecondWindow.hm_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr3(self):
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.h_red1, self.h_red2, self.h_red4, self.h_red3,
                                self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2,
                                self.KumiteSecondWindow.hm_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmr0.setText(penaltyB_hmr.text())

    def penaltyButton_hmr4(self):
        penaltyB_hmr = self.sender()
        if penaltyB_hmr.isChecked():
            self.setStyleButton(self.h_red1, self.h_red2, self.h_red3, self.h_red4,
                                self.KumiteSecondWindow.hm_r1, self.KumiteSecondWindow.hm_r2, self.KumiteSecondWindow.hm_r3)
            self.KumiteSecondWindow.label_kum_hmr0.setText(None)

    def penaltyButton_jr1(self):
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.j_red2, self.j_red3, self.j_red4, self.j_red1,
                                self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2, self.KumiteSecondWindow.j_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr2(self):
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.j_red1, self.j_red3, self.j_red4, self.j_red2,
                                self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2, self.KumiteSecondWindow.j_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr3(self):
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.j_red1, self.j_red2, self.j_red4, self.j_red3,
                                self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2, self.KumiteSecondWindow.j_r3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jr0.setText(penaltyB_jr.text())

    def penaltyButton_jr4(self):
        penaltyB_jr = self.sender()
        if penaltyB_jr.isChecked():
            self.setStyleButton(self.j_red1, self.j_red2, self.j_red3, self.j_red4,
                                self.KumiteSecondWindow.j_r1, self.KumiteSecondWindow.j_r2, self.KumiteSecondWindow.j_r3)
            self.KumiteSecondWindow.label_kum_jr0.setText(None)

    def penaltyButton_hmw1(self):
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.h_white2, self.h_white3, self.h_white4, self.h_white1,
                                self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2, self.KumiteSecondWindow.hm_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw2(self):
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.h_white1, self.h_white3, self.h_white4, self.h_white2,
                                self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2, self.KumiteSecondWindow.hm_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw3(self):
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.h_white1, self.h_white2, self.h_white4, self.h_white3,
                                self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2, self.KumiteSecondWindow.hm_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_hmw0.setText(penaltyB_hmw.text())

    def penaltyButton_hmw4(self):
        penaltyB_hmw = self.sender()
        if penaltyB_hmw.isChecked():
            self.setStyleButton(self.h_white1, self.h_white2, self.h_white3, self.h_white4,
                                self.KumiteSecondWindow.hm_w1, self.KumiteSecondWindow.hm_w2, self.KumiteSecondWindow.hm_w3)
            self.KumiteSecondWindow.label_kum_hmw0.setText(None)

    def penaltyButton_jw1(self):
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.j_white2, self.j_white3, self.j_white4, self.j_white1,
                                self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2, self.KumiteSecondWindow.j_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw2(self):
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.j_white1, self.j_white3, self.j_white4, self.j_white2,
                                self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2, self.KumiteSecondWindow.j_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw3(self):
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.j_white1, self.j_white2, self.j_white4, self.j_white3,
                                self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2, self.KumiteSecondWindow.j_w3,
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;',
                                'background-color: grey; border-radius: 30px; border: 4px solid black;')
            self.KumiteSecondWindow.label_kum_jw0.setText(penaltyB_jw.text())

    def penaltyButton_jw4(self):
        penaltyB_jw = self.sender()
        if penaltyB_jw.isChecked():
            self.setStyleButton(self.j_white1, self.j_white2, self.j_white3, self.j_white4,
                                self.KumiteSecondWindow.j_w1, self.KumiteSecondWindow.j_w2, self.KumiteSecondWindow.j_w3)
            self.KumiteSecondWindow.label_kum_jw0.setText(None)

    def setStyleButton(self, rad_M0, rad_M1, rad_M2, rad_M3, rad_S1, rad_S2, rad_S3,
                       rad_S1_FontSize='border-radius: 30px; border: 4px solid grey;',
                       rad_S2_FontSize='border-radius: 30px; border: 4px solid grey;',
                       rad_S3_FontSize='border-radius: 30px; border: 4px solid grey;'):
        rad_M0.setStyleSheet('background-color: white; font-family: Gotham-Light; font: 20px')
        rad_M1.setStyleSheet('background-color: white; font-family: Gotham-Light; font: 20px;')
        rad_M2.setStyleSheet('background-color: white; font-family: Gotham-Light; font: 20px;')
        rad_M3.setStyleSheet('background-color: rgb(206, 238, 255);font-family: Gotham-Light; font: 20px;')
        rad_S1.setStyleSheet(rad_S1_FontSize)
        rad_S2.setStyleSheet(rad_S2_FontSize)
        rad_S3.setStyleSheet(rad_S3_FontSize)


class dialogWindow_Ui(object):
    def setupUi_dialog(self, Dialog):
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
