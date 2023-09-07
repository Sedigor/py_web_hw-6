import sqlite3
import faker
import random


fake = faker.Faker()

NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 10
subjects = ['Mathematics', 'Literature', 'History', 'Geography', 'Physics']


def insert_data_to_db(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS, subjects) -> None:
    
    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()

        groups = [(None, 'group_' + str(i + 1)) for i in range(NUMBER_GROUPS)]
        cursor.executemany('INSERT INTO groups VALUES (?, ?)', groups)

        teachers = [(None, fake.name()) for _ in range(NUMBER_TEACHERS)]
        cursor.executemany('INSERT INTO teachers VALUES (?, ?)', teachers)

        subjects = [(None, subject, random.randint(1, 5)) for subject in subjects]
        cursor.executemany('INSERT INTO subjects VALUES (?, ?, ?)', subjects)
        
        students = [(None, fake.name(), random.randint(1, 3)) for _ in range(NUMBER_STUDENTS)]
        cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

        total = NUMBER_GRADES * NUMBER_SUBJECTS * NUMBER_STUDENTS
        grades = [(None, random.randint(1, 40), random.randint(1, 5), random.randint(60, 100), fake.date_this_year()) for _ in range(total)]
        cursor.executemany('INSERT INTO grades VALUES (?, ?, ?, ?, ?)', grades)


if __name__ == "__main__":
    insert_data_to_db(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS, subjects)