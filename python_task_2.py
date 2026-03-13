#Bitwise Operator

# 1.

a=10
b=6
print(a&b)

# 2.

x=12
y=5
print(x|y)

# 3.

num=8
print(~num)

# 4.

a=15
b=9
print(a^b)

# 5.

num=7
n=num<<2
print(n)

# 6.

num=20
n=num>>1
print(n)

# 7.

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(num1 & num2)

# 8.

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(num1 ^ num2)

#String Task
 
# 9.

str="hi"
val=str*4
print(val)

# 10.

str0="python"
print(str0*3)

# 11.

str1="super"
str2="man"
print(str1+str2)

# 12.

str1="hello"
str2="world"
print(str1+" "+str2)

# 13.

string=input("Enter a String:")
print(string*5)

# 14.

string1=input("Enter a String1:")
string2=input("Enter a String2:")
print(string1+" "+string2)

#Input & Type Casting Task

# 15.

name=input("Enter a Name:")
print(type(name))

# 16.

age=int(input("Enter a Age:"))
print(type(age))

# 17.

num1=int(input("Enter a num1:"))
num2=int(input("Enter a num2:"))
print("Sum= ",num1+num2)

# 18.

mark1=int(input("Enter a mark1:"))
mark2=int(input("Enter a mark2:"))
m=mark1+mark2
print("Avg= ",m/2)

# 19.

a=int(input("Enter a n1:"))
b=int(input("Enter a n2:"))
print(3*a*2 + b - 2)

# 20.

number=input("Enter a number: ")
print(type(number))
num=int(number)
print(type(num))

# Unit Digit Task

# 21.

number=input("Enter a number: ")
print(number[-1])

# 22.

num=int(input("Enter a number: "))
print(num%10)

# 23.

num=int(input("Enter a number: "))
num //= 10
print(num)

# 24.

num=int(input("Enter a number: "))
num //= 10
print(num%10)

# 25.

num=int(input("Enter a number: "))
print(num%10)

# If Statement Task

# 26.

if(10>=5):
    print("Greater")

# 27.

number=int(input("Enter a number: "))
if(number>50):
    print("Greater than 50")
else:
    print("Smaller than 50")

# 28.

age=int(input("Enter a Age: "))
if(age>=18):
    print("Above 18")
else:
    print("Below 18")

# 29.

number=int(input("Enter a number: "))
if(number>100):
    print("Greater than 100")
else:
    print("Smaller than 100")

# 30.

number=int(input("Enter a number: "))
if(number>=0):
    print("Greater than 0")
else:
    print("Smaller than 0")

# If Else Task

# 31. 

n=int(input("Enter a number: "))
if(n%2==0):
    print("number is even")
else:
    print("number is odd")

# 32.

mark=int(input("Enter a Mark: "))
if(mark>=35):
    print("Pass")
else:
    print("Fail")

# 33.

num=int(input("Enter a Mark: "))
if(num>=0):
    print("Postive")
else:
    print("negative")

# 34.

number=int(input("Enter a number: "))
if(number>10):
    print("Greater than 10")
elif(number==10):
    print("Equals to 10")
else:
    print("Smaller than 10")

# Nested If Task

# 35. 

age=int(input("Enter a Age: "))
height=int(input("Enter a Height: "))
weight=int(input("Enter a Weight: "))
if(age>=18):
    if(height>=160):
        if(weight>=60):
            print("Eligible")
        else:
            print("Less weight")
    else:
        print("Less height")
else:
    print("Less age")    

# 36.

mark=int(input("Enter a Mark: "))
age=int(input("Enter a Age: "))
if(mark>=60):
    if(age>=17):
        print("Eligible")
    else:
        print("Less age")
else:
    print("Less mark")      

# 37.

age=int(input("Enter a Age: "))
height=int(input("Enter a Height: "))
weight=int(input("Enter a Weight: "))
if(age>=16):
    if(height>=150):
        if(weight>=50):
            print("Eligible")
        else:
            print("Less weight")
    else:
        print("Less height")
else:
    print("Less age")    

# Match Statement Task

# 38.

day=int(input("Enter a day number 1-7: "))
match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")

# 39.

colour=int(input("Enter a day number 1-3: "))
match colour:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

# 40.

fruit=int(input("Enter a day number 1-4: "))
match fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
