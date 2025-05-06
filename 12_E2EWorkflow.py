import pytest
import pandas as pd

# Test if there are any duplicates in the Target csv

def test_checkDuplicates():
    target_df = pd.read_csv('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/TestFiles/12_employee.csv',sep= ",")
    count = target_df.duplicated().sum()
    assert count == 0,"Duplicate records found: Please verify the Target csv"

# Test if Target csv is not empty

def test_checkDataCompleteness():
    target_df = pd.read_csv('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/TestFiles/12_employee.csv',sep= ",")
    assert not target_df.empty, "Target csv is empty"

# Test if DeptName is mandatory column

def test_checkDeptNameForNullValue():
    target_df = pd.read_csv('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/TestFiles/12_employee.csv',
                            sep=",")
    isDeptNameNotNull = target_df['DeptName'].isnull().any()
    assert isDeptNameNotNull == False, "DeptName is having null"

# Test if EmpNo is a Primaru key

def test_checkEmpNoPK():
    target_df = pd.read_csv('E:/Python/MyPython/PycharmProjects/MyLearnings1/ETLQASession/TestFiles/12_employee.csv',sep= ",")
    totalcount = target_df['EmpNo'].count()
    empnouniqcount = len (target_df['EmpNo'].unique())
    assert empnouniqcount == totalcount, "EmpNo is not unique"





