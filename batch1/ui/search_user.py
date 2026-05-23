from utils.common import clear_console
from utils.inputs import get_input
from utils.ui import print_menu_title

def search_user():
    clear_console()

    print_menu_title("Search User")

    user_id = get_input("Enter ID to Search User: ")

    return int(user_id)