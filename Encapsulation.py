# Task 1: Encapsulation (User Class)

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