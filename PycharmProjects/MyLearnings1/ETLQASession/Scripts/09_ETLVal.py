# Sample test suite to check count, duplicates, unique
# other way to run scripts is in POwershell.. type python nameofscript then tab
import pandas as pd
source = pd.read_excel('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/TestFiles/09_employee.xlsx')
print("Test Case 1: Following are the column names in the Source file : \n ")
print(source.columns)
print("\n")

print("Test Case 2: Rows ** Columns in the Source file : \n ")
print(source.shape)
print("\n")

print("Test Case 3: No. of rows under each column of Source  : \n ")
print(source.count())
print("\n")

print("Test Case 4: Duplicate records in the source : \n ")
print(source.duplicated().sum())
print("\n")

print("Test Case 5: Duplicate records saved in the below file : \n ")
dupes = source[source.duplicated()].to_csv('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/OutputFiles/09_duplicate.csv')
print("Path is : E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/OutputFiles/09_duplicate.csv")
print("\n")

print("Test Case 6: Check if NULL value exists in te column DeptName : \n ")
print(source[source['DeptName'].isnull()])
print("\n")

print("Test Case 6A: Check if NULL value exists in te column Salary : \n ")
print(source[source['Salary'].isnull()])
print("\n")

print("Test Case 7: Unique values of the column EmpName in the source : \n ")
print(source['EmpName'].unique())
print("\n")

print("Test Case 8: Unique values of the column EmpNo in the Source file : \n ")
print(source['EmpNo'].unique())
print("\n")

print("Test Case 9: Unique values of the column DeptName in the Source file : \n ")
print(source['DeptName'].unique())
print("\n")

print("Test Case 9: Unique values of the column DeptName in the Source file : \n ")
print(source['DeptName'].unique())
print("\n")

print("Test Case 10: Unique values of the column Salary in the Source file : \n ")
print(source['Salary'].unique())
print("\n")

print("Test Case 11: Sample (Top 3) records in the Source file : \n ")
print(source.head(3))
print("\n")

print("Test Case 12: Sample (Bottom 3) records in the Source file : \n ")
print(source.tail(3))
print("\n")

print("TEST COMPLETED")


