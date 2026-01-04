import numpy as np # importing numpy for numerical operations
import pandas as pd # importing pandas for data manipulation

# Displaying the version of pandas
print(pd.__version__)

# Creating a Pandas Series from a list
# Data can be of any data type
data = [10, 20, 30]
series = pd.Series(data) # Creating Series from list
print("Series from list:")
print(series)

labels = ['a', 'b', 'c']
# We can also specify index
series1 = pd.Series(data , ['a', 'b', 'c']) # Creating Series from list with custom index
# series1 = pd.Series(data , labels) # Creating Series from list with custom index
print("Series from list with custom index:")
print(series1)

print(series1.loc["b"]) # Accessing element by label
print(series1.iloc[2]) # Accessing element by position
print(series[series > 15]) # Conditional selection

# Creating a Pandas Series from a NumPy array
db = {'Day1': 100, 'Day2':200, 'Day3':300, 'Day4':400}
series2 = pd.Series(db)
print(series2)

# Creating a Pandas DataFrame from a dictionary

# dictionary with list values
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [28, 24, 22],
}

df = pd.DataFrame(data) # Creating DataFrame from dictionary
print("DataFrame from dictionary:")
print(df)

print(df.loc[1]) # Accessing row by label
print(df.iloc[0]) # Accessing row by position

db = {
    'student':['abc','def','ghi'], 
    'admission':[2023,2022,2021]
}

dataframe = pd.DataFrame(db)
print(dataframe)

db = {'Product':['T-shirt','Pent','shirt','cap','shoes'], 'Price':[4000,2000,5000,500,5000],'QTY':[1,2,1,2,3]}
dataframe = pd.DataFrame(db)
print(dataframe)

print(dataframe.loc[3])

# import csv data in pandas dataframe
data_csv = pd.read_csv('studentData.csv')
print("CSV Data:")
print(data_csv)

# import json data in pandas dataframe
# data_json = pd.read_json('studentData.json')
# print("JSON Data:")
# print(data_json)

# Select specific columns
print(data_csv['Name'])

# select multiple columns
print(data_csv[['Name', 'Total Marks']])

# Selection by rows
print(data_csv.loc[2]) # by label
print(data_csv.iloc[4]) # by position

# Display first and last few records
print(data_csv.head())
print(data_csv.tail())

# Display pandas options
print(pd.options.display.max_rows) # Get the maximum number of rows to display
print(pd.options.display.max_columns) # Get the maximum number of columns to display

# Set pandas options
pd.options.display.max_rows = 120
print(pd.options.display.max_rows)

# Display DataFrame information
print(data_csv.info())

# ========== Finding Missing Data ==========

# Create a DataFrame with missing values (NaN)
data_missing = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}

df_missing = pd.DataFrame(data_missing)

print("\n\n========== DataFrame with Missing Data ==========")
print(df_missing)

# Check which cells contain missing values (returns boolean DataFrame)
print("\n\nChecking for missing values using .isna():")
print(df_missing.isna())

# Count the total number of missing values in each column
print("\n\nCounting missing values per column:")
print(df_missing.isna().sum())

# Check if any column contains at least one missing value
print("\n\nChecking if any column has missing values:")
print(df_missing.isna().any())

# ========== Removing Missing Data ==========

# Remove all rows that contain any missing values
print("\n\nRemoving rows with any missing values using .dropna():")
print(df_missing.dropna())

# Note: dropna() doesn't modify the original DataFrame by default
print("\n\nOriginal DataFrame (unchanged):")
print(df_missing)

# Remove rows that don't have at least 'n' non-missing values
# thresh=1 means keep rows that have at least 1 non-null value
print("\n\nRemoving rows using threshold (thresh=1):")
print(df_missing.dropna(thresh=1))

# ========== Filling Missing Data ==========

# Fill all missing values with a constant value (0)
print("\n\nFilling all missing values with 0:")
print(df_missing.fillna(0))

# Fill missing values with column-specific values using a dictionary
values = {'A': 0, 'B': 100, 'C': 300, 'D': 400}
print("\n\nFilling missing values with column-specific values:")
print(df_missing.fillna(value=values))

# Original DataFrame remains unchanged
print("\n\nOriginal DataFrame (unchanged):")
print(df_missing)

# Fill missing values with the mean of each column
print("\n\nFilling missing values with column means:")
print(df_missing.fillna(df_missing.mean()))

# Load student marks data from CSV file
StMarks = pd.read_csv('studentData.csv')
print(StMarks)

# Remove rows with any missing values
new_std = StMarks.dropna()
print(new_std)

# Fill missing values with a constant value (111)
fill_std = StMarks.fillna(111)
print(fill_std)

# Fill missing values in "Total Marks" column with 111
std1 = StMarks["Total Marks"].fillna(111)
print(std1)

# Calculate mean, median, and mode of "Obtained marks" column
mean = StMarks["Obtained marks"].mean()
print("Mean:", mean)
median = StMarks["Obtained marks"].median()
print("Median:", median)
mode = StMarks["Obtained marks"].mode()
print("Mode:", mode)

# print columns of the DataFrame
print(StMarks.columns)

# Sort DataFrame by "Obtained marks" in descending order
print("DataFrame sorted by 'Obtained marks' in descending order:")
print(StMarks.sort_values(["Obtained marks"] , ascending=False))

# Sort DataFrame by "Name" in ascending order
print("DataFrame sorted by 'Name' in ascending order:")
print(StMarks.sort_values(["Name"] , ascending=True))

# Create a new column "Percentage" calculating the percentage of obtained marks
StMarks["Percentage"] = (StMarks['Obtained marks'] / StMarks['Total Marks']) * 100
print(StMarks) #full data
print(StMarks.head(5)) #top 5 data

# Display first 5 records using .loc
print("First 5 records using .loc:")
print(StMarks.loc[0:4])

# Simple lambda function to add two numbers
add = lambda a, b: a+b
add(5,3)


# Function to assign grades based on percentage using apply and lambda
# def assign_grade(percentage):
#     if percentage >= 80 and percentage <= 100:
#         return 'A'
#     elif percentage >= 60 and percentage <= 80:
#         return 'B'
#     elif percentage >= 40 and percentage <= 60:
#         return 'C'
#     elif percentage >= 40 and percentage <= 20:
#         return 'D'
#     else:
#         return 'F'

# StMarks['Grade'] = StMarks['percentage'].apply(assign_grade)
# print(StMarks)

# Assigning grades using lambda function
StMarks['Grade'] = StMarks['Percentage'].apply(lambda x: 'A' if x >= 80 and x <= 100 else
                                     'B' if x >= 60 and x <= 80 else
                                     'C' if x >= 40 and x <= 60 else
                                     'D' if x >= 40 and x <= 20 else 'F')

print(StMarks)
