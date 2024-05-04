import keyboard
from mysql.connector import connect, Error, errorcode

from mysql_management import connect_databases

#Основное меню по управлению приложения
#================================================================
def main_menu():
    while True:
        print("""
MENU:
    1.database management
    2.wor

Enter EXIT or press CTRL+Q to exit!
                    """)
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
            pass

        elif main_line == 'exit':
            exit_program()

        else:
            print("Нет такой опции попробуйте еще раз!")

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

