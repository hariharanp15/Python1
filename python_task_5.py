# Task 1: User Info Manager



users=[]
def create_user(name, age, role):
    user = { "name": name.title(), "Age":age, "Role":role.title()}
    return  user

n=int(input("Enter no of user: "))
for i in range(n):
    name=input("Enter a Name: ")
    age=int(input("Enter a Age: "))
    role=input("Enter a Role: ")
    user=create_user(name,age,role)
    users.append(user)
for i in users:
    print(i)



# Task 2: Dynamic Calculator (*args)



def total(*a):
    sum = 0
    for i in a:
        sum = sum + i
    avg=sum/len(a)
    return sum, avg
print(total(1,2,3,4,5,6,7,8,9,10))



# Task 3: Keyword Config System (**kwargs)



def system_config(**settings):
    for key, val in settings.items():
        print(key,val,sep=":")

system_config(mode="debug", version=1.0)



# Task 4: Factorial Service (Recursion)



def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)

n=int(input("Enter a number: "))
if n==0:
    print("Error because num is 0...")
else:
    print(fact(n))



# Task 5: Memory Optimization (Generator)



def list(n):
    value = []
    for i in range(1,n+1):
        value.append(i*i)
    return value

def generator(n):
    for i in range(1,n+1):
        yield i*i

num = int(input("Enter a number: "))

list= list(num)
print(list)

newvalue = generator(num)
print(newvalue)
for i in newvalue:
    print(i)

print(type(list))
print(type(newvalue))



# Task 6: Exception Handling Module



try:

    num = int(input("Enter Numerator: "))
    den = int(input("Enter Denominator: "))

    r = num/den
    print(r)

except ZeroDivisionError:
    print("Can't divide by 0..")

except ValueError:
    print("Give valid input (Only Numbers)..")

finally:
    print("Program Completed")



# Task 7: File Handling



n=input("About You (1st line): ")

f = open("text_data.txt", "w")
f.write(n + "\n")
f.close()

n=input("About You (2nd line): ")
f = open("text_data.txt", "a")
f.write(n + "\n")
f.close()

f = open("text_data.txt", "r")
print(f.read())
f.close()