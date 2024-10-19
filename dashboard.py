import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from gui.dashboard import Ui_MainWindow

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowOpacity(0)
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    def show(self):
        super().show()
        self.setFocus()
        self.activateWindow()

        self.animation.start()