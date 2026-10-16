"""Изолированные проверки зрительских окон: без книг, сети и главного меню."""

import os
from types import SimpleNamespace
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5 import QtCore, QtGui, QtWidgets
import resources  # Регистрирует изображения и шрифты, не запускает приложение.
from Kata_final import KataMainWindow_Ui, KataSecondWindow, KataSecondWindow_Ui
from Kata_qual import KataQual_MainWindow_Ui, KataQual_SecondWindow, KataQual_SecondWindow_Ui
from Kumite import KumiteMainWindow_Ui, KumiteSecondWindow, KumiteSWindow_Ui, RoundedLabel
from test_kata_qual_winner import QualHarness, load_methods


class ScreenStub(QtCore.QObject):
    geometryChanged = QtCore.pyqtSignal(QtCore.QRect)

    def __init__(self, rect):
        super().__init__()
        self.rect = rect

    def geometry(self):
        return self.rect


class AdaptiveDisplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        for weight in ("Light", "Medium", "Bold"):
            QtGui.QFontDatabase.addApplicationFont(f":/Fonts/Gotham-{weight}.ttf")

    def make_window(self, cls):
        window = cls()
        window.show()
        self.app.processEvents()
        self.addCleanup(window.close)
        self.addCleanup(window.deleteLater)
        return window

    def assert_fits(self, window, width, height):
        window.resize(width, height)
        self.app.processEvents()
        rect = window.mapFromScene(window.sceneRect()).boundingRect()
        viewport = window.viewport().rect()
        # Округление координат Qt может добавить один пиксель на границе.
        self.assertTrue(viewport.adjusted(-1, -1, 1, 1).contains(rect))
        self.assertLessEqual(abs(rect.center().x() - viewport.center().x()), 1)
        self.assertLessEqual(abs(rect.center().y() - viewport.center().y()), 1)
        self.assertAlmostEqual(window.transform().m11(), window.transform().m22())
        self.assertEqual(window.canvas.size(), QtCore.QSize(1920, 1080))
        self.assertEqual(window.horizontalScrollBar().maximum(), 0)
        self.assertEqual(window.verticalScrollBar().maximum(), 0)

    def test_all_modes_fit_without_accumulating_scale(self):
        for cls in (KumiteSecondWindow, KataQual_SecondWindow, KataSecondWindow):
            with self.subTest(mode=cls.__name__):
                window = self.make_window(cls)
                label = window.label_name_red_2
                geometry, font, style = label.geometry(), label.font(), label.styleSheet()
                for width, height in ((1920, 1080), (1366, 768), (3840, 2160),
                                      (1280, 1024), (1080, 1920), (1920, 1080)):
                    self.assert_fits(window, width, height)
                    self.assertEqual(label.geometry(), geometry)
                    self.assertEqual(label.font(), font)
                    self.assertEqual(label.styleSheet(), style)
                self.assertEqual(window.transform().m11(), 1)

    def test_screen_size_changes_never_move_window(self):
        window = self.make_window(KataQual_SecondWindow)
        window.move(-1366, 180)
        self.app.processEvents()
        position = window.pos()
        first = ScreenStub(QtCore.QRect(-1366, 180, 1366, 768))
        second = ScreenStub(QtCore.QRect(-1920, 180, 1920, 1080))
        window._use_screen(first)
        self.assertEqual(window.size(), first.geometry().size())
        first.rect.setSize(QtCore.QSize(1280, 720))
        first.geometryChanged.emit(first.rect)
        self.assertEqual(window.size(), QtCore.QSize(1280, 720))
        window._use_screen(second)
        first.geometryChanged.emit(first.rect)
        self.assertEqual(window.size(), QtCore.QSize(1920, 1080))
        self.assertEqual(window.pos(), position)

    def test_show_uses_logical_screen_size(self):
        window = self.make_window(KataQual_SecondWindow)
        self.assertEqual(window.size(), window.windowHandle().screen().geometry().size())

    def test_vector_flag_retains_round_mask_and_can_change(self):
        flag = RoundedLabel()
        flag.setFixedSize(80, 80)
        self.addCleanup(flag.deleteLater)

        def render():
            image = QtGui.QImage(320, 320, QtGui.QImage.Format_ARGB32)
            image.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(image)
            painter.scale(4, 4)
            flag.render(painter, flags=QtWidgets.QWidget.DrawChildren)
            painter.end()
            return image

        # Диагональная линия нужна, чтобы отличить отрисовку вектора от
        # увеличенного растра 80×80. Исходные флаги в тесте не перезаписываются.
        flag.setSvg(QtCore.QByteArray(b'<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80">'
                                     b'<rect width="80" height="80" fill="red"/>'
                                     b'<path d="M0 0 L80 80" stroke="white" stroke-width="1"/></svg>'))
        first = render()
        self.assertEqual(first.pixelColor(0, 0).alpha(), 0)
        self.assertEqual(first.pixelColor(319, 0).alpha(), 0)
        self.assertEqual(first.pixelColor(160, 100), QtGui.QColor("red"))
        self.assertEqual(first.pixelColor(160, 160), QtGui.QColor("white"))
        # Линия 1 px при масштабе 4 занимает около 6 px по горизонтали.
        # Увеличенный сглаженный растр дал бы белый ореол и в точке x=164.
        self.assertEqual(first.pixelColor(164, 160), QtGui.QColor("red"))
        flag.setSvg(QtCore.QByteArray(b'<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80">'
                                     b'<rect width="80" height="80" fill="blue"/></svg>'))
        self.assertEqual(render().pixelColor(160, 100), QtGui.QColor("blue"))
        empty = QtGui.QPixmap(80, 80)
        empty.fill(QtCore.Qt.transparent)
        flag.setPixmap(empty)
        self.assertEqual(render().pixelColor(160, 100).alpha(), 0)

    def test_qual_winner_switch_and_new_pair_keep_scale(self):
        harness = QualHarness()
        self.addCleanup(harness.deleteLater)
        window = self.make_window(KataQual_SecondWindow)
        harness.KataQual_SecondWindow = window
        for width, height in ((1366, 768), (3840, 2160)):
            self.assert_fits(window, width, height)
            scale = window.transform().m11()
            harness.setSportsmanName()
            for side in ("Red", "White"):
                getattr(harness, f"setWinner{side}")()
                frame = getattr(window, f"frame_{side.lower()}2")
                self.assertEqual(frame.y(), 350)
                self.assertFalse(window.label_winner.isHidden())
                self.assertEqual(window.transform().m11(), scale)
            harness.setSportsmanName()
            self.assertEqual(window.frame_red2.y(), 150)
            self.assertEqual(window.frame_white2.y(), 600)
            self.assertTrue(window.label_winner.isHidden())
            self.assertEqual(window.transform().m11(), scale)

    def test_kumite_winner_uses_same_scaled_scene(self):
        window = self.make_window(KumiteSecondWindow)
        method = load_methods("Kumite.py", "KumiteMainWindow_Ui", ("setWinner",))["setWinner"]
        for side in ("АКА", "СИРО"):
            radio = QtWidgets.QRadioButton(f"Победил {side}")
            radio.setChecked(True)
            harness = SimpleNamespace(
                show_screen=lambda: None, sender=lambda: radio,
                btn_start=QtWidgets.QPushButton("START"),
                winnerWhite=QtWidgets.QRadioButton(), winnerRed=QtWidgets.QRadioButton(),
                KumiteSecondWindow=window, KumiteSWindow_Ui=KumiteSWindow_Ui(),
            )
            self.assert_fits(window, 1366, 768)
            method(harness)
            self.assertEqual(window.sportsman_screen.y(), 150)
            self.assertEqual(window.transform().m11(), 768 / 1080)
            self.assertFalse(window.label_winner.isHidden())

    def test_final_live_scores_and_extreme_marks_survive_resize(self):
        window = self.make_window(KataSecondWindow)
        for index, score in enumerate(("7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7"), 1):
            getattr(window, f"input_referee{index}").setText(score)
        window.label_sum2.setText("37.0")
        window.Extream_Value()
        style = window.input_referee1.styleSheet()
        self.assertIn("Grey", style)
        self.assert_fits(window, 3840, 2160)
        self.assert_fits(window, 1366, 768)
        self.assertEqual(window.label_sum2.text(), "37.0")
        self.assertEqual(window.input_referee1.styleSheet(), style)
        self.assertEqual(window.input_referee7.text(), "7.7")

    def test_real_name_fitting_and_five_or_seven_referees(self):
        # Проверяем настоящий подбор шрифтов через судейские окна. Их модули
        # содержат только Qt-интерфейс; главное меню с Excel/HTTP не импортируется.
        for cls, attr in ((KumiteMainWindow_Ui, "KumiteSecondWindow"),
                          (KataQual_MainWindow_Ui, "KataQual_SecondWindow"),
                          (KataMainWindow_Ui, "KataSecondWindow")):
            with self.subTest(mode=cls.__name__):
                control = cls()
                window = getattr(control, attr)
                self.addCleanup(control.deleteLater)
                self.addCleanup(control.close)
                self.addCleanup(window.deleteLater)
                self.addCleanup(window.close)
                control.show()
                self.app.processEvents()
                control.flags_dict = {}
                name = "Александров-Константинопольский Александр"
                region = "Республика Северная Осетия — Алания"
                for side in ("red", "white"):
                    field = getattr(control, f"lineEdit_name_{side}_1", None)
                    if field is not None:
                        field.setText(name)
                        combo = getattr(control, f"lineEdit_region_{side}_1")
                        combo.addItem(region)
                        combo.setCurrentIndex(combo.count() - 1)
                control.setSportsmanName()
                window.show()
                self.app.processEvents()
                label = window.label_name_red_2
                self.assertEqual(label.text(), name)
                font, style = label.font(), label.styleSheet()
                for width, height in ((1366, 768), (3840, 2160), (1280, 1024)):
                    self.assert_fits(window, width, height)
                    control.setSportsmanName()
                    self.assertEqual(label.text(), name)
                    self.assertEqual(label.font(), font)
                    self.assertEqual(label.styleSheet(), style)
                if cls is KataMainWindow_Ui:
                    for count in (5, 7, 5):
                        for index in range(1, 8):
                            getattr(control, f"lineEdit_referee{index}").setText(
                                "7.0" if index <= count else "0.0")
                        control.calcResult()
                        self.app.processEvents()
                        self.assertEqual(window.label_sum2.text(), "21.0" if count == 5 else "35.0")
                        self.assertEqual(window.input_referee1.width(), 352 if count == 5 else 250)
                        self.assertEqual(window.input_referee7.isHidden(), count == 5)

    def test_full_hd_render_matches_original_widget(self):
        # Сравниваем настоящий старый макет с новой сценой в масштабе 1:1.
        # Это ловит пропавшие элементы, рамку proxy и сдвиг всего изображения.
        for cls, ui_cls, setup in (
            (KumiteSecondWindow, KumiteSWindow_Ui, "setupUi2"),
            (KataQual_SecondWindow, KataQual_SecondWindow_Ui, "setupUi2"),
            (KataSecondWindow, KataSecondWindow_Ui, "setupUi_Kata2"),
        ):
            with self.subTest(mode=cls.__name__):
                window = self.make_window(cls)
                original = QtWidgets.QWidget()
                ui = ui_cls()
                getattr(ui, setup)(original)
                original.show()
                self.addCleanup(original.close)
                self.addCleanup(original.deleteLater)
                self.assert_fits(window, 1920, 1080)
                self.app.processEvents()
                expected = original.grab().toImage()
                actual = window.viewport().grab().toImage()
                self.assertEqual(actual, expected)

    def test_final_region_changes_and_clear_remove_previous_flag(self):
        control = KataMainWindow_Ui()
        self.addCleanup(control.close)
        self.addCleanup(control.KataSecondWindow.close)
        self.addCleanup(control.deleteLater)
        control.flags_dict = {'московскаяобласть': '50', 'республикасевернаяосетия': '15'}
        control.matchName1.setText('Татами №7, Юноши 14–15 лет')
        window = control.KataSecondWindow
        for region in ('Московская область', 'Республика Северная Осетия', 'Неизвестный регион'):
            control.lineEdit_name_red_1.setText('Петров Александр')
            control.lineEdit_region_red_1.addItem(region)
            control.lineEdit_region_red_1.setCurrentText(region)
            control.setSportsmanName()
            self.assertEqual(window.label_region_red_2.text(), region)
            self.assertEqual(window.flag_red.isHidden(), region == 'Неизвестный регион')
            self.assertEqual(window.matchName2.text().count('Татами №7'), 1)
        control.clearKataData()
        self.assertTrue(window.flag_red.isHidden())
        self.assertEqual(window.label_sum2.text(), '')
        self.assertEqual(window.label_name_red_2.text(), 'ФАМИЛИЯ')

    def test_final_excluded_marks_clear_on_edit_and_reset(self):
        control = KataMainWindow_Ui()
        self.addCleanup(control.close)
        self.addCleanup(control.KataSecondWindow.close)
        self.addCleanup(control.deleteLater)
        window = control.KataSecondWindow
        for index, value in enumerate(('7.8', '8.1', '8.2', '8.0', '8.4', '0.0', '0.0'), 1):
            getattr(control, f'lineEdit_referee{index}').setText(value)
        control.calcResult()
        self.assertEqual(window.label_sum2.text(), '24.3')
        self.assertTrue(window.input_referee1.font().strikeOut())
        self.assertTrue(window.input_referee5.font().strikeOut())
        self.assertEqual(window.score_notes[0].text(), 'мин. исключён')
        self.assertTrue(window.score_panels[6].isHidden())
        control.lineEdit_referee1.setText('8.3')
        self.assertFalse(window.input_referee1.font().strikeOut())
        self.assertTrue(all(not note.text() for note in window.score_notes))
        control.clearKataData()
        self.assertTrue(all(not getattr(window, f'input_referee{i}').text() for i in range(1, 8)))
        self.assertFalse(window.score_panels[6].isHidden())

    def test_final_long_text_fits_with_vector_flag_at_all_sizes(self):
        window = self.make_window(KataSecondWindow)
        name = 'Александров-Константинопольский Александр Александрович'
        region = 'Республика Северная Осетия — Алания'
        window.set_athlete(name, region, '15')
        for width, height in ((1920, 1080), (1366, 768), (1280, 1024), (3840, 2160)):
            self.assert_fits(window, width, height)
            for label in (window.label_name_red_2, window.label_region_red_2):
                bounds = label.fontMetrics().boundingRect(label.contentsRect(), QtCore.Qt.TextWordWrap, label.text())
                self.assertLessEqual(bounds.width(), label.width())
                self.assertLessEqual(bounds.height(), label.height())
            self.assertLess(window.flag_red.geometry().right(), window.label_name_red_2.x())
            self.assertLess(window.label_name_red_2.geometry().bottom(), window.region_line.y())
            self.assertLess(window.label_region_red_2.geometry().bottom(), window.score_panels[0].y())


if __name__ == "__main__":
    unittest.main()
