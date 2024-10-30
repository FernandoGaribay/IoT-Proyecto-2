import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt

from modules.dashboardFunctions import UIFunctions, UsersFunctions, TemplatesFunctions, SendCorrespondency
from gui.dashboard import Ui_MainWindow

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        global widgets
        widgets = self.ui

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        # Buttons left menu
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_users.clicked.connect(self.buttonClick)
        widgets.btn_send.clicked.connect(self.buttonClick)
        widgets.btn_template.clicked.connect(self.buttonClick)

        self.users_functions = UsersFunctions(self.ui)
        widgets.btn_updateUsers.clicked.connect(lambda: self.users_functions.addContact())
        widgets.btn_cancelUsers.clicked.connect(lambda: UIFunctions.toggleRightBoxUsers(self, True))
        widgets.btn_deleteUsers.clicked.connect(lambda: self.users_functions.deleteContact())
        widgets.btn_editUsers.clicked.connect(lambda: self.users_functions.updateContact())
        widgets.btn_randomUsers.clicked.connect(lambda: self.users_functions.randomContact())
        widgets.btn_refreshUsers.clicked.connect(lambda: self.users_functions.showContacts())
        widgets.btn_addUsers.clicked.connect(lambda: UIFunctions.toggleRightBoxUsers(self, True))
        widgets.btn_clearUsers.clicked.connect(lambda: self.users_functions.clearCamps())

        def showHideUserData(item):
            show = not widgets.txt_idUsers.text()
            print(show)
            self.users_functions.showUserData(item, show)
        widgets.tableWidget.itemClicked.connect(showHideUserData)


        # Widgets Templates
        templates_functions = TemplatesFunctions()
        widgets.btn_accoutSumaryTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/account_summary_template.docx"))
        widgets.btn_paymenyReminderTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/payment_reminder_template.docx"))
        widgets.btn_accountStatementTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/account_statement.docx"))


        # Widgets Send Correspondency
        self.send_correspondency = SendCorrespondency(self.ui)
        widgets.tableWidgetSend.itemClicked.connect(self.send_correspondency.showUserData)
        widgets.listContacts.itemClicked.connect(self.send_correspondency.removeContactFromSending)
        widgets.btn_confirmSend.clicked.connect(self.send_correspondency.confirmSending)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        def resizeEvent(self, event):
            UIFunctions.resize_grips(self)

        UIFunctions.uiDefinitions(self)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_users":
            widgets.stackedWidget.setCurrentWidget(widgets.usersPage)
            UIFunctions.resetStyle(self, btnName)
            self.users_functions.showContacts()
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_send":
            widgets.stackedWidget.setCurrentWidget(widgets.sendPage)
            UIFunctions.resetStyle(self, btnName)
            self.send_correspondency.showContacts()
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_template":
            widgets.stackedWidget.setCurrentWidget(widgets.templatePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        print(f'Boton "{btnName}"')

    def show(self):
        super().show()
        self.setFocus()
        self.activateWindow()

        self.setWindowOpacity(0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.animation.start()