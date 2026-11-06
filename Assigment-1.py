#1.WAP to enter two integer from the keyboard and perform all the arithmeticoperations on them.
Ans:
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
print("Addition is :", x+y)
print("Subtraction is :",x-y)
print("Multiplication is :",x*y)
print("Division is :",x/y)
print("Reminder is :", x%y)
print("Floor value is :",x//y)

    #OUTPUT
enter the value of x:15
enter the value of y:10
addition is: 25
substraction is: 5
Multiplication is: 150
division is : 1.5
reminder is: 5
floor value is: 1

#2.WAP to enter three sides of a tringle. Find out the area of the tringle.
Ans:
import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
s=float((a+b+c)/2)
z=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of tringle is :",z)

    #OUTPUT
enter the value of a:6
enter the value of b:8
enter the value of c:10
area of tringle is: 24.0

#3.WAP to enter an integer number and find out its binary, octal and hexadecimal equivalents.
Ans:
x=int(input("enter a number:"))
print(x)
print("binary equivalent is :",bin(x))
print("octal equivalent is :",oct(x))
print("hexadecimal equivalent is :",hex(x))

         #OUTPUT
enter a number:7
7
binary equivalent is: O0b111
octal equivalent is: 007
hexadecimal equivalent is: 0x7

#4.WAP to enter the coefficients of a quadratic equation and findout the roots of the equivalent
Ans:
import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=math.sqrt(b*b)-(4*c*a)
x=(-b+d)/(2*a)
y=(-b-d)/(2*a)
print("the roots are:",x,"&",y)

        #OUTPUT
enter the value of a:6
enter the value of b:5 
enter the value of c:7
the roots are: -14.0 & 13.17

#5.WAP to enter a temperature in farenheite and convert it into celsiuss.
Ans:
F=float(input("enter the temp. in farenheite:"))
C= ((F-32)*5)/9
print("The value of farenheite in celsius is :",C)

           #OUTPUT
enter the temp. in farenheite:98.6
The value of farenheite in celsius is: 37.0

#6.WAP to convert distance in meters to Kilometers.
Ans:
x=int(input("Enter the distance in meter:"))
y=int(x/1000)
z=int(x%1000)
print(y,"kilometer",z,"meter") 

          #OUTPUT
Enter the distance in meter: 2536
2 kilometer 536 meter

#7. WAP to enter time in minutes and print it in hour and minute format.
Ans:
x=int(input("enter the time:"))
h=int(x/60)
m=x%60
print(h,"hour",m,"minute")

          #OUTPUT
enter the time in minutes: 2436
40 hour 36 minute

#8.WAP to enter two numbers nd swap them using bitwise operators.
Ans:
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
a=a^b
b=a^b
a=a^b
print("after convesion the value of a:",a)
print("after convesion the value of b:",b)

         #OUTPUT
enter the value of a:15
enter the value of b:12
after convesion the value of a: 12
after convesion the value of b: 15
