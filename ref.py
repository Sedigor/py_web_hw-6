import sqlite3
from faker import Faker
import random


fake = Faker()

groups = ['el-22' + str(i) for i in range(3)]

teachers = [fake.name() for _ in range(5)]

students = [fake.name() for _ in range(50)]

subjects = ['Biology', 'Mathematics', 'Physics' 'Chemistry', 'History', 'English']

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT)''')

# Генерація випадкових даних
fake = Faker()

# Генерація груп
groups = [(None, fake.word()) for _ in range(3)]
cursor.executemany('INSERT INTO groups VALUES (?, ?)', groups)

# Генерація викладачів
teachers = [(None, fake.name()) for _ in range(5)]
cursor.executemany('INSERT INTO teachers VALUES (?, ?)', teachers)

# Генерація студентів
students = [(None, fake.name(), random.randint(1, 3)) for _ in range(50)]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

# Генерація предметів
subjects = [(None, fake.word(), random.randint(1, 5)) for _ in range(8)]
cursor.executemany('INSERT INTO subjects VALUES (?, ?, ?)', subjects)

# Генерація оцінок
grades = [(None, random.randint(1, 50), random.randint(1, 8), random.randint(60, 100), fake.date_this_year()) for _ in range(300)]
cursor.executemany('INSERT INTO grades VALUES (?, ?, ?, ?, ?)', grades)

# Збереження змін у базі даних
conn.commit()

# Виконання запитів та вивід результатів
queries = [
    "SELECT students.name, AVG(grades.grade) AS avg_grade FROM students "
    "JOIN grades ON students.id = grades.student_id GROUP BY students.id "
    "ORDER BY avg_grade DESC LIMIT 5",

    # Додайте інші запити тут, відповідно до вимог завдання
]

for i, query in enumerate(queries, start=1):
    filename = f"query_{i}.sql"
    with open(filename, "w") as f:
        f.write(query)

    print(f"Query {i} saved to {filename}")

# Закриття підключення до бази даних
conn.close()
