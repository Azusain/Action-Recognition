import sys
import threading
import time

from PySide6.QtWidgets import *
from PySide6.QtGui import QImage, QPixmap, QPainter
import cv2

canvas = None
app = None
is_activated = True
img_buf = None


def update_canvas(canvas_widget, interval_sec=0.015):
    global is_activated
    while is_activated:
        canvas_widget.update()
        time.sleep(interval_sec)


class CanvasWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.resize(960, 540)

    def paintEvent(self, event):
        global img_buf, canvas
        p = QPainter()
        p.begin(self)
        if img_buf is not None:
            pixmap = QPixmap.fromImage(img_format_converter(img_buf))
            p.drawPixmap(0, 0, pixmap)
        p.end()


def img_format_converter(cv_img) -> QImage:
    qt_img = QImage(cv_img.data, cv_img.shape[1], cv_img.shape[0], QImage.Format_RGB888)
    qt_img.rgbSwap()
    return qt_img


class InterfaceThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # init interface
        global canvas, app, is_activated
        app = QApplication(sys.argv)
        canvas = CanvasWidget()
        canvas.show()
        # sub-thread for updating canvas
        threading.Thread(target=update_canvas, args=(canvas,)).start()
        # main interface
        app.exec()
        is_activated = False


if __name__ == '__main__':

    it = InterfaceThread()
    it.start()

