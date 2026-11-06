#1.WAP to input two dictionaries and print the values by merging the two dictionaries.
Ans:
dict1=dict(eval(input("Enter a dictionary values:")))
print(dict1)
dict2=dict(eval(input("Enter a dictionary values:")))
print(dict2)
dict1.update(dict2)
print("After merging the list is:")
print(dict1)

           #OOUTPUT
Enter a dictionary values: {"Apple": 10, "Banana": 20}
{'Apple': 10, 'Banana': 20}
Enter a dictionary values: {"Orange": 30, "Banana": 50}
{'Orange': 30, 'Banana': 50}
After merging the list is:
{'Apple': 10, 'Banana': 50, 'Orange': 30}

#2.WAP to create a dictionary and print the key which has the maximum unique value.
Ans:
d = dict(eval(input("Enter the dictionary: ")))
s = []
s1 = []
for v in d.keys():
s.append(v)
for b in d.values():
s1.append(b)
mv = s1[0]
mk = s[0]
for i in range(1, len(s)):
if s1[i] > mv:
mv = s1[i]
mk = s[i]
print("The key has maximum unique value is:",mk)

        #OUTPUT
Enter the dictionary: {"Maths": 85, "Science": 94, "English": 78}
The key has maximum unique value is: Science

#3.WAP to enter a dictionary and remove the duplicate value inside the dictionary.
Ans:
d=dict(eval(input("Enter the dictionary:")))
temp = []
res = dict()
for key, val in d.items():
if val not in temp:
temp.append(val)
res[key] = val
print(res)

         #OUTPUT
Enter the dictionary: {"A": 10, "B": 20, "C": 10, "D": 30, "E": 20}
{'A': 10, 'B': 20, 'D': 30}

#4.WAP to enter a set and copy the content of the set into a new set one element at a time.
Ans:
s=set(eval(input("Enter a set element:")))
s1=set()
for i in range(1,len(s)+1):
s1.update(s)
print("Updated set is :",s1);

        #OUTPUT
Enter a set element: {10, 20, 30, 20, 10}
Updated set is : {10, 20, 30}

#5.WAP to enter two sets and perform alll the set operations on it.
Ans:
s1=set(eval(input('Enter the 1st set:')))
s2=set(eval(input('Enter the 2nd set:')))
print("Union operation is:",s1.union(s2))
print("Intersection operation is:",s1.intersection(s2))
print("The difference is:",s1.difference(s2))
print("The symmetric_difference is:",s1.symmetric_difference(s2))

              #OUTPUT
Enter the 1st set: {1, 2, 3, 4}
Enter the 2nd set: {3, 4, 5, 6}
Union operation is: {1, 2, 3, 4, 5, 6}
Intersection operation is: {3, 4}
The difference is: {1, 2}
The symmetric_difference is: {1, 2, 5, 6}

#6.WAP to enter two different sets with string elements combine both the sets remove any duplicates are present, print the new set.
Ans:
s2=set(eval(input('Enter the 2nd set:')))
s3=set()
s1.update(s2)
s3=s1
print("After updation the new set is:",s3)

         #OUTPUT
Enter the 1st set: {10, 20, 30}
Enter the 2nd set: {30, 40, 50}
After updation the new set is: {40, 10, 50, 20, 30}
