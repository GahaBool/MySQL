from mysql.connector import connect, Error
from text import text_main_app

from

def create_table(connection, table_name):

    # Валидация имени таблицы через простое регулярное выражение
    if not re.match(r'^[A-Za-z0-9_]+$', table_name):
        print("Ошибка: Введенное имя таблицы недействительно.")
        return

    create_table_main_app = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
          id INT AUTO_INCREMENT PRIMARY KEY,
          deposit_name VARCHAR(255) NOT NULL,
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


create_table