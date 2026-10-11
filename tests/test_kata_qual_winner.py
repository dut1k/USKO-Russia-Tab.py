"""Проверки сигналов победителя без запуска табло, Excel и сетевых запросов.

Запуск из корня проекта: python -B -m unittest discover -s tests -v
Нужен PyQt5 из зависимостей проекта.
"""

import ast
import contextlib
import io
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton, QWidget


ROOT = Path(__file__).resolve().parents[1]


def load_methods(filename, class_name, names):
    # Импорт главного модуля запускает зависимости рабочего табло. Извлекаем
    # методы целиком, чтобы проверять текущий код без Excel, сети и запуска окон.
    tree = ast.parse((ROOT / filename).read_text(encoding="utf-8-sig"))
    source_class = next(
        node for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == class_name
    )
    methods = [
        node for node in source_class.body
        if isinstance(node, ast.FunctionDef) and node.name in names
    ]
    if {node.name for node in methods} != set(names):
        raise AssertionError(f"Не найдены методы {class_name}: {names}")
    namespace = {"QtCore": QtCore}
    exec(compile(ast.Module(body=methods, type_ignores=[]), filename, "exec"), namespace)
    return {name: namespace[name] for name in names}


class QualHarness(QWidget):
    locals().update(load_methods(
        "Kata_qual.py", "KataQual_MainWindow_Ui",
        ("setSportsmanName", "setWinnerRed", "setWinnerWhite"),
    ))

    def __init__(self):
        super().__init__()
        # Общий родитель сохраняет настоящую взаимную исключительность кнопок:
        # переключение выдаёт сначала toggled(False), затем toggled(True).
        self.winnerRed = QRadioButton(self)
        self.winnerWhite = QRadioButton(self)
        self.btn_showData = QPushButton(self)
        self.matchName1 = QLabel("Категория A", self)
        for side in ("red", "white"):
            setattr(self, f"label_name_{side}_1", QLabel(f"A {side}", self))
            setattr(self, f"label_region_{side}_1", QLabel("Регион", self))
            setattr(self, f"lineEdit_name_{side}_1", QLabel(f"A {side}", self))
            setattr(self, f"lineEdit_region_{side}_1", SimpleNamespace(
                currentText=lambda: "Новый регион",
            ))
        self.KataQual_SecondWindow = SimpleNamespace(
            label_name_red_2=QLabel(self), label_name_white_2=QLabel(self),
            label_region_red_2=QLabel(self), label_region_white_2=QLabel(self),
            frame_red2=QWidget(self), frame_white2=QWidget(self),
            label_winner=QLabel(self),
        )
        self.setMatchName = Mock()


class MenuHarness(QObject):
    locals().update(load_methods(
        "USKO-Russia-Tab.py", "MenuWindow",
        ("set_winner", "build_kata_qual_state", "setSportsmanName"),
    ))

    def __init__(self, file_type="other"):
        super().__init__()
        self.ui_kataQual = QualHarness()
        self.ui_kataFinal = SimpleNamespace(
            btn_showData=QPushButton(), Calc_Button=QPushButton(), calcResult=Mock(),
        )
        self.ui_kumite = SimpleNamespace(
            btn_showData=QPushButton(), btn_show_screen=QPushButton(),
            winnerRed=QPushButton(), winnerWhite=QPushButton(),
            isShowSportsmanName=Mock(), setWinner=Mock(),
        )
        self.loaded_file_data_type = file_type
        self.has_server_info = True
        self.overlay_health_ok = Mock(return_value=True)
        self.tatamiName = "Тестовое татами"
        self.USKO_PC = "test-only"
        self.send_overlay_message = Mock()
        self.svg_resource_to_data_url = Mock(return_value="")
        self.check_to_wopf = Mock()
        self.pyatnov_winner = None
        self.sportsmen_dict = {
            "combo_box": {1: "A white - A red", 2: "B white - B red"},
            "row_num": {1: 10, 2: 20},
        }
        self.ui_kataQual.winnerRed.toggled.connect(self.set_winner)
        self.ui_kataQual.winnerWhite.toggled.connect(self.set_winner)
        self.ui_kataQual.btn_showData.clicked.connect(self.setSportsmanName)
        self.ui_kataFinal.Calc_Button.clicked.connect(self.set_winner)
        self.ui_kumite.winnerRed.clicked.connect(self.set_winner)

    def messages(self):
        return [call.args[0] for call in self.send_overlay_message.call_args_list]


class WinnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.output = io.StringIO()
        self.capture = contextlib.redirect_stdout(self.output)
        self.capture.__enter__()

    def tearDown(self):
        self.capture.__exit__(None, None, None)
        # Рабочие методы перехватывают исключения; тест не должен молча принять
        # отсутствие отправки, вызванное ошибкой неподготовленного окружения.
        self.assertNotIn("error", self.output.getvalue())
        self.assertNotIn("Exception", self.output.getvalue())

    def test_unchecking_does_not_announce_or_prepare_winner(self):
        for file_type in ("other", "file_pyatnov"):
            for button_name in ("winnerRed", "winnerWhite"):
                with self.subTest(file_type=file_type, button=button_name):
                    menu = MenuHarness(file_type)
                    button = getattr(menu.ui_kataQual, button_name)
                    button.setChecked(True)
                    prepared = menu.pyatnov_winner
                    menu.send_overlay_message.reset_mock()
                    # Маркер позволяет обнаружить повторную подготовку даже
                    # при записи того же словаря с теми же значениями.
                    if prepared is not None:
                        prepared["test_marker"] = True
                    button.setAutoExclusive(False)
                    button.setChecked(False)
                    button.setAutoExclusive(True)
                    menu.send_overlay_message.assert_not_called()
                    self.assertIs(menu.pyatnov_winner, prepared)

    def test_switch_announces_only_selected_side(self):
        for first, second, expected in (
            ("winnerRed", "winnerWhite", "siro"),
            ("winnerWhite", "winnerRed", "aka"),
        ):
            with self.subTest(side=expected):
                menu = MenuHarness("file_pyatnov")
                getattr(menu.ui_kataQual, first).setChecked(True)
                menu.send_overlay_message.reset_mock()
                getattr(menu.ui_kataQual, second).setChecked(True)
                self.assertEqual(len(menu.messages()), 1)
                self.assertEqual(menu.messages()[0]["winner_side"], expected)
                self.assertEqual(menu.pyatnov_winner["side"], expected)
                self.assertEqual(menu.pyatnov_winner["cell"],
                                 "G10" if expected == "siro" else "L10")

    def test_new_pair_removes_winner_and_next_choice_uses_new_names(self):
        for file_type in ("other", "file_pyatnov"):
            for previous in ("winnerRed", "winnerWhite"):
                with self.subTest(file_type=file_type, previous=previous):
                    menu = MenuHarness(file_type)
                    qual = menu.ui_kataQual
                    getattr(qual, previous).setChecked(True)
                    menu.send_overlay_message.reset_mock()
                    qual.matchName1.setText("Категория B")
                    qual.lineEdit_name_red_1.setText("B red")
                    qual.lineEdit_name_white_1.setText("B white")
                    # Настоящий обработчик кнопки вызывает настоящий метод UI:
                    # сброс выбранного победителя происходит до смены ФИО.
                    qual.btn_showData.click()
                    self.assertEqual(len(menu.messages()), 1)
                    state = menu.messages()[0]
                    self.assertNotIn("winner_side", state)
                    self.assertEqual(state["aka"]["name"], "B red")
                    self.assertEqual(state["siro"]["name"], "B white")
                    self.assertEqual(state["category"], "Категория B")
                    self.assertFalse(qual.winnerRed.isChecked())
                    self.assertFalse(qual.winnerWhite.isChecked())
                    self.assertTrue(qual.KataQual_SecondWindow.label_winner.isHidden())
                    qual.winnerWhite.setChecked(True)
                    winner = menu.messages()[-1]
                    self.assertEqual(winner["winner_side"], "siro")
                    self.assertEqual(winner["siro"]["name"], "B white")
                    if file_type == "file_pyatnov":
                        self.assertEqual(menu.pyatnov_winner["cell"], "G20")

    def test_final_calc_button_still_works_without_checked_state(self):
        menu = MenuHarness()
        menu.build_kata_final_state = Mock(return_value={"mode": "kata_final"})
        menu.ui_kataFinal.Calc_Button.click()
        menu.ui_kataFinal.calcResult.assert_called_once()

    def test_kumite_button_still_works_without_checked_state(self):
        menu = MenuHarness()
        menu.overlay_kumite_state = {"mode": "kumite"}
        menu.build_kumite_state = Mock(return_value=menu.overlay_kumite_state)
        menu.ui_kumite.winnerRed.click()
        menu.ui_kumite.setWinner.assert_called_once()
        self.assertEqual(menu.messages(), [{"mode": "kumite", "winner_side": "aka"}])


if __name__ == "__main__":
    unittest.main()
