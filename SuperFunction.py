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

