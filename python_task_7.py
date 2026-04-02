
'''
# Abstract Files

from abc import ABC, abstractmethod

class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass


class User(AbstractUser):                              

    name = None
    id      = None

    def __init__(self,name,id):
        self.name = name
        self.id   = id

    def register(self) :
        print("register...")

    def login(self) :
        print("login")

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def student_greet(self) :
        print("hi student "+ self.name+" from Dept "+ self.dept)

    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User) :
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def faculty_greet(self) :
        print("hi faculty", self.salary)

    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"


class TempFaculty(Faculty) :
   def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

   def tempfaculty_greet(self):
        print("hi tempfaculty"+ self.duration)
'''

# Task 1: Use super() properly

from SuperFunction import User,Student,Faculty,TempFaculty


student1 = Student("Hari", 1, "CSE", 12000)
student1.student_greet()


faculty1 = Faculty("Siva", 1, 150000)
faculty1.faculty_greet()

TempFac1 = TempFaculty("Raja", 2, 120000, "9Hrs")
TempFac1.tempfaculty_greet()

#Task 2: Apply Abstraction

students = [
    Student("Hari", 1, "CSE", 50000),
    Student("Ilan", 2, "AI", 48000)
]

for s in students:
    print(s.get_details())

#  Task 3: Sorting using key

students=[Student("Hari", 1, "CSE", 50500),Student("Ilan", 2, "AI", 49450),Student("Rithivk", 3, "IT", 52520),Student("Muthu", 4, "CSE", 36020)]
students.sort(key=lambda x: x.fees)
for i in students:
    print(i.name, i.fees)

facultys=[Faculty("Siva", 1, 20110),Faculty("Lakshman", 2, 34600),Faculty("Suba", 3, 29460),Faculty("Raja", 1, 32500)]
facultys.sort(key=lambda x: x.salary)
for i in facultys:
    print(i.name, i.salary)

# Task 4: Use map()

names = list(map(lambda s: s.name, students))
print(names)

# Task 5: Use filter()

high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
for i in high_fee_students:
    print(i.name)

high_salary_faculty = list(filter(lambda s: int(s.salary) > 30000, facultys))
for i in high_salary_faculty:
    print(i.name)

# Task 6: Use reduce()

from functools import reduce
total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
print("Total Fees:",total_fees)


total_salary = reduce(lambda acc, s: acc + int(s.salary), facultys, 0)
print("Total Salary:",total_salary)

#Task 7: Higher Order Function

def process_users(users, func):
    return list(map(func, users))

names = process_users(students, lambda s: s.name)
print("Student Names:", names)

fees = process_users(students, lambda s: s.fees)
print("Student Fees:", fees)

# Final Challenge 

# All details (get_details())
list(map(lambda s: print(s.get_details()), students))

list(map(lambda f: print(f.get_details()), facultys))

#Sorted data
students.sort(key=lambda x: x.name)
print("Students Name:")
for i in students:
    print(i.name)

facultys.sort(key=lambda x: x.name)
print("Faculties Names:")
for i in facultys:
    print(i.name)

#Filtered data
high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
for i in high_fee_students:
    print(i.name,i.fees)

high_salary_faculty = list(filter(lambda s: int(s.salary) > 30000, facultys))
for i in high_salary_faculty:
    print(i.name,i.salary)

#Total fees & salary
total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
print("Total Fees:",total_fees)


total_salary = reduce(lambda acc, s: acc + int(s.salary), facultys, 0)
print("Total Salary:",total_salary)

#3 functional programming
def total_filtered(user, func, value):
    return reduce(lambda acc, x: acc + x,map(value, filter(func, user)),0)
print(total_filtered(students, lambda s: s.fees > 50000, lambda s: s.fees))
