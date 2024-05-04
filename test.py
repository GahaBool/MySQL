import keyboard
from mysql.connector import connect, Error, errorcode

#Добавление горячей клавиши для завершение программы
#================================================================
def exit_program():
    print("Exit program...")
    quit()

try:
    #Подключение к серверу MYSQL. Показывает количество баз.данных которые находятся на сервере
    #================================================================
    with connect(host = "Localhost",
    username = input('Username: '),
    password = input('Password: '))as connection:
    # Доработанная версия работы с базой данных
    # ================================================================
        while True:
            cmd = input("Inpurt comand: ")
            with connection.cursor() as cursor:
                cursor.execute(cmd)
                for db in cursor:
                    print(db)
            keyboard.add_hotkey('ctrl+q', exit_program)

#Отработка ошибок которые выходятв  процессе работы программы
#============================================================================
except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Password or user name is incorrect! Please try again')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)