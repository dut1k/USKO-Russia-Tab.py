from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication, QLineEdit, \
    QVBoxLayout, QLCDNumber, QSlider, QComboBox
from PyQt5.Qt import QHBoxLayout, QPoint
from PyQt5.QtMultimedia import QSound
from datetime import datetime, timedelta


class KumiteSWindow_Ui(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: white;")
        Form.resize(1920, 1080)

        self.matchName21 = QtWidgets.QLabel(Form)
        self.matchName22 = QtWidgets.QLabel(Form)
        self.lcd2 = QtWidgets.QLCDNumber(Form)
        self.line2 = QtWidgets.QFrame(Form)

##############################################
        self.frame_red2 = QtWidgets.QFrame(Form)
        self.label_score21 = QtWidgets.QLabel(self.frame_red2)
        self.background_red21 = QtWidgets.QFrame(self.frame_red2)
        self.background_red22 = QtWidgets.QFrame(self.frame_red2)

        self.frame_hm_red = QtWidgets.QFrame(self.frame_red2)
        self.label_kum_hmr0 = QtWidgets.QLabel(self.frame_hm_red)
        self.label_kum_hmr1 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r1 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r2 = QtWidgets.QLabel(self.frame_hm_red)
        self.hm_r3 = QtWidgets.QLabel(self.frame_hm_red)

        self.frame_j_red = QtWidgets.QFrame(self.frame_red2)
        self.label_kum_jr0 = QtWidgets.QLabel(self.frame_j_red)
        self.label_kum_jr1 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r1 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r2 = QtWidgets.QLabel(self.frame_j_red)
        self.j_r3 = QtWidgets.QLabel(self.frame_j_red)
##############################################
        self.frame_white2 = QtWidgets.QFrame(Form)
        self.label_score22 = QtWidgets.QLabel(self.frame_white2)
        self.background_white21 = QtWidgets.QFrame(self.frame_white2)
        self.background_white22 = QtWidgets.QFrame(self.frame_white2)

        self.frame_hm_white = QtWidgets.QFrame(self.frame_white2)
        self.label_kum_hmw0 = QtWidgets.QLabel(self.frame_hm_white)
        self.label_kum_hmw1 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w1 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w2 = QtWidgets.QLabel(self.frame_hm_white)
        self.hm_w3 = QtWidgets.QLabel(self.frame_hm_white)

        self.frame_j_white = QtWidgets.QFrame(self.frame_white2)
        self.label_kum_jw0 = QtWidgets.QLabel(self.frame_j_white)
        self.label_kum_jw1 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w1 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w2 = QtWidgets.QLabel(self.frame_j_white)
        self.j_w3 = QtWidgets.QLabel(self.frame_j_white)

        self.matchName21.setGeometry(QtCore.QRect(20, 10, 730, 140))
        self.matchName21.setStyleSheet("font-family: Gotham-Medium; font-size: 90px; color: grey;")
        self.matchName21.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName21.setObjectName("matchName21")

        self.matchName22.setGeometry(QtCore.QRect(1170, 10, 730, 140))
        self.matchName22.setStyleSheet("font-family: Gotham-Medium; font-size: 50px; color: grey;")
        self.matchName22.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName22.setObjectName("matchName22")

        self.label_winner = QtWidgets.QLabel(Form)
        self.label_winner.hide()
        self.label_winner.setGeometry(QtCore.QRect(0, 150, 550, 50))
        self.label_winner.setStyleSheet(
            "background-color: none; font-family: Gotham-Medium; font-size: 60px; ")
        self.label_winner.setAlignment(QtCore.Qt.AlignCenter)
        self.label_winner.setObjectName("label_winner")

        self.lcd2.setGeometry(QtCore.QRect(770, 0, 380, 140))
        self.lcd2.setStyleSheet("background-color: None; border: None")

        self.line2.setGeometry(QtCore.QRect(957, 150, 6, 890))
        self.line2.setLineWidth(1)
        self.line2.setMidLineWidth(6)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line")

        self.label_score21.setGeometry(QtCore.QRect(265, 0, 350, 420))
        self.label_score21.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; color: white; font-size: 530px;")
        self.label_score21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score21.setObjectName("label_score1")

        self.label_score22.setGeometry(QtCore.QRect(265, 0, 350, 420))
        self.label_score22.setStyleSheet(
            "background-color: none; font-family: Gotham-Bold; font-size: 530px; ")
        self.label_score22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score22.setObjectName("label_score2")

        self.frame_red2.setGeometry(QtCore.QRect(40, 150, 880, 850))
        self.frame_red2.setStyleSheet("background-color: None; ")
        self.frame_red2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red2.setObjectName("frame_red2")

        self.background_red21.setGeometry(QtCore.QRect(0, 0, 880, 450))
        self.background_red21.setStyleSheet("background-color: rgb(255, 95, 95); border-top-left-radius: 15px;"
                                            "border-top-right-radius: 15px; border: 2px solid grey")
        self.background_red21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red21.setObjectName("background_red21")

        self.background_red22.setGeometry(QtCore.QRect(0, 430, 880, 420))
        self.background_red22.setStyleSheet("background-color: white; border-radius: 15px;"
                                            "border: 2px solid grey")
        self.background_red22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_red22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_red22.setObjectName("background_red22")

        self.frame_hm_red.setGeometry(QtCore.QRect(0, 430, 880, 190))
        self.frame_hm_red.setStyleSheet("background-color: None;")
        self.frame_hm_red.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_hm_red.setObjectName("frame_hm_red")

        self.label_kum_hmr0.setGeometry(QtCore.QRect(400, 0, 480, 120))
        self.label_kum_hmr0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_hmr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr0.setObjectName("label_kum_hmr0")

        self.label_kum_hmr1.setGeometry(QtCore.QRect(0, 20, 400, 190))
        self.label_kum_hmr1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 190px;")
        self.label_kum_hmr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmr1.setObjectName("label_kum_hmr1")

        self.hm_r1.setGeometry(QtCore.QRect(475, 125, 60, 60))
        self.hm_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r1.setObjectName("hm_r1")

        self.hm_r2.setGeometry(QtCore.QRect(610, 125, 60, 60))
        self.hm_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r2.setObjectName("hm_r2")

        self.hm_r3.setGeometry(QtCore.QRect(745, 125, 60, 60))
        self.hm_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_r3.setObjectName("hm_r3")

        self.frame_j_red.setGeometry(QtCore.QRect(0, 620, 880, 190))
        self.frame_j_red.setStyleSheet("background-color: None;")
        self.frame_j_red.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_j_red.setObjectName("frame_j_red")

        self.label_kum_jr0.setGeometry(QtCore.QRect(400, 0, 480, 120))
        self.label_kum_jr0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_jr0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jr0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr0.setObjectName("label_kum_jr0")

        self.label_kum_jr1.setGeometry(QtCore.QRect(0, 20, 400, 190))
        self.label_kum_jr1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 190px;")
        self.label_kum_jr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jr1.setObjectName("label_kum_jr1")

        self.j_r1.setGeometry(QtCore.QRect(475, 125, 60, 60))
        self.j_r1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r1.setObjectName("j_r1")

        self.j_r2.setGeometry(QtCore.QRect(610, 125, 60, 60))
        self.j_r2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r2.setObjectName("j_r2")

        self.j_r3.setGeometry(QtCore.QRect(745, 125, 60, 60))
        self.j_r3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_r3.setObjectName("j_r3")

        self.frame_white2.setGeometry(QtCore.QRect(1000, 150, 880, 850))
        self.frame_white2.setStyleSheet("background-color: None;")
        self.frame_white2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white2.setObjectName("frame_white2")

        self.background_white21.setGeometry(QtCore.QRect(0, 0, 880, 450))
        self.background_white21.setStyleSheet("background-color: None; border-top-left-radius: 15px;"
                                            "border-top-right-radius: 15px; border: 2px solid grey")
        self.background_white21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white21.setObjectName("background_white21")

        self.background_white22.setGeometry(QtCore.QRect(0, 430, 880, 420))
        self.background_white22.setStyleSheet("background-color: white; border-radius: 15px;"
                                            "border: 2px solid grey")
        self.background_white22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_white22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_white22.setObjectName("background_white22")

        self.frame_hm_white.setGeometry(QtCore.QRect(0, 430, 880, 190))
        self.frame_hm_white.setStyleSheet("background-color: None;")
        self.frame_hm_white.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_hm_white.setObjectName("frame_hm_white")

        self.label_kum_hmw0.setGeometry(QtCore.QRect(400, 0, 480, 120))
        self.label_kum_hmw0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_hmw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_hmw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw0.setObjectName("label_kum_hmw0")

        self.label_kum_hmw1.setGeometry(QtCore.QRect(0, 20, 400, 190))
        self.label_kum_hmw1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 190px;")
        self.label_kum_hmw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_hmw1.setObjectName("label_kum_hmw1")

        self.hm_w1.setGeometry(QtCore.QRect(475, 125, 60, 60))
        self.hm_w1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w1.setObjectName("hm_w1")

        self.hm_w2.setGeometry(QtCore.QRect(610, 125, 60, 60))
        self.hm_w2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w2.setObjectName("hm_w2")

        self.hm_w3.setGeometry(QtCore.QRect(745, 125, 60, 60))
        self.hm_w3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.hm_w3.setObjectName("hm_w3")

        self.frame_j_white.setGeometry(QtCore.QRect(0, 620, 880, 190))
        self.frame_j_white.setStyleSheet("background-color: None;")
        self.frame_j_white.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_j_white.setObjectName("frame_j_white")

        self.label_kum_jw0.setGeometry(QtCore.QRect(400, 0, 480, 120))
        self.label_kum_jw0.setStyleSheet("background-color: None;font-family: Gotham-Medium; font-size: 100px;")
        self.label_kum_jw0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_kum_jw0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw0.setObjectName("label_kum_jw0")

        self.label_kum_jw1.setGeometry(QtCore.QRect(0, 20, 400, 190))
        self.label_kum_jw1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 190px;")
        self.label_kum_jw1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kum_jw1.setObjectName("label_kum_jw1")

        self.j_w1.setGeometry(QtCore.QRect(475, 125, 60, 60))
        self.j_w1.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w1.setObjectName("j_w1")

        self.j_w2.setGeometry(QtCore.QRect(610, 125, 60, 60))
        self.j_w2.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w2.setObjectName("j_w2")

        self.j_w3.setGeometry(QtCore.QRect(745, 125, 60, 60))
        self.j_w3.setStyleSheet("border-radius: 30px; border: 4px solid grey;")
        self.j_w3.setObjectName("j_w3")
        
        self.line2.raise_()
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
        self.matchName21.setText(_translate("Form", "Татами №#"))
        self.matchName22.setText(_translate("Form", "М/Ж - возраст"))
        self.label_winner.setText(_translate("Form", "ПОБЕДИТЕЛЬ"))


class KumiteSecondWindow(QWidget, KumiteSWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)

########################################################################################################################
########################################################################################################################


class Frame_Header(QWidget):
    def __init__(self, parent):
        super(Frame_Header, self).__init__()
        self.parent = parent

        self.btn_style_2 = """
            QPushButton {
                color: #555B6E;
                background-color: none;
                border: none;
                }
            QPushButton:hover {
                border: 1px solid black;
                background-color: #FAF9F9;
                color: black;
                }
            QPushButton:pressed {
                border: none;
                background-color: #555B6E;
                color: white;
                }
        """

        self.combo_style_1 = """
        QComboBox {
            border-top: none;
            border-bottom: 1px solid gray;
            border-left: none;
            border-right: none;
            padding: 1px 18px 1px 3px;
        }

        QComboBox:editable {
            background: white;
        }

        QComboBox:!editable, QComboBox::drop-down:editable {
             background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                         stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
            font-family: Gotham-Light;
            font-size: 15px;
        }

        QComboBox:!editable:on, QComboBox::drop-down:editable:on {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
        }

        QComboBox:on { 
            padding-top: 3px;
            padding-left: 4px;
        }

        QComboBox::drop-down {
            subcontrol-position: right center;
            width: 1px;
            border: none;
        }
        QComboBox QAbstractItemView {
            border: none;
            selection-background-color: #3e6ae1;
        }
        """

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 3, 0)

        self.frame_title = QtWidgets.QFrame(self)
        self.frame_title.setStyleSheet("background-color: #FAF9F9; border: none;")
        self.frame_title.setFixedSize(200, 30)

        self.label_windowsTitle = QLabel("Кумите. Судейское окно", self.frame_title)
        self.label_windowsTitle.setStyleSheet("font-family: Gotham-Medium; font-size: 12px;")
        self.label_windowsTitle.setGeometry(QtCore.QRect(10, 0, 190, 30))

        self.frame_combo = QtWidgets.QFrame(self)
        self.frame_combo.setStyleSheet("background-color: none;")
        self.frame_combo.setFixedSize(147, 24)

        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.combo.setGeometry(0, 0, 147, 24)
        self.combo.addItems(["Главное меню", "Ката отбороч.", "Ката финал"])
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.combo.setFont(font)

        self.frame_btn = QtWidgets.QFrame(self)
        self.frame_btn.setFixedSize(47, 24)

        self.btn_showMinimized = QtWidgets.QPushButton("_", self.frame_btn)
        self.btn_showMinimized.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.btn_showMinimized.setFont(font)
        self.btn_showMinimized.clicked.connect(self.btn_showMinimized_clicked)
        self.btn_showMinimized.setGeometry(QtCore.QRect(0, 0, 24, 24))

        self.btn_closeWin = QtWidgets.QPushButton("×", self.frame_btn)
        self.btn_closeWin.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(22)
        self.btn_closeWin.setFont(font)
        self.btn_closeWin.clicked.connect(self.btn_closeWin_clicked)
        self.btn_closeWin.setGeometry(QtCore.QRect(23, 0, 24, 24))

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

    def btn_closeWin_clicked(self):
        print('111')
    #     self.parent.close()

    def btn_showMinimized_clicked(self):
        self.parent.showMinimized()




class KumiteMainWindow_Ui(QWidget):
    def __init__(self):
        super(KumiteMainWindow_Ui, self).__init__()

        self.Form2 = QtWidgets.QFrame(self)
        self.Form2.setFixedSize(900, 530)
        self.Form2.setStyleSheet("background-color: white;")
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # self.frame_header = QtWidgets.QFrame(self.Form2)
        # self.label_windowsTitle = QtWidgets.QLabel(self.frame_header)
        # self.frame_combo = QtWidgets.QFrame(self.Form2)
        # self.combo = QtWidgets.QComboBox(self.frame_combo)
        # self.btn_closeWin = QtWidgets.QPushButton(self.frame_header)
        # self.btn_showMinimized = QtWidgets.QPushButton(self.frame_header)

        self.frame_matchName = QtWidgets.QFrame(self.Form2)
        self.label_matchName1 = QtWidgets.QLabel('<b>Заголовок</b>', self.frame_matchName)
        self.label_matchName2 = QtWidgets.QLabel('Любой текст, после которого ставится <b>запятая</b>, не меняется программой', self.frame_matchName)
        self.matchName11 = QtWidgets.QLineEdit("Татами №#", self.frame_matchName)
        self.matchName12 = QtWidgets.QLineEdit("М/Ж - возраст", self.frame_matchName)
        self.btn_clearData = QtWidgets.QPushButton("ОЧИСТИТЬ\nДАННЫЕ", self.frame_matchName)
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

        self.frame_white1 = QtWidgets.QFrame(self.Form2)
        self.label_score12 = QtWidgets.QLabel("0", self.frame_white1)
        self.score_white_0 = QtWidgets.QRadioButton("0", self.frame_white1)
        self.score_white_1 = QtWidgets.QRadioButton("1", self.frame_white1)
        self.score_white_2 = QtWidgets.QRadioButton("2", self.frame_white1)
        self.score_white_3 = QtWidgets.QRadioButton("3", self.frame_white1)
        self.score_white_4 = QtWidgets.QRadioButton("4", self.frame_white1)
        self.score_white_5 = QtWidgets.QRadioButton("5", self.frame_white1)
        self.score_white_6 = QtWidgets.QRadioButton("6", self.frame_white1)

        self.frame_winner = QtWidgets.QFrame(self.Form2)
        self.winnerRed = QtWidgets.QRadioButton("Победил АКА", self.frame_winner)
        self.winnerWhite = QtWidgets.QRadioButton("Победил СИРО", self.frame_winner)

        self.frame_rh = QtWidgets.QFrame(self.Form2)
        self.h_red0 = QtWidgets.QLabel("H \nM", self.frame_rh)
        self.h_red1 = QtWidgets.QRadioButton("Keikoku", self.frame_rh)
        self.h_red2 = QtWidgets.QRadioButton("Chui", self.frame_rh)
        self.h_red3 = QtWidgets.QRadioButton("Hansoku", self.frame_rh)
        self.h_red4 = QtWidgets.QRadioButton("Off", self.frame_rh)
        self.frame_rj = QtWidgets.QFrame(self.Form2)
        self.j_red0 = QtWidgets.QLabel("J", self.frame_rj)
        self.j_red1 = QtWidgets.QRadioButton("Keikoku", self.frame_rj)
        self.j_red2 = QtWidgets.QRadioButton("Chui", self.frame_rj)
        self.j_red3 = QtWidgets.QRadioButton("Hansoku", self.frame_rj)
        self.j_red4 = QtWidgets.QRadioButton("Off", self.frame_rj)
        self.frame_wh = QtWidgets.QFrame(self.Form2)
        self.h_white0 = QtWidgets.QLabel("H \nM", self.frame_wh)
        self.h_white1 = QtWidgets.QRadioButton("Keikoku", self.frame_wh)
        self.h_white2 = QtWidgets.QRadioButton("Chui", self.frame_wh)
        self.h_white3 = QtWidgets.QRadioButton("Hansoku", self.frame_wh)
        self.h_white4 = QtWidgets.QRadioButton("Off", self.frame_wh)
        self.frame_wj = QtWidgets.QFrame(self.Form2)
        self.j_white0 = QtWidgets.QLabel("J", self.frame_wj)
        self.j_white1 = QtWidgets.QRadioButton("Keikoku", self.frame_wj)
        self.j_white2 = QtWidgets.QRadioButton("Chui", self.frame_wj)
        self.j_white3 = QtWidgets.QRadioButton("Hansoku", self.frame_wj)
        self.j_white4 = QtWidgets.QRadioButton("Off", self.frame_wj)

        self.btn_style_1 = """
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

        self.btn_style_2 = """
            QPushButton {
                color: #555B6E;
                background-color: none;
                }
            QPushButton:hover {
                border: 1px solid black;
                background-color: #FAF9F9;
                color: black;
                }
            QPushButton:pressed {
                border: none;
                background-color: #555B6E;
                color: white;
                }
        """

        self.combo_style_1 = """
        QComboBox {
            border-top: none;
            border-bottom: 1px solid gray;
            border-left: none;
            border-right: none;
            padding: 1px 18px 1px 3px;
        }
        
        QComboBox:editable {
            background: white;
        }
        
        QComboBox:!editable, QComboBox::drop-down:editable {
             background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                         stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                         stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
            font-family: Gotham-Light;
            font-size: 15px;
        }
        
        /* QComboBox gets the "on" state when the popup is open */
        QComboBox:!editable:on, QComboBox::drop-down:editable:on {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
        }
        
        QComboBox:on { /* shift the text when the popup opens */
            padding-top: 3px;
            padding-left: 4px;
        }
        
        QComboBox::drop-down {
            subcontrol-position: right center;
            width: 1px;
            border: none;
        }
        QComboBox QAbstractItemView {
            border: none;
            selection-background-color: #3e6ae1;
        }
        """

        LEdit_style_1 = """
            QLineEdit {
                border-bottom: 1px solid black;
                background-color: #FAF9F9;
                color: #555B6E;
                }
            QLineEdit:hover {
                border-bottom: 1px solid grey;
                background-color: #fdfdfd;
                color: black;
                }
        """
        self.frame_upper = QtWidgets.QFrame(self.Form2)
        self.frame_bottom = QtWidgets.QFrame(self.Form2)
        self.frame_left = QtWidgets.QFrame(self.Form2)
        self.frame_right = QtWidgets.QFrame(self.Form2)

        self.frame_upper.setGeometry(QtCore.QRect(0, 0, 900, 1))
        self.frame_upper.setStyleSheet("background-color: grey;")
        self.frame_upper.setObjectName("frame_upper")
        self.frame_bottom.setGeometry(QtCore.QRect(0, 529, 900, 1))
        self.frame_bottom.setStyleSheet("background-color: grey;")
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 1, 530))
        self.frame_left.setStyleSheet("background-color: grey;")
        self.frame_left.setObjectName("frame_left")
        self.frame_right.setGeometry(QtCore.QRect(899, 0, 1, 530))
        self.frame_right.setStyleSheet("background-color: grey;")
        self.frame_right.setObjectName("frame_right")

        # self.frame_header.setGeometry(QtCore.QRect(0, 0, 900, 30))
        # self.frame_header.setStyleSheet("background-color: #FAF9F9; border: none;")
        # self.frame_header.setObjectName("frame_header")
        #
        # self.label_windowsTitle.setGeometry(QtCore.QRect(20, 0, 200, 30))
        # self.label_windowsTitle.setStyleSheet("font-family: Gotham-Medium; font-size: 12px;")
        # self.label_windowsTitle.setObjectName("label_windowsTitle")
        #
        # self.btn_closeWin.setGeometry(QtCore.QRect(873, 3, 24, 24))
        # self.btn_closeWin.setStyleSheet(self.btn_style_2)
        # font = QtGui.QFont()
        # font.setFamily("Gotham-Light")
        # font.setPixelSize(22)
        # self.btn_closeWin.setFont(font)
        # self.btn_closeWin.setObjectName("btn_closeWin")
        #
        # self.btn_showMinimized.setGeometry(QtCore.QRect(850, 3, 24, 24))
        # self.btn_showMinimized.setStyleSheet(self.btn_style_2)
        # font = QtGui.QFont()
        # font.setFamily("Gotham-Light")
        # font.setPixelSize(13)
        # self.btn_showMinimized.setFont(font)
        # self.btn_showMinimized.setObjectName("btn_showMinimized")
        #
        # self.frame_combo.setGeometry(QtCore.QRect(700,3, 147, 24))
        # self.frame_combo.setStyleSheet("background-color: none;")
        # self.frame_combo.setObjectName("frame_combo")
        #
        # self.combo.setGeometry(0, 0, 147, 24)
        # self.combo.addItems(["Главное меню", "Ката отбороч.", "Ката финал"])
        # self.combo.setObjectName("combo")

        self.frame_matchName.setGeometry(QtCore.QRect(0, 30, 900, 70))
        self.frame_matchName.setStyleSheet("background-color: none; border: none;")

        self.btn_showData.setGeometry(QtCore.QRect(50, 10, 120, 50))
        self.btn_showData.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(13)
        self.btn_showData.setFont(font)
        self.btn_showData.setObjectName("btn_showData")

        self.btn_clearData.setGeometry(QtCore.QRect(730, 10, 120, 50))
        self.btn_clearData.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(13)
        self.btn_clearData.setFont(font)
        self.btn_clearData.setObjectName("btn_clearData")

        self.label_matchName1.setGeometry(QtCore.QRect(210, 0, 480, 25))
        self.label_matchName1.setStyleSheet("font-family: Gotham-Light; color: black; font-size: 20px;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.label_matchName2.setGeometry(QtCore.QRect(210, 55, 480, 15))
        self.label_matchName2.setStyleSheet("font-family: Gotham-Light; font-size: 12px;")
        self.label_matchName2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName2.setObjectName("label_matchName2")

        self.matchName11.setGeometry(QtCore.QRect(210, 25, 150, 30))
        self.matchName11.setStyleSheet(LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(20)
        self.matchName11.setFont(font)
        self.matchName11.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName11.setObjectName("matchName11")

        self.matchName12.setGeometry(QtCore.QRect(370, 25, 320, 30))
        self.matchName12.setStyleSheet(LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(20)
        self.matchName12.setFont(font)
        self.matchName12.setAlignment(QtCore.Qt.AlignCenter)
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

        self.frame_winner.setGeometry(QtCore.QRect(135, 170, 630, 25))
        self.frame_winner.setStyleSheet("background-color: none")
        self.frame_winner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_winner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_winner.setObjectName("frame_winner")

        self.winnerRed.setGeometry(QtCore.QRect(455, 0, 200, 25))
        self.winnerRed.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerRed.setObjectName("winnerRed")

        self.winnerWhite.setGeometry(QtCore.QRect(0, 0, 200, 25))
        self.winnerWhite.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerWhite.setObjectName("winnerWhite")

        self.frame_red1.setGeometry(QtCore.QRect(475, 170, 400, 240))
        self.frame_red1.setStyleSheet("background-color: rgb(255, 222, 219);")
        self.frame_red1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_red1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_red1.setObjectName("frame_red")

        self.label_score11.setGeometry(QtCore.QRect(150, 20, 100, 200))
        self.label_score11.setStyleSheet("font-family: Gotham-Light; font-size: 135px;")
        self.label_score11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score11.setObjectName("label_score1")

        self.score_red_0.setGeometry(QtCore.QRect(10, 8, 40, 25))
        self.score_red_0.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_0.setChecked(True)
        self.score_red_0.setObjectName("score_red_0")

        self.score_red_1.setGeometry(QtCore.QRect(10, 41, 40, 25))
        self.score_red_1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_1.setObjectName("score_red_1")

        self.score_red_2.setGeometry(QtCore.QRect(10, 74, 40, 25))
        self.score_red_2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_2.setObjectName("score_red_2")

        self.score_red_3.setGeometry(QtCore.QRect(10, 107, 40, 25))
        self.score_red_3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_3.setObjectName("score_red_3")

        self.score_red_4.setGeometry(QtCore.QRect(10, 140, 40, 25))
        self.score_red_4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_4.setObjectName("score_red_4")

        self.score_red_5.setGeometry(QtCore.QRect(10, 173, 40, 25))
        self.score_red_5.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_5.setObjectName("score_red_5")

        self.score_red_6.setGeometry(QtCore.QRect(10, 206, 40, 25))
        self.score_red_6.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_red_6.setObjectName("score_red_6")

        self.frame_white1.setGeometry(QtCore.QRect(25, 170, 400, 240))
        self.frame_white1.setStyleSheet("background-color: white")
        self.frame_white1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_white1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white1.setObjectName("frame_white")

        self.label_score12.setGeometry(QtCore.QRect(150, 20, 100, 200))
        self.label_score12.setStyleSheet("background-color: None;font-family: Gotham-Light; font-size: 135px;")
        self.label_score12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score12.setObjectName("label_score2")

        self.control_panel.setGeometry(QtCore.QRect(0, 100, 900, 70))
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
        self.label_1min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_1min.setObjectName("label_1min")

        self.label_15min.setGeometry(QtCore.QRect(35, 40, 45, 14))
        self.label_15min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_15min.setObjectName("label_15min")

        self.label_2min.setGeometry(QtCore.QRect(80, 40, 40, 14))
        self.label_2min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_2min.setObjectName("label_2min")

        self.label_3min.setGeometry(QtCore.QRect(120, 40, 35, 14))
        self.label_3min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
        self.label_3min.setObjectName("label_3min")

        self.label_5min.setGeometry(QtCore.QRect(155, 40, 34, 14))
        self.label_5min.setStyleSheet("font-family: Gotham-Light; font-size: 10px;")
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
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(13)
        self.btn_reset.setFont(font)
        self.btn_reset.setToolTip('Сбросить всё')
        self.btn_showData.setToolTip('Отобразить на Большом экране номер татами и категорию')

        self.btn_reset.setObjectName("btn_reset")

        self.btn_pause.setGeometry(QtCore.QRect(725, 20, 150, 30))
        self.btn_pause.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(13)
        self.btn_pause.setFont(font)
        self.btn_pause.setToolTip('Сбросить только секундомер')
        self.btn_pause.setObjectName("btn_pause")

        self.btn_start.setGeometry(QtCore.QRect(230, 10, 115, 50))
        self.btn_start.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")


        self.score_white_0.setGeometry(QtCore.QRect(10, 8, 40, 25))
        self.score_white_0.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_0.setChecked(True)
        self.score_white_0.setObjectName("score_white_0")

        self.score_white_1.setGeometry(QtCore.QRect(10, 41, 40, 25))
        self.score_white_1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_1.setObjectName("score_white_1")

        self.score_white_2.setGeometry(QtCore.QRect(10, 74, 40, 25))
        self.score_white_2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_2.setObjectName("score_white_2")

        self.score_white_3.setGeometry(QtCore.QRect(10, 107, 40, 25))
        self.score_white_3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_3.setObjectName("score_white_3")

        self.score_white_4.setGeometry(QtCore.QRect(10, 140, 40, 25))
        self.score_white_4.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_4.setObjectName("score_white_4")

        self.score_white_5.setGeometry(QtCore.QRect(10, 173, 40, 25))
        self.score_white_5.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_5.setObjectName("score_white_5")

        self.score_white_6.setGeometry(QtCore.QRect(10, 206, 40, 25))
        self.score_white_6.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.score_white_6.setObjectName("score_white_6")

        self.frame_rh.setGeometry(QtCore.QRect(475, 430, 405, 40))
        self.frame_rh.setStyleSheet("border-color: None")
        self.frame_rh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rh.setObjectName("frame_rh")

        self.h_red0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.h_red0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_red0.setObjectName("h_red0")

        self.h_red1.setGeometry(QtCore.QRect(35, 5, 110, 25))
        self.h_red1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red1.setObjectName("h_red1")

        self.h_red2.setGeometry(QtCore.QRect(145, 5, 80, 25))
        self.h_red2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red2.setObjectName("h_red2")

        self.h_red3.setGeometry(QtCore.QRect(225, 5, 110, 25))
        self.h_red3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_red3.setObjectName("h_red3")

        self.h_red4.setGeometry(QtCore.QRect(345, 5, 60, 25))
        self.h_red4.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.h_red4.setChecked(True)
        self.h_red4.setObjectName("h_red4")

        self.frame_rj.setGeometry(QtCore.QRect(475, 480, 405, 40))
        self.frame_rj.setStyleSheet("border-color: None")
        self.frame_rj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_rj.setObjectName("frame_rj")

        self.j_red0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.j_red0.setStyleSheet("font-family: Gotham-Light; font-size: 40px;")
        self.j_red0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_red0.setObjectName("j_red0")

        self.j_red1.setGeometry(QtCore.QRect(35, 5, 110, 25))
        self.j_red1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red1.setObjectName("j_red1")

        self.j_red2.setGeometry(QtCore.QRect(145, 5, 80, 25))
        self.j_red2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red2.setObjectName("j_red2")

        self.j_red3.setGeometry(QtCore.QRect(225, 5, 110, 25))
        self.j_red3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_red3.setObjectName("j_red3")

        self.j_red4.setGeometry(QtCore.QRect(345, 5, 60, 25))
        self.j_red4.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.j_red4.setChecked(True)
        self.j_red4.setObjectName("j_red4")

        self.frame_wh.setGeometry(QtCore.QRect(25, 430, 405, 40))
        self.frame_wh.setStyleSheet("border-color: None;")
        self.frame_wh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wh.setObjectName("frame_wh")

        self.h_white0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.h_white0.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.h_white0.setObjectName("h_white0")

        self.h_white1.setGeometry(QtCore.QRect(35, 5, 110, 25))
        self.h_white1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white1.setObjectName("h_white1")

        self.h_white2.setGeometry(QtCore.QRect(145, 5, 80, 25))
        self.h_white2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white2.setObjectName("h_white2")

        self.h_white3.setGeometry(QtCore.QRect(225, 5, 110, 25))
        self.h_white3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.h_white3.setObjectName("h_white3")

        self.h_white4.setGeometry(QtCore.QRect(345, 5, 60, 25))
        self.h_white4.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.h_white4.setChecked(True)
        self.h_white4.setObjectName("h_white4")

        self.frame_wj.setGeometry(QtCore.QRect(25, 480, 405, 40))
        self.frame_wj.setStyleSheet("border-color: None;")
        self.frame_wj.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_wj.setObjectName("frame_wj")

        self.j_white0.setGeometry(QtCore.QRect(0, 0, 25, 40))
        self.j_white0.setStyleSheet("font-family: Gotham-Light; font-size: 40px;")
        self.j_white0.setAlignment(QtCore.Qt.AlignCenter)
        self.j_white0.setObjectName("j_white0")

        self.j_white1.setGeometry(QtCore.QRect(35, 5, 110, 25))
        self.j_white1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white1.setObjectName("j_white1")

        self.j_white2.setGeometry(QtCore.QRect(145, 5, 80, 25))
        self.j_white2.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white2.setObjectName("j_white2")

        self.j_white3.setGeometry(QtCore.QRect(225, 5, 110, 25))
        self.j_white3.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.j_white3.setObjectName("j_white3")

        self.j_white4.setGeometry(QtCore.QRect(345, 5, 60, 25))
        self.j_white4.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.j_white4.setChecked(True)
        self.j_white4.setObjectName("j_white4")

        # self.retranslateUi(self.Form2)
        QtCore.QMetaObject.connectSlotsByName(self.Form2)


# class KumiteMainWindow(QWidget, KumiteMainWindow_Ui):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

        self.KumiteSecondWindow = KumiteSecondWindow()

        self.lcd1.setNumDigits(5)
        self.KumiteSecondWindow.lcd2.setNumDigits(5)
        self.timeRound()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.sound_gong1 = QSound(":/audio/gong1.wav")
        self.sound_gong2 = QSound(":/audio/gong2.wav")
        self.slider.valueChanged.connect(self.timeRound)

        # self.btn_showMinimized.clicked.connect(self.MinimizedWindow)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(Frame_Header(self))
        self.layout2.addWidget(self.Form2, 1)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint)




    def MinimizedWindow(self):
        print('1')
        self.showMinimized()



    def openSecondWinKumite(self):
        self.KumiteSecondWindow.show()

    def closeSecondWinKumite(self):
        self.KumiteSecondWindow.close()

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
            print('22222')
            self.tics -= timedelta(seconds=2)
            self.lcd1.display(str(self.tics).split()[1])
            self.KumiteSecondWindow.lcd2.display(str(self.tics).split()[1])
            self.btn_start.setText('► START')

    def update_time(self):
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
        if self.btn_start.text() == '► START':
            self.btn_start.setText('▇ STOP')
            self.timer.start(1000)
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            font = QtGui.QFont()
            font.setFamily("Gotham-Medium")
            font.setPixelSize(13)
            self.btn_pause.setFont(font)
            self.btn_reset.setFont(font)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)
        else:
            self.timer.stop()
            self.btn_start.setText('► START')
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            font = QtGui.QFont()
            font.setFamily("Gotham-Medium")
            font.setPixelSize(13)
            self.btn_pause.setFont(font)
            self.btn_reset.setFont(font)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)

    def reset_timer(self):
        if self.btn_start.text() != '► START':
            self.btn_pause.setText('Останови бой')
            self.btn_pause.setStyleSheet("color: red")
            self.btn_pause.setToolTip('Сперва нужно остановить бой')


        else:
            self.timeRound()
            self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
            self.btn_reset.setText('НОВЫЙ БОЙ')
            font = QtGui.QFont()
            font.setFamily("Gotham-Medium")
            font.setPixelSize(13)
            self.btn_pause.setFont(font)
            self.btn_reset.setFont(font)
            self.btn_pause.setStyleSheet(self.btn_style_1)
            self.btn_reset.setStyleSheet(self.btn_style_1)
            self.btn_pause.setToolTip('Сбросить только секундомер')
            self.btn_reset.setToolTip('Сбросить всё')

    def reset_all(self):
        if self.btn_start.text() != '► START':
            self.btn_reset.setText('Останови бой')
            self.btn_reset.setStyleSheet("color: red")
            self.btn_pause.setToolTip('Сперва нужно остановить бой')

        else:
            self.clearKumiteData()
            self.btn_pause.setToolTip('Сбросить только секундомер')
            self.btn_reset.setToolTip('Сбросить всё')

    def clearKumiteData(self):
        self.timer.stop()
        self.timeRound()
        self.j_red4.clicked.connect(self.penaltyButton_jr4)
        self.h_white4.clicked.connect(self.penaltyButton_hmw4)
        self.j_white4.clicked.connect(self.penaltyButton_jw4)
        self.winnerRed.setAutoExclusive(False)
        self.winnerWhite.setAutoExclusive(False)
        self.winnerRed.setChecked(False)
        self.winnerWhite.setChecked(False)
        self.winnerRed.setAutoExclusive(True)
        self.winnerWhite.setAutoExclusive(True)
        self.winnerRed.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerWhite.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.KumiteSecondWindow.line2.show()
        self.KumiteSecondWindow.frame_white2.setGeometry(QtCore.QRect(1000, 150, 880, 850))
        self.KumiteSecondWindow.frame_red2.setGeometry(QtCore.QRect(40, 150, 880, 850))
        self.KumiteSecondWindow.frame_white2.show()
        self.KumiteSecondWindow.frame_red2.show()
        self.KumiteSecondWindow.label_winner.hide()

        self.btn_pause.setText('ОБНУЛИТЬ ТАЙМЕР')
        self.btn_reset.setText('НОВЫЙ БОЙ')
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(13)
        self.btn_pause.setFont(font)
        self.btn_reset.setFont(font)
        self.btn_pause.setStyleSheet(self.btn_style_1)
        self.btn_reset.setStyleSheet(self.btn_style_1)
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
        self.score_red_0.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_1.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_2.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_3.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_4.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_5.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_red_6.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        radio = self.sender()
        if radio.isChecked():
            radio.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
            self.label_score11.setText(radio.text())
            self.KumiteSecondWindow.label_score21.setText(radio.text())

    def onClickedW(self):
        self.score_white_0.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_1.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_2.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_3.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_4.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_5.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        self.score_white_6.setStyleSheet("border-bottom: none; font-family: Gotham-Light; font-size: 20px;")
        radio = self.sender()
        if radio.isChecked():
            radio.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
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
        rad_M0.setStyleSheet('border-bottom: none; font-family: Gotham-Light; font: 20px')
        rad_M1.setStyleSheet('border-bottom: none; font-family: Gotham-Light; font: 20px;')
        rad_M2.setStyleSheet('border-bottom: none; font-family: Gotham-Light; font: 20px;')
        rad_M3.setStyleSheet('border-bottom: 1px solid black; font-family: Gotham-Light; font: 20px;')
        rad_S1.setStyleSheet(rad_S1_FontSize)
        rad_S2.setStyleSheet(rad_S2_FontSize)
        rad_S3.setStyleSheet(rad_S3_FontSize)

    def setWinnerRed(self):
        self.winnerWhite.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerRed.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.KumiteSecondWindow.frame_red2.setGeometry(QtCore.QRect(520, 150, 880, 850))
        self.KumiteSecondWindow.line2.hide()
        self.KumiteSecondWindow.label_winner.show()
        self.KumiteSecondWindow.frame_red2.show()
        self.KumiteSecondWindow.frame_white2.hide()

    def setWinnerWhite(self):
        self.winnerRed.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.winnerWhite.setStyleSheet("border-bottom: 1px solid black; font-family: Gotham-Light; font-size: 20px;")
        self.KumiteSecondWindow.frame_white2.setGeometry(QtCore.QRect(520, 150, 880, 850))
        self.KumiteSecondWindow.line2.hide()
        self.KumiteSecondWindow.label_winner.show()
        self.KumiteSecondWindow.frame_white2.show()
        self.KumiteSecondWindow.frame_red2.hide()

    def setMatchTitle(self):
        firstWindowMatchName1 = self.matchName11.fontMetrics().boundingRect(self.matchName11.text()).width()
        firstWindowMatchName2 = self.matchName12.fontMetrics().boundingRect(self.matchName12.text()).width()
        print('Татами =', firstWindowMatchName1)
        print('Категория =', firstWindowMatchName2)

        if firstWindowMatchName1 > 100:
            n = "font-family: Gotham-Medium; font-size: "\
                + str(int(20 * (650 / firstWindowMatchName1))) + "px; color: grey;"
            self.KumiteSecondWindow.matchName21.setStyleSheet(n)
            print('Татами на экране =', str(int(20 * (650 / firstWindowMatchName1))))
        else:
            self.KumiteSecondWindow.matchName21.setStyleSheet("font-family: Gotham-Medium;"
                                                              "font-size: 50px; color: grey;")

        if firstWindowMatchName2 > 100:
            n = "background-color: none; font-family: Gotham-Medium; font-size: "\
                + str(int(20 * (680 / firstWindowMatchName2))) + "px; color: grey;"
            self.KumiteSecondWindow.matchName22.setStyleSheet(n)
            print('Татами на экране =', str(int(20 * (680 / firstWindowMatchName2))))
        else:
            self.KumiteSecondWindow.matchName22.setStyleSheet("font-family: Gotham-Medium;"
                                                              "font-size: 50px; color: grey;")
        self.KumiteSecondWindow.matchName21.setText(self.matchName11.text())
        self.KumiteSecondWindow.matchName22.setText(self.matchName12.text())


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

