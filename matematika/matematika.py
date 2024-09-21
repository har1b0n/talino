import random
import re
from matematika_functions import clear_console,welcome_screen,main_menu,goodbye_screen
from matematika_operations import choose_level,perform_addition,perform_subtraction,perform_multiplication,perform_division,perform_count    

welcome_screen()

yourname = input("\033[1;37mEnter your name: ").strip()
sanitized_name = re.sub(r'[^\w\-_.]', '_', yourname)

exit = 'n'
while exit == 'n':

    clear_console()
    choice1 = main_menu()
    match choice1:
        case 1:
            clear_console()
            level = choose_level(1)
            perform_addition(level, sanitized_name)
        case 2:
            clear_console()
            level = choose_level(2)
            perform_subtraction(level, sanitized_name)
        case 3:
            clear_console()
            level = choose_level(3)
            perform_multiplication(level, sanitized_name)
        case 4:
            clear_console()
            level = choose_level(4)
            perform_division(level, sanitized_name)
        case 5:
            clear_console()
            perform_count()
        case _:  # Handles any invalid input
            print("\033[1;31mInvalid choice. Please choose a valid option.")

    print("\033[1;34m")
    exit = input("\n\033[1;37mDo you want to exit the game? (y/n): ")
    if exit.lower() == 'y':
        goodbye_screen()
        break
