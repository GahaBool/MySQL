import keyboard
from text import menu_work_table, menu_work_deposit, text_main_menu
from main_app import create_table, make_deposit, delete_deposit, delete_table, sum_deposit, show_deposit


#Создание нового файла для работы с меню в cmd
#================================================================
def choise_work_space(connection):
    print(text_main_menu)
    main_line = input("Enter query: ").lower()

    if main_line == "1":
        table_menu(connection)

    if main_line == "2":
        deposit_menu(connection)


def table_menu(connection):
    print(menu_work_table)
    main_line = input("Enter query: ").lower()

    if main_line == "1":
        print(menu_work_table)
        main_line = input("Enter query: ").lower()

    if main_line == "1":
        create_table(connection)
        table_menu(connection)

    if main_line == "2":
        delete_table(connection)
        table_menu(connection)

    if main_line == "back":
        back_menu(connection)

    else:
        print("\nThere is no such menu option!")
        print("Try again...")
        table_menu(connection)


def deposit_menu(connection):
    print(menu_work_deposit)
    main_line = input("Enter query: ").lower()

    if main_line == "2":
        print(menu_work_deposit)
        main_line = input("Enter query: ").lower()

    if main_line == "1":
        make_deposit(connection)
        deposit_menu(connection)

    if main_line == "2":
        delete_deposit(connection)
        deposit_menu(connection)

    if main_line == "3":
        show_deposit(connection)
        deposit_menu(connection)

    if main_line == "4":
        sum_deposit(connection)
        deposit_menu(connection)

    if main_line == "back":
        back_menu(connection)

    else:
        print("\nThere is no such menu option!")
        print("Try again...")
        deposit_menu(connection)

def back_menu(connection):
    choise_work_space(connection)

keyboard.add_hotkey("ctrl+1", back_menu)