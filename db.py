import sqlite3 as sql

# Создание БД
def create_db(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pwd TEXT,
            salt TEXT,
            num_char INTEGER,
            result TEXT
        );
        """
    )
    connect.commit()
    connect.close()

# Функция записи данных в БД
def write_db(path, data):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO logs (pwd, salt, num_char, result) VALUES (?, ?, ?, ?);", data)
    connect.commit()
    connect.close()

# Чтение данных из БД
def read_db(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM logs;")
    return cursor.fetchall()

# Тестирование
# path = "test.db"
# create_db(path)
# write_db(path, [("qwerty", "mail", 7, "asdfghj"), ("qwe1234", "gmail", 6, "qwerty")])
# print(read_db(path))
