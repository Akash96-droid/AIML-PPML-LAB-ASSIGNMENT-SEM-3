#1.WAP to triple all numbers in a given list of integers. Use map()
Ans:
x=list(eval(input("Enter a list:")))
def triple(x):
return x*3
y=list(map(triple,x))
print(y)

               #OUTPUT
Enter a list: [1, 2, 3, 4]
[3, 6, 9, 12]

#2.WAP to add three given list using python map and lambda.
Ans:
x=list(eval(input("Enter the 1st list:")))
y=list(eval(input("Enter the 2nd list:")))
z=list(eval(input("Enter the 3rd list:")))
print("Original list:")
print(x)
print(y)
print(z)
l1=list(map(lambda x,y,z:x+y+z,x,y,z))
print("The resulttant list is:",l1)

           #OUTPUT
Enter the 1st list: [1, 2, 3]
Enter the 2nd list: [4, 5, 6]
Enter the 3rd list: [7, 8, 9]
Original list:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
The resulttant list is: [12, 15, 18]

#3..WAP to create a list containing the power of said number in bases raised to the corresponding number in the index using python map.
Ans:
from math import *
x=list(eval(input("Enter the power list:")))
y=list(eval(input("enter the number list:")))
def power(x,y):
z=int(pow(y,x))
return z
l=list(map(power,x,y))
print("The resultant list:",l)

                 #OUTPUT
Enter the power list: [1, 2, 3, 4]
enter the number list: [5, 5, 5, 5]
The resultant list: [5, 25, 125, 625]

#4.WAP to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
Ans:
def swap(y):
if (y.isupper()):
return str(y).lower()
else:
return str(y).upper()
y=list(eval(input("Enter the character list:")))
s=map(swap,y)
print(set(s))

                 #OUTPUT
Enter the character list: ["a", "B", "a", "c", "C"]
{'c', 'A', 'b', 'C'}

#5.WAP to convert a given list of integer and a tuple of integer in a list of string using map().
Ans:
def convert(c):
if c==1:
return "one"
elif c==2:
return "Two"
elif c==3:
return "three"
elif c==4:
return "four"
elif c==5:
return "five"
elif c==6:
return "six"
elif c==7:
return "Seven"
elif c==8:
return "eight"
elif c==9:
return "nine"
else:
return "zero"
l1=list(eval(input("Enter the number list:")))
l2=list(map(convert,l1))
print(l2)
t1=tuple(eval(input("enter the number tuple:")))
t2=list(map(convert,l2))
print(l2)

               #OUTPUT
Enter the number list: [1, 5, 0, 2]
['one', 'five', 'zero', 'Two']
enter the number tuple: (7, 9, 3)
('Seven', 'nine', 'three')

#6.WAP to find the ratio of positive numbers, negative numbers and zeroes in an array of integers using map().
Ans:
x=list(eval(input("Enter the integer array:")))
print("The original list:",x)
pos=list(filter(lambda y:y>0,x))
zero=list(filter(lambda y:y==0,x))
neg=list(filter(lambda y:y<0,x))
n=len(x)
z1=[]
P_ratio=round(len(pos)/n,2)
N_ratio=round(len(neg)/n,2)
Z_ratio=round(len(zero)/n,2)
z1.append(P_ratio)
z1.append(N_ratio)
z1.append(Z_ratio)
def ratio(z1):
return z1
l1=list(map(ratio,z1))
print("The ratio array:",l1)

                #OUTPUT
Enter the integer array: [1, -2, 0, 4, -5, 6]
The original list: [1, -2, 0, 4, -5, 6]
The ratio array: [0.5, 0.33, 0.17]



