from helpers.line_edit import is_empy
from PySide6.QtWidgets import QLineEdit

def validate_log_in(txt_username: QLineEdit, txt_password: QLineEdit):
    if is_empy(txt_username) or is_empy(txt_password):
        print('Username and password cannot be empty.')
    else:
        print('campos')
        
