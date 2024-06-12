# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 892)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1151, 851))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.lblPicture_2 = QLabel(self.frame_2)
        self.lblPicture_2.setObjectName(u"lblPicture_2")
        self.lblPicture_2.setGeometry(QRect(30, 610, 271, 231))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 610, 271, 231))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.btnPicture_1 = QPushButton(self.frame_2)
        self.btnPicture_1.setObjectName(u"btnPicture_1")
        self.btnPicture_1.setGeometry(QRect(50, 150, 241, 51))
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 220, 271, 181))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.lblPicture_1 = QLabel(self.frame)
        self.lblPicture_1.setObjectName(u"lblPicture_1")
        self.lblPicture_1.setGeometry(QRect(0, -20, 271, 231))
        self.lblStatus_2 = QLabel(self.frame_2)
        self.lblStatus_2.setObjectName(u"lblStatus_2")
        self.lblStatus_2.setGeometry(QRect(130, 440, 91, 51))
        font = QFont()
        font.setPointSize(50)
        self.lblStatus_2.setFont(font)
        self.btnStart = QPushButton(self.frame_2)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(320, 450, 61, 71))
        self.lblStatus = QLabel(self.frame_2)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setGeometry(QRect(390, 460, 291, 51))
        font1 = QFont()
        font1.setPointSize(25)
        self.lblStatus.setFont(font1)
        self.btnPicture_2 = QPushButton(self.frame_2)
        self.btnPicture_2.setObjectName(u"btnPicture_2")
        self.btnPicture_2.setGeometry(QRect(50, 540, 241, 51))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 0, 471, 81))
        self.label.setFont(font)
        self.lblPicture_2.raise_()
        self.btnPicture_1.raise_()
        self.frame.raise_()
        self.lblStatus_2.raise_()
        self.btnStart.raise_()
        self.lblStatus.raise_()
        self.frame_3.raise_()
        self.btnPicture_2.raise_()
        self.label.raise_()
        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setGeometry(QRect(690, 300, 451, 381))
        self.frame3.setFrameShape(QFrame.Panel)
        self.frame3.setFrameShadow(QFrame.Sunken)
        self.lblPicture_3 = QLabel(self.frame3)
        self.lblPicture_3.setObjectName(u"lblPicture_3")
        self.lblPicture_3.setGeometry(QRect(0, 0, 451, 381))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblPicture_2.setText("")
        self.btnPicture_1.setText(QCoreApplication.translate("MainWindow", u"\u9078\u53d6\u98a8\u683c", None))
        self.lblPicture_1.setText("")
        self.lblStatus_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"\u6e96\u5099\u878d\u5408", None))
        self.btnPicture_2.setText(QCoreApplication.translate("MainWindow", u"\u5e36\u5165\u98a8\u683c\u7167\u7247", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5716\u7247\u878d\u5408\u751f\u7522\u5668", None))
        self.lblPicture_3.setText("")
    # retranslateUi

