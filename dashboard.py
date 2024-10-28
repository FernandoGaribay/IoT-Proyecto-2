import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt

from modules.dashboardFunctions import UIFunctions, UsersFunctions, TemplatesFunctions
from gui.dashboard import Ui_MainWindow

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)


        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        # Buttons left menu
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_users.clicked.connect(self.buttonClick)
        widgets.btn_send.clicked.connect(self.buttonClick)
        widgets.btn_template.clicked.connect(self.buttonClick)
        widgets.btn_history.clicked.connect(self.buttonClick)

        users_functions = UsersFunctions(self.ui)
        users_functions.showContacts()
        widgets.btn_updateUsers.clicked.connect(lambda: users_functions.addContact())
        widgets.btn_cancelUsers.clicked.connect(lambda: UIFunctions.toggleRightBoxUsers(self, True))
        widgets.btn_deleteUsers.clicked.connect(lambda: users_functions.deleteContact())
        widgets.btn_editUsers.clicked.connect(lambda: users_functions.updateContact())
        widgets.btn_randomUsers.clicked.connect(lambda: users_functions.randomContact())
        widgets.btn_refreshUsers.clicked.connect(lambda: users_functions.showContacts())
        widgets.btn_addUsers.clicked.connect(lambda: UIFunctions.toggleRightBoxUsers(self, True))
        widgets.btn_clearUsers.clicked.connect(lambda: users_functions.clearCamps())

        widgets.tableWidget.itemClicked.connect(users_functions.showDataUser)


        # Widgets Templates
        templates_functions = TemplatesFunctions()
        widgets.btn_accoutSumaryTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/account_summary_template.docx"))
        widgets.btn_paymenyReminderTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/payment_reminder_template.docx"))
        widgets.btn_accountStatementTemplates.clicked.connect(lambda: templates_functions.openTemplate("templates/account_statement.docx"))

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

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
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_send":
            widgets.stackedWidget.setCurrentWidget(widgets.sendPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_template":
            widgets.stackedWidget.setCurrentWidget(widgets.templatePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_history":
            widgets.stackedWidget.setCurrentWidget(widgets.historyPage)
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