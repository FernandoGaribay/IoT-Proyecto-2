import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from gui.dashboard import Ui_MainWindow

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)