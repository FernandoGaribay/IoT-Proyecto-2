import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt

from modules.dashboardFunctions import UIFunctions
from gui.dashboard import Ui_MainWindow

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global widgets
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)


        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

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