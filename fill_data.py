from datetime import datetime
import faker
import sqlite3
import random


fake = faker.Faker()

NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 15


def insert_data_to_db(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS) -> None:
    
    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()

        groups = [(None, 'UG_' + str(i + 1)) for i in range(NUMBER_GROUPS)]
        cursor.executemany('INSERT INTO groups VALUES (?, ?)', groups)

        teachers = [(None, fake.name()) for _ in range(NUMBER_TEACHERS)]
        cursor.executemany('INSERT INTO teachers VALUES (?, ?)', teachers)

        students = [(None, fake.name(), random.randint(1, 3)) for _ in range(NUMBER_STUDENTS)]
        cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

        subjects = ['Mathematics', 'Literature', 'History', 'Geography', 'Physics', 'Chemistry', 'Biology', 'English']
        cursor.executemany('INSERT INTO subjects VALUES (?, ?, ?)', subjects)

        grades = [(None, random.randint(1, 50), random.randint(1, 8), random.randint(60, 100), fake.date_this_year()) for _ in range(300)]
        cursor.executemany('INSERT INTO grades VALUES (?, ?, ?, ?, ?)', grades)


if __name__ == "__main__":
    insert_data_to_db(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS)