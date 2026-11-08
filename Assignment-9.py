#1.WAP to create and work with a Pandas Series.
Ans:
import pandas as pd
# Create a Series
data = [10, 20, 30]
labels = ['a', 'b', 'c']
series = pd.Series(data, index=labels)
print("Pandas Series:")
print(series)
# Access data using label
print("Value at label 'b':", series['b'])

             #OUTPUT
Pandas Series:
a    10
b    20
c    30
dtype: int64
Value at label 'b': 20

#2.WAP to create and manipulate a data frame.
# Create a DataFrame
data = {
 'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 35],
 'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Access a column
print("\nAge column:")
print(df['Age'])
# Access a row
print("\nRow at index 1:")
print(df.iloc[1])


                #OUTPUT
DataFrame:
      Name  Age           City
0    Alice   25       New York
1      Bob   30  San Francisco
2  Charlie   35    Los Angeles

Age column:
0    25
1    30
2    35
Name: Age, dtype: int64

Row at index 1:
Name              Bob
Age                30
City    San Francisco
Name: 1, dtype: object

#3.WAP to to read CSV and JSON files.
Ans:
# Reading a CSV file
df_csv = pd.read_csv('sample.csv') # Replace 'sample.csv' with your file path
print("DataFrame from CSV:")
print(df_csv)
# Reading a JSON file
df_json = pd.read_json('sample.json') # Replace 'sample.json' with your file path
print("\nDataFrame from JSON:")
print(df_json)

                   #OUTPUT
DataFrame from CSV:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago

DataFrame from JSON:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago

#4.WAP to calculate the correlation between columns in a data frame.
Ans:
# Create a DataFrame with numerical data
data = {
 'Math': [90, 85, 80, 95],
 'Science': [88, 82, 85, 90],
 'English': [78, 75, 80, 85]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Calculate correlation
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

                #OUTPUT
DataFrame:
   Math  Science  English
0    90       88       78
1    85       82       75
2    80       85       80
3    95       90       85

Correlation Matrix:
             Math   Science   English
Math     1.000000  0.774597  0.552866
Science  0.774597  1.000000  0.827040
English  0.552866  0.827040  1.000000
