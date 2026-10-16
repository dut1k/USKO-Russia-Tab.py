"""Изолированный запуск сервера: этот модуль до run_worker использует только stdlib."""
import argparse
import asyncio
import importlib.util
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import sys
from datetime import datetime


class JsonLogFormatter(logging.Formatter):
    def format(self, record):
        message = record.getMessage()
        if record.exc_info:
            message += "\n" + self.formatException(record.exc_info)
        data = {"time": datetime.fromtimestamp(record.created).isoformat(timespec="seconds"),
                "level": record.levelname, "source": record.name, "message": message}
        # Access-log содержит адрес, метод, путь и статус, но не тело запроса
        # с ФИО. Статус сохраняем отдельно для окраски ответов в интерфейсе.
        if record.name == "uvicorn.access" and isinstance(record.args, tuple) and len(record.args) == 5:
            client, method, path, version, status = record.args
            data.update(client=client, method=method, path=path, http_version=version, status=int(status))
        return json.dumps(data, ensure_ascii=False)


def configure_log(path):
    handler = RotatingFileHandler(path, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8")
    handler.setFormatter(JsonLogFormatter())
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    # DEBUG протокола WebSocket может записать содержимое кадров с ФИО.
    # HTTP access-log включён постоянно; отладку содержимого кадров не включаем.
    root.setLevel(logging.INFO)
    logging.getLogger("usko.server").setLevel(logging.INFO)


def backend_path():
    # В сборку попадает исходник из соседнего репозитория вместе с его assets:
    # отдельная копия серверной логики в проекте табло не поддерживается.
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "overlay_server" / "server.py"
    return Path(__file__).resolve().parent.parent / "server_USKO-Russia-Tab" / "server.py"


def load_backend():
    spec = importlib.util.spec_from_file_location("usko_overlay_backend", backend_path())
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ParentWatch:
    """Не оставляем сервер занимать порт после аварийного завершения окна."""
    def __init__(self, pid):
        self.pid = pid
        self.handle = None
        if os.name == "nt":
            import ctypes
            from ctypes import wintypes
            self.api = ctypes.WinDLL("kernel32", use_last_error=True)
            self.api.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            self.api.OpenProcess.restype = wintypes.HANDLE
            self.api.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
            self.api.WaitForSingleObject.restype = wintypes.DWORD
            self.api.CloseHandle.argtypes = [wintypes.HANDLE]
            self.handle = self.api.OpenProcess(0x00100000, False, pid)
            if not self.handle:
                raise OSError("Не удалось открыть процесс окна сервера")

    def alive(self):
        if self.handle:
            return self.api.WaitForSingleObject(self.handle, 0) == 0x00000102
        try:
            os.kill(self.pid, 0)
            return True
        except ProcessLookupError:
            return False

    def close(self):
        if self.handle:
            self.api.CloseHandle(self.handle)
            self.handle = None

    def terminate(self):
        if not self.alive():
            return
        if os.name == "nt":
            import ctypes
            from ctypes import wintypes
            self.api.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
            self.api.TerminateProcess.restype = wintypes.BOOL
            handle = self.api.OpenProcess(0x0001, False, self.pid)
            if not handle:
                raise ctypes.WinError(ctypes.get_last_error())
            try:
                if not self.api.TerminateProcess(handle, 1):
                    raise ctypes.WinError(ctypes.get_last_error())
            finally:
                self.api.CloseHandle(handle)
        else:
            import signal
            os.kill(self.pid, signal.SIGKILL)


async def serve(args):
    import uvicorn
    backend = load_backend()
    # Явные реализации также позволяют PyInstaller собрать сервер без auto-import.
    config = uvicorn.Config(backend.app, host=args.host, port=args.port, loop="asyncio",
                            http="h11", ws="websockets", log_config=None,
                            access_log=True, timeout_graceful_shutdown=3)
    server = uvicorn.Server(config)
    watch = ParentWatch(args.parent_pid)
    # В свежем однофайловом exe PyInstaller создаёт промежуточный процесс.
    # Его аварийный выход тоже должен остановить настоящий сервер.
    launcher_watch = ParentWatch(os.getppid()) if os.getppid() != args.parent_pid else None

    async def monitor():
        announced = False
        while True:
            if (Path(args.stop_file).exists() or not watch.alive()
                    or (launcher_watch is not None and not launcher_watch.alive())):
                logging.info("Получена команда остановки или закрыто окно управления")
                server.should_exit = True
                return
            if server.started and not announced:
                # Готовность подтверждается только после успешного bind порта,
                # а не по запуску процесса или ответу чужого /health.
                Path(args.ready_file).write_text(str(os.getpid()), encoding="utf-8")
                logging.info("Сервер готов: %s:%s", args.host, args.port)
                announced = True
            await asyncio.sleep(0.2)

    task = asyncio.create_task(monitor())
    try:
        await server.serve()
    finally:
        task.cancel()
        await asyncio.gather(task, return_exceptions=True)
        watch.close()
        if launcher_watch:
            launcher_watch.close()
        Path(args.ready_file).unlink(missing_ok=True)


def run_worker(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--log-file", required=True)
    parser.add_argument("--stop-file", required=True)
    parser.add_argument("--ready-file", required=True)
    parser.add_argument("--parent-pid", type=int, required=True)
    parser.add_argument("--version", default="development")
    args = parser.parse_args(argv)
    configure_log(args.log_file)
    logging.info("USKO Tab %s; Python %s; PID %s; порт %s", args.version, sys.version.split()[0], os.getpid(), args.port)
    try:
        asyncio.run(serve(args))
    except BaseException:
        logging.exception("Сервер завершился с ошибкой")
        return 1
    logging.info("Сервер остановлен")
    return 0
