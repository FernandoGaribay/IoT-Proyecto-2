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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
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
        self.label_2.setGeometry(QRect(60, 8, 161, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.topLogoInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 25, 111, 16))
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
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"background-image: url(:/resources/homeIcon.png);")

        self.verticalLayout_10.addWidget(self.btn_home)

        self.btn_users = QPushButton(self.topMenu)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setMinimumSize(QSize(0, 45))
        self.btn_users.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_users.setStyleSheet(u"background-image: url(:/resources/usersIcon.png);")

        self.verticalLayout_10.addWidget(self.btn_users)

        self.btn_send = QPushButton(self.topMenu)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setMinimumSize(QSize(0, 45))
        self.btn_send.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_send.setStyleSheet(u"background-image: url(:/resources/newDocument.png);")

        self.verticalLayout_10.addWidget(self.btn_send)

        self.btn_template = QPushButton(self.topMenu)
        self.btn_template.setObjectName(u"btn_template")
        self.btn_template.setMinimumSize(QSize(0, 45))
        self.btn_template.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_template.setStyleSheet(u"background-image: url(:/resources/documentsIcon.png);")

        self.verticalLayout_10.addWidget(self.btn_template)

        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_history.setStyleSheet(u"background-image: url(:/resources/historyIcon.png);")

        self.verticalLayout_10.addWidget(self.btn_history)


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
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/configIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.settingsTopBtn)

        self.pushButton_11 = QPushButton(self.rightButtons)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(28, 28))
        self.pushButton_11.setMaximumSize(QSize(28, 28))
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resources/minimizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.rightButtons)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(28, 28))
        self.pushButton_12.setMaximumSize(QSize(28, 28))
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/resources/maximizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.rightButtons)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(28, 28))
        self.pushButton_13.setMaximumSize(QSize(28, 28))
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_7 = QHBoxLayout(self.homePage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.logoHome = QLabel(self.homePage)
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

        self.stackedWidget.addWidget(self.homePage)
        self.usersPage = QWidget()
        self.usersPage.setObjectName(u"usersPage")
        self.horizontalLayout_8 = QHBoxLayout(self.usersPage)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.usersPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(15, -1, -1, -1)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/resources/searchIcon.png"))
        self.label_4.setScaledContents(False)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.txt_searchUsers = QLineEdit(self.frame_4)
        self.txt_searchUsers.setObjectName(u"txt_searchUsers")
        self.txt_searchUsers.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px 10px;\n"
"	background-color: #FFFFFF;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #3c4043;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_11.addWidget(self.txt_searchUsers)


        self.horizontalLayout_9.addWidget(self.frame_4)

        self.pnl_topSearchBottonsUsers = QFrame(self.frame_3)
        self.pnl_topSearchBottonsUsers.setObjectName(u"pnl_topSearchBottonsUsers")
        self.pnl_topSearchBottonsUsers.setStyleSheet(u"#pnl_topSearchBottonsUsers .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}\n"
"#pnl_topSearchBottonsUsers .QPushButton:hover { \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#pnl_topSearchBottonsUsers .QPushButton:pressed { \n"
"	background-color: rgb(173, 216, 230);\n"
"}")
        self.pnl_topSearchBottonsUsers.setFrameShape(QFrame.NoFrame)
        self.pnl_topSearchBottonsUsers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.pnl_topSearchBottonsUsers)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_deleteUsers = QPushButton(self.pnl_topSearchBottonsUsers)
        self.btn_deleteUsers.setObjectName(u"btn_deleteUsers")
        self.btn_deleteUsers.setMinimumSize(QSize(40, 40))
        self.btn_deleteUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/resources/trashIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_deleteUsers.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.btn_deleteUsers)

        self.btn_addUsers = QPushButton(self.pnl_topSearchBottonsUsers)
        self.btn_addUsers.setObjectName(u"btn_addUsers")
        self.btn_addUsers.setMinimumSize(QSize(40, 40))
        self.btn_addUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/resources/addIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_addUsers.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.btn_addUsers)


        self.horizontalLayout_9.addWidget(self.pnl_topSearchBottonsUsers)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 17):
            self.tableWidget.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: #F0F0F0;\n"
"	border: 1px solid red;\n"
"	padding: 8px;\n"
"	margin: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"        background-color: #D0D0D0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(79, 145, 201);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(17)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_18.addWidget(self.tableWidget)


        self.verticalLayout_17.addWidget(self.frame)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.menuUsers = QFrame(self.usersPage)
        self.menuUsers.setObjectName(u"menuUsers")
        self.menuUsers.setMinimumSize(QSize(240, 0))
        self.menuUsers.setMaximumSize(QSize(240, 16777215))
        self.menuUsers.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.menuUsers.setFrameShape(QFrame.NoFrame)
        self.menuUsers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.menuUsers)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pnl_topButtonsUsers = QFrame(self.menuUsers)
        self.pnl_topButtonsUsers.setObjectName(u"pnl_topButtonsUsers")
        self.pnl_topButtonsUsers.setMinimumSize(QSize(0, 70))
        self.pnl_topButtonsUsers.setMaximumSize(QSize(16777215, 70))
        self.pnl_topButtonsUsers.setStyleSheet(u"#pnl_topButtonsUsers .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"#pnl_topButtonsUsers .QPushButton:hover { \n"
"	background-color: rgb(240, 248, 255);\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}\n"
"#pnl_topButtonsUsers .QPushButton:pressed { \n"
"	background-color: rgb(173, 216, 230);\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}")
        self.pnl_topButtonsUsers.setFrameShape(QFrame.NoFrame)
        self.pnl_topButtonsUsers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.pnl_topButtonsUsers)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_refreshUsers = QPushButton(self.pnl_topButtonsUsers)
        self.btn_refreshUsers.setObjectName(u"btn_refreshUsers")
        self.btn_refreshUsers.setMinimumSize(QSize(0, 40))
        self.btn_refreshUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refreshUsers.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/resources/refreshIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_refreshUsers.setIcon(icon6)
        self.btn_refreshUsers.setIconSize(QSize(16, 16))

        self.horizontalLayout_12.addWidget(self.btn_refreshUsers)

        self.btn_randomUsers = QPushButton(self.pnl_topButtonsUsers)
        self.btn_randomUsers.setObjectName(u"btn_randomUsers")
        self.btn_randomUsers.setMinimumSize(QSize(0, 40))
        self.btn_randomUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_randomUsers.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/resources/randomIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_randomUsers.setIcon(icon7)
        self.btn_randomUsers.setIconSize(QSize(16, 16))

        self.horizontalLayout_12.addWidget(self.btn_randomUsers)

        self.btn_editUsers = QPushButton(self.pnl_topButtonsUsers)
        self.btn_editUsers.setObjectName(u"btn_editUsers")
        self.btn_editUsers.setMinimumSize(QSize(0, 40))
        self.btn_editUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_editUsers.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/resources/pencilIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_editUsers.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.btn_editUsers)

        self.btn_clearUsers = QPushButton(self.pnl_topButtonsUsers)
        self.btn_clearUsers.setObjectName(u"btn_clearUsers")
        self.btn_clearUsers.setMinimumSize(QSize(0, 40))
        self.btn_clearUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clearUsers.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/resources/eraserIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clearUsers.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.btn_clearUsers)


        self.verticalLayout_19.addWidget(self.pnl_topButtonsUsers)

        self.camposUsers = QFrame(self.menuUsers)
        self.camposUsers.setObjectName(u"camposUsers")
        self.camposUsers.setStyleSheet(u"#camposUsers .QLineEdit {\n"
"	padding: 6px 10px;\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #3c4043;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#camposUsers .QLineEdit:focus{\n"
"	outline: none;\n"
"}\n"
"\n"
"#camposUsers .QLabel{\n"
"	color: rgb(66, 123, 170);\n"
"}\n"
"")
        self.camposUsers.setFrameShape(QFrame.NoFrame)
        self.camposUsers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.camposUsers)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.camposUsers)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"#scrollArea .QScrollBar:vertical {\n"
"    margin: 30px 0 30px 0;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollArea .QScrollBar::handle:vertical {\n"
"    background-color: rgb(79, 145, 201);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollArea .QScrollBar::add-line:vertical, #scrollArea .QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 230, 1198))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setSpacing(9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_10)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lbl_idUsers = QLabel(self.frame_10)
        self.lbl_idUsers.setObjectName(u"lbl_idUsers")
        self.lbl_idUsers.setFont(font2)
        self.lbl_idUsers.setScaledContents(True)
        self.lbl_idUsers.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.lbl_idUsers)

        self.txt_idUsers = QLineEdit(self.frame_10)
        self.txt_idUsers.setObjectName(u"txt_idUsers")
        self.txt_idUsers.setEnabled(False)
        self.txt_idUsers.setStyleSheet(u"background-color: rgb(217, 217, 217);")

        self.verticalLayout_23.addWidget(self.txt_idUsers)


        self.verticalLayout_21.addWidget(self.frame_10)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_20)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 9, 0, 0)
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(False)

        self.verticalLayout_33.addWidget(self.label_18)

        self.txt_nameUsers = QLineEdit(self.frame_20)
        self.txt_nameUsers.setObjectName(u"txt_nameUsers")

        self.verticalLayout_33.addWidget(self.txt_nameUsers)


        self.verticalLayout_21.addWidget(self.frame_20)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 9, 0, 0)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)

        self.verticalLayout_24.addWidget(self.label_9)

        self.txt_lastNameFatherUsers = QLineEdit(self.frame_11)
        self.txt_lastNameFatherUsers.setObjectName(u"txt_lastNameFatherUsers")

        self.verticalLayout_24.addWidget(self.txt_lastNameFatherUsers)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_13)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 9, 0, 0)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setScaledContents(True)
        self.label_11.setWordWrap(False)

        self.verticalLayout_26.addWidget(self.label_11)

        self.txt_lastNameMotherUsers = QLineEdit(self.frame_13)
        self.txt_lastNameMotherUsers.setObjectName(u"txt_lastNameMotherUsers")

        self.verticalLayout_26.addWidget(self.txt_lastNameMotherUsers)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 9, 0, 0)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setScaledContents(True)
        self.label_12.setWordWrap(False)

        self.verticalLayout_27.addWidget(self.label_12)

        self.txt_positionUsers = QLineEdit(self.frame_14)
        self.txt_positionUsers.setObjectName(u"txt_positionUsers")

        self.verticalLayout_27.addWidget(self.txt_positionUsers)


        self.verticalLayout_21.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_12)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 9, 0, 0)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_10)

        self.txt_companyUsers = QLineEdit(self.frame_12)
        self.txt_companyUsers.setObjectName(u"txt_companyUsers")

        self.verticalLayout_25.addWidget(self.txt_companyUsers)


        self.verticalLayout_21.addWidget(self.frame_12)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_15)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 9, 0, 0)
        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(False)

        self.verticalLayout_28.addWidget(self.label_13)

        self.txt_streetUsers = QLineEdit(self.frame_15)
        self.txt_streetUsers.setObjectName(u"txt_streetUsers")

        self.verticalLayout_28.addWidget(self.txt_streetUsers)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.frame_29 = QFrame(self.scrollAreaWidgetContents)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_29)
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 9, 0, 0)
        self.label_27 = QLabel(self.frame_29)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setScaledContents(True)
        self.label_27.setWordWrap(False)

        self.verticalLayout_42.addWidget(self.label_27)

        self.txt_extNumberUsers = QLineEdit(self.frame_29)
        self.txt_extNumberUsers.setObjectName(u"txt_extNumberUsers")

        self.verticalLayout_42.addWidget(self.txt_extNumberUsers)


        self.verticalLayout_21.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_28)
        self.verticalLayout_41.setSpacing(6)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 9, 0, 0)
        self.label_26 = QLabel(self.frame_28)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setScaledContents(True)
        self.label_26.setWordWrap(False)

        self.verticalLayout_41.addWidget(self.label_26)

        self.txt_intNumberUsers = QLineEdit(self.frame_28)
        self.txt_intNumberUsers.setObjectName(u"txt_intNumberUsers")

        self.verticalLayout_41.addWidget(self.txt_intNumberUsers)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_27)
        self.verticalLayout_40.setSpacing(6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 9, 0, 0)
        self.label_25 = QLabel(self.frame_27)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setScaledContents(True)
        self.label_25.setWordWrap(False)

        self.verticalLayout_40.addWidget(self.label_25)

        self.txt_neighborhoodUsers = QLineEdit(self.frame_27)
        self.txt_neighborhoodUsers.setObjectName(u"txt_neighborhoodUsers")

        self.verticalLayout_40.addWidget(self.txt_neighborhoodUsers)


        self.verticalLayout_21.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_26)
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 9, 0, 0)
        self.label_24 = QLabel(self.frame_26)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(False)

        self.verticalLayout_39.addWidget(self.label_24)

        self.txt_municipalyUsers = QLineEdit(self.frame_26)
        self.txt_municipalyUsers.setObjectName(u"txt_municipalyUsers")

        self.verticalLayout_39.addWidget(self.txt_municipalyUsers)


        self.verticalLayout_21.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.scrollAreaWidgetContents)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_25)
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 9, 0, 0)
        self.label_23 = QLabel(self.frame_25)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(False)

        self.verticalLayout_38.addWidget(self.label_23)

        self.txt_stateUsers = QLineEdit(self.frame_25)
        self.txt_stateUsers.setObjectName(u"txt_stateUsers")

        self.verticalLayout_38.addWidget(self.txt_stateUsers)


        self.verticalLayout_21.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_24)
        self.verticalLayout_37.setSpacing(6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 9, 0, 0)
        self.label_22 = QLabel(self.frame_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setScaledContents(True)
        self.label_22.setWordWrap(False)

        self.verticalLayout_37.addWidget(self.label_22)

        self.txt_postalCodeUsers = QLineEdit(self.frame_24)
        self.txt_postalCodeUsers.setObjectName(u"txt_postalCodeUsers")

        self.verticalLayout_37.addWidget(self.txt_postalCodeUsers)


        self.verticalLayout_21.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_23)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 9, 0, 0)
        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setScaledContents(True)
        self.label_21.setWordWrap(False)

        self.verticalLayout_36.addWidget(self.label_21)

        self.txt_phoneUsers = QLineEdit(self.frame_23)
        self.txt_phoneUsers.setObjectName(u"txt_phoneUsers")

        self.verticalLayout_36.addWidget(self.txt_phoneUsers)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_22)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 9, 0, 0)
        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setScaledContents(True)
        self.label_20.setWordWrap(False)

        self.verticalLayout_35.addWidget(self.label_20)

        self.txt_emailUsers = QLineEdit(self.frame_22)
        self.txt_emailUsers.setObjectName(u"txt_emailUsers")

        self.verticalLayout_35.addWidget(self.txt_emailUsers)


        self.verticalLayout_21.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_21)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 9, 0, 0)
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setScaledContents(True)
        self.label_19.setWordWrap(False)

        self.verticalLayout_34.addWidget(self.label_19)

        self.txt_birthDayUsers = QLineEdit(self.frame_21)
        self.txt_birthDayUsers.setObjectName(u"txt_birthDayUsers")

        self.verticalLayout_34.addWidget(self.txt_birthDayUsers)


        self.verticalLayout_21.addWidget(self.frame_21)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_16)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 9, 0, 0)
        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setScaledContents(True)
        self.label_14.setWordWrap(False)

        self.verticalLayout_29.addWidget(self.label_14)

        self.txt_calculatedAgeUsers = QLineEdit(self.frame_16)
        self.txt_calculatedAgeUsers.setObjectName(u"txt_calculatedAgeUsers")
        self.txt_calculatedAgeUsers.setEnabled(False)
        self.txt_calculatedAgeUsers.setStyleSheet(u"background-color: rgb(217, 217, 217);")

        self.verticalLayout_29.addWidget(self.txt_calculatedAgeUsers)


        self.verticalLayout_21.addWidget(self.frame_16)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)


        self.verticalLayout_19.addWidget(self.camposUsers)

        self.pnl_bottomButtonsUsers = QFrame(self.menuUsers)
        self.pnl_bottomButtonsUsers.setObjectName(u"pnl_bottomButtonsUsers")
        self.pnl_bottomButtonsUsers.setMinimumSize(QSize(0, 70))
        self.pnl_bottomButtonsUsers.setMaximumSize(QSize(16777215, 70))
        self.pnl_bottomButtonsUsers.setStyleSheet(u"#pnl_bottomButtonsUsers .QPushButton { \n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"	border-style: solid; \n"
"	border-radius: 4px;\n"
"}")
        self.pnl_bottomButtonsUsers.setFrameShape(QFrame.NoFrame)
        self.pnl_bottomButtonsUsers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.pnl_bottomButtonsUsers)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, 15, 15, 9)
        self.btn_cancelUsers = QPushButton(self.pnl_bottomButtonsUsers)
        self.btn_cancelUsers.setObjectName(u"btn_cancelUsers")
        self.btn_cancelUsers.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(11)
        self.btn_cancelUsers.setFont(font3)
        self.btn_cancelUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancelUsers.setStyleSheet(u"#btn_cancelUsers {\n"
"    color: rgb(79, 145, 201);\n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"#btn_cancelUsers:hover { \n"
"    background-color: rgb(240, 248, 255);\n"
"}\n"
"\n"
"#btn_cancelUsers:pressed { \n"
"    background-color: rgb(173, 216, 230);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_cancelUsers)

        self.btn_updateUsers = QPushButton(self.pnl_bottomButtonsUsers)
        self.btn_updateUsers.setObjectName(u"btn_updateUsers")
        self.btn_updateUsers.setMinimumSize(QSize(0, 40))
        self.btn_updateUsers.setFont(font3)
        self.btn_updateUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_updateUsers.setStyleSheet(u"#btn_updateUsers{\n"
"	background-color: rgb(79, 145, 201);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#btn_updateUsers:hover { \n"
"    \n"
"	background-color: rgb(135, 206, 235);\n"
"}\n"
"\n"
"#btn_updateUsers:pressed { \n"
"    background-color: rgb(66, 123, 170);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/resources/checkIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_updateUsers.setIcon(icon10)
        self.btn_updateUsers.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.btn_updateUsers)


        self.verticalLayout_19.addWidget(self.pnl_bottomButtonsUsers)


        self.horizontalLayout_8.addWidget(self.menuUsers)

        self.stackedWidget.addWidget(self.usersPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.stackedWidget.addWidget(self.historyPage)
        self.templatePage = QWidget()
        self.templatePage.setObjectName(u"templatePage")
        self.stackedWidget.addWidget(self.templatePage)
        self.sendPage = QWidget()
        self.sendPage.setObjectName(u"sendPage")
        self.stackedWidget.addWidget(self.sendPage)

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
        self.horizontalLayout_5.setContentsMargins(10, 3, 3, 3)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QuantumBank", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Correspondence Tool", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide Menu", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.btn_users.setText(QCoreApplication.translate("MainWindow", u"User Management", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"Create Correspondence", None))
        self.btn_template.setText(QCoreApplication.translate("MainWindow", u"Edit Template", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"Correspondence History", None))
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
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"QuantumBank \u2013 Automation and control of internal correspondence", None))
        self.settingsTopBtn.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.logoHome.setText("")
        self.label_4.setText("")
        self.txt_searchUsers.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by id...", None))
        self.btn_deleteUsers.setText("")
        self.btn_addUsers.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name Father", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Name Mother", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Street", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ext. Number", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Int. Number", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Neighborhood", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Municipality", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Postal Code", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Calculated Age", None));
#if QT_CONFIG(statustip)
        self.btn_refreshUsers.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_refreshUsers.setText("")
        self.btn_randomUsers.setText("")
        self.btn_editUsers.setText("")
        self.btn_clearUsers.setText("")
        self.lbl_idUsers.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Last Name Father", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Last Name Mother", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Street", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Ext. Number", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Int. Number", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Neighborhood", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Municipaly", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Postal Code", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Calculated Age", None))
        self.btn_cancelUsers.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_updateUsers.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2024 QuantumBank. All rights reserved.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v1.0.0  ", None))
    # retranslateUi

