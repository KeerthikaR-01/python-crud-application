from utils.common import clear_console
from utils.ui import print_menu_title

def print_users(users):
    clear_console()

    print_menu_title("Users List")
    
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email} Password: {user.password}")