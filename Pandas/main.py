"""
Pandas Series
A Series is a one-dimensional labeled array capable of holding any data type.
The axis labels are collectively called the index.
"""

import numpy as np
import pandas as pd

# ========== Creating Series - Different Methods ==========

# Prepare sample data
labels = ['a', 'b', 'c']           # Custom index labels
my_list = [10, 20, 30]             # Python list
arr = np.array([10, 20, 30])       # NumPy array
d = {'a': 10, 'b': 20, 'c': 30}    # Dictionary

# Method 1: Creating Series from a list (default numeric index 0, 1, 2)
print("pd.Series(my_list)")
print(pd.Series(my_list))

# Method 2: Creating Series from a list with custom index labels
print("\npd.Series(my_list, index=labels)")
print(pd.Series(my_list, index=labels))

# Method 3: Creating Series from a NumPy array (default numeric index)
print("\npd.Series(arr)")
print(pd.Series(arr))

# Method 4: Creating Series from a dictionary (keys become index automatically)
print("\npd.Series(d)")
print(pd.Series(d))


"""
Pandas DataFrame 
A Pandas DataFrame is a two-dimensional, tabular data structure that works like a spreadsheet with rows and columns.
"""

# ========== Creating a DataFrame ==========

# Method 1: Creating DataFrame from a dictionary (keys become column names)
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print("\n\nDataFrame from dictionary:")
print(df)

# Method 2: Creating DataFrame from a list of lists (rows)
data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]

# Without column names (default: 0, 1, 2, 3)
df2 = pd.DataFrame(data_list)
print("\n\nDataFrame from list without column names:")
print(df2)

# With custom column names
columns = ["Name", "Age", "City", "Salary"]
df2 = pd.DataFrame(data_list, columns=columns)
print("\n\nDataFrame from list with column names:")
print(df2)

# ========== Selection and Indexing of Columns ==========

# Select single column by passing a column name
print("\n\nSelecting specific columns (Name):")
print(df2["Name"])

# Select multiple columns by passing a list of column names
print("\n\nSelecting specific columns (Name and City):")
print(df2[["Name", "City"]])

# ========== Creating a New Column ==========

# Add a new column by assigning values
df2["Designation"] = ["Doctor", "Eng.", "Doctor", "Eng."]
print("\n\nDataFrame after adding 'Designation' column:")
print(df2)

# ========== Removing Columns/Rows ==========

# Drop a column by label (axis=0 for rows, axis=1 for columns)
# Note: This returns a new DataFrame without modifying the original
print("\n\nDropping column 'Designation' (returns new DataFrame):")
print(df2.drop("Designation", axis=1))

# It Does not return a new DataFrame, modifies the original DataFrame inplace
df2.drop("Designation", axis=1 , inplace=True) 

# It can also drop multiple columns by passing a list of column names
df2.drop(["Designation" , "Salary"], axis=1 , inplace=True) 

# Drop a row by index (axis=0 for rows, axis=1 for columns)
# Note: This returns a new DataFrame without modifying the original
print("\n\nDropping row at index 0 (returns new DataFrame):")
print(df2.drop(0, axis=0))

# Original DataFrame remains unchanged use inplace=True to modify original
print("\n\nOriginal DataFrame (unchanged):")
print(df2)

# ========== Selecting Rows ==========

# Method 1: Using .loc (label-based indexing) - select row by index label
print("\n\nSelecting single rows 0 using .loc:")
print(df2.loc[0])

# Method 1: Using .loc (label-based indexing) - select rows by index labels 
# select row from index 0 and 1
print("\n\nSelecting rows 0 and 1 using .loc:")
print(df2.loc[[0, 1]])

# Method 2: Using .iloc (integer-based indexing) - select rows by position
print("\n\nSelecting row at position 3 using .iloc:")
print(df.iloc[3])

# ========== Selecting Subsets of Rows and Columns ==========

# Select specific rows and then specific columns
print("\n\nSelecting rows 0,1 and columns City, Salary:")
print(df.loc[[0, 1]][["City", "Salary"]])

# ========== Conditional Selection ==========

# Filter rows based on a condition
print("\n\nPeople whose age is above 30:")
print(df2[df2["Age"] > 30])

# Filter rows based on multiple conditions using & (AND) operator
print("\n\nPeople whose age is above 30 AND city is Paris:")
print(df2[(df2["Age"] > 30) & (df2["City"] == 'Paris')])
