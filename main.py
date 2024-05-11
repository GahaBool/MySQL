import keyboard
from mysql.connector import connect, Error, errorcode

from main_app import create_table, connection_db
from mysql_management import connect_databases
from text import text_main_menu , text_main_app

#Основное меню по управлению приложения
#================================================================
def main_menu():
    print(text_main_menu)
    main_line = input("Enter: ").lower()

    if main_line == '1':
        # Подключение к серверу MySQL таблицы
        # ===============================================================
        host = "localhost"
        User_name = input("Enter user name: ")
        Password_user = input("Enter user passoword: ")
        choose_databases = input("Enter database: ")

        connect_databases(host, User_name, Password_user, choose_databases)

    elif main_line == '2':
        print(text_main_app)
        main_line = input("Enter: ").lower()

        if main_line == '1':
            create_table(connection_db)

    if main_line == 'exit':
        exit_program()

    else:
        print("Нет такой опции попробуйте еще раз!")
        main_menu()

#Добавление горячей клавиши для завершение программы
#================================================================
def exit_program():
    print("\nExit program...")
    quit()
keyboard.add_hotkey("ctrl+q", exit_program)

#
#================================================================
if __name__ == "__main__":
    main_menu()

