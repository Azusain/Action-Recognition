/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSource;
    QAction *actionScreenShot;
    QAction *actionOutputPath;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_2;
    QLabel *label;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout_5;
    QLabel *src_path_hint;
    QLabel *src_path;
    QHBoxLayout *horizontalLayout_2;
    QLabel *output_path_hint;
    QLabel *output_path;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer;
    QPushButton *btn_run;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *btn_teminate;
    QSpacerItem *horizontalSpacer_3;
    QVBoxLayout *verticalLayout_3;
    QListWidget *detected_list;
    QVBoxLayout *args_conf;
    QLabel *model_chosen;
    QLabel *label_3;
    QLabel *other_args;
    QLabel *label_2;
    QProgressBar *progressBar;
    QMenuBar *menubar;
    QMenu *menu;
    QMenu *menuAbout;
    QMenu *menuTools;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->setEnabled(true);
        MainWindow->resize(960, 540);
        MainWindow->setMinimumSize(QSize(960, 540));
        MainWindow->setMaximumSize(QSize(1920, 1097));
        MainWindow->setStyleSheet(QString::fromUtf8("QListWidget::item{\n"
"	alternate-background-color: rgb(144, 144, 144);\n"
"}\n"
""));
        actionSource = new QAction(MainWindow);
        actionSource->setObjectName(QString::fromUtf8("actionSource"));
        actionScreenShot = new QAction(MainWindow);
        actionScreenShot->setObjectName(QString::fromUtf8("actionScreenShot"));
        actionOutputPath = new QAction(MainWindow);
        actionOutputPath->setObjectName(QString::fromUtf8("actionOutputPath"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        centralwidget->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        centralwidget->setMinimumSize(QSize(0, 0));
        centralwidget->setMaximumSize(QSize(1920, 1080));
        centralwidget->setStyleSheet(QString::fromUtf8("background-color: rgb(38, 38, 38);\n"
"\n"
""));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setSpacing(0);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(8);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));

        verticalLayout_2->addWidget(label);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        src_path_hint = new QLabel(centralwidget);
        src_path_hint->setObjectName(QString::fromUtf8("src_path_hint"));
        src_path_hint->setStyleSheet(QString::fromUtf8("font: 20pt \"Cascadia Code SemiBold\";\n"
"color: rgb(255, 255, 255);"));

        horizontalLayout_5->addWidget(src_path_hint);

        src_path = new QLabel(centralwidget);
        src_path->setObjectName(QString::fromUtf8("src_path"));
        src_path->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
""));

        horizontalLayout_5->addWidget(src_path);


        verticalLayout_4->addLayout(horizontalLayout_5);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        output_path_hint = new QLabel(centralwidget);
        output_path_hint->setObjectName(QString::fromUtf8("output_path_hint"));
        output_path_hint->setStyleSheet(QString::fromUtf8("font: 20pt \"Cascadia Code SemiBold\";\n"
"color: rgb(255, 255, 255);"));

        horizontalLayout_2->addWidget(output_path_hint);

        output_path = new QLabel(centralwidget);
        output_path->setObjectName(QString::fromUtf8("output_path"));
        output_path->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);"));

        horizontalLayout_2->addWidget(output_path);


        verticalLayout_4->addLayout(horizontalLayout_2);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer);

        btn_run = new QPushButton(centralwidget);
        btn_run->setObjectName(QString::fromUtf8("btn_run"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(btn_run->sizePolicy().hasHeightForWidth());
        btn_run->setSizePolicy(sizePolicy1);
        btn_run->setStyleSheet(QString::fromUtf8("font: 12pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);\n"
""));

        horizontalLayout_4->addWidget(btn_run);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_2);

        btn_teminate = new QPushButton(centralwidget);
        btn_teminate->setObjectName(QString::fromUtf8("btn_teminate"));
        btn_teminate->setStyleSheet(QString::fromUtf8("font: 12pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(72, 72, 72);"));
        btn_teminate->setIconSize(QSize(12, 12));

        horizontalLayout_4->addWidget(btn_teminate);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_3);


        verticalLayout_4->addLayout(horizontalLayout_4);

        verticalLayout_4->setStretch(0, 1);
        verticalLayout_4->setStretch(1, 1);
        verticalLayout_4->setStretch(2, 1);

        verticalLayout_2->addLayout(verticalLayout_4);

        verticalLayout_2->setStretch(0, 3);
        verticalLayout_2->setStretch(1, 2);

        horizontalLayout->addLayout(verticalLayout_2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        detected_list = new QListWidget(centralwidget);
        new QListWidgetItem(detected_list);
        new QListWidgetItem(detected_list);
        new QListWidgetItem(detected_list);
        new QListWidgetItem(detected_list);
        new QListWidgetItem(detected_list);
        new QListWidgetItem(detected_list);
        detected_list->setObjectName(QString::fromUtf8("detected_list"));
        detected_list->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);\n"
"border:1px solid gray;\n"
"background-color: rgb(50, 50, 50);\n"
""));
        detected_list->setAlternatingRowColors(true);
        detected_list->setLayoutMode(QListView::SinglePass);
        detected_list->setSpacing(4);
        detected_list->setSortingEnabled(false);

        verticalLayout_3->addWidget(detected_list);

        args_conf = new QVBoxLayout();
        args_conf->setObjectName(QString::fromUtf8("args_conf"));
        model_chosen = new QLabel(centralwidget);
        model_chosen->setObjectName(QString::fromUtf8("model_chosen"));
        model_chosen->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);"));

        args_conf->addWidget(model_chosen);

        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);"));

        args_conf->addWidget(label_3);

        other_args = new QLabel(centralwidget);
        other_args->setObjectName(QString::fromUtf8("other_args"));
        other_args->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);"));

        args_conf->addWidget(other_args);

        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setStyleSheet(QString::fromUtf8("font: 15pt \"Cascadia Code\";\n"
"color: rgb(255, 255, 255);"));

        args_conf->addWidget(label_2);


        verticalLayout_3->addLayout(args_conf);

        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setMouseTracking(true);
        progressBar->setLayoutDirection(Qt::LeftToRight);
        progressBar->setAutoFillBackground(false);
        progressBar->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);\n"
"font: 15pt \"Cascadia Code\";\n"
""));
        progressBar->setValue(24);

        verticalLayout_3->addWidget(progressBar);

        verticalLayout_3->setStretch(0, 2);
        verticalLayout_3->setStretch(1, 2);
        verticalLayout_3->setStretch(2, 1);

        horizontalLayout->addLayout(verticalLayout_3);

        horizontalLayout->setStretch(0, 3);
        horizontalLayout->setStretch(1, 2);

        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 960, 17));
        menu = new QMenu(menubar);
        menu->setObjectName(QString::fromUtf8("menu"));
        menuAbout = new QMenu(menubar);
        menuAbout->setObjectName(QString::fromUtf8("menuAbout"));
        menuTools = new QMenu(menubar);
        menuTools->setObjectName(QString::fromUtf8("menuTools"));
        MainWindow->setMenuBar(menubar);

        menubar->addAction(menuTools->menuAction());
        menubar->addAction(menu->menuAction());
        menubar->addAction(menuAbout->menuAction());
        menu->addAction(actionSource);
        menu->addAction(actionOutputPath);
        menuTools->addAction(actionScreenShot);

        retranslateUi(MainWindow);
        QObject::connect(actionOutputPath, SIGNAL(triggered()), MainWindow, SLOT(close()));

        detected_list->setCurrentRow(-1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionSource->setText(QCoreApplication::translate("MainWindow", "Source", nullptr));
        actionScreenShot->setText(QCoreApplication::translate("MainWindow", "ScreenShot", nullptr));
        actionOutputPath->setText(QCoreApplication::translate("MainWindow", "Output Path", nullptr));
        label->setText(QString());
        src_path_hint->setText(QCoreApplication::translate("MainWindow", "      Source\357\274\232", nullptr));
        src_path->setText(QCoreApplication::translate("MainWindow", "Empty", nullptr));
        output_path_hint->setText(QCoreApplication::translate("MainWindow", "      Output to\357\274\232", nullptr));
        output_path->setText(QCoreApplication::translate("MainWindow", "Empty", nullptr));
        btn_run->setText(QCoreApplication::translate("MainWindow", "Run", nullptr));
        btn_teminate->setText(QCoreApplication::translate("MainWindow", "Terminate", nullptr));

        const bool __sortingEnabled = detected_list->isSortingEnabled();
        detected_list->setSortingEnabled(false);
        QListWidgetItem *___qlistwidgetitem = detected_list->item(0);
        ___qlistwidgetitem->setText(QCoreApplication::translate("MainWindow", "Man 01   (200,400) to (500, 800)", nullptr));
        QListWidgetItem *___qlistwidgetitem1 = detected_list->item(1);
        ___qlistwidgetitem1->setText(QCoreApplication::translate("MainWindow", "Man 02   (200,400) to (500, 800)", nullptr));
        QListWidgetItem *___qlistwidgetitem2 = detected_list->item(2);
        ___qlistwidgetitem2->setText(QCoreApplication::translate("MainWindow", "Women   (200,400) to (500, 800)", nullptr));
        QListWidgetItem *___qlistwidgetitem3 = detected_list->item(3);
        ___qlistwidgetitem3->setText(QCoreApplication::translate("MainWindow", "Women   (200,400) to (500, 800)", nullptr));
        QListWidgetItem *___qlistwidgetitem4 = detected_list->item(4);
        ___qlistwidgetitem4->setText(QCoreApplication::translate("MainWindow", "Cat      (200,400) to (500, 800)", nullptr));
        QListWidgetItem *___qlistwidgetitem5 = detected_list->item(5);
        ___qlistwidgetitem5->setText(QCoreApplication::translate("MainWindow", "Dog     (200,400) to (500, 800)", nullptr));
        detected_list->setSortingEnabled(__sortingEnabled);

        model_chosen->setText(QCoreApplication::translate("MainWindow", "Model: yolov5s.pt", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "args_0", nullptr));
        other_args->setText(QCoreApplication::translate("MainWindow", "args_1", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "args_2", nullptr));
        menu->setTitle(QCoreApplication::translate("MainWindow", "Settings", nullptr));
        menuAbout->setTitle(QCoreApplication::translate("MainWindow", "About", nullptr));
        menuTools->setTitle(QCoreApplication::translate("MainWindow", "Tools", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
