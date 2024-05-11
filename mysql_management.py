import keyboard
from mysql.connector import connect, Error, errorcode


#Работа с MySQL
#================================================================
def connect_databases(host_name, user_name, password_name, name_database):
    try:
        with connect(
            host = host_name,
            username = user_name,
            password = password_name,
            database = name_database
        ) as connection:
            while True:
                query = input("Enter query: ")
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        for query in cursor:
                            print(query)
                except Error as err:
                    print(f"Error: {err}")

        # Горячие клавиша для работы с MySQL БД
        # ================================================================
        def close_database():
            connection.close()
            print("Database closed!")

        keyboard.add_hotkey("ctrl+1", close_database)#Кнопка не работает! Переделать.

    except Error as err:
        print(f"The error '{err}' occurred")


