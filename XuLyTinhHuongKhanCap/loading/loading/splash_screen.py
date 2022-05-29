# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(991, 640)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 20, 781, 561))
        self.circularProgressBarBase.setStyleSheet(u"QFrame{\n"
"	border-top-left-radius: 50px;\n"
"	border-bottom-right-radius: 50px;\n"
"}")
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(390, 80, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(390, 80, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(405, 95, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 266, 250))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelPercentage = QLabel(self.layoutWidget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font = QFont()
        font.setFamily(u"Roboto Thin")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 0, 0, 1, 1)

        self.labelCredits = QLabel(self.layoutWidget)
        self.labelCredits.setObjectName(u"labelCredits")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.labelCredits.setFont(font1)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.layoutWidget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        self.labelLoadingInfo.setFont(font1)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 1, 0, 1, 1)

        self.poster = QLabel(self.circularProgressBarBase)
        self.poster.setObjectName(u"poster")
        self.poster.setGeometry(QRect(0, 0, 301, 561))
        self.poster.setStyleSheet(u"QLabel{\n"
"	background-image: url(:/images/images/khoidong300.png);\n"
"	border-top-left-radius: 50px;\n"
"	border-bottom-right-radius: 0px;\n"
"\n"
"}")
        self.label = QLabel(self.circularProgressBarBase)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 0, 481, 561))
        self.label.setStyleSheet(u"QLabel{\n"
"	background-image: url(:/images/images/BLUE.png);\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-right-radius: 50px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.circularProgressBarBase)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 420, 481, 71))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	\n"
"	font: 25 8pt \"#9Slide03 Comfortaa Light\";\n"
"}")
        self.poster.raise_()
        self.label.raise_()
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        self.label_2.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"H\u1ec7 th\u1ed1ng \u0111ang k\u1ebft n\u1ed1i...", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.poster.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">C\u1ea3m \u01a1n b\u1ea1n \u0111\u00e3 ki\u00ean nh\u1eabn</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">H\u1ec7 th\u1ed1ng \u0111ang \u0111\u01b0\u1ee3c t\u1ef1 \u0111\u1ed9ng thi\u1ebft l\u1eadp</span></p></body></html>", None))
    # retranslateUi

