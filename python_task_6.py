# Task 1: Encapsulation (User Class)

'''
class User:
    user_name:None
    pwd:None

    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd

    def register(self):
        print("Registering user: "+self.user_name)

    def login(self):
        print("Logging in: "+self.user_name)
'''


from Encapsulation import User

user1= User("Hari",12345)
 
user1.register()
user1.login()


# Task 2: Inheritance (User → Student, Faculty)

'''
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
'''

from Inheritance import User,student,faculty,tempfaculty

student1=student()

student1.student_greet()


faculty1=faculty()

faculty1.faculty_greet()

student1.register()
faculty1.login()

user1=User()

tempfaculty1=tempfaculty()
tempfaculty1.tempfaculty_greet()


# Task 3: Method Overriding

'''
class User:
    def greet(self):
        print("Welcome User..")

class student(User):
    def greet(self):
        print("Welcome Student")

class faculty(User):
    def greet(self):
        print("Welcome Faculty")
'''

from MethodOverRiding import User,student,faculty

student1=student()
student1.greet()

faculty1=faculty()
faculty1.greet() 


# Task 4: Method Chaining

'''
class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self
    
    def greet(self):
        print("enjoy everyone")
        return self
'''

from MethodChaining import User

user1= User()

user1.login().greet().register()


# Task 5: Combined Task (Real-Time)
# Mini User System

'''
class User:
    c=0
    user_name:None
    pwd:None

    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd
        User.c+=1

    def register(self):
        print("Registering user: "+self.user_name)
        return self

    def login(self):
        print("Logging in: "+self.user_name)
        return self

    def greet(self):
        print("Welcome User")
        return self

class student(User):
    def greet(self):
        print("Hello Student")
        return self

class faculty(User):
    def greet(self):
        print("Hello Faculty")       
        return self
'''

from MiniUserSystem import User,student,faculty

user1= student("Hari",12345)
user2= faculty("Siva",67890)

user1.login().greet().register()

user2.login().greet().register()

print("Count: ",User.c)
