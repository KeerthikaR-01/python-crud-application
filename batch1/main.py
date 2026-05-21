from ui.create_user import create_user
from ui.main_menu import print_main_menu
from utils.inputs import get_choice
from utils.common import clear_console
from utils.logger import log_info_message, log_error_message
from repository.UserRepository import UserRepository
from ui.print_users import print_users

def main():

    user_repository = UserRepository()
    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            clear_console()

            new_user = create_user()
            

            user_id = len(user_repository.users) + 1
            new_user.id = user_id

            user_repository.add_user(new_user)

            log_info_message(f"User created Successfully: ID: {new_user.id}, Name: {new_user.name}, Email: {new_user.email}, Password: {new_user.password}")

            continue

        elif choice == 2:

            users = user_repository.get_users()
            print_users(users)

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