import os
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch
import winsound

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from Kumite import KumiteMainWindow_Ui


class KumiteGongTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        for weight in ("Light", "Medium", "Bold"):
            QtGui.QFontDatabase.addApplicationFont(f":/Fonts/Gotham-{weight}.ttf")

    def test_gongs_use_current_resources_and_finish_round_before_playback(self):
        window = KumiteMainWindow_Ui()
        self.addCleanup(window.close)
        self.addCleanup(window.KumiteSecondWindow.close)
        self.addCleanup(window.timer.stop)
        played = []

        def play(path, flags):
            name = Path(path).name
            resource = QtCore.QFile(f":/Audio/{name}")
            self.assertTrue(resource.open(QtCore.QIODevice.ReadOnly))
            self.assertEqual(Path(path).read_bytes(), bytes(resource.readAll()))
            self.assertTrue(flags & winsound.SND_ASYNC)
            self.assertTrue(flags & winsound.SND_FILENAME)
            played.append(name)
            if name == "gong_x1.wav":
                self.assertFalse(window.timer.isActive())
                self.assertTrue(window.winnerRed.isEnabled())
                self.assertTrue(window.winnerWhite.isEnabled())
                raise RuntimeError("Аудиоустройство недоступно")

        with patch("Kumite.winsound.PlaySound", side_effect=play), patch("builtins.print"):
            window.tics = datetime.strptime("00:31", "%M:%S")
            window.update_time()
            self.assertTrue(window.timer.isActive())
            window.update_time()
            window.tics = datetime.strptime("00:00", "%M:%S") + timedelta(seconds=1)
            window.update_time()

        self.assertEqual(played, ["gong_x2.wav", "gong_x1.wav"])
