# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QFileDialog)

# tmp global vars
source_path = None
output_path = None

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1920, 1097))
        MainWindow.setStyleSheet(u"QListWidget::item{\n"
"	alternate-background-color: rgb(144, 144, 144);\n"
"}\n"
"")
        self.actionSource = QMenu(MainWindow)
        self.actionSource.setObjectName(u"actionSource")
        self.actionScreenShot = QAction(MainWindow)
        self.actionScreenShot.setObjectName(u"actionScreenShot")
        self.actionWebCam = QAction(MainWindow)
        self.actionLocalFile = QAction(MainWindow)
        self.actionOutputPath = QAction(MainWindow)
        self.actionOutputPath.setObjectName(u"actionOutputPath")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.src_path_hint = QLabel(self.centralwidget)
        self.src_path_hint.setObjectName(u"src_path_hint")
        self.src_path_hint.setStyleSheet(u"font: 20pt \"Cascadia Code SemiBold\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.src_path_hint)

        self.src_path = QLabel(self.centralwidget)
        self.src_path.setObjectName(u"src_path")
        self.src_path.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_5.addWidget(self.src_path)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output_path_hint = QLabel(self.centralwidget)
        self.output_path_hint.setObjectName(u"output_path_hint")
        self.output_path_hint.setStyleSheet(u"font: 20pt \"Cascadia Code SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_2.addWidget(self.output_path_hint)
        self.output_path = QLabel(self.centralwidget)
        self.output_path.setObjectName(u"output_path")
        self.output_path.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.output_path)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(self.horizontalSpacer)
        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy1)
        self.btn_run.setStyleSheet(u"font: 12pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_run)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_teminate = QPushButton(self.centralwidget)
        self.btn_teminate.setObjectName(u"btn_teminate")
        self.btn_teminate.setStyleSheet(u"font: 12pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);")
        self.btn_teminate.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.btn_teminate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.detected_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.detected_list)
        QListWidgetItem(self.detected_list)
        QListWidgetItem(self.detected_list)
        QListWidgetItem(self.detected_list)
        QListWidgetItem(self.detected_list)
        QListWidgetItem(self.detected_list)
        self.detected_list.setObjectName(u"detected_list")
        self.detected_list.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"border:1px solid gray;\n"
"background-color: rgb(50, 50, 50);\n"
"")
        self.detected_list.setAlternatingRowColors(True)
        self.detected_list.setLayoutMode(QListView.SinglePass)
        self.detected_list.setSpacing(4)
        self.detected_list.setSortingEnabled(False)

        self.verticalLayout_3.addWidget(self.detected_list)

        self.args_conf = QVBoxLayout()
        self.args_conf.setObjectName(u"args_conf")
        self.model_chosen = QLabel(self.centralwidget)
        self.model_chosen.setObjectName(u"model_chosen")
        self.model_chosen.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")

        self.args_conf.addWidget(self.model_chosen)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")

        self.args_conf.addWidget(self.label_3)

        self.other_args = QLabel(self.centralwidget)
        self.other_args.setObjectName(u"other_args")
        self.other_args.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")

        self.args_conf.addWidget(self.other_args)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);")

        self.args_conf.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.args_conf)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMouseTracking(True)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15pt \"Cascadia Code\";\n"
"")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 17))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menu.addMenu(self.actionSource)
        self.menu.addAction(self.actionOutputPath)
        self.menuTools.addAction(self.actionScreenShot)

        self.actionSource.addAction(self.actionWebCam)
        self.actionSource.addAction(self.actionLocalFile)



        self.retranslateUi(MainWindow)

        # Slots Connections
        self.actionOutputPath.triggered.connect(self.set_output_path)
        self.actionWebCam.triggered.connect(self.set_src_webcam)
        self.actionLocalFile.triggered.connect(self.set_src_local_file)



        self.detected_list.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionScreenShot.setText(QCoreApplication.translate("MainWindow", u"ScreenShot", None))
        self.actionOutputPath.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.actionWebCam.setText(QCoreApplication.translate("MainWindow", u"WebCam", None))
        self.actionLocalFile.setText(QCoreApplication.translate("MainWindow", u"LocalFile", None))

        self.label.setText("")
        self.src_path_hint.setText(QCoreApplication.translate("MainWindow", u"      Source\uff1a", None))
        self.src_path.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.output_path_hint.setText(QCoreApplication.translate("MainWindow", u"      Output to\uff1a", None))
        self.output_path.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_teminate.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))

        __sortingEnabled = self.detected_list.isSortingEnabled()
        self.detected_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.detected_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Man 01   (200,400) to (500, 800)", None));
        ___qlistwidgetitem1 = self.detected_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Man 02   (200,400) to (500, 800)", None));
        ___qlistwidgetitem2 = self.detected_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Women   (200,400) to (500, 800)", None));
        ___qlistwidgetitem3 = self.detected_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Women   (200,400) to (500, 800)", None));
        ___qlistwidgetitem4 = self.detected_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cat      (200,400) to (500, 800)", None));
        ___qlistwidgetitem5 = self.detected_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Dog     (200,400) to (500, 800)", None));
        self.detected_list.setSortingEnabled(__sortingEnabled)

        self.model_chosen.setText(QCoreApplication.translate("MainWindow", u"Model: yolov5s.pt", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"args_0", None))
        self.other_args.setText(QCoreApplication.translate("MainWindow", u"args_1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"args_2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.actionSource.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
    # customized slot functions
    def set_output_path(self):
        file_name, file_type = QFileDialog.getOpenFileName()
        self.output_path.setText(file_name[-10:])
        return

    def set_src_webcam(self):
        self.src_path.setText("192.168.31.217:4747")
        self.src_path_hint.setText(u"      WebCam\uff1a")
        return

    def set_src_local_file(self):
        file_name, file_type = QFileDialog.getOpenFileName()
        self.src_path.setText(file_name[-10:])
        self.src_path_hint.setText(u"      Local\uff1a")
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Ui_MainWindow()
    mw.show()
    app.exec()


