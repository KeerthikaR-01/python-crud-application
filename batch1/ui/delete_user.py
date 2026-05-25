from utils.common import clear_console
from utils.inputs import get_input
from utils.ui import print_menu_title

def delete_user():
    clear_console()

    print_menu_title("Delete User")

    user_id = get_input("Enter the user ID to delete: ")

    return int(user_id)