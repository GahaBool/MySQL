import re
import datetime

from mysql.connector import connect, Error


def create_table(connection):

    table_name = input("Enter table name: ")

    # Валидация имени таблицы через простое регулярное выражение
    if not re.match(r'^[A-Za-z0-9_]+$', table_name):
        print("Ошибка: Введенное имя таблицы недействительно.")
        return

    create_table_main_app = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
          id INT AUTO_INCREMENT PRIMARY KEY,
          deposit_name VARCHAR(255) NOT NULL,
          amount_deposit DECIMAL(10, 2),
          deposit_time TIME NOT NULL,
          deposit_date DATE NOT NULL,
          description TEXT
        );
        """

    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_main_app)
            for tb in cursor:
                print(f"{tb} created successfully")
    except Error as err:
        print(f"The error '{err}' occurred")


def delete_table(connection):
    table_name = input("Enter delete table name: ")

    # Валидация имени таблицы через простое регулярное выражение
    if not re.match(r'^[A-Za-z0-9_]+$', table_name):
        print("Ошибка: Введенное имя таблицы недействительно.")
        return

    create_table_main_app = f"""
    DROP TABLE IF EXISTS {table_name};
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_main_app)
            for tb in cursor:
                print(f"{tb} drop successfully")
    except Error as err:
        print(f"The error '{err}' occurred")


def make_deposit(connection):
    database = input("Enter database name: ")

    ds_name = input("Enter name deposit: ")
    amount = int(input("Enter amount deposit: "))
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    time = datetime.datetime.today().strftime("%H:%M")
    dc_name = input("Enter a description of the deposit: ")

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {database} (deposit_name, amount_deposit, deposit_time, deposit_date, description) VALUES ('{ds_name}', '{amount}', '{time}', '{date}', '{dc_name}')""")
            connection.commit()
            print("depocit created successfully")
    except Error as err:
        print(f"The error '{err}' occurred")


def delete_deposit(connection):

    name_table = input("Enter name table: ")
    id_deposit = input("Enter id deposit: ")

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM {name_table} WHERE id = {id_deposit}""")
            connection.commit()
            print("depocit delete successfully")
    except Error as err:
        print(f"The error '{err}' occurred")


def sum_deposit(connection):

    name_table = input("Enter name table: ")

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT SUM(amount_deposit) FROM {name_table}""")
            for query in cursor:
                print(query)
    except Error as err:
        print(f"The error '{err}' occurred")

def show_deposit(connection):

    name_table = input("Enter name table: ")

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM {name_table}""")
            for query in cursor:
                print(query)
    except Error as err:
        print(f"The error '{err}' occurred")


