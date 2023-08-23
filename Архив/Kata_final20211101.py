from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class KataSecondWindow_Ui(object):
    def setupUi_Kata2(self, Form12):
        Form12.setObjectName("Form")
        Form12.setEnabled(True)
        Form12.resize(1920, 1080)
        Form12.setWindowOpacity(1.0)
        Form12.setStyleSheet("background-color: white;")
        Form12.setWindowIcon(QtGui.QIcon(':/Images/Empty.png'))


        self.label_sum2 = QtWidgets.QLabel(Form12)
        self.input_referee1 = QtWidgets.QLabel(Form12)
        self.input_referee2 = QtWidgets.QLabel(Form12)
        self.input_referee3 = QtWidgets.QLabel(Form12)
        self.input_referee4 = QtWidgets.QLabel(Form12)
        self.input_referee5 = QtWidgets.QLabel(Form12)
        self.input_referee6 = QtWidgets.QLabel(Form12)
        self.input_referee7 = QtWidgets.QLabel(Form12)
        self.label_1 = QtWidgets.QLabel(Form12)
        self.label_2 = QtWidgets.QLabel(Form12)
        self.label_3 = QtWidgets.QLabel(Form12)
        self.label_4 = QtWidgets.QLabel(Form12)
        self.label_5 = QtWidgets.QLabel(Form12)
        self.label_6 = QtWidgets.QLabel(Form12)
        self.label_7 = QtWidgets.QLabel(Form12)
        self.matchName2 = QtWidgets.QLabel(Form12)
        self.label_name_red_2 = QtWidgets.QLabel(Form12)
        self.label_region_red_2 = QtWidgets.QLabel(Form12)

        self.label_sum2.setGeometry(QtCore.QRect(1050, 150, 800, 490))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_sum2.sizePolicy().hasHeightForWidth())
        self.label_sum2.setStyleSheet("background-color: white; font-family: Gotham-Bold; font-size: 350px; ")
        self.label_sum2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sum2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_sum2.setLineWidth(1)
        self.label_sum2.setMidLineWidth(0)
        self.label_sum2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum2.setObjectName("label_sum2")

        self.label_1.setEnabled(True)
        self.label_1.setGeometry(QtCore.QRect(70, 680, 250, 50))
        self.label_1.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_1.setObjectName("label_1")

        self.label_2.setGeometry(QtCore.QRect(325, 680, 250, 50))
        self.label_2.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(580, 680, 250, 50))
        self.label_3.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(835, 680, 250, 50))
        self.label_4.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(1090, 680, 250, 50))
        self.label_5.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")

        self.label_6.setGeometry(QtCore.QRect(1345, 680, 250, 50))
        self.label_6.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")

        self.label_7.setGeometry(QtCore.QRect(1600, 680, 250, 50))
        self.label_7.setStyleSheet("font-family: Gotham-Medium; font-size: 35px; ")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")

        self.input_referee1.setGeometry(QtCore.QRect(70, 740, 250, 250))
        self.input_referee1.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee1.setObjectName("input_referee1")

        self.input_referee2.setGeometry(QtCore.QRect(325, 740, 250, 250))
        self.input_referee2.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee2.setObjectName("input_referee2")

        self.input_referee3.setGeometry(QtCore.QRect(580, 740, 250, 250))
        self.input_referee3.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee3.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee3.setObjectName("input_referee3")

        self.input_referee4.setGeometry(QtCore.QRect(835, 740, 250, 250))
        self.input_referee4.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee4.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee4.setObjectName("input_referee4")

        self.input_referee5.setGeometry(QtCore.QRect(1090, 740, 250, 250))
        self.input_referee5.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee5.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee5.setObjectName("input_referee5")

        self.input_referee6.setGeometry(QtCore.QRect(1345, 740, 250, 250))
        self.input_referee6.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee6.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee6.setObjectName("input_referee6")

        self.input_referee7.setGeometry(QtCore.QRect(1600, 740, 250, 250))
        self.input_referee7.setFrameShape(QtWidgets.QFrame.Box)
        self.input_referee7.setAlignment(QtCore.Qt.AlignCenter)
        self.input_referee7.setObjectName("input_referee7")

        self.matchName2.setGeometry(QtCore.QRect(20, 10, 1880, 100))
        self.matchName2.setStyleSheet("font-family: Gotham-Medium; font-size: 100px; color: grey;")
        self.matchName2.setAlignment(QtCore.Qt.AlignCenter)
        self.matchName2.setObjectName("matchName2")

        self.label_name_red_2.setGeometry(QtCore.QRect(40, 160, 1000, 260))
        self.label_name_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium; font-size: 133px;")
        self.label_name_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_2.setObjectName("label_name_red_2")

        self.label_region_red_2.setGeometry(QtCore.QRect(40, 440, 1000, 130))
        self.label_region_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium; font-size: 53px;")
        self.label_region_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_2.setObjectName("label_region_red_2")


        self.retranslateUi(Form12)
        QtCore.QMetaObject.connectSlotsByName(Form12)

    def retranslateUi(self, Form12):
        _translate = QtCore.QCoreApplication.translate
        Form12.setWindowTitle(_translate("Form12", " "))
        self.label_sum2.setText(_translate("Form12", ""))
        self.label_1.setText(_translate("Form12", "1"))
        self.label_3.setText(_translate("Form12", "3"))
        self.label_4.setText(_translate("Form12", "4"))
        self.label_2.setText(_translate("Form12", "2"))
        self.label_5.setText(_translate("Form12", "5"))
        self.label_7.setText(_translate("Form12", "7"))
        self.label_6.setText(_translate("Form12", "6"))
        self.input_referee6.setText(_translate("Form12", ""))
        self.input_referee4.setText(_translate("Form12", ""))
        self.input_referee2.setText(_translate("Form12", ""))
        self.input_referee7.setText(_translate("Form12", ""))
        self.input_referee1.setText(_translate("Form12", ""))
        self.input_referee3.setText(_translate("Form12", ""))
        self.input_referee5.setText(_translate("Form12", ""))
        #self.matchName2.setText(_translate("Form12", "Татами №#, Возраст"))
        self.label_region_red_2.setText(_translate("Form12", "регион"))
        self.label_name_red_2.setText(_translate("Form12", "ФАМИЛИЯ"))


class KataSecondWindow(QWidget, KataSecondWindow_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi_Kata2(self)

    def Extream_Value(self):
        q1 = self.input_referee1.text()
        q2 = self.input_referee2.text()
        q3 = self.input_referee3.text()
        q4 = self.input_referee4.text()
        q5 = self.input_referee5.text()
        q6 = self.input_referee6.text()
        q7 = self.input_referee7.text()

        l = [q1, q2, q3, q4, q5, q6, q7]
        m = [num for num in l if num != '']
        try:
            if min(m) == self.input_referee1.text():
                self.extreamLabelStyle(self.input_referee1)
            elif min(m) == self.input_referee2.text():
                self.extreamLabelStyle(self.input_referee2)
            elif min(m) == self.input_referee3.text():
                self.extreamLabelStyle(self.input_referee3)
            elif min(m) == self.input_referee4.text():
                self.extreamLabelStyle(self.input_referee4)
            elif min(m) == self.input_referee5.text():
                self.extreamLabelStyle(self.input_referee5)
            elif min(m) == self.input_referee6.text():
                self.extreamLabelStyle(self.input_referee6)
            elif min(m) == self.input_referee7.text():
                self.extreamLabelStyle(self.input_referee7)
            else:
                pass
            if max(m) == self.input_referee2.text():
                self.extreamLabelStyle(self.input_referee2)
            elif max(m) == self.input_referee1.text():
                self.extreamLabelStyle(self.input_referee1)
            elif max(m) == self.input_referee3.text():
                self.extreamLabelStyle(self.input_referee3)
            elif max(m) == self.input_referee4.text():
                self.extreamLabelStyle(self.input_referee4)
            elif max(m) == self.input_referee5.text():
                self.extreamLabelStyle(self.input_referee5)
            elif max(m) == self.input_referee6.text():
                self.extreamLabelStyle(self.input_referee6)
            elif max(m) == self.input_referee7.text():
                self.extreamLabelStyle(self.input_referee7)
            else:
                pass

        except ValueError:
            self.label_1.setText('1')
            self.label_2.setText('2')
            self.label_3.setText('3')
            self.label_4.setText('4')
            self.label_5.setText('5')
            self.label_6.setText('6')
            self.label_7.setText('7')

    def extreamLabelStyle(self, input_referee):
        input_referee.setStyleSheet("background-color: white; font-family: Gotham-Medium;"
                                    "color: Grey; font-size: 120px; text-align : left")


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
            border: none;
            border-bottom: 1px solid gray;
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

        self.label_windowsTitle = QLabel("КАТА ФИНАЛ/ПОЛУФИНАЛ. Судейское окно", self.frame_title)
        self.label_windowsTitle.setStyleSheet("border: none; font-family: Gotham-Medium; font-size: 12px;")
        self.label_windowsTitle.move(30, 9)

        self.frame_combo = QtWidgets.QFrame(self)
        self.frame_combo.setGeometry(QtCore.QRect(0, 0, 153, 31))

        self.frame_combo_border = QtWidgets.QFrame(self.frame_combo)
        self.frame_combo_border.setStyleSheet("background-color: grey;")
        self.frame_combo_border.setGeometry(QtCore.QRect(0, 0, 200, 1))

        self.combo = QtWidgets.QComboBox(self.frame_combo)
        self.combo.setGeometry(0, 4, 147, 24)
        self.combo.addItems(["Главное меню", "Ката отбороч.", "Кумите"])
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.combo.setFont(font)

        self.frame_btn = QtWidgets.QFrame(self)
        self.frame_btn.setFixedSize(51, 31)
        self.frame_btn.setStyleSheet("border-top: 1px solid gray; border-bottom: none; border-left: none;"
                                     "border-right: 1px solid gray;")

        self.btn_showMinimized = QtWidgets.QPushButton("_", self.frame_btn)
        self.btn_showMinimized.setGeometry(QtCore.QRect(0, 4, 24, 24))
        self.btn_showMinimized.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.btn_showMinimized.setFont(font)
        self.btn_showMinimized.clicked.connect(self.btn_showMinimized_clicked)

        self.btn_closeWin = QtWidgets.QPushButton("×", self.frame_btn)
        self.btn_closeWin.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(22)
        self.btn_closeWin.setFont(font)
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



class KataMainWindow_Ui(QWidget):
    def __init__(self):
        super(KataMainWindow_Ui, self).__init__()
        QWidget.setWindowTitle(self, "Ката финал. Судейское окно")

        self.Form11 = QtWidgets.QFrame(self)
        self.Form11.setFixedSize(900, 500)
        self.Form11.setStyleSheet("background-color: white;")

        self.Calc_Button = QtWidgets.QPushButton("Рассчитать", self.Form11)
        self.Clear_Button = QtWidgets.QPushButton("Очистить", self.Form11)
        self.heading_sum = QtWidgets.QLabel("Сумма баллов", self.Form11)
        self.label_sum = QtWidgets.QLabel("Нажми кнопку\n«Рассчитать»", self.Form11)
        self.referee_point = QtWidgets.QLabel("Оценки судей", self.Form11)
        self.label_help = QtWidgets.QLabel("Переключайся между судьями кнопкой Tab", self.Form11)

        self.frame_sportsmans = QtWidgets.QFrame(self.Form11)
        self.comboBox_age = QtWidgets.QComboBox(self.frame_sportsmans)
        self.frame_sex = QtWidgets.QFrame(self.frame_sportsmans)
        self.label_name_red_1 = QtWidgets.QLabel("ФАМИЛИЯ", self.Form11)
        self.label_region_red_1 = QtWidgets.QLabel("регион", self.Form11)
        self.male = QtWidgets.QRadioButton("М", self.frame_sex)
        self.female = QtWidgets.QRadioButton("Ж", self.frame_sex)
        self.sex_1 = QtWidgets.QLabel("Пол", self.frame_sportsmans)
        self.age_1 = QtWidgets.QLabel("Возраст", self.frame_sportsmans)
        self.comboBox_name_red_1 = QtWidgets.QComboBox(self.frame_sportsmans)
        self.name_red_1 = QtWidgets.QLabel("Выберите спортсмена", self.frame_sportsmans)
        self.lineEdit_name_red_1 = QtWidgets.QLineEdit(self.Form11, placeholderText="Введите имя спортсмена")
        self.lineEdit_region_red_1 = QtWidgets.QLineEdit(self.Form11, placeholderText="Введите регион")
        self.frame_matchName = QtWidgets.QFrame(self.Form11)
        self.label_matchName1 = QtWidgets.QLabel('<b>Заголовок</b>', self.frame_matchName)
        self.matchName1 = QtWidgets.QLineEdit("Татами №#, Возраст", self.frame_matchName)

        self.btn_clearData = QtWidgets.QPushButton("Очистить данные", self.Form11)
        self.btn_NewCategory = QtWidgets.QPushButton("Новая\nкатегория", self.Form11)
        self.btn_showData = QtWidgets.QPushButton("Показать фамилию\nна экране", self.Form11)

        self.frame_referee = QtWidgets.QFrame(self.Form11)
        self.lineEdit_referee1 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee2 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee3 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee4 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee5 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee6 = QtWidgets.QLineEdit(self.frame_referee)
        self.lineEdit_referee7 = QtWidgets.QLineEdit(self.frame_referee)
        self.label_1 = QtWidgets.QLabel("1 судья", self.frame_referee)
        self.label_2 = QtWidgets.QLabel("2 судья", self.frame_referee)
        self.label_3 = QtWidgets.QLabel("3 судья", self.frame_referee)
        self.label_4 = QtWidgets.QLabel("4 судья", self.frame_referee)
        self.label_5 = QtWidgets.QLabel("5 судья", self.frame_referee)
        self.label_6 = QtWidgets.QLabel("6 судья", self.frame_referee)
        self.label_7 = QtWidgets.QLabel("7 судья", self.frame_referee)

        self.frame_bottom = QtWidgets.QFrame(self.Form11)
        self.frame_left = QtWidgets.QFrame(self.Form11)
        self.frame_right = QtWidgets.QFrame(self.Form11)

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

        self.LEdit_style_1 = """
            QLineEdit {
                border: none;
                border-bottom: 1px solid grey;
                background-color: #FAF9F9;
                color: #555B6E;
                }
            QLineEdit:hover {
                border-bottom: 2px solid #3e6ae1;
                background-color: #fdfdfd;
                color: black;
                }
        """

        self.frame_bottom.setGeometry(QtCore.QRect(0, 499, 900, 1))
        self.frame_bottom.setStyleSheet("background-color: grey;")
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 1, 500))
        self.frame_left.setStyleSheet("background-color: grey;")
        self.frame_left.setObjectName("frame_left")
        self.frame_right.setGeometry(QtCore.QRect(899, 0, 1, 500))
        self.frame_right.setStyleSheet("background-color: grey;")
        self.frame_right.setObjectName("frame_right")

        self.frame_matchName.setGeometry(QtCore.QRect(200, 0, 500, 70))
        self.frame_matchName.setObjectName("matchName")

        self.label_matchName1.setGeometry(QtCore.QRect(0, 0, 500, 25))
        self.label_matchName1.setStyleSheet("font-family: Gotham-Light; font-size: 20px;")
        self.label_matchName1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_matchName1.setObjectName("label_matchName1")

        self.matchName1.setGeometry(QtCore.QRect(0, 25, 500, 30))
        self.matchName1.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(20)
        self.matchName1.setFont(font)
        self.matchName1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.matchName1.setObjectName("matchName1")

        self.btn_clearData.hide()
        self.btn_clearData.setGeometry(QtCore.QRect(710, 385, 170, 30))
        self.btn_clearData.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(16)
        self.btn_clearData.setFont(font)
        # self.btn_clearData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
        #                                         "font-size: 16px;")
        self.btn_clearData.setObjectName("btn_clearData")

        self.btn_NewCategory.hide()
        self.btn_NewCategory.setGeometry(QtCore.QRect(780, 440, 100, 40))
        self.btn_NewCategory.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.btn_NewCategory.setFont(font)
        # self.btn_NewCategory.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Light;"
        #                                           "font-size: 13px;")
        # self.btn_NewCategory.setObjectName("btn_NewCategory")

        self.btn_showData.setGeometry(QtCore.QRect(650, 330, 230, 45))
        self.btn_showData.setStyleSheet(self.btn_style_2)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(16)
        self.btn_showData.setFont(font)
        # self.btn_showData.setStyleSheet("background-color: rgb(242, 242, 242); font-family: Gotham-Medium;"
        #                                        "font-size: 16px;")
        self.btn_showData.setObjectName("btn_showData")

        self.label_name_red_1.setGeometry(QtCore.QRect(360, 40, 405, 100))
        self.label_name_red_1.setStyleSheet("background-color: none; color: grey; font-family: Gotham-Medium;"
                                            "font-size: 33px;")
        self.label_name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_red_1.setObjectName("label_name_red_1")

        self.label_region_red_1.setGeometry(QtCore.QRect(360, 90, 405, 100))
        self.label_region_red_1.setStyleSheet("background-color: none; color: grey; font-family: Gotham-Medium;"
                                              "font-size: 20px;")
        self.label_region_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_region_red_1.setObjectName("label_region_red_1")

        self.frame_sportsmans.setGeometry(QtCore.QRect(0, 440, 900, 60))
        self.frame_sportsmans.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sportsmans.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sportsmans.setStyleSheet("background-color: none;")
        self.frame_sportsmans.setObjectName("frame_sportsmans")

        self.comboBox_age.setEnabled(False)
        self.comboBox_age.setGeometry(QtCore.QRect(250, 20, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(13)
        self.comboBox_age.setFont(font)
        self.comboBox_age.setObjectName("comboBox_age")

        self.frame_sex.setGeometry(QtCore.QRect(60, 20, 150, 25))
        self.frame_sex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sex.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sex.setObjectName("frame_sex")

        self.male.setGeometry(QtCore.QRect(20, 0, 40, 25))
        self.male.setStyleSheet("font-family: Gotham-Bold; font-size: 20px;")
        self.male.setObjectName("male")

        self.female.setGeometry(QtCore.QRect(90, 0, 40, 25))
        self.female.setStyleSheet("font-family: Gotham-Bold; font-size: 20px;")
        self.female.setObjectName("female")

        self.sex_1.setGeometry(QtCore.QRect(60, 0, 150, 13))
        self.sex_1.setStyleSheet("color: black; font-family: Gotham-Bold; font-size: 13px;")
        self.sex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_1.setObjectName("sex_1")

        self.age_1.setGeometry(QtCore.QRect(250, 0, 110, 13))
        self.age_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.age_1.setAlignment(QtCore.Qt.AlignCenter)
        self.age_1.setObjectName("age_1")

        self.comboBox_name_red_1.setEnabled(False)
        self.comboBox_name_red_1.setGeometry(QtCore.QRect(400, 20, 350, 25))
        self.comboBox_name_red_1.setFont(font)
        self.comboBox_name_red_1.setObjectName("comboBox_name_red_1")

        self.name_red_1.setGeometry(QtCore.QRect(400, 0, 350, 16))
        self.name_red_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.name_red_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_red_1.setObjectName("name_red_1")

        self.lineEdit_name_red_1.setGeometry(QtCore.QRect(280, 350, 340, 30))
        self.lineEdit_name_red_1.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(20)
        self.lineEdit_name_red_1.setFont(font)
        self.lineEdit_name_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_name_red_1.setObjectName("lineEdit_name_red_1")

        self.lineEdit_region_red_1.setGeometry(QtCore.QRect(300, 400, 300, 25))
        self.lineEdit_region_red_1.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(16)
        self.lineEdit_region_red_1.setFont(font)
        self.lineEdit_region_red_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_region_red_1.setObjectName("lineEdit_region_red_1")

        self.Calc_Button.setGeometry(QtCore.QRect(60, 330, 170, 45))
        self.Calc_Button.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Medium")
        font.setPixelSize(20)
        self.Calc_Button.setFont(font)
        # self.Calc_Button.setStyleSheet("background-color: #3e6ae1; font-family: Gotham-Medium;"
        #                                "color: white; font-size: 20pt;")
        self.Calc_Button.setObjectName("Calc_Button")

        self.Clear_Button.setGeometry(QtCore.QRect(90, 385, 110, 30))
        self.Clear_Button.setStyleSheet(self.btn_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(16)
        self.Clear_Button.setFont(font)
        # self.Clear_Button.setStyleSheet("background-color: #3e6ae1; font-family: Gotham-Light;"
        #                                 "color: white; font-size: 16px;")
        self.Clear_Button.setObjectName("Clear_Button")

        self.heading_sum.setGeometry(QtCore.QRect(0, 60, 300, 20))
        self.heading_sum.setStyleSheet("font-family: Gotham-Medium; font-size: 13px;")
        self.heading_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_sum.setObjectName("heading_sum")

        self.label_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum.setGeometry(QtCore.QRect(0, 80, 300, 130))
        self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light; color: grey; font-size: 20px;")
        self.label_sum.setObjectName("label_sum")

        self.referee_point.setGeometry(QtCore.QRect(300, 180, 300, 50))
        self.referee_point.setAlignment(QtCore.Qt.AlignCenter)
        self.referee_point.setStyleSheet("font-family: Gotham-Bold; font-size: 40px;")
        self.referee_point.setObjectName("referee_point")

        self.label_help.setGeometry(QtCore.QRect(335, 317, 250, 13))
        self.label_help.setStyleSheet("color: grey; font-size: 10px;")
        self.label_help.setObjectName("label_help")

        self.frame_referee.setGeometry(QtCore.QRect(0, 230, 900, 80))
        self.frame_referee.setStyleSheet("border: none;")

        self.lineEdit_referee1.setGeometry(QtCore.QRect(70, 20, 100, 60))
        self.lineEdit_referee1.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee1.setFont(font)
        self.lineEdit_referee1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee1.setInputMask('9.9')
        self.lineEdit_referee1.setText(str('0.0'))
        self.lineEdit_referee1.setObjectName("lineEdit_referee1")

        self.lineEdit_referee2.setGeometry(QtCore.QRect(180, 20, 100, 60))
        self.lineEdit_referee2.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee2.setFont(font)
        self.lineEdit_referee2.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee2.setInputMask('9.9')
        self.lineEdit_referee2.setText(str('0.0'))
        self.lineEdit_referee2.setObjectName("lineEdit_referee2")

        self.lineEdit_referee3.setGeometry(QtCore.QRect(290, 20, 100, 60))
        self.lineEdit_referee3.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee3.setFont(font)
        self.lineEdit_referee3.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee3.setInputMask('9.9')
        self.lineEdit_referee3.setText(str('0.0'))
        self.lineEdit_referee3.setObjectName("lineEdit_referee3")

        self.lineEdit_referee4.setGeometry(QtCore.QRect(400, 20, 100, 60))
        self.lineEdit_referee4.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee4.setFont(font)
        self.lineEdit_referee4.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee4.setInputMask('9.9')
        self.lineEdit_referee4.setText(str('0.0'))
        self.lineEdit_referee4.setObjectName("lineEdit_referee4")

        self.lineEdit_referee5.setGeometry(QtCore.QRect(510, 20, 100, 60))
        self.lineEdit_referee5.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee5.setFont(font)
        self.lineEdit_referee5.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee5.setInputMask('9.9')
        self.lineEdit_referee5.setText(str('0.0'))
        self.lineEdit_referee5.setObjectName("lineEdit_referee5")

        self.lineEdit_referee6.setGeometry(QtCore.QRect(620, 20, 100, 60))
        self.lineEdit_referee6.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee6.setFont(font)
        self.lineEdit_referee6.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee6.setInputMask('9.9')
        self.lineEdit_referee6.setText(str('0.0'))
        self.lineEdit_referee6.setObjectName("lineEdit_referee6")

        self.lineEdit_referee7.setGeometry(QtCore.QRect(730, 20, 100, 60))
        self.lineEdit_referee7.setStyleSheet(self.LEdit_style_1)
        font = QtGui.QFont()
        font.setFamily("Gotham-Light")
        font.setPixelSize(46)
        self.lineEdit_referee7.setFont(font)
        self.lineEdit_referee7.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.lineEdit_referee7.setInputMask('9.9')
        self.lineEdit_referee7.setText(str('0.0'))
        self.lineEdit_referee7.setObjectName("lineEdit_referee7")

        self.label_1.setGeometry(QtCore.QRect(70, 0, 100, 13))
        self.label_1.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.label_2.setGeometry(QtCore.QRect(180, 0, 100, 13))
        self.label_2.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(290, 0, 100, 13))
        self.label_3.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(400, 0, 100, 13))
        self.label_4.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5.setGeometry(QtCore.QRect(510, 0, 100, 13))
        self.label_5.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6.setGeometry(QtCore.QRect(620, 0, 100, 13))
        self.label_6.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7.setGeometry(QtCore.QRect(730, 0, 100, 13))
        self.label_7.setStyleSheet("color: grey; font-family: Gotham-Light; font-size: 13px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")


        # self.comboBox_age.raise_()
        # self.frame_sex.raise_()
        # self.sex_1.raise_()
        # self.age_1.raise_()
        # self.comboBox_name_red_1.raise_()
        # self.name_red_1.raise_()

        QtCore.QMetaObject.connectSlotsByName(self.Form11)

        self.KataSecondWindow = KataSecondWindow()

        self.Frame_Header = Frame_Header(self)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addWidget(self.Frame_Header)
        self.layout2.addWidget(self.Form11, 1)
        self.layout2.setContentsMargins(0, 0, 0, 0)
        self.layout2.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.lineEdit_referee1.textChanged.connect(self.onChanged)
        self.lineEdit_referee2.textChanged.connect(self.onChanged)
        self.lineEdit_referee3.textChanged.connect(self.onChanged)
        self.lineEdit_referee4.textChanged.connect(self.onChanged)
        self.lineEdit_referee5.textChanged.connect(self.onChanged)
        self.lineEdit_referee6.textChanged.connect(self.onChanged)
        self.lineEdit_referee7.textChanged.connect(self.onChanged)

    def onChanged(self, text):
        sender = self.sender()
        if text == "0.":
            text = "0.0"
        elif text == "1.":
            text = "1.0"
        elif text == "2.":
            text = "2.0"
        elif text == "3.":
            text = "3.0"
        elif text == "4.":
            text = "4.0"
        elif text == "5.":
            text = "5.0"
        elif text == "6.":
            text = "6.0"
        elif text == "7.":
            text = "7.0"
        elif text == "8.":
            text = "8.0"
        elif text == "9.":
            text = "9.0"
        if text == ".":
            text = None
        else:
            if sender == self.lineEdit_referee1:
                self.KataSecondWindow.input_referee1.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee1.setText(text)
            elif sender == self.lineEdit_referee2:
                self.KataSecondWindow.input_referee2.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee2.setText(text)
            elif sender == self.lineEdit_referee3:
                self.KataSecondWindow.input_referee3.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee3.setText(text)
            elif sender == self.lineEdit_referee4:
                self.KataSecondWindow.input_referee4.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee4.setText(text)
            elif sender == self.lineEdit_referee5:
                self.KataSecondWindow.input_referee5.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee5.setText(text)
            elif sender == self.lineEdit_referee6:
                self.KataSecondWindow.input_referee6.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee6.setText(text)
            elif sender == self.lineEdit_referee7:
                self.KataSecondWindow.input_referee7.setStyleSheet("background-color: white;"
                                                                   "font-family: Gotham-Medium; color: black;"
                                                                   "font-size: 150px; text-align: left")
                self.KataSecondWindow.input_referee7.setText(text)

    def calc_display_moveCoord(self, display_coord_x1, display_coord_y1, display_width, display_height,
                               display_coord_x1_secW, display_coord_y1_secW):
        self.show()
        coord_x1 = display_coord_x1 + (display_width - self.size().width())//2
        coord_y1 = display_coord_y1 + (display_height - self.size().height())//2
        self.move(coord_x1, coord_y1)
        self.KataSecondWindow.move(display_coord_x1_secW, display_coord_y1_secW)
        self.KataSecondWindow.show()

    def closeSecondWin(self):
        self.KataSecondWindow.close()
        self.close()

    def calcResult(self):
        self.KataSecondWindow.label_1.setText('1')
        self.KataSecondWindow.label_2.setText('2')
        self.KataSecondWindow.label_3.setText('3')
        self.KataSecondWindow.label_4.setText('4')
        self.KataSecondWindow.label_5.setText('5')
        self.KataSecondWindow.label_6.setText('6')
        self.KataSecondWindow.label_7.setText('7')

        q1 = self.lineEdit_referee1.text()
        q2 = self.lineEdit_referee2.text()
        q3 = self.lineEdit_referee3.text()
        q4 = self.lineEdit_referee4.text()
        q5 = self.lineEdit_referee5.text()
        q6 = self.lineEdit_referee6.text()
        q7 = self.lineEdit_referee7.text()

        l = [q1, q2, q3, q4, q5, q6, q7]
        e = []

        for n in l:
            if n == '.':
                e.append(0.0)
            else:
                e.append(n)
        l = e
        newlst = [float(x) for x in l]

        m = newlst
        m = [num for num in m if num != 0]
        m_tuple = tuple(newlst)

        if len(m) < 3:
            self.label_sum.setText('Введи оценки судей')
            self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light;"
                                         "color: red; font-size: 20px;")
            self.KataSecondWindow.label_sum2.setText('')
            return
        else:
            m.remove(max(m))
            m.remove(min(m))
            m1 = round(sum(m), 1)
            m2 = str(m1)
            self.label_sum.setText(m2)
            l1 = str(m_tuple[0])
            self.lineEdit_referee1.setText(l1)
            self.KataSecondWindow.label_sum2.setText(self.label_sum.text())

        n_tuple = list(m_tuple)
        for num in range(len(n_tuple)):
            if n_tuple[0] == 0.0:
                n_tuple[0] = ''
                self.KataSecondWindow.label_1.setText('')
            elif n_tuple[1] == 0.0:
                n_tuple[1] = ''
                self.KataSecondWindow.label_2.setText('')
            elif n_tuple[2] == 0.0:
                n_tuple[2] = ''
                self.KataSecondWindow.label_3.setText('')
            elif n_tuple[3] == 0.0:
                n_tuple[3] = ''
                self.KataSecondWindow.label_4.setText('')
            elif n_tuple[4] == 0.0:
                n_tuple[4] = ''
                self.KataSecondWindow.label_5.setText('')
            elif n_tuple[5] == 0.0:
                n_tuple[5] = ''
                self.KataSecondWindow.label_6.setText('')
            elif n_tuple[6] == 0.0:
                n_tuple[6] = ''
                self.KataSecondWindow.label_7.setText('')

        self.KataSecondWindow.input_referee1.setText(str(n_tuple[0]))
        self.KataSecondWindow.input_referee2.setText(str(n_tuple[1]))
        self.KataSecondWindow.input_referee3.setText(str(n_tuple[2]))
        self.KataSecondWindow.input_referee4.setText(str(n_tuple[3]))
        self.KataSecondWindow.input_referee5.setText(str(n_tuple[4]))
        self.KataSecondWindow.input_referee6.setText(str(n_tuple[5]))
        self.KataSecondWindow.input_referee7.setText(str(n_tuple[6]))
        self.label_sum.setStyleSheet('background-color: None; font-family: Gotham-Light;'
                                     'font-size: 120px; color: rgb(0, 178, 80);')
        self.labelStyle(self.KataSecondWindow.input_referee1)
        self.labelStyle(self.KataSecondWindow.input_referee2)
        self.labelStyle(self.KataSecondWindow.input_referee3)
        self.labelStyle(self.KataSecondWindow.input_referee4)
        self.labelStyle(self.KataSecondWindow.input_referee5)
        self.labelStyle(self.KataSecondWindow.input_referee6)
        self.labelStyle(self.KataSecondWindow.input_referee7)

        self.lineEdit_referee1.setText(str(n_tuple[0]))
        self.lineEdit_referee2.setText(str(n_tuple[1]))
        self.lineEdit_referee3.setText(str(n_tuple[2]))
        self.lineEdit_referee4.setText(str(n_tuple[3]))
        self.lineEdit_referee5.setText(str(n_tuple[4]))
        self.lineEdit_referee6.setText(str(n_tuple[5]))
        self.lineEdit_referee7.setText(str(n_tuple[6]))

        self.KataSecondWindow.Extream_Value()
        self.fiveReferee(n_tuple[5])

    def labelStyle(self, input_referee):
        input_referee.setStyleSheet(
            "background-color: white; font-family: Gotham-Medium; color: black; font-size: 150px; text-align: left")

    def fiveReferee(self, tuple_five_referee_score):
        if tuple_five_referee_score == '':
            self.KataSecondWindow.input_referee1.setGeometry(QtCore.QRect(70, 740, 352, 250))
            self.KataSecondWindow.input_referee2.setGeometry(QtCore.QRect(427, 740, 352, 250))
            self.KataSecondWindow.input_referee3.setGeometry(QtCore.QRect(784, 740, 352, 250))
            self.KataSecondWindow.input_referee4.setGeometry(QtCore.QRect(1141, 740, 352, 250))
            self.KataSecondWindow.input_referee5.setGeometry(QtCore.QRect(1498, 740, 352, 250))
            self.KataSecondWindow.input_referee6.hide()
            self.KataSecondWindow.input_referee7.hide()
            self.KataSecondWindow.label_1.setGeometry(QtCore.QRect(70, 680, 352, 50))
            self.KataSecondWindow.label_2.setGeometry(QtCore.QRect(427, 680, 352, 50))
            self.KataSecondWindow.label_3.setGeometry(QtCore.QRect(784, 680, 352, 50))
            self.KataSecondWindow.label_4.setGeometry(QtCore.QRect(1141, 680, 352, 50))
            self.KataSecondWindow.label_5.setGeometry(QtCore.QRect(1498, 680, 352, 50))
            self.KataSecondWindow.label_6.hide()
            self.KataSecondWindow.label_7.hide()
        else:
            self.KataSecondWindow.input_referee1.setGeometry(QtCore.QRect(70, 740, 250, 250))
            self.KataSecondWindow.input_referee2.setGeometry(QtCore.QRect(325, 740, 250, 250))
            self.KataSecondWindow.input_referee3.setGeometry(QtCore.QRect(580, 740, 250, 250))
            self.KataSecondWindow.input_referee4.setGeometry(QtCore.QRect(835, 740, 250, 250))
            self.KataSecondWindow.input_referee5.setGeometry(QtCore.QRect(1090, 740, 250, 250))
            self.KataSecondWindow.input_referee6.show()
            self.KataSecondWindow.input_referee7.show()
            self.KataSecondWindow.label_1.setGeometry(QtCore.QRect(70, 680, 250, 50))
            self.KataSecondWindow.label_2.setGeometry(QtCore.QRect(325, 680, 250, 50))
            self.KataSecondWindow.label_3.setGeometry(QtCore.QRect(580, 680, 250, 50))
            self.KataSecondWindow.label_4.setGeometry(QtCore.QRect(835, 680, 250, 50))
            self.KataSecondWindow.label_5.setGeometry(QtCore.QRect(1090, 680, 250, 50))
            self.KataSecondWindow.label_6.setGeometry(QtCore.QRect(1345, 680, 250, 50))
            self.KataSecondWindow.label_7.setGeometry(QtCore.QRect(1600, 680, 250, 50))
            self.KataSecondWindow.label_6.show()
            self.KataSecondWindow.label_7.show()

    def clearKataData(self):
        self.label_sum.setText("Нажми кнопку\n«Рассчитать»")
        self.label_sum.setStyleSheet("background-color: None; font-family: Gotham-Light; color: grey; font-size: 20px;")
        self.lineEdit_referee1.setText('0.0')
        self.lineEdit_referee2.setText('0.0')
        self.lineEdit_referee3.setText('0.0')
        self.lineEdit_referee4.setText('0.0')
        self.lineEdit_referee5.setText('0.0')
        self.lineEdit_referee6.setText('0.0')
        self.lineEdit_referee7.setText('0.0')

        self.label_name_red_1.setText("ФАМИЛИЯ")
        self.label_region_red_1.setText("регион")

        self.KataSecondWindow.label_sum2.setText('')
        self.KataSecondWindow.input_referee1.setText('')
        self.KataSecondWindow.input_referee2.setText('')
        self.KataSecondWindow.input_referee3.setText('')
        self.KataSecondWindow.input_referee4.setText('')
        self.KataSecondWindow.input_referee5.setText('')
        self.KataSecondWindow.input_referee6.setText('')
        self.KataSecondWindow.input_referee7.setText('')
        self.KataSecondWindow.label_1.setText('1')
        self.KataSecondWindow.label_2.setText('2')
        self.KataSecondWindow.label_3.setText('3')
        self.KataSecondWindow.label_4.setText('4')
        self.KataSecondWindow.label_5.setText('5')
        self.KataSecondWindow.label_6.setText('6')
        self.KataSecondWindow.label_7.setText('7')

        self.KataSecondWindow.label_name_red_2.setText("ФАМИЛИЯ")
        self.KataSecondWindow.label_region_red_2.setText("регион")

    def setMatchName(self):
        matchName1_width = self.matchName1.fontMetrics().boundingRect(self.matchName1.text()).width()

        if matchName1_width > 356:
            n = "font-family: Gotham-Medium; font-size: "\
                + str(int(17.8 * (1880 / matchName1_width))) + "px; color: grey;"
            self.KataSecondWindow.matchName2.setStyleSheet(n)
        else:
            self.KataSecondWindow.matchName2.setStyleSheet(
                "font-family: Gotham-Medium; font-size: 100px; color: grey;")
        self.KataSecondWindow.matchName2.setText(self.matchName1.text())

    def setSportsmanName(self):
        self.setMatchName()
        self.label_name_red_1.setText(self.lineEdit_name_red_1.text())
        self.label_region_red_1.setText(self.lineEdit_region_red_1.text())
        first_window_name_red = self.lineEdit_name_red_1.fontMetrics().\
            boundingRect(self.lineEdit_name_red_1.text()).width()
        first_window_region_red = self.lineEdit_region_red_1.fontMetrics().\
            boundingRect(self.lineEdit_region_red_1.text()).width()

        if first_window_name_red > 145:
            n = "background-color: none; font-family: Gotham-Medium; font-size: " \
                + str(int(19.3 * (1000 / first_window_name_red))) + "px;"
            self.KataSecondWindow.label_name_red_2.setStyleSheet(n)
        else:
            self.KataSecondWindow.label_name_red_2.setStyleSheet("background-color: None; font-family: Gotham-Medium;"
                                                                 "font-size: 133px;")

        if first_window_region_red > 235:
            n = "background-color: none; font-family: Gotham-Medium; font-size: "\
                + str(int(12.5 * (1000 / first_window_region_red))) + "px;"
            self.KataSecondWindow.label_region_red_2.setStyleSheet(n)
        else:
            self.KataSecondWindow.label_region_red_2.setStyleSheet(
                "background-color: None; font-family: Gotham-Medium; font-size: 53px;")
        self.KataSecondWindow.label_name_red_2.setText(self.lineEdit_name_red_1.text())
        self.KataSecondWindow.label_region_red_2.setText(self.lineEdit_region_red_1.text())
