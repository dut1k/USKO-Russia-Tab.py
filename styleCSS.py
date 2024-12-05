from PyQt5 import QtGui

btn_style_header = """
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

btn_style_1 = """
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
    QPushButton:disabled {
        border: 3px solid #FAF9F9;
        background-color:#edede9;
        color: #dad7cd;
        }
"""

btn_style_2 = """
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

# Кнопка, как обычный текст
btn_style_3 = """
    QPushButton {
        border: none;
        color: black;
        background-color: none;
        }
    QPushButton:hover {
        border-bottom: 1px solid #3e6ae1;
        color: #3e6ae1;
        }
    QPushButton:pressed {
        border-bottom: 1px solid white;
        background-color: #3e6ae1;
        color: white;
        }
    QPushButton:disabled {
        color: #dad7cd;
        }
"""

combo_style_header = """
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

combo_style_1 = """
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

combo_style_2 = """
QLineEdit {
        border: none;
        border-radius: 0;
        background-color: #FAF9F9;
        color: #555B6E;
        }
    QLineEdit:hover {
        background-color: #fdfdfd;
        color: black;
        }  
QComboBox {
        border-radius: 0;
        border: 1px solid gray;
        background-color: #FAF9F9;
        color: #555B6E;
        }
    QComboBox:hover {
        border: 1px solid #3e6ae1;
        background-color: #fdfdfd;
        color: black;
        }
    QComboBox::drop-down {
        background-color: white;
        width: 30px;
        border: none;
    }
    QComboBox::drop-down:pressed, QComboBox::drop-down:focus , QComboBox::drop-down:hover {
        background-color: #cce4f7;
    }
    QComboBox::down-arrow {
        image: url(:/Images/icon_regions/flags/QComboBox_down_arrow.svg);
        width: 20px;
        height: 20px;
    }
    QComboBox::down-arrow:on {
        image: url(:/Images/icon_regions/flags/QComboBox_down_arrow_on.svg);
    }
    /* ===================== focused row ===================== */
    QComboBox QAbstractItemView {
        border: none;
        selection-background-color: #3e6ae1;
    }
    /* ===================== vertical scroll ===================== */
    /* = шкала = */
    QScrollBar:vertical {
        background-color: none;
        border: 1px transparent gray;
        width: 5px;
    }
    /* = ползунок = */
    QScrollBar::handle:vertical {
        background-color: #3e6ae1;         
        min-height: 5px;
        border-radius: 0;
    }
    QListView {
        background-color: #FAF9F9;
        color: black;
        border-radius: 0;
        border-left: 1px solid red;
    }
    QComboBox:disabled {
        border: none;
        background-color:#edede9;
        color: grey;
    }
    QLineEdit:disabled {
        border: none;
        background-color:#edede9;
        color: grey;
    }
    QComboBox::down-arrow:disabled {
        image: none;
    }
    QComboBox::drop-down:disabled {
        background-color: #edede9;
    }
"""

LEdit_style_referee = """
    QLineEdit {
        border: none;
        border-bottom: 1px solid grey;
        background-color: #FAF9F9;
        color: #555B6E;
        font-size: 46px;
        font-family: Gotham-Light;
        }
    QLineEdit:hover {
        border-bottom: 2px solid #3e6ae1;
        background-color: #fdfdfd;
        color: black;
        }
"""

LEdit_style_1 = """
    QLineEdit {
        border: none;
        border-radius: none;
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
    QLineEdit:disabled {
        border: none;
        background-color:#edede9;
        color: grey;
        }
"""

LEdit_style_2 = """
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

label_style_1 = """
color: black;
background-color: white;
font-size: 150px;
font-family: Gotham-Medium; 
text-align: left;
"""

Radio_style_1 = """
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

Radio_style_2 = """
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

pers_com_qbx_style_1 = """
QCheckBox::indicator:unchecked {
    image: url(:/Images/toggle-pers.svg);
}
QCheckBox::indicator:unchecked:hover {
    image: url(:/Images/toggle-pers_hover.svg);
}
QCheckBox::indicator:checked {
    image: url(:/Images/toggle-group.svg);
}
QCheckBox::indicator:checked:hover {
    image: url(:/Images/toggle-group_hover.svg);
}
"""

lbl_style_1 = """
    QLabel:hover {
        border-bottom: 1px solid #3e6ae1;
        color: #3e6ae1;
        }
    QLabel {
        border: none;
        color: black;
    """

#################################################################
# Стиль текста
#################################################################
font_l_10 = QtGui.QFont()
font_l_10.setFamily("Gotham-Light")
font_l_10.setPixelSize(10)

font_l_12 = QtGui.QFont()
font_l_12.setFamily("Gotham-Light")
font_l_12.setPixelSize(12)

font_l_13 = QtGui.QFont()
font_l_13.setFamily("Gotham-Light")
font_l_13.setPixelSize(13)

font_m_13 = QtGui.QFont()
font_m_13.setFamily("Gotham-Medium")
font_m_13.setPixelSize(13)

font_b_13 = QtGui.QFont()
font_b_13.setFamily("Gotham-Bold")
font_b_13.setPixelSize(13)

font_l_15 = QtGui.QFont()
font_l_15.setFamily("Gotham-Light")
font_l_15.setPixelSize(15)

font_m_15 = QtGui.QFont()
font_m_15.setFamily("Gotham-Medium")
font_m_15.setPixelSize(15)

font_l_16 = QtGui.QFont()
font_l_16.setFamily("Gotham-Light")
font_l_16.setPixelSize(16)

font_m_16 = QtGui.QFont()
font_m_16.setFamily("Gotham-Medium")
font_m_16.setPixelSize(16)

font_l_20 = QtGui.QFont()
font_l_20.setFamily("Gotham-Light")
font_l_20.setPixelSize(20)

font_m_20 = QtGui.QFont()
font_m_20.setFamily("Gotham-Medium")
font_m_20.setPixelSize(20)

font_b_20 = QtGui.QFont()
font_b_20.setFamily("Gotham-Bold")
font_b_20.setPixelSize(20)

font_l_22 = QtGui.QFont()
font_l_22.setFamily("Gotham-Light")
font_l_22.setPixelSize(22)

font_l_30 = QtGui.QFont()
font_l_30.setFamily("Gotham-Light")
font_l_30.setPixelSize(30)

font_m_33 = QtGui.QFont()
font_m_33.setFamily("Gotham-Medium")
font_m_33.setPixelSize(33)

font_m_35 = QtGui.QFont()
font_m_35.setFamily("Gotham-Medium")
font_m_35.setPixelSize(35)

font_l_40 = QtGui.QFont()
font_l_40.setFamily("Gotham-Light")
font_l_40.setPixelSize(40)

font_b_40 = QtGui.QFont()
font_b_40.setFamily("Gotham-Bold")
font_b_40.setPixelSize(40)

font_l_46 = QtGui.QFont()
font_l_46.setFamily("Gotham-Light")
font_l_46.setPixelSize(46)

font_b_60 = QtGui.QFont()
font_b_60.setFamily("Gotham-Bold")
font_b_60.setPixelSize(60)

font_m_60 = QtGui.QFont()
font_m_60.setFamily("Gotham-Medium")
font_m_60.setPixelSize(60)

font_m_100 = QtGui.QFont()
font_m_100.setFamily("Gotham-Medium")
font_m_100.setPixelSize(100)

font_m_530 = QtGui.QFont()
font_m_530.setFamily("Gotham-Medium")
font_m_530.setPixelSize(530)

font_l_150 = QtGui.QFont()
font_l_150.setFamily("Gotham-Light")
font_l_150.setPixelSize(150)

font_l_190 = QtGui.QFont()
font_l_190.setFamily("Gotham-Light")
font_l_190.setPixelSize(190)

font_b_250 = QtGui.QFont()
font_b_250.setFamily("Gotham-Bold")
font_b_250.setPixelSize(250)
