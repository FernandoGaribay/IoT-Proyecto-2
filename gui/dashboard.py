# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg_app = QFrame(self.styleSheet)
        self.bg_app.setObjectName(u"bg_app")
        self.bg_app.setFrameShape(QFrame.NoFrame)
        self.bg_app.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bg_app)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bg_app)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"#topLogoInfo {\n"
"	border: none;\n"
"	border-bottom: 3px solid rgb(135, 206, 235);\n"
"}")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.topLogoInfo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 161, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.topLogoInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 30, 52, 15))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_3.setFont(font1)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 3, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"#topLogo {\n"
"    background-image: url(:/resources/QuantumBankLogo.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"#leftMenuFrame .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#leftMenuFrame .QPushButton:hover {\n"
"	background-color: rgb(240, 248, 255);\n"
"}\n"
"#leftMenuFrame .QPushButton:pressed {	\n"
"	background-color: rgb(173, 216, 230);\n"
"}")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setStyleSheet(u"background-image: url(:/resources/menuIcon.png)")

        self.verticalLayout_11.addWidget(self.toggleButton)


        self.verticalLayout_8.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.topMenu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.topMenu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 45))
        self.pushButton_6.setStyleSheet(u"background-image: url(:/resources/homeIcon.png);")

        self.verticalLayout_10.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.topMenu)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 45))
        self.pushButton_7.setStyleSheet(u"background-image: url(:/resources/menuIcon.png);")

        self.verticalLayout_10.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.topMenu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 45))
        self.pushButton_8.setStyleSheet(u"background-image: url(:/resources/menuIcon.png);")

        self.verticalLayout_10.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.topMenu)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 45))
        self.pushButton_9.setStyleSheet(u"background-image: url(:/resources/menuIcon.png);")

        self.verticalLayout_10.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.topMenu)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 45))
        self.pushButton_10.setStyleSheet(u"background-image: url(:/resources/menuIcon.png);")

        self.verticalLayout_10.addWidget(self.pushButton_10)


        self.verticalLayout_8.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setStyleSheet(u"")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/resources/configIcon.png);\n"
"")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalLayout_8.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.leftMenuFrame)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bg_app)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setStyleSheet(u"#extraTopBg{	\n"
"	background-color: rgb(79, 145, 201);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(135, 206, 235);\n"
"}")
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(28, 38))
        self.extraLabel.setFont(font)
        self.extraLabel.setStyleSheet(u"#extraLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setStyleSheet(u"#extraCloseColumnBtn { \n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px; \n"
"}\n"
"#extraCloseColumnBtn:hover { \n"
"	background-color: rgb(196, 161, 249); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}\n"
"#extraCloseColumnBtn:pressed { \n"
"	background-color: rgb(180, 141, 238); \n"
"	border-style: solid; \n"
"	border-radius: 4px; \n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/closeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))
        self.extraCloseColumnBtn.setFlat(False)

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 3, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"#extraIcon {\n"
"	border-image: url(:/resources/configIcon.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setStyleSheet(u"#extraContent {\n"
"	background-color: rgb(173, 216, 230);\n"
"}")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraContent)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setStyleSheet(u"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(50, 50, 50);\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(79, 145, 201);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(66, 123, 170);\n"
"}")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.extraTopMenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
        self.pushButton.setStyleSheet(u"background-image: url(:/resources/layersIcon.png)")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.extraTopMenu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 45))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/resources/layersIcon.png)")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.extraTopMenu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 45))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/resources/layersIcon.png)")
        self.pushButton_3.setIconSize(QSize(8, 8))

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_5.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.textEdit)


        self.verticalLayout_5.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.horizontalLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bg_app)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"#contentTopBg {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 3px solid rgb(135, 206, 235);\n"
"}")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setPointSize(10)
        self.titleRightInfo.setFont(font2)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout_2.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"#rightButtons .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover { \n"
"	background-color: rgb(240, 248, 255);\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed { \n"
"	background-color: rgb(173, 216, 230);\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/configIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.settingsTopBtn)

        self.pushButton_11 = QPushButton(self.rightButtons)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(28, 28))
        self.pushButton_11.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/resources/minimizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.rightButtons)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(28, 28))
        self.pushButton_12.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/resources/maximizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.rightButtons)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(28, 28))
        self.pushButton_13.setMaximumSize(QSize(28, 28))
        self.pushButton_13.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton_13)


        self.horizontalLayout_2.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(240, 248, 255);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_7 = QHBoxLayout(self.home)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.logoHome = QLabel(self.home)
        self.logoHome.setObjectName(u"logoHome")
        self.logoHome.setStyleSheet(u"#logoHome {\n"
"	background-image: url(:/resources/logo.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"")
        self.logoHome.setScaledContents(True)
        self.logoHome.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.logoHome)

        self.stackedWidget.addWidget(self.home)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_16.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setStyleSheet(u"#extraRightBox .QFrame {\n"
"	background-color: rgb(173, 216, 230);\n"
"	border: none;\n"
"	border-top: 2px solid rgb(79, 145, 201)\n"
"}\n"
"")
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setStyleSheet(u"#topMenus .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(50, 50, 50);\n"
"}\n"
"#topMenus .QPushButton:hover {\n"
"	background-color: rgb(79, 145, 201);\n"
"}\n"
"#topMenus .QPushButton:pressed {	\n"
"	background-color: rgb(66, 123, 170);\n"
"}")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.topMenus)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.topMenus)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 45))

        self.verticalLayout_15.addWidget(self.pushButton_4)

        self.pushButton_14 = QPushButton(self.topMenus)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 45))

        self.verticalLayout_15.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.topMenus)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 45))

        self.verticalLayout_15.addWidget(self.pushButton_15)


        self.verticalLayout_14.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.contentSettings)


        self.horizontalLayout_6.addWidget(self.extraRightBox)


        self.verticalLayout_12.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color: rgb(173, 216, 230);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.bottomBar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16))
        self.label_5.setStyleSheet(u"color: rgb(50, 50, 50);")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label = QLabel(self.bottomBar)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16))
        self.label.setStyleSheet(u"color: rgb(50, 50, 50);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/resources/sizeGrip.png);")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_12.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bg_app)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraCloseColumnBtn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"QuantumBank \u2013 Automatizaci\u00f3n y control de correspondencia interna", None))
        self.settingsTopBtn.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.logoHome.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2024 SoftBank. All rights reserved.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1.0.0     ", None))
    # retranslateUi

