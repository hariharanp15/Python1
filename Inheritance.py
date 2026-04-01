# Task 2: Inheritance (User → Student, Faculty)

class User:
    def register(self):
        print("Register..")

    def login(self):
        print("Login..")

class student(User):
    def student_greet(self):
        print("Hello Student")

class faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

class tempfaculty(faculty):
    def tempfaculty_greet(self):
        print("Hello Temp Faculty")