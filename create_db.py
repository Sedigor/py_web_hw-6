import sqlite3


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('university.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(sql)
        
if __name__ == "__main__":
    create_db()