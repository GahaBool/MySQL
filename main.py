import keyboard
from mysql.connector import connect, Error, errorcode
from menu_for_cmd import choise_work_space

#Подключение к базам MySQL
#================================================================
def connection_db():
    try:
        connection = connect(host='localhost',
                             user='root',
                             password='2wsx$RFV',
                             db='finance',)
        print("successfully connected...")
        print("################################################################")
    except Error as err:
        print(f"The error '{err}' occurred")
    return connection

connection = connection_db()#Для того что бы проще работать с данными.

#Главное меню
#================================================================
def main_menu():

    choise_work_space(connection)

    if main_line == "exit":
        exit_program()

    else:
        print("\nThere is no such menu option!")
        print("Try again...")
        main_menu()

    connection.close()

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

