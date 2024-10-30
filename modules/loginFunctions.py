from helpers.line_edit import is_empy
from helpers.message_box import show_alert
from PySide6.QtWidgets import QLineEdit

class LoginFuctions:

    def validate_log_in(txt_username: QLineEdit, txt_password: QLineEdit, parent):
        if is_empy(txt_username) or is_empy(txt_password):
            show_alert(parent, "Username and password cannot be empty.")
            return

        if txt_username.text() == "admin" and txt_password.text() == "123":
            from dashboard import DashboardWindow

            dashboard_window = DashboardWindow()
            dashboard_window.show()
            return dashboard_window
        else:
            show_alert(parent, "Incorrect username or password. Please try again.")
