"""Главное меню без запуска MenuWindow, Excel и сетевого подключения."""
import ast
import base64
import os
from pathlib import Path
import unittest

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import styleCSS as css
from program_download import DOWNLOAD_URL, DOWNLOAD_QR_PNG


def make_menu():
    # Импорт основного файла запускает приложение. Извлекаем только класс
    # построения интерфейса, чтобы не открывать книги и не подключать трансляцию.
    path = Path(__file__).resolve().parents[1] / 'USKO-Russia-Tab.py'
    tree = ast.parse(path.read_text(encoding='utf-8-sig'))
    node = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'Ui_Form0')
    namespace = dict(QtCore=QtCore, QtGui=QtGui, QtWidgets=QtWidgets, css=css,
                     base64=base64, DOWNLOAD_URL=DOWNLOAD_URL, DOWNLOAD_QR_PNG=DOWNLOAD_QR_PNG)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
    form = QtWidgets.QWidget()
    ui = namespace['Ui_Form0']()
    ui.setupUi0(form)
    return form, ui


class MainMenuQrTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    def test_qr_and_link_fit_between_selection_and_modes(self):
        form, ui = make_menu()
        self.addCleanup(form.deleteLater)
        self.assertFalse(ui.download_qr.pixmap().isNull())
        self.assertEqual(ui.download_qr.pixmap().size(), QtCore.QSize(147, 147))
        self.assertIn(DOWNLOAD_URL, ui.download_link.text())
        self.assertTrue(ui.download_link.openExternalLinks())
        for widget in (ui.download_qr, ui.download_link):
            self.assertTrue(form.rect().contains(widget.geometry()))
            self.assertGreater(widget.y(), ui.frame_combo.geometry().bottom())
            self.assertLess(widget.geometry().bottom(), ui.btn_Kata_qual.y())
            self.assertLess(widget.geometry().right(), ui.frame_logo.x())

    def test_qr_resource_has_white_quiet_zone(self):
        image = QtGui.QImage.fromData(base64.b64decode(DOWNLOAD_QR_PNG), 'PNG')
        self.assertEqual(image.size(), QtCore.QSize(196, 196))
        # Белое поле нужно сканеру; оно не должно теряться при встраивании PNG.
        for x, y in ((0, 0), (15, 15), (195, 195), (0, 100), (100, 0)):
            self.assertEqual(image.pixelColor(x, y), QtGui.QColor('white'))
