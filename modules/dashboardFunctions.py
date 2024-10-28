from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from modules.app_settings import *
from controllers.contact_controller import ContactController
from helpers.random_contact_generator import RandomContactGenerator

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

    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def toggleRightBoxUsers(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.menuUsers.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_USERS_WIDTH
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.menuUsers, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    def uiDefinitions(self):
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                delta = event.globalPos() - self.dragPos
                self.move(self.pos() + delta)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

class UsersFunctions():

    def __init__(self, ui):
        self.ui = ui 

    def addContact(self):
        controller = ContactController(self.ui)
        controller.add_contact(controller.get_fields())
        self.clearCamps()
        self.showContacts()

    def deleteContact(self):
        id = self.ui.txt_idUsers.text()

        controller = ContactController(self.ui)
        controller.delete_contact(id)
        self.clearCamps()
        self.showContacts()

    def updateContact(self):
        controller = ContactController(self.ui)

        id = self.ui.txt_idUsers.text()
        contact = controller.get_fields()
        controller.update_contact(id, contact)
        self.clearCamps()
        self.showContacts()

    def randomContact(self):
        random_contact = RandomContactGenerator()
        contact = random_contact.generate_contact()
        self.clearCamps()
        self.fill_contact_fields(contact)

    def showContacts(self):
        controller = ContactController(self.ui)
        contacts = controller.view_contacts()

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(17)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            'ID', 'Name', 'Surname1', 'Surname2', 'Job Title', 'Company',
            'Street', 'Ext Number', 'Int Number', 'Neighborhood', 
            'City', 'State', 'Postal Code', 'Phone', 'Email', 
            'Birth Date', 'Age'
        ])

        for contact in contacts:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(contact.id)))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(contact.name))
            self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(contact.surname1))
            self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(contact.surname2))
            self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(contact.job_title))
            self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(contact.company))
            self.ui.tableWidget.setItem(row_position, 6, QTableWidgetItem(contact.street))
            self.ui.tableWidget.setItem(row_position, 7, QTableWidgetItem(contact.ext_number))
            self.ui.tableWidget.setItem(row_position, 8, QTableWidgetItem(contact.int_number))
            self.ui.tableWidget.setItem(row_position, 9, QTableWidgetItem(contact.neighborhood))
            self.ui.tableWidget.setItem(row_position, 10, QTableWidgetItem(contact.city))
            self.ui.tableWidget.setItem(row_position, 11, QTableWidgetItem(contact.state))
            self.ui.tableWidget.setItem(row_position, 12, QTableWidgetItem(contact.postal_code))
            self.ui.tableWidget.setItem(row_position, 13, QTableWidgetItem(contact.phone))
            self.ui.tableWidget.setItem(row_position, 14, QTableWidgetItem(contact.email))
            self.ui.tableWidget.setItem(row_position, 15, QTableWidgetItem(contact.birth_date))
            self.ui.tableWidget.setItem(row_position, 16, QTableWidgetItem(str(contact.age)))
        print("Data updated")

    def clearCamps(self):
        id = self.ui.txt_idUsers.setText("")
        name = self.ui.txt_nameUsers.setText("")
        surname1 = self.ui.txt_lastNameFatherUsers.setText("")
        surname2 = self.ui.txt_lastNameMotherUsers.setText("")
        job_title = self.ui.txt_positionUsers.setText("")
        company = self.ui.txt_companyUsers.setText("")
        street = self.ui.txt_streetUsers.setText("")
        ext_number = self.ui.txt_extNumberUsers.setText("")
        int_number = self.ui.txt_intNumberUsers.setText("")
        neighborhood = self.ui.txt_neighborhoodUsers.setText("")
        city = self.ui.txt_municipalyUsers.setText("")
        state = self.ui.txt_stateUsers.setText("")
        postal_code = self.ui.txt_postalCodeUsers.setText("")
        phone = self.ui.txt_phoneUsers.setText("")
        email = self.ui.txt_emailUsers.setText("")
        birth_date = self.ui.txt_birthDayUsers.setText("")
        age = self.ui.txt_calculatedAgeUsers.setText("")

    def showDataUser(self, item):
        controller = ContactController(self.ui)

        contact = controller.get_contact_by_id(self._get_fist_column(item))
        self.fill_contact_fields(contact)
        
    def fill_contact_fields(self, contact):
        if contact:
            self.ui.txt_idUsers.setText(str(contact.id))
            self.ui.txt_nameUsers.setText(contact.name)
            self.ui.txt_lastNameFatherUsers.setText(contact.surname1)
            self.ui.txt_lastNameMotherUsers.setText(contact.surname2)
            self.ui.txt_positionUsers.setText(contact.job_title)
            self.ui.txt_companyUsers.setText(contact.company)
            self.ui.txt_streetUsers.setText(contact.street)
            self.ui.txt_extNumberUsers.setText(contact.ext_number)
            self.ui.txt_intNumberUsers.setText(contact.int_number)
            self.ui.txt_neighborhoodUsers.setText(contact.neighborhood)
            self.ui.txt_municipalyUsers.setText(contact.city)
            self.ui.txt_stateUsers.setText(contact.state)
            self.ui.txt_postalCodeUsers.setText(contact.postal_code)
            self.ui.txt_phoneUsers.setText(contact.phone)
            self.ui.txt_emailUsers.setText(contact.email)
            self.ui.txt_birthDayUsers.setText(contact.birth_date)
            self.ui.txt_calculatedAgeUsers.setText(str(contact.age))

    def _get_fist_column(self, item):
        row = item.row()
        first_column_value = self.ui.tableWidget.item(row, 0).text()
        return first_column_value
        