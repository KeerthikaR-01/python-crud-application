from ui.main_menu import print_main_menu
from utils.inputs import get_choice
from utils.common import clear_console
from ui.create_user import create_user
from utils.logger import log_info_message
from repository.UserRepository import UserRepository
from ui.print_users import print_users

def main():
    userRepository = UserRepository()

    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            
            new_user = create_user()

            if userRepository.get_user_email(new_user.email):
                log_info_message(f"Email {new_user.email} already exists.")
                continue

            user_id = len(userRepository.users) + 1
            new_user.id = user_id

            userRepository.add_user(new_user)

            log_info_message(f"User created Successfully: ID: {new_user.id}, Name: {new_user.name}, Email: {new_user.email}, Password: {new_user.password}")
            continue

        elif choice == 2:
            users = userRepository.get_users()
            print_users(users)
            continue

        elif choice == 3:
            print("Update User")
            continue
        
        elif choice == 4:
            print("Delete User")
            continue

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
            break

main()   
