import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from gui.login import Ui_MainWindow
from events.login_event_handler import validate_log_in

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnLogIn.clicked.connect(lambda: validate_log_in(self.ui.txtUsername, self.ui.txtPassword))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
