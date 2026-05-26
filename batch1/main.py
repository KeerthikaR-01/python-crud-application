from ui.create_user import create_user
from ui.main_menu import print_main_menu
from ui.update_user import update_user
from utils.inputs import get_choice
from utils.common import clear_console
from utils.logger import log_info_message, log_error_message
from repository.UserRepository import UserRepository
from ui.print_users import print_users
from ui.search_user import search_user
from ui.delete_user import delete_user

def main():

    user_repository = UserRepository()

    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            clear_console()

            new_user = create_user()

            if user_repository.get_user_by_email(new_user.email):
                log_error_message("Email already exists. Please try again.")
                continue

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
            updated_user = update_user(user_repository)
            if updated_user:
                log_info_message(f"User updated successfully: ID: {updated_user.id}, Name: {updated_user.name}, Email: {updated_user.email}, Password: {updated_user.password}")
            continue

        elif choice == 4:
            user_id = delete_user()

            if user_repository.get_users_by_id(user_id) == None:
                log_error_message("User not found")
                continue

            user_repository.delete_user(user_id)
            log_info_message("User deleted successfully")

        elif choice == 5:
            user_id = search_user()

            users = user_repository.get_users_by_id(user_id)

            if users:
                print(f"User found: ID: {users.id}, Name: {users.name}, Email: {users.email}, Password: {users.password}")

            else:
                log_info_message("User not found")

        elif choice == 6:
            log_info_message("Exit")
            break

        else:
            log_error_message("Invalid choice. Please try again.")
            break

main()