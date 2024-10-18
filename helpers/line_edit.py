from PySide6.QtWidgets import QLineEdit

def is_empy(line_edit: QLineEdit):
    if line_edit.text():
        return False
    else:
        return True