"""Сервер проверяется только на loopback и свободных портах, без Excel и OBS."""
import ast
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
from urllib.request import Request, urlopen

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
from PyQt5 import QtCore, QtWidgets
from websockets.sync.client import connect

from server_console import LogTail, ServerWindow
from server_worker import ParentWatch

ROOT = Path(__file__).resolve().parents[1]


def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def settings_class():
    tree = ast.parse((ROOT / "USKO-Russia-Tab.py").read_text(encoding="utf-8-sig"))
    node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "ServerSettingsDialog")
    import styleCSS as css
    namespace = dict(QtCore=QtCore, QtWidgets=QtWidgets, css=css)
    exec(compile(ast.Module(body=[node], type_ignores=[]), "settings", "exec"), namespace)
    return namespace["ServerSettingsDialog"]


class ServerModeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        cls.app.setQuitOnLastWindowClosed(False)

    def wait_for(self, predicate, seconds=12):
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            self.app.processEvents()
            if predicate():
                return
            time.sleep(0.02)
        window = getattr(self, "window", None)
        self.fail("Истекло время ожидания; " + getattr(window, "state", "") + "\n" +
                  (window.terminal.toPlainText()[-5000:] if window else ""))

    def make_window(self):
        directory = tempfile.TemporaryDirectory(prefix="usko-test-")
        self.addCleanup(directory.cleanup)
        executable = os.environ.get("USKO_TEST_EXE")
        command = (executable, ["--usko-server-worker", "--host", "127.0.0.1"]) if executable else (
            sys.executable, [str(ROOT / "USKO-Russia-Tab.py"), "--usko-server-worker", "--host", "127.0.0.1"])
        self.window = ServerWindow(directory.name, command)
        self.window.port.setValue(free_port())
        self.addCleanup(self.dispose_window)
        return self.window

    def dispose_window(self):
        window = self.window
        if window.process.state() != QtCore.QProcess.NotRunning or window.pending_finish:
            window.stop_server()
            self.wait_for(lambda: window.process.state() == QtCore.QProcess.NotRunning and not window.pending_finish)
        window.timer.stop()
        if window.session:
            window.session.cleanup()
            window.session = None
        for handler in window.logger.handlers[:]:
            handler.close()
            window.logger.removeHandler(handler)
        window.hide()
        window.deleteLater()
        self.app.processEvents()

    def http(self, path, payload=None):
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = Request("http://127.0.0.1:{}{}".format(self.window.port.value(), path),
                          data=data, headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=3) as response:
            return response.read()

    def test_settings_default_to_table_and_disable_client_fields_for_server(self):
        dialog = settings_class()()
        self.addCleanup(dialog.deleteLater)
        self.assertEqual(dialog.mode_combo.currentIndex(), 0)
        self.assertTrue(dialog.edt_path.isEnabled())
        dialog.mode_combo.setCurrentIndex(1)
        self.assertFalse(dialog.edt_path.isEnabled())
        self.assertTrue(dialog.btn_ok.isEnabled())

    def test_main_menu_switches_modes_without_starting_server(self):
        window = self.make_window()
        chosen = [1]

        class SelectionDialog(settings_class()):
            def exec_(self):
                self.mode_combo.setCurrentIndex(chosen[0])
                return self.Accepted

        tree = ast.parse((ROOT / "USKO-Russia-Tab.py").read_text(encoding="utf-8-sig"))
        menu_node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "MenuWindow")
        method = next(n for n in menu_node.body if isinstance(n, ast.FunctionDef)
                      and n.name == "open_settings_dialog")
        namespace = dict(QtWidgets=QtWidgets, ServerSettingsDialog=SelectionDialog)
        exec(compile(ast.Module(body=[method], type_ignores=[]), "menu", "exec"), namespace)

        class MenuHarness(QtWidgets.QWidget):
            open_settings_dialog = namespace["open_settings_dialog"]
            server_config_path = None
            program_release_number = "test"

        menu = MenuHarness()
        self.addCleanup(menu.deleteLater)
        menu.show()
        with patch("server_console.ServerWindow", return_value=window):
            menu.open_settings_dialog()
        self.assertFalse(menu.isVisible())
        self.assertTrue(window.isVisible())
        self.assertEqual(window.process.state(), QtCore.QProcess.NotRunning)
        chosen[0] = 0
        menu.open_settings_dialog()
        self.assertTrue(menu.isVisible())
        self.assertFalse(window.isVisible())
        menu.hide()

    def test_http_websocket_isolation_reset_reconnect_and_restart(self):
        window = self.make_window()
        self.assertEqual(window.state, "off")
        self.assertEqual(window.process.state(), QtCore.QProcess.NotRunning)
        window.start_server()
        self.wait_for(lambda: window.state == "running")
        self.assertTrue(json.loads(self.http("/health"))["ok"])
        self.assertIn(b"<html", self.http("/overlay/1").lower())
        self.assertIn(b"WebSocket", self.http("/assets/usko-overlay-server-script.js"))
        self.assertIn(b"<svg", self.http("/assets/regions/77.svg"))
        self.assertGreater(len(self.http("/assets/fonts/Gotham-Light.ttf")), 1000)
        url = "ws://127.0.0.1:{}/ws/".format(window.port.value())
        with connect(url + "1") as one, connect(url + "2") as two:
            first = dict(tatami_id="1", mode="kumite", winner="aka", name="Тест А", seq=1)
            other = dict(tatami_id="2", mode="kata_final", winner="shiro", name="Тест Б", seq=1)
            self.http("/api/state", first)
            self.http("/api/state", other)
            self.assertEqual(json.loads(one.recv(timeout=4)), first)
            self.assertEqual(json.loads(two.recv(timeout=4)), other)
            reset = dict(tatami_id="1", mode="idle", winner=None, seq=2)
            self.http("/api/state", reset)
            self.assertEqual(json.loads(one.recv(timeout=4)), reset)
            with self.assertRaises(TimeoutError):
                two.recv(timeout=0.2)
        with connect(url + "1") as reconnected:
            self.assertEqual(json.loads(reconnected.recv(timeout=3)), reset)
        window.dock.hide()
        self.assertTrue(json.loads(self.http("/health"))["ok"])
        window.stop_server()
        self.wait_for(lambda: window.state == "off")
        window.start_server()
        self.wait_for(lambda: window.state == "running")
        self.assertEqual(json.loads(self.http("/health"))["tatami_states"], 0)
        logs = "\n".join(p.read_text(encoding="utf-8") for p in window.log_dir.glob("*.jsonl"))
        self.assertIn("WebSocket", logs)
        self.assertIn("Сервер готов", logs)
        self.assertIn("uvicorn.access", logs)
        window._poll()
        self.assertIn("POST /api/state", window.requests_terminal.toPlainText())
        self.assertNotIn("POST /api/state", window.terminal.toPlainText())
        self.assertNotIn("Тест А", logs)

    def test_occupied_port_reports_error_without_stopping_existing_listener(self):
        window = self.make_window()
        with socket.socket() as occupied:
            occupied.bind(("127.0.0.1", window.port.value()))
            occupied.listen()
            window.start_server()
            self.wait_for(lambda: window.state == "error")
            self.assertTrue(window.start_button.isEnabled())
            self.assertGreaterEqual(occupied.fileno(), 0)
        window._poll()
        self.assertIn("ERROR", window.terminal.toPlainText())

    def test_missing_executable_is_recoverable(self):
        window = self.make_window()
        window.worker_command = (str(ROOT / "no-such-program.exe"), [])
        window.start_server()
        self.wait_for(lambda: window.state == "error")
        self.assertTrue(window.start_button.isEnabled())

    def test_unexpected_exit_is_reported_and_server_can_restart(self):
        window = self.make_window()
        window.start_server()
        self.wait_for(lambda: window.state == "running")
        window.process.kill()
        self.wait_for(lambda: window.state == "error")
        window.start_server()
        self.wait_for(lambda: window.state == "running")

    def test_unresponsive_process_is_killed_after_stop_deadline(self):
        window = self.make_window()
        window.worker_command = (sys.executable, ["-c", "import time; time.sleep(60)"])
        window.start_server()
        self.wait_for(lambda: window.process.state() == QtCore.QProcess.Running)
        window.stop_server()
        # Ускоряем только таймер теста, не заменяя реальное завершение процесса.
        window.stop_timer.start(100)
        self.wait_for(lambda: window.process.state() == QtCore.QProcess.NotRunning)
        self.assertEqual(window.state, "error")

    def test_close_can_be_cancelled_and_waits_for_server(self):
        window = self.make_window()
        window.show()
        window.start_server()
        self.wait_for(lambda: window.state == "running")
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.No):
            self.assertFalse(window.close())
        self.assertEqual(window.state, "running")
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.Yes):
            self.assertFalse(window.close())
        self.wait_for(lambda: window.process.state() == QtCore.QProcess.NotRunning)
        self.assertFalse(window.isVisible())

    def test_clear_keeps_file_and_scrolling_keeps_selection(self):
        window = self.make_window()
        window.show()
        for index in range(120):
            window._note("INFO", "Строка " + str(index))
        window._poll()
        cursor = window.terminal.textCursor()
        cursor.setPosition(0)
        cursor.setPosition(12, cursor.KeepAnchor)
        window.terminal.setTextCursor(cursor)
        window.terminal.verticalScrollBar().setValue(0)
        selected = window.terminal.textCursor().selectedText()
        window._note("ERROR", "Ошибка проверки")
        window._poll()
        self.assertEqual(window.terminal.textCursor().selectedText(), selected)
        self.assertEqual(window.terminal.verticalScrollBar().value(), 0)
        window.clear_screen()
        self.assertEqual(window.terminal.toPlainText(), "")
        self.assertIn("Ошибка проверки", next(window.log_dir.glob("controller-*.jsonl")).read_text(encoding="utf-8"))

    def test_hidden_and_floating_journal_can_be_restored_without_losing_text(self):
        window = self.make_window()
        window.show()
        window._note("INFO", "Сохранённая строка журнала")
        window._poll()
        text = window.terminal.toPlainText()
        window.dock.close()
        self.assertFalse(window.dock.isVisible())
        window.show_log_action.trigger()
        self.assertTrue(window.dock.isVisible())
        self.assertFalse(window.dock.isFloating())
        window.dock.setFloating(True)
        self.assertTrue(window.dock.isFloating())
        self.assertTrue(window.attach_log_action.isEnabled())
        self.assertTrue(window.attach_log_button.isEnabled())
        self.assertTrue(window.attach_log_button.isVisible())
        self.assertIsNone(window.dock.titleBarWidget())
        self.assertFalse(window.dock.windowFlags() & QtCore.Qt.FramelessWindowHint)
        window.attach_log_button.click()
        self.assertFalse(window.dock.isFloating())
        self.assertTrue(window.dock.isVisible())
        self.assertEqual(window.terminal.toPlainText(), text)
        # Закрытие всей отделённой панели тоже исправляется основной кнопкой.
        window.dock.setFloating(True)
        window.dock.close()
        window.show_log_action.trigger()
        self.assertTrue(window.dock.isVisible())
        self.assertFalse(window.dock.isFloating())

    def test_two_logs_are_independent_and_splitter_cannot_collapse_them(self):
        window = self.make_window()
        window.show()
        window._append(dict(level="INFO", source="uvicorn.error", message="connection open"))
        window._append(dict(level="INFO", source="uvicorn.access", message='127.0.0.1 - "POST /api/state HTTP/1.1" 200', status=200))
        self.assertIn("Сервер: connection open", window.terminal.toPlainText())
        self.assertNotIn("uvicorn.error", window.terminal.toPlainText())
        self.assertIn("POST /api/state", window.requests_terminal.toPlainText())
        self.assertNotIn("connection open", window.requests_terminal.toPlainText())
        for sizes in ([0, 10000], [10000, 0]):
            window.log_splitter.setSizes(sizes)
            self.app.processEvents()
            self.assertTrue(all(size >= 240 for size in window.log_splitter.sizes()))
        window.clear_screen()
        self.assertEqual(window.terminal.toPlainText(), "")
        self.assertIn("POST /api/state", window.requests_terminal.toPlainText())
        window.clear_screen(True)
        self.assertEqual(window.requests_terminal.toPlainText(), "")

    def test_http_burst_does_not_hide_server_error(self):
        window = self.make_window()
        records = [dict(level="ERROR", source="uvicorn.error", message="Ошибка соединения")]
        records.extend(dict(level="INFO", source="uvicorn.access", message="POST /api/state 200", status=200)
                       for _ in range(2500))
        class TailStub:
            def read(self):
                return records
        window.tail = TailStub()
        window._poll()
        self.assertIn("Ошибка соединения", window.terminal.toPlainText())
        self.assertIn("POST /api/state", window.requests_terminal.toPlainText())

    def test_small_labels_use_application_font_and_stop_message_is_red(self):
        window = self.make_window()
        window.show()
        window.dock.hide()
        self.app.processEvents()
        self.assertLess(window.centralWidget().sizeHint().height(), 300)
        for label in window.findChildren(QtWidgets.QLabel):
            self.assertIn(label.font().family(), ("Gotham-Light", "Gotham-Medium"), label.text())
            self.assertGreaterEqual(label.font().pixelSize(), 13, label.text())
        window._set_state("off")
        window._note("INFO", "Сервер остановлен")
        window._poll()
        cursor = window.terminal.document().find("Сервер остановлен")
        self.assertFalse(cursor.isNull())
        self.assertEqual(cursor.charFormat().foreground().color().name(), "#ff7f87")
        self.assertIn("#b91c1c", window.status.styleSheet())

    def test_return_to_table_waits_for_shutdown_and_can_be_cancelled(self):
        window = self.make_window()
        window.start_server()
        self.wait_for(lambda: window.state == "running")
        returned = []
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.No):
            window.request_table_mode(lambda: returned.append(True))
        self.assertEqual(window.state, "running")
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.Yes):
            window.request_table_mode(lambda: returned.append(True))
        self.assertEqual(returned, [])
        self.wait_for(lambda: bool(returned))
        self.assertEqual(window.process.state(), QtCore.QProcess.NotRunning)

    def test_single_action_starts_and_stops_with_confirmation(self):
        window = self.make_window()
        window.start_button.click()
        self.wait_for(lambda: window.state == "running")
        self.assertEqual(window.start_button.text(), "Остановить сервер")
        self.assertFalse(window.port.isEnabled())
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.No):
            window.start_button.click()
        self.assertEqual(window.state, "running")
        with patch.object(QtWidgets.QMessageBox, "question", return_value=QtWidgets.QMessageBox.Yes):
            window.start_button.click()
        self.assertFalse(window.start_button.isEnabled())
        self.wait_for(lambda: window.state == "off")
        self.assertEqual(window.start_button.text(), "Запустить сервер")
        self.assertTrue(window.port.isEnabled())

    def test_copy_all_from_context_menu_keeps_panels_separate(self):
        window = self.make_window()
        window._append(dict(level="INFO", source="root", message="Событие сервера"))
        window._append(dict(level="INFO", source="uvicorn.access", message="POST /api/state"))
        for terminal in (window.terminal, window.requests_terminal):
            action = next(a for a in terminal.actions() if a.text() == "Копировать всё")
            action.trigger()
            self.assertEqual(self.app.clipboard().text(), terminal.toPlainText())
        self.assertFalse(window.start_button.icon().isNull())
        window._set_state("running")
        self.assertFalse(window.start_button.icon().isNull())

    def test_friendly_sources_only_change_display(self):
        window = self.make_window()
        for source, title in (("USKO", "Программа"), ("root", "Сервер"),
                              ("uvicorn.error", "Сервер"), ("usko.connections", "Подключения")):
            window.terminal.clear()
            window._append(dict(level="INFO", source=source, message="Проверка источника"))
            self.assertIn(title + ": Проверка источника", window.terminal.toPlainText())
        window.tatami.setValue(111)
        self.assertEqual(window.overlay_url.text(), window.base_url() + "/overlay/111")


class LogTailTests(unittest.TestCase):
    def test_parent_monitor_detects_exit(self):
        parent = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"],
                                  creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        watch = ParentWatch(parent.pid)
        try:
            self.assertTrue(watch.alive())
            parent.terminate()
            parent.wait(timeout=5)
            self.assertFalse(watch.alive())
        finally:
            watch.close()
            if parent.poll() is None:
                parent.kill()
                parent.wait(timeout=5)

    def test_split_utf8_and_rotation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.jsonl"
            tail = LogTail(path)
            self.assertEqual(tail.read(), [])
            record = dict(level="INFO", message="Русский текст")
            data = (json.dumps(record, ensure_ascii=False) + "\n").encode("utf-8")
            path.write_bytes(data[:40])
            self.assertEqual(tail.read(), [])
            with path.open("ab") as output:
                output.write(data[40:])
            self.assertEqual(tail.read(), [record])
            path.rename(path.with_suffix(".old"))
            path.write_bytes(data)
            self.assertEqual(tail.read(), [record])


if __name__ == "__main__":
    unittest.main()
