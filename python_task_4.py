# Mini Project 1: Employee Management System

employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("Employee added successfully\n")

def update_employee():
    name = input("Enter employee name to update: ")

    for emp in employees:
        if emp["name"] == name:
            emp["age"] = int(input("Enter new age: "))
            emp["role"] = input("Enter new role: ")
            emp["salary"] = float(input("Enter new salary: "))
            print("Employee updated\n")
            return

    print("Employee not found\n")


def delete_employee():
    name = input("Enter employee name to delete: ")

    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Employee deleted\n")
            return

    print("Employee not found\n")


def display_employees():
    for emp in employees:
        print(emp)
    print()

while True:
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")

# Mini Project 2: Student Report Card

name = input("Enter name: ")
m1= int(input("Mark 1: "))
m2= int(input("Mark 2: "))
m3= int(input("Mark 3: "))


total = m1+m2+m3
avg = total / 3

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "Fail"
student = {"name":name,"total":total,"avg":avg,"grade":grade }
print(student)


# Mini Project 3: Shopping Cart System

cart = {}

def add_item():
    name = input("Product name: ")
    price = int(input("Price: "))
    qty = int(input("Quantity: "))
    cart[name] = {"price": price, "qty": qty}

def delete_item():
    name = input("Enter product to delete: ")
    if name in cart:
        del cart[name]

def show_cart():
    for k in cart:
        print(k, cart[k])

def total_bill():
    total = 0
    for k in cart:
        total += cart[k]["price"] * cart[k]["qty"]
    print("Total:", total)

while True:
    print("1.Add 2.Delete 3.Show 4.Total 5.Exit")
    ch = input()

    if ch == "1":
        add_item()
    elif ch == "2":
        delete_item()
    elif ch == "3":
        show_cart()
    elif ch == "4":
        total_bill()
    elif ch == "5":
        break

# Mini Project 4: Login & User Validation

users = {
    "hari": "1234",
    "raja": "abcd",
    "siva": "pass"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username] == password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("User not found")


# Mini Project 5: Unique Visitor Counter

visitors = set()

while True:
    name = input("Enter visitor name (or 'exit'): ")

    if name == "exit":
        break

    visitors.add(name)

print("\nUnique Visitors:", visitors)
print("Total Unique Visitors:", len(visitors))

# Mini Project 6: String Formatter Tool

name= input("Enter name: ")
product1= input("Enter Product name1: ")
product2= input("Enter Product name2: ")

print(name+" bought "+ product1 + " and " + product2)

text="{0} bought {2} and {1}"
print(text.format(name,product1,product2))


print("***{var:<20}***".format(var="HI"))
print("***{var:>20}***".format(var="HI"))
print("***{var:^10}***".format(var="HELLO"))
print("***{var:^10}***".format(var="WELCOME"))
print("***{var:^10}***".format(var="TO"))
print("***{var:^10}***".format(var="PYTHON"))


# Mini Project 7: Bank Account System

account = {}

def create():
    account["name"] = input("Name: ")
    account["balance"] = float(input("Balance: "))

def deposit():
    amt = float(input("Deposit: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Withdraw: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("No balance")

def balance():
    print(account)

while True:
    print("1.Create 2.Deposit 3.Withdraw 4.balance 5.Exit")
    ch = input()

    if ch == "1":
        create()
    elif ch == "2":
        deposit()
    elif ch == "3":
        withdraw()
    elif ch == "4":
        balance()
    elif ch == "5":
        break

# Mini Project 8: Voting System

votes = {
    "hari": 0,
    "siva": 0,
    "raja": 0
}

while True:
    print("Vote for hari / siva / raja (or type 'exit')")
    choice = input("Enter vote: ")

    if choice == "exit":
        break

    if choice in votes:
        votes[choice] += 1
    else:
        print("Invalid candidate")

winner = max(votes, key=votes.get)
print("Winner:", winner)

# Mini Project 9: Course Enrollment System

students = []

def add_student():
    name = input("Enter name: ")
    courses = input("Enter courses: ")
    students.append({"name": name, "courses": courses})


def update_student():
    name = input("Enter name to update: ")
    for s in students:
        if s["name"] == name:
            s["courses"] = input("Enter new courses: ")

def display():
    for s in students:
        print("Name:", s["name"])
        print("Courses:", s["courses"])
        print()

while True:
    print("1.Add 2.Update 3.Display 4.Exit")
    ch = input()

    if ch == "1":
        add_student()
    elif ch == "2":
        update_student()
    elif ch == "3":
        display()
    elif ch == "4":
        break
    
    # Mini Project 10: Number Utility Tool

number = int(input("Enter a number: "))
print(" Binary value: {:b}".format(number))
print(" Octal value: {:o}".format(number))
print(" Hexa value: {:x}".format(number))
print(" Scientific value: {:e}".format(number))

number = 10240253
print("Number {:,}".format(number))