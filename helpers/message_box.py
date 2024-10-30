from PySide6.QtWidgets import QMessageBox

def show_alert(parent, message):
    QMessageBox.warning(parent, "Warning", message)