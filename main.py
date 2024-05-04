import keyboard
from mysql.connector import connect, Error, errorcode


def create_table(cconnection, table):
    cursor = connection.cursor()
    try:
        cursor.execute(table)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#Добавление горячей клавиши для завершение программы
#================================================================
def exit_program():
    print("Exit program...")
    quit()


# Функция которая запрашивает данные MySQL сервера и помогает войти
# ================================================================
def connect_database(host_name, user_name, password_name):
    try:
        with connect(
            host = host_name,
            username = user_name,
            password = password_name
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            for db in cursor:
                print(db)
    except Error as err:
        print(f"The error '{err}' occurred")
        return None

#Выбор БД
#================================================================
def choose_database(host_name, user_name, password_name, name_database):
    try:
        connection = connect(
            host = host_name,
            username = user_name,
            password = password_name,
            database = name_database
        )
        return connection
    except Error as err:
        print(f"The error '{err}' occurred")
    return None

#Работа с запросами в MySQL
#================================================================
def query_database(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for query in cursor:
            print(query)
    except Error as e:
        print(f"The error '{e}' occurred")


#Создание таблицы
#===============================================================
def create_table(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

host = "localhost"
User_name = input("Enter user name: ")
Password_user = input("Enter user passoword: ")

connection = connect_database(host, User_name, Password_user)
choose_database = (host, User_name, Password_user, input("Enter database: "))
query_database(choose_database, input("""Enter your query:
 """))


table_creation_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""