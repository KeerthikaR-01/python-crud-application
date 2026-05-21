from utils.common import clear_console
from utils.logger import log_error_message
from utils.ui import print_menu_title
from utils.inputs import get_input
from model.user import User
from utils.user_validation import validate_name, validate_email, validate_password

def create_user():
    clear_console()
    print_menu_title("Create User")

    while True:
        name = get_input("Enter name: ")
        name_error = validate_name(name)
        if name_error:
            log_error_message(name_error)
            continue
        else:
            break
    
    while True:
        email = get_input("Enter email: ")
        email_error = validate_email(email)
        if email_error:
            log_error_message(email_error)
            continue
        else:
            break
  
    while True:
        password = get_input("Enter password: ")
        password_error = validate_password(password)
        if password_error:
            log_error_message(password_error)
            continue
        else:
            break

    return User(None, name, email, password)

