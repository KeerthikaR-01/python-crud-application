from utils.ui import print_line, print_menu

def print_main_menu():
    menu_title = "User Management System"
    menu_options = ["Create User", "Read User", "Update User", "Delete User", "Exit"]
    print_menu(menu_title, menu_options)
    print_line()