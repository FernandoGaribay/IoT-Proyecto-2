from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class UIFunctions():

    def toggleMenu(self, enable):
            if enable:
                # GET WIDTH
                width = self.ui.leftMenuBg.width()
                maxExtend = 200 #Settings.MENU_WIDTH
                standard = 60

                # SET MAX WIDTH
                if width == 60:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                # ANIMATION
                self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
                self.animation.setDuration(600) # Settings.TIME_ANIMATION
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QEasingCurve.InOutQuart)
                self.animation.start()