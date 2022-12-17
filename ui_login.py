# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(824, 623)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        Login.setFont(font)
        Login.setLayoutDirection(Qt.LeftToRight)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet(u"background-color: rgb(115, 143, 167);")
        self.verticalLayout_4 = QVBoxLayout(Login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setKerning(True)
        self.frame.setFont(font1)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(-1, 15, 0, 15)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy2)
        self.txt_user.setMinimumSize(QSize(0, 30))
        self.txt_user.setMaximumSize(QSize(600, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_user.setFont(font2)
        self.txt_user.setContextMenuPolicy(Qt.NoContextMenu)
        self.txt_user.setAcceptDrops(True)
        self.txt_user.setLayoutDirection(Qt.LeftToRight)
        self.txt_user.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_user)

        self.txt_pass = QLineEdit(self.frame)
        self.txt_pass.setObjectName(u"txt_pass")
        sizePolicy.setHeightForWidth(self.txt_pass.sizePolicy().hasHeightForWidth())
        self.txt_pass.setSizePolicy(sizePolicy)
        self.txt_pass.setMinimumSize(QSize(0, 30))
        self.txt_pass.setMaximumSize(QSize(600, 16777215))
        self.txt_pass.setFont(font2)
        self.txt_pass.setLayoutDirection(Qt.LeftToRight)
        self.txt_pass.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_pass.setEchoMode(QLineEdit.Password)
        self.txt_pass.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_pass)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(300, 40))
        self.btn_login.setMaximumSize(QSize(396, 16777209))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_login.setFont(font3)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 65, 96);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 20px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 206, 218);\n"
"	color: rgb(7, 19, 48);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_login)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><img src=\"file:///C:/Users/USER/Pictures/Frame 81.png\"/></p></body></html>", None))
        self.label_2.setText("")
        self.label_7.setText("")
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"USER", None))
        self.txt_pass.setText("")
        self.txt_pass.setPlaceholderText(QCoreApplication.translate("Login", u"PASSWORD", None))
        self.label_6.setText("")
        self.label_4.setText("")
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_3.setText("")
    # retranslateUi

