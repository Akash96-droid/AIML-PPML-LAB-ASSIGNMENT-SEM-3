#1.WAP to enter a percentage and display the gradation system.
Ans:
x=int(input("enter the percentage:"))
if x>=90:
print("the equivalent grade is 'O'")
elif x>=80 and x<90:
print("the equivalent grade is 'E'")
elif x>=70 and x<80:
print("the equivalent grade is 'A'")
elif x>=60 and x<70:
print("the equivalent grade is 'B'")
elif x>=50 and x<60:
print("the equivalent grade is 'C'")
elif x>=40 and x<50:
print("the equivalent grade is 'D'")
else:
print("the equivalent grade is 'F'")

      #OUTPUT
enter the percentage: 85
the equivalent grade is E

#2.WAP to enter a 5 digit number and print the digits present at odd locations.
Ans:
I=[]
x=int(input("Enter a 5 digit number:"))
while(x!=0):
y=x%10
x=int(x/10)
I.append(y)
print("Numbers at odd postion :")
for i in range(len(I)-1,-1,-2):
print(I[i])

            #OUTPUT
Enter a 5 digit number: 12345
Numbers at odd postion :
1
3
5

#3. WAP to enter a number and check wheather it is a palindrome number or not.
Ans:
x=int(input("enter a number:"))
temp=x
rev=0
while x>0:
y=x%10
rev=rev*10+y
x=x//10
if temp==rev:
print("It is a Palindrome number")
else:
print("It is not a Palindorme number")

             #OUTPUT
enter a number: 121
It is a Palindrome number

#4.WAP to enter a number and check whether the number is perfect number or not.
Ans:
x=int(input("enter a number:"))
s=0
for i in range(1,x):
if(x%i==0):
s=s+i
if(s==x):
print("It is a perfect number")
else:
print("It is not a perfect number")

         #OUTPUT
enter a number: 6
It is a perfect number

#5.WAP to enter a string and print it in reverse also print the no of vowels and consonant in it.
Ans:
x=input("enter a string:")
I=x.split()
I1=[]
i=len(I)-1
while i>=0:
I1.append(I[i])
i=i-1
output=' '.join(I1)
print(output)
vowels=0
consonant=0
for i in x:
if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or
i=='U'):
vowels=vowels+1
else:
consonant=consonant+1
print("The vowels are:",vowels)
print("The consonants are:",consonant

          #OUTPUT
enter a string: Hello World
World Hello
The vowels are: 3
The consonants are: 7

#6.WAP to enter a 3 digit number and print all the prime factors of the number.
Ans:
x=int(input("Enter a 3 digit numbers:"))
c=2
while(x>1):
if(x%c == 0):
print(c,end=" ")
x=x/c
else:
c=c+1

          #OUTPUT
Enter a 3 digit numbers: 100
2 2 5 5 
