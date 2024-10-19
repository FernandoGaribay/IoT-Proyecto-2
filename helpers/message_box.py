from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget

def show_alert(parent):
    QMessageBox.warning(parent, "Warning", "Username and password cannot be empty.")