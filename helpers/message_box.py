from PySide6.QtWidgets import QMessageBox

def show_alert(parent):
    QMessageBox.warning(parent, "Warning", "Username and password cannot be empty.")