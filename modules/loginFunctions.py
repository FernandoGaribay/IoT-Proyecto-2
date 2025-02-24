from helpers.line_edit import is_empy
from helpers.message_box import show_alert
from PySide6.QtWidgets import QLineEdit

class LoginFuctions:

    def validate_log_in(txt_username: QLineEdit, txt_password: QLineEdit, parent):
        if is_empy(txt_username) or is_empy(txt_password):
            show_alert(parent)
            # return None

        if txt_username.text() == "" and txt_password.text() == "": # Contraseña eliminada temporalmente
            from dashboard import DashboardWindow

            dashboard_window = DashboardWindow()
            dashboard_window.show()
            return dashboard_window
