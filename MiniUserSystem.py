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