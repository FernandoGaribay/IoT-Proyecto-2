from helpers.line_edit import is_empy
from helpers.message_box import show_alert
from PySide6.QtWidgets import QLineEdit

def validate_log_in(txt_username: QLineEdit, txt_password: QLineEdit, parent):
    if is_empy(txt_username) or is_empy(txt_password):
        show_alert(parent)
    else:
        print('campos')
        
