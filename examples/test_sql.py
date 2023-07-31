# Система управления базами данных (СУБД) SQLite
 
import sqlite3 as sql

# Соединение с базой данных
conn = sql.connect("examples/test.db")

# курсор - "Панель управления" БД
cursor = conn.cursor()

# Создание таблицы
sql_cmd = """
    create table if not exists users (
        user_id int primary key,
        f_name text,
        l_name text,
        age real,
        gender text
    );
"""
cursor.execute(sql_cmd)
conn.commit()

# Запись данных
# одна строка
# sql_cmd = "INSERT INTO users VALUES (?,?,?,?,?);"
# cursor.execute(sql_cmd, (0, "Jphn", "Sherman", 30.5, "m"))
# conn.commit()

# много строк
# sql_cmd = "INSERT INTO users VALUES (?,?,?,?,?);"
# data = [
#     (1, "Misha", "Kychkin", 28.10, "m"),
#     (2, "Alesha", "Kychkin", 30.5, "m"),
#     (3, "Kolya", "Nikiforov", 28.11, "m")
# ]
# cursor.executemany(sql_cmd, data)
# conn.commit()

# Чтение данных
# Все столбцы
# sql_cmd = "SELECT * FROM users;"

# Определенные столбцы
# sql_cmd = "SELECT user_id, f_name, age FROM users;"

# с условием
# sql_cmd = "SELECT user_id, f_name, age FROM users where age > 29 and gender = 'm';"
# cursor.execute(sql_cmd)

# Первая строка из таблицы
# result = cursor.fetchone()

# # Много строк из таблицы
# result = cursor.fetchmany(2)

# Все строки из таблицы
# result = cursor.fetchall()

# print(result)

# Удаление данных
# sql_cmd = "DELETE FROM users WHERE l_name='Sherman';"
# cursor.execute(sql_cmd)
# conn.commit()

# Создание второй таблицы
sql_cmd = """
    create table if not exists orders (
        order_id int primary key,
        date text,
        user_id int,
        total real
    );
"""
cursor.execute(sql_cmd)
conn.commit()

# Запись данных
# sql_cmd = "INSERT INTO orders VALUES (?,?,?,?);"
# data = [
#     (0, "21.08.22", "1", 28.10),
#     (1, "3.05.19", "2", 130.5),
#     (2, "16.12.21", "3", 528.11),
#     (3, "9.1.23", "0", 50.11),
#     (4, "10.06.20", "2", 1000),
#     (5, "19.2.23", "2", 3000),
#     (6, "30.5.23", "0", 2000)
# ]
# cursor.executemany(sql_cmd, data)
# conn.commit()

# Чтение данных из двух таблиц
sql_cmd = "SELECT * FROM users LEFT JOIN orders ON users.user_id=orders.user_id;"
cursor.execute(sql_cmd)
# Все строки из таблицы
result = cursor.fetchall()

print(result)
conn.close()
