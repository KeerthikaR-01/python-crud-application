from ui.create_user import create_user
from ui.main_menu import print_main_menu
from utils.inputs import get_choice
from utils.common import clear_console
from utils.logger import log_info_message, log_error_message

def main():
    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            clear_console()

            new_user = create_user()
            log_info_message(f"User created Successfully: Name: {new_user.name}, Email: {new_user.email}, Password: {new_user.password}")

            continue

        elif choice == 2:
            log_info_message("Read User")
            continue

        elif choice == 3:
            log_info_message("Update User")
            continue

        elif choice == 4:
            log_info_message("Delete User")
            continue

        elif choice == 5:
            log_info_message("Exit")
            break

        else:
            log_error_message("Invalid choice. Please try again.")
            break

main()