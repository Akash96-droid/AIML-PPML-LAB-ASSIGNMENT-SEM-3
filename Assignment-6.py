#1..WAP to print a matrix containing group of similar elements by giving the input randomly in another matrix.
Ans:
from collections import Counter
test_list=[1,3,5,1,3,2,5,4,2,1]
print("The original lis:"+str(test_list))
temp=Counter(test_list)
res=[[key]*val for key,val in temp.items()]
print("Matrix after grouping:"+str(res))

           #OUTPUT
The original lis:[1, 3, 5, 1, 3, 2, 5, 4, 2, 1]
Matrix after grouping:[[1, 1, 1], [3, 3], [5, 5], [2, 2], [4]]

#2.WAP to print a matrix along with a sumation of row elements and column elements after entering a 3*3 matrix.
Ans:
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, " "]]
rows = len(a)
cols = len(a[0])
for i in range(0, rows):
sumRow = 0
for j in range(0, cols):
sumRow = sumRow + a[i][j]
b[i][j] = a[i][j]
b[i][cols] = sumRow
for i in range(0, cols):
sumCol = 0
for j in range(0, rows):
sumCol = sumCol + a[j][i]
b[rows][i] = sumCol
for i in range(0,rows+1):
for j in range(0,cols+1):
print(b[i][j],"\t",end=" ")
print()

             #OUTPUT
1 	 2 	 3 	 6 	 
4 	 5 	 6 	 15 	 
7 	 8 	 9 	 24 	 
12 	 15 	 18 	 45 	 

#3.WAP to print the transpose of a matrix of n*n order.
Ans:
Rows=int(input("Give the number of rows:"))
Columns=int(input("Give the number of columns:"))
matrix=[[int(input()) for c in range(Columns)] for r in range(Rows)]
print(Rows)
print("Original Matrix")
for i in range(0,Rows):
for j in range(0,Columns):
print(matrix[i][j],"\t",end=" ")
print()
print("Matrix after transpose")
for i in range(0,Rows):
for j in range(0,Columns):
print(matrix[j][i],"\t",end="")
print()

            #OUTPUT
Give the number of rows: 2
Give the number of columns: 3
Enter element for row 0, col 0: 1
Enter element for row 0, col 1: 2
Enter element for row 0, col 2: 3
Enter element for row 1, col 0: 4
Enter element for row 1, col 1: 5
Enter element for row 1, col 2: 6

Number of rows: 2
Original Matrix:
1 	 2 	 3 	 
4 	 5 	 6 	 

Matrix after transpose:
1 	4 	
2 	5 	
3 	6 	

#4.WAP to check if a value is present in the list or not, using lambda function.
Ans:
x=list(eval(input("Enter the list:")))
y=int(input("enter the element you want to search:"))
z = lambda x: (x == y)
found = False
for e in x:
if z(e):
found = True
break
if found:
print(y, "is present in the list.")
else:
print(y, "is not present in the list.")

            #OUTPUT
Enter the list: [10, 20, 30, 40, 50]
enter the element you want to search: 30
30 is present in the list.

#5.WAP to print Fibonacci series up to n terms using lambda function.
Ans:
n = int(input("Enter the number of terms: "))
Fibonacci = lambda n: [0] if n == 1 else [0, 1] if n == 2 else Fibonacci(n-1) + [Fibonacci(n1)[-1] + Fibonacci(n-2)[-1]]
print("Fibonacciseries:")
for i in range(n):
print(fibonacci(i+1)[-1], end=" ")

                #OUTPUT
Enter the number of terms: 6
Fibonacciseries:
0 1 1 2 3 5 

#6.WAP to print the intersection of 2 arrays using lambda function.
Ans:
array1=list(eval(input("Enter the 1st list:")))
array2=list(eval(input("Enter the 2nd list:")))
intersection = list(filter(lambda x: x in array1, array2))
print("Intersection of array1 & array2 is: ", intersection)

          #OUTPUT
Enter the 1st list: [1, 2, 3, 4, 5]
Enter the 2nd list: [3, 4, 5, 6, 7]
Intersection of array1 & array2 is:  [3, 4, 5]
