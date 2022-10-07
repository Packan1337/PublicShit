from faker import Faker
import random
from enum import Enum, auto


# TODO RANDOM STUDENT_ID

# global variables
fake = Faker()
students = []
passwords = {}


# student constructor
class Students:
    def __init__(self, name, mail, student_id, ssn, password):
        self.name = name
        self.student_id = student_id
        self.mail = mail
        self.ssn = ssn
        self.password = password


# function to add a new student and appends student obj. to "students" list.
def add_student():
    new_student = Students(fake.name(),
                           fake.email(),
                           random.randint(1000000, 9999999),
                           fake.ssn(),
                           fake.license_plate())

    students.append(new_student)
    passwords[new_student.name] = new_student.password


# function that prints all students with their associated password.
def show_students_passwords():
    print("")
    for student, password in passwords.items():
        print(f"{student}: {password}")


def remove_student(student_index):
    print(f"\nRemoved {student_index.name}")
    del passwords[student_index.name]
    students.remove(student_index)


# def student_ssn_validation(student_index):
    # if student_index.ssn


# function that prints students list.
def show_all_students():
    for people in students:
        print(f"""
Name: {people.name}
E-mail: {people.mail}
StudentID: {people.student_id}
SSN: {people.ssn}
Password: {people.password}""")

    print(f"\n{len(students)} Students.")


# generates 5 student obj.
for _ in range(5):
    add_student()

show_all_students()




