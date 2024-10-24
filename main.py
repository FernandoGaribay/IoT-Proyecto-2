import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

from gui.login import Ui_MainWindow
from modules.loginFunctions import LoginFuctions

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Mantener una referencia al dashboard
        self.dashboard_window = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.btnLogIn.clicked.connect(self.handle_login)

    def handle_login(self):
        self.dashboard_window = LoginFuctions.validate_log_in(self.ui.txtUsername, self.ui.txtPassword, self)
        if self.dashboard_window:
            self.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
