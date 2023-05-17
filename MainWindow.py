# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'ActionRecognization.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import PySide6

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSlider, QStatusBar, QWidget)

from InjectedCode import CanvasWidget


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(800, 600)
        self.actionSource = QAction(MainWindow)
        self.actionSource.setObjectName(u"actionSource")
        self.actionScreenShot = QAction(MainWindow)
        self.actionScreenShot.setObjectName(u"actionScreenShot")
        self.actionDestinationPath = QAction(MainWindow)
        self.actionDestinationPath.setObjectName(u"actionDestinationPath")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = CanvasWidget()    # display area !!!!!!
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 521, 361))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(150, 404, 160, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 400, 81, 21))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(540, 0, 256, 351))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 376, 54, 12))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 376, 54, 12))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 372, 81, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 376, 54, 12))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menu.addAction(self.actionSource)
        self.menu.addAction(self.actionDestinationPath)
        self.menuTools.addAction(self.actionScreenShot)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSource.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.actionScreenShot.setText(QCoreApplication.translate("MainWindow", u"ScreenShot", None))
        self.actionDestinationPath.setText(QCoreApplication.translate("MainWindow", u"DestinationPath", None))
        # self.label.setText(QCoreApplication.translate("MainWindow", u"I Am Ouput Screen!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FrameRatio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saved to:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))


# Test scripts
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    app.exec()
