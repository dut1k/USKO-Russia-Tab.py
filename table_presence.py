"""Служебная связь судейского стола с сервером трансляции."""
import json
from uuid import uuid4

from PyQt5 import QtCore, QtNetwork


class TablePresence(QtCore.QObject):
    disconnected = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.network = QtNetwork.QNetworkAccessManager(self)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self._heartbeat)
        self.endpoint = None
        self.session_id = None
        self.heartbeat_reply = None
        self.disconnect_replies = set()

    def configure(self, host, port, tatami_id):
        endpoint = (host, port, str(tatami_id))
        if endpoint != self.endpoint:
            self.pause()
            self.endpoint = endpoint
        self.resume()

    def resume(self):
        if self.endpoint is not None and self.session_id is None:
            self.session_id = uuid4().hex
            self._heartbeat()
            self.timer.start()

    def _post(self, action):
        host, port, tatami_id = self.endpoint
        url = QtCore.QUrl()
        url.setScheme("http")
        url.setHost(host)
        url.setPort(port)
        url.setPath("/api/presence/" + action)
        request = QtNetwork.QNetworkRequest(url)
        request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
        request.setTransferTimeout(2000)
        body = json.dumps({"tatami_id": tatami_id, "session_id": self.session_id}).encode("utf-8")
        return self.network.post(request, body)

    def _heartbeat(self):
        # Qt ведёт сеть асинхронно. При недоступном сервере не накапливаем
        # запросы и повторяем попытку на следующем тике.
        if self.session_id is not None and self.heartbeat_reply is None:
            reply = self._post("heartbeat")
            self.heartbeat_reply = reply
            reply.finished.connect(lambda: self._finish_heartbeat(reply))

    def _finish_heartbeat(self, reply):
        if self.heartbeat_reply is reply:
            self.heartbeat_reply = None
        reply.deleteLater()

    def pause(self):
        self.timer.stop()
        if self.session_id is None:
            return
        if self.heartbeat_reply is not None:
            reply = self.heartbeat_reply
            self.heartbeat_reply = None
            reply.abort()
        reply = self._post("disconnect")
        self.disconnect_replies.add(reply)
        reply.finished.connect(lambda: self._finish_disconnect(reply))
        self.session_id = None

    def _finish_disconnect(self, reply):
        self.disconnect_replies.discard(reply)
        reply.deleteLater()
        if not self.disconnect_replies:
            self.disconnected.emit()

    def shutdown(self):
        self.pause()
        if not self.disconnect_replies:
            return
        # При завершении Qt перестаёт обслуживать сеть. Даём локальному
        # серверу короткое окно для ответа; при обрыве сработает тайм-аут.
        loop = QtCore.QEventLoop()
        timeout = QtCore.QTimer()
        timeout.setSingleShot(True)
        timeout.timeout.connect(loop.quit)
        self.disconnected.connect(loop.quit)
        timeout.start(350)
        loop.exec_()
        self.disconnected.disconnect(loop.quit)
