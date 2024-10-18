# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 800))
        MainWindow.setMaximumSize(QSize(1280, 800))
        MainWindow.setStyleSheet(u"QFrame { border: none; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.controles = QFrame(self.centralwidget)
        self.controles.setObjectName(u"controles")
        self.controles.setGeometry(QRect(640, 0, 640, 800))
        sizePolicy.setHeightForWidth(self.controles.sizePolicy().hasHeightForWidth())
        self.controles.setSizePolicy(sizePolicy)
        self.controles.setStyleSheet(u"QFrame#controles {\n"
"    background-color: rgba(255, 255, 255, 1); /* Rojo semi-transparente */\n"
"}\n"
"")
        self.controles.setFrameShape(QFrame.StyledPanel)
        self.controles.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.controles)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 641, 51))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #4788D0;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.controles)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 110, 641, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.controles)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 170, 641, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, 0, 100, 0)
        self.lblLoginHeader = QLabel(self.frame)
        self.lblLoginHeader.setObjectName(u"lblLoginHeader")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setUnderline(True)
        self.lblLoginHeader.setFont(font2)
        self.lblLoginHeader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblLoginHeader.setStyleSheet(u"color: #4788D0;")
        self.lblLoginHeader.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lblLoginHeader)

        self.lblSignUpHeader = QLabel(self.frame)
        self.lblSignUpHeader.setObjectName(u"lblSignUpHeader")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.lblSignUpHeader.setFont(font3)
        self.lblSignUpHeader.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblSignUpHeader.setStyleSheet(u"color: rgb(103, 103, 103);")
        self.lblSignUpHeader.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lblSignUpHeader)

        self.frame_2 = QFrame(self.controles)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 250, 641, 521))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.txtUsername = QLineEdit(self.frame_2)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setGeometry(QRect(90, 105, 461, 40))
        self.txtUsername.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(12)
        self.txtUsername.setFont(font4)
        self.txtUsername.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 2px solid #ccc;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #4285F4;\n"
"}\n"
"")
        self.txtUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtPassword = QLineEdit(self.frame_2)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(90, 185, 461, 40))
        self.txtPassword.setMinimumSize(QSize(0, 40))
        self.txtPassword.setFont(font4)
        self.txtPassword.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 2px solid #ccc;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #4285F4;\n"
"}\n"
"")
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 240, 461, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(13)
        font5.setUnderline(True)
        self.label_4.setFont(font5)
        self.label_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblSignUp = QLabel(self.frame_2)
        self.lblSignUp.setObjectName(u"lblSignUp")
        self.lblSignUp.setGeometry(QRect(380, 450, 60, 43))
        font6 = QFont()
        font6.setPointSize(13)
        self.lblSignUp.setFont(font6)
        self.lblSignUp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblSignUp.setStyleSheet(u"color: #4788D0;")
        self.lblSignUp.setScaledContents(True)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 450, 173, 43))
        self.label_5.setFont(font6)
        self.btnLogIn = QPushButton(self.frame_2)
        self.btnLogIn.setObjectName(u"btnLogIn")
        self.btnLogIn.setGeometry(QRect(200, 410, 241, 41))
        self.btnLogIn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogIn.setStyleSheet(u"QPushButton {\n"
"    background-color: #3F8AE0;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 16px; \n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357AE8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2C6FDD;\n"
"}\n"
"")
        self.btnShowPassword = QPushButton(self.frame_2)
        self.btnShowPassword.setObjectName(u"btnShowPassword")
        self.btnShowPassword.setGeometry(QRect(520, 189, 31, 31))
        self.btnShowPassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnShowPassword.setLayoutDirection(Qt.LeftToRight)
        self.btnShowPassword.setAutoFillBackground(False)
        self.btnShowPassword.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(239, 239, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(209, 209, 209);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/invisiblePass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnShowPassword.setIcon(icon)
        self.btnShowPassword.setIconSize(QSize(20, 20))
        self.btnShowPassword.setFlat(True)
        self.label_7 = QLabel(self.controles)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 770, 121, 31))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 641, 801))
        self.label.setPixmap(QPixmap(u":/resources/loginBackground.png"))
        self.label.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 330, 641, 161))
        self.label_6.setStyleSheet(u"")
        self.label_6.setPixmap(QPixmap(u":/resources/whiteIcon.png"))
        self.label_6.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log in to your account to continue", None))
        self.lblLoginHeader.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lblSignUpHeader.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your username", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Forgot your password?", None))
        self.lblSignUp.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.btnLogIn.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.btnShowPassword.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0", None))
        self.label.setText("")
        self.label_6.setText("")
    # retranslateUi

