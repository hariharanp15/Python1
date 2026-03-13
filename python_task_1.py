#Task 1 - Print Formatting

print("Hello World", end=" ")
print("Welcome Python")
print("Laptop","Mouse","Keyboard", sep="|")

#Task 2 - Variables

name="Ravi"
age=22
city="Chennai"
print(name,age,city, sep="-")

#Task 3 - Multiple Assingment

name,age,student="Meena",20,True
print(name,age,student, end="\n")

#Task 4 Indexing

word="Python"
print(word[0])
print(word[2])
print(word[-1])

#Task 5 - Arithmetic Operators

a=25+10
b=50-20
c=8*5
d=100/10
e=10%3
f=2**4
g=20//3
print(a,b,c,d,e,f,g)

#Task 6 - BODMAS Expression

print(3 + 2 * 5 ** 2)

#Task 7 - Assingment Operator

num = 50
num += 25
print(num)
num = 100
num /= 10
print(num)

#Task 8 - Comparision Operator

print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

#Task 9 - String Comparision

a = "apple"
b = "Apple"
print(a == b)
#Task 10 - Logical Operator

print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

#Task 11 - Membership Operator

numbers=[10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

#Task 12 - Swapping

a=10
b=20
print("Before Swap= ", a,b)
a,b=b,a
print("After Swap= ", a,b)

#Task 13 - Bitwisw XOR

a=6
b=3
print(a^b)