# Task 3: Method Overriding

class User:
    def greet(self):
        print("Welcome User..")

class student(User):
    def greet(self):
        print("Welcome Student")

class faculty(User):
    def greet(self):
        print("Welcome Faculty")