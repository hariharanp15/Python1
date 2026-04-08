import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod


app = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hari@1502",
    port=3306,
    database="user_db"
)
cursor = app.cursor()

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class User(AbstractUser):
    def __init__(self, name):
        self.__name = name

    def adduser(self):
        cursor.execute("INSERT INTO users (name) VALUES (%s)", [self.__name])
        app.commit()
        print("\nUser added successfully!")

    def get_details(self):
        return f"User: {self.__name}"


class Expense(User):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id

    def get_details(self):
        return f"Expense User ID: {self.user_id}"

    def addexp(self):
        amt = float(input("Enter Amount: "))
        cat = input("Enter Category: ")
        des = input("Enter Description: ")
        cursor.execute("INSERT INTO expenses (user_id,amount,category,description,date) VALUES (%s,%s,%s,%s,now())",[self.user_id, amt, cat, des])
        app.commit()
        print("\nExpense successfully...!")

    def viewexp(self):
        cursor.execute("SELECT u.name,e.amount,e.category,e.description,e.date FROM users u JOIN expenses e ON u.user_id=e.user_id ORDER BY u.name ASC")
        for i in cursor.fetchall():
            print(i)

    def filterexp(self):
        cursor.execute("SELECT u.name,e.amount,e.category,e.description,e.date FROM users u JOIN expenses e ON u.user_id=e.user_id ORDER BY u.name ASC")
        data = cursor.fetchall()

        x = int(input("Enter 1 for Category Filter 2 for Date Filter: "))

        if x == 1:
            category = input("Enter category: ")
            data = list(filter(lambda x: x[2] == category, data))

        elif x == 2:
            date = input("Enter date (YYYY-MM-DD): ")
            data = [x for x in data if str(x[4]) == date]

        for i in data:
            print(i)

    def total(self):
        cursor.execute("SELECT u.name,e.amount,e.category,e.description,e.date FROM users u JOIN expenses e ON u.user_id=e.user_id ORDER BY u.name ASC")
        data = cursor.fetchall()

        amounts = list(map(lambda x: float(x[1]), data))
        print("All Amounts: ",amounts)

        total = reduce(lambda a, b: a + b, amounts,0)
        print("Total Expenses: ",total)

    def category(self):
        cursor.execute("SELECT u.name,e.amount,e.category,e.description,e.date FROM users u JOIN expenses e ON u.user_id=e.user_id ORDER BY u.name ASC")
        data = cursor.fetchall()

        category = {
        cat: sum([float(x[1]) for x in data if x[2] == cat]) for cat in set(x[2] for x in data)
        }
        print(category)

    def delete(self):
        id = int(input("Enter Expense ID to delete: "))
        cursor.execute("DELETE FROM expenses WHERE exp_id=%s", [id])
        app.commit()
        print("\nExpense Deleted Successfully...!")

    def monthly_report(self):
        cursor.execute("SELECT amount, date FROM expenses WHERE user_id=%s", [self.user_id])
        data = cursor.fetchall()

        report = {}
        for amt, dt in data:
            month = dt.strftime("%Y-%m")
            report[month] = report.get(month, 0) + float(amt)

        print("\nMonthly Report:")
        for k, v in report.items():
            print(f"{k}: {v}")

    def highest_expense(self):
        cursor.execute("SELECT amount, category, date FROM expenses WHERE user_id=%s", [self.user_id])
        data = cursor.fetchall()

        highest = reduce(lambda a, b: a if float(a[0]) > float(b[0]) else b, data)

        print("\nHighest Expense:", highest)

    def smart_insight(self):
        cursor.execute("SELECT amount, category FROM expenses WHERE user_id=%s", [self.user_id])
        data = cursor.fetchall()

        cat_total = {cat: sum(float(x[0]) for x in data if x[1] == cat)for cat in {x[1] for x in data}}

        max_cat = max(cat_total, key=cat_total.get)

        print(f"\nYou are spending too much on {max_cat}!")


while True:
    print("\n0--Exit\n1--Add New User\n2--Add Expense\n3--View Expenses\n4--Filter Expenses\n5--Total Expenses\n6--Category-wise Spending\n7--Delete Note\n8--Monthly Report\n9--Highest Expenses\n10--Smart Insight")

    c = int(input("Enter Choice: "))

    if c == 0:
        break

    elif c == 1:
        name = input("Enter Name: ")
        User(name).adduser()

    elif c == 2:
        id = int(input("Enter User ID: "))
        Expense("temp", id).addexp()

    elif c == 3:
        Expense("temp", 0).viewexp()

    elif c == 4:
        Expense("temp", 0).filterexp()

    elif c == 5:
        Expense("temp", 0).total()

    elif c == 6:
        Expense("temp", 0).category()

    elif c == 7:
        Expense("temp", 0).delete()

    elif c == 8:
        id = int(input("Enter User ID: "))
        Expense("temp", id).monthly_report()

    elif c == 9:
        id = int(input("Enter User ID: "))
        Expense("temp", id).highest_expense()

    elif c == 10:
        id = int(input("Enter User ID: "))
        Expense("temp", id).smart_insight()

    else:
        print("Invalid Choice")