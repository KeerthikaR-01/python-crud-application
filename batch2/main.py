from constants.ui import DEFAULT_LINE_COUNT, DEFAULT_LINE_CHARACTER

def print_line(character = DEFAULT_LINE_CHARACTER, count = DEFAULT_LINE_COUNT):
    for i in range(1, count + 1, 1):
        print(character, end='')
    print()

def print_menu_title(title):
    print_line()
    print(title.center(DEFAULT_LINE_COUNT))
    print_line()

def print_menu_options(options):
    for i, opt in enumerate(options, 1):
        right = f"Press: {i}"
        spaces = DEFAULT_LINE_COUNT - len(opt) - len(right)
        spaces = max(spaces, 1)

        print(f"{opt}{' ' * spaces}{right}")


def print_menu(title, options):
    print_menu_title(title)
    print_menu_options(options)
    print_line()

def print_main_menu():
    menu_title = 'User Management System'
    menu_options = ['Create User', 'View Users', 'Update User', 'Delete User', 'Exit']
    print_menu(menu_title, menu_options)

def main():
    print_main_menu()

main()