# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 686)
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.previous_label = QLabel(self.groupBox_3)
        self.previous_label.setObjectName(u"previous_label")
        self.previous_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.previous_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.current_label = QLabel(self.groupBox_3)
        self.current_label.setObjectName(u"current_label")
        self.current_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.current_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.next_label = QLabel(self.groupBox_3)
        self.next_label.setObjectName(u"next_label")
        self.next_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.next_label)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.err_msg = QLabel(self.groupBox_3)
        self.err_msg.setObjectName(u"err_msg")
        self.err_msg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.err_msg)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_4.addWidget(self.listView)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pause_btn = QPushButton(self.centralwidget)
        self.pause_btn.setObjectName(u"pause_btn")

        self.horizontalLayout_4.addWidget(self.pause_btn)

        self.prev_btn = QPushButton(self.centralwidget)
        self.prev_btn.setObjectName(u"prev_btn")

        self.horizontalLayout_4.addWidget(self.prev_btn)

        self.next_btn = QPushButton(self.centralwidget)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout_4.addWidget(self.next_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 27))
        self.menufiles = QMenu(self.menubar)
        self.menufiles.setObjectName(u"menufiles")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menufiles.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menufiles.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimplePaste", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Load Structure Data", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Pasted Data", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Previous Item", None))
        self.previous_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Item", None))
        self.current_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Next Item", None))
        self.next_label.setText("")
        self.err_msg.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Items last", None))
        self.pause_btn.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.prev_btn.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.menufiles.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

