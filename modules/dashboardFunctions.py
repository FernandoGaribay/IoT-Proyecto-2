from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from modules.app_settings import *

class UIFunctions():

    def toggleMenu(self, enable):
            if enable:
                width = self.ui.leftMenuBg.width()
                maxExtend = Settings.MENU_WIDTH
                standard = 60

                if width == 60:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
                self.animation.setDuration(Settings.TIME_ANIMATION)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QEasingCurve.InOutQuart)
                self.animation.start()