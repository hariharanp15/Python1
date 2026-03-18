# Section 1: loop Basic

# 1.

for i in range(1,51):
    print(i)

# 2.

for i in range(1,101):
    if i%2==0:
        print(i)

# 3.

for i in range(1,101):
    if i%2==1:
        print(i)

# 4.

for i in range(1,11):
    a=7*i
    print(a)

# 5.

a=0
for i in range(1,101):
    a+=i
print(a)

# 6.

for i in range(50, 0, -1):
    print(i)

# 7.

c=0
for i in range(1, 101):
    if i%3==0:
        c+=1
print(c)

# 8.

for i in range(1,11):
    i=i*i
    print(i)

# 9.

for i in range(1,11):
    i=i*i*i
    print(i)

# 10.

n=int(input("Enter N value: "))
for i in range(1,n+1):
    print(i)

# Section 2: While Loop

# 11.

i=0
while i<20:
    i+=1
    print(i)

# 12.

n=int(input("Enter n number: "))
i=1
f=1
while i<=n:
    f=f*i
    i=i+1
print(f)

# 13. 

n=int(input("Enter a Num: "))
r=0
while n>0:
    r=r*10 + n%10
    n=n//10
print(r)

# 14.

n=int(input("Enter a number: "))
d=0
while n>0:
    n=n//10
    d+=1
print(d)

# 15.

lst=[]
while True:
    n=input("Enter input: ")
    if n=="stop":
        break
    lst.append(n)
print(lst)

# Section 3: Nested Loop

# 16.

for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()

# 17.

for i in range(1,6):
    for j in range(1,i):
        print(j, end="")
    print()

# 18.

for i in range(1, 6):
    for j in range(1, 11):
        print(i*j)
    print()

# 19.

for i in range(3):
    for j in range(3):
        if j==0:
            print("A", end=" ")
        if j==1:
            print("B", end=" ")
        if j==2:
            print("C", end=" ")
    print()

# 20.

n=0
for i in range(3):
    for j in range(3):
        n+=1
        print(n, end=" ")
    print()

# Section 4: String Basics

# 21. 

n=input("Enter String: ")
print(len(n))

# 22.

n=input("Enter String: ")
c=0
for i in n:
    if i in "aeiouAEIOU":
        c+=1
print(c)

# 23.

n=input("Enter String: ")
c=0
for i in n:
    if i not in "aeiouAEIOU":
        c+=1
print(c)

#24.

s=input("Enter a String: ")
rev=""
for i in s:
    rev=i+rev
print(rev)

# 25.

s=input("Enter a String: ")
rev=""
for i in s:
    rev=i+rev
if(s==rev):
    print("Palindrome")
else:
    print(" Not a Palindrome")

# Section 5: String Slicing

str=input("Enter a String: ")

# 26.

print(str[:5])

# 27.

print(str[-3:])

# 28.

print(str[ : :-1])

# 29.

print(str[ : :2])

# 30.

print(str[1:-1])

# Section 6: List Basics

# 31.

n=[10,20,30,40,50]
sum=0
for i in n:
    sum=sum+i
print(sum)

# 32.
print(max(n))

# 33.
print(min(n))

# 34.

c=0
for i in n:
    c+=1
print(c)

# 35.

x=int(input("Enter element: "))
if x in n:
    print("Exist")
else:
    print("Not Exist")

# Section 7: List Operation

# 36.

fruits=[]
fruits.append("Apple")
fruits.append("Mango")
fruits.append("Orange")
fruits.append("Banana")
print(fruits)

# 37.

fruits.insert(1,"Pineapple")
print(fruits)

# 38.

fruits.remove("Mango")
print(fruits)

# 39.

print(fruits[::-1])

# 40.

for i in range(len(fruits)):
    for j in range(i + 1, len(fruits)):
        if fruits[i] > fruits[j]:
            fruits[i], fruits[j] = fruits[j], fruits[i]
print(fruits)