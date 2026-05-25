from utils.common import clear_console
from utils.inputs import get_choice, get_input
from utils.ui import print_menu_title, print_menu_options, print_line
from utils.logger import log_info_message, log_error_message

def update_user(user_repository):
    clear_console()

    print_menu_title("Update User")

    user_id = get_input("Enter the user ID to update: ")

    user = user_repository.get_users_by_id(int(user_id))

    if user == None:
        log_error_message("User not found")
        return
    
    print('\nName: ' + user.name)
    print('\nEmail: ' + user.email)
    print('\nPassword: ' + user.password)

    print()

    print_line()
    print_menu_options(["Update Name", "Update Email", "Update Password", "Exit"])
    print_line()

    choice = get_choice()

    if choice == 1:
        new_name = get_input("Enter the new name: ")
        user.name = new_name
        log_info_message("Name updated successfully")
    else:
        log_error_message("Invalid choice")

    return user