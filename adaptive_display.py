"""Пропорциональное отображение зрительского макета без изменения его логики."""

from PyQt5 import QtCore, QtGui, QtWidgets


class AdaptiveDisplay(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        # Все существующие координаты и подбор шрифтов остаются в системе
        # 1920×1080. Масштаб применяется один раз при отрисовке всей сцены,
        # поэтому смена победителя и сброс не возвращают элементы к старому размеру.
        self.canvas = QtWidgets.QWidget()
        self.canvas.setFixedSize(1920, 1080)
        self._display_screen = None
        self._screen_signal_connected = False
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setBackgroundBrush(QtGui.QColor("white"))
        self.setRenderHints(QtGui.QPainter.TextAntialiasing |
                            QtGui.QPainter.SmoothPixmapTransform)
        self.resize(1920, 1080)

    def mount_canvas(self):
        self.setWindowTitle(self.canvas.windowTitle())
        self.setWindowIcon(self.canvas.windowIcon())
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0, 0, 1920, 1080)
        proxy = scene.addWidget(self.canvas)
        # Не увеличиваем закешированный растр макета: текст и примитивы Qt
        # должны отрисовываться заново под текущий размер и плотность экрана.
        proxy.setCacheMode(QtWidgets.QGraphicsItem.NoCache)
        self.setScene(scene)
        self._fit_canvas()

    def _fit_canvas(self):
        if self.scene() is None:
            return
        size = self.viewport().size()
        scale = min(size.width() / 1920, size.height() / 1080)
        if scale > 0:
            # При дробном уменьшении линии толщиной 1 px могут исчезнуть без
            # сглаживания. В масштабе 1:1 сохраняем исходную отрисовку рамок.
            self.setRenderHint(QtGui.QPainter.Antialiasing, scale != 1)
            # setTransform заменяет масштаб, а не накапливает его после resize.
            self.setTransform(QtGui.QTransform.fromScale(scale, scale))
            self.centerOn(960, 540)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._fit_canvas()

    def showEvent(self, event):
        super().showEvent(event)
        handle = self.windowHandle()
        if handle is not None:
            if not self._screen_signal_connected:
                handle.screenChanged.connect(self._use_screen)
                self._screen_signal_connected = True
            # Позицию уже задал прежний calc_display_moveCoord. Здесь выбираем
            # только размер экрана в координатах Qt, не перемещая само окно.
            screen = QtGui.QGuiApplication.screenAt(self.pos()) or handle.screen()
            self._use_screen(screen)

    def _use_screen(self, screen):
        if screen is None:
            return
        if self._display_screen is not screen:
            if self._display_screen is not None:
                try:
                    self._display_screen.geometryChanged.disconnect(self._resize_to_screen)
                except (TypeError, RuntimeError):
                    # При отключении монитора объект QScreen уже может быть удалён.
                    pass
            self._display_screen = screen
            screen.geometryChanged.connect(self._resize_to_screen)
        self._resize_to_screen()

    def _resize_to_screen(self, _geometry=None):
        # QScreen уже учитывает масштаб Windows. Дополнительное умножение на
        # devicePixelRatio привело бы к выходу окна за границы телевизора.
        if self._display_screen is not None:
            self.resize(self._display_screen.geometry().size())
