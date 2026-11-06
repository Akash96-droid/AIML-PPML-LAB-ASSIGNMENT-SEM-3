#1.WAP to print twin prime numbers between 1 to N.
Ans:
N=int(input("Enter a number:"))
for i in range(2,N):
d=0
for j in range(1,i+1):
if i%j==0:
d=d+1
if d==2:
d=0
N=i+2
for j in range(1,N+1):
if N%j==0:
d=d+1
if d==2:
print("(%d,%d)"%(i,N))

           #OUTPUT
Enter a number: 20
(3,5)
(5,7)
(11,13)
(17,19)

#2.WAP to find the factorial of a number.
Ans:
x=int(input("Enter a number:"))
factorial=1
if x<0:
print("It is a negative number")
elif x==0:
print("The factorial of ",x,"is :",factorial)
else:
for i in range(1,x+1):
factorial=factorial*i
print("The factorial of",x,"is:",factorial)

         #OUTPUT
Enter a number: 5
The factorial of 5 is: 120

#3.WAP to check the leap year.
Ans:
x=int(input("Enter a year:"))
if(x%4 == 0) and (x%100 != 0) or (x%400==0):
print(x,"is a leap year")
else:
print(x,"is not a leap year")

          #OUTPUT
Enter a year: 2024
2024 is a leap year

#4.WAP to check whether the string is symmetrical or palindrome.
Ans:
x=input("enter a string:")
z=(str(str(x)[::-1]))
if x == z:
print("it is a palindrome")
else:
print("it is not a palindrome")

           #OUTPUT
enter a string: racecar
it is a palindrome

#5.WAP to print even length words in a string.
Ans:
x=input("Enter a String:")
y= ""
for c in x:
if c != " ":
y=y+c
else:
if len(y) % 2 == 0:
print(y)
y = ""
if len(y) % 2 == 0:
print(y)

         #OUTPUT
Enter a String: Python is easy
Python
is

#6.WAP to remove all duplicates from a given string.
Ans:
x=input("Enter a string:")
result = ""
for char in x:
if char not in result:
result=result+char
print(result)

              #OUTPUT
Enter a string: programming
progamin

