import numpy as np # importing numpy for numerical operations
import pandas as pd # importing pandas for data manipulation

customer_data = pd.read_csv("customer_data.csv") # Importing CSV data into a Pandas DataFrame
print(customer_data)

#1. Load data set using pandas function and display last 5 rows
data = pd.read_csv('customer_data.csv')
print(data.tail(5))

#2. Print all the column header of data set
print(data.columns)

#3. Delete Surname column from data set axis = 1 means column , axis = 0 means row
data = data.drop('Surname', axis=1)
print(data)

#4. create a new dataframe with selecting Age , Gender and Balance Fields
new_data = data[['Age', 'Gender', 'Balance']]
print(new_data)

#5. Count the number of missing values in each column of customer_data DataFrame
missing_values_count = customer_data.isna().sum()
print(missing_values_count)

#6. Display the row having balance between 8000 and 10000
filtered_data = customer_data[(customer_data['Balance'] >= 8000) & (customer_data['Balance'] <= 10000)]
# filtered_data = customer_data[customer_data['Balance'].between(8000, 10000)] 
print(filtered_data)

#7. Count the sum of each category in geography column
geography_counts = customer_data['Geography'].value_counts()
print(geography_counts)

#8. Print all the statical information of customer_data dataset
statistical_info = customer_data.describe()
print(statistical_info)

#9. print first 10 number in factor of 8
for i in range(1, 11):
    print(i * 8)

#10. create a chart for customer balance column

import matplotlib.pyplot as plt
plt.plot(data['Balance'] , marker='o')
plt.show()
