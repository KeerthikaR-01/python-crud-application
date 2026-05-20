from ui.main_menu import print_main_menu
from utils.inputs import get_choice
from utils.common import clear_console
from utils.ui import print_menu_title

def main():
    while True:
        print_main_menu()

        choice = get_choice()

        if choice == 1:
            clear_console()
            print_menu_title("Create User")
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
