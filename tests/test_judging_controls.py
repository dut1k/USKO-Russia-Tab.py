import ast
import os
from pathlib import Path
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from Kata_final import KataMainWindow_Ui
from Kata_qual import KataQual_MainWindow_Ui
from Kumite import KumiteMainWindow_Ui


class JudgingControlsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        for weight in ("Light", "Medium", "Bold"):
            QtGui.QFontDatabase.addApplicationFont(f":/Fonts/Gotham-{weight}.ttf")

    def test_sex_radio_buttons_have_room_for_labels_and_start_unselected(self):
        for window_class in (KumiteMainWindow_Ui, KataQual_MainWindow_Ui, KataMainWindow_Ui):
            with self.subTest(mode=window_class.__name__):
                window = window_class()
                self.addCleanup(window.deleteLater)
                male, female = window.male, window.female
                self.assertEqual((male.isChecked(), female.isChecked()), (False, False))
                self.assertFalse(male.geometry().intersects(female.geometry()))
                for button in (male, female):
                    self.assertIsInstance(button, QtWidgets.QRadioButton)
                    self.assertTrue(window.frame_sex.rect().contains(button.geometry()))
                    option = QtWidgets.QStyleOptionButton()
                    option.initFrom(button)
                    option.text = button.text()
                    text_rect = button.style().subElementRect(
                        QtWidgets.QStyle.SE_RadioButtonContents, option, button)
                    # Запас нужен для системного индикатора на экране с высоким DPI.
                    text_width = button.fontMetrics().horizontalAdvance(button.text())
                    self.assertGreaterEqual(text_rect.width() - text_width, 8)
                male.click()
                self.assertEqual((male.isChecked(), female.isChecked()), (True, False))
                female.click()
                self.assertEqual((male.isChecked(), female.isChecked()), (False, True))

    def test_selected_name_uses_gotham_and_shows_start_of_long_text(self):
        # Извлекаем настройку поля без запуска меню, Excel и трансляции.
        path = Path(__file__).resolve().parents[1] / "USKO-Russia-Tab.py"
        tree = ast.parse(path.read_text(encoding="utf-8-sig"))
        menu = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "MenuWindow")
        setup = next(node for node in menu.body if isinstance(node, ast.FunctionDef)
                     and node.name == "make_searchable_combo")
        namespace = dict(QtCore=QtCore, QtWidgets=QtWidgets)
        exec(compile(ast.Module(body=[setup], type_ignores=[]), str(path), "exec"), namespace)

        combo = QtWidgets.QComboBox()
        self.addCleanup(combo.deleteLater)
        font = QtGui.QFont("Gotham-Light")
        font.setPixelSize(12)
        combo.setFont(font)
        combo.resize(160, 25)
        namespace[setup.name](None, combo)
        editor = combo.lineEdit()
        name = "Александрова Александра Александровна — Нижегородская область"
        combo.addItems(["Выбор", name])
        combo.setCurrentIndex(1)

        self.assertEqual(editor.text(), name)
        self.assertEqual(editor.font().family(), "Gotham-Light")
        self.assertEqual(editor.font().pixelSize(), 12)
        self.assertTrue(editor.alignment() & QtCore.Qt.AlignLeft)
        self.assertEqual(editor.cursorPosition(), 0)
