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