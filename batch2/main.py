from ui.main_menu import print_main_menu
from utils.inputs import get_choice
from utils.common import clear_console
from ui.create_user import create_user
from utils.logger import log_info_message

def main():
    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            
            new_user = create_user()

            log_info_message(f"User created Successfully: Name: {new_user.name}, Email: {new_user.email}, Password: {new_user.password}")
            continue

        elif choice == 2:
            clear_console()
            print("View Users")
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
