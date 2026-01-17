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

# 11. Load data set using pandas function and display last 5 records
data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/tips.csv") # Importing CSV data into a Pandas DataFrame
data.tail(5)

# 12. Add a new column 'Net Bill' = 'Total Bill' * size + 15%GST
data['Net Bill'] = data['total_bill'] * data['size'] + 1.15
data

# 13. Count the number of male and female members in the dataset
gender_counts = data['sex'].value_counts()
print(gender_counts)

# 14. Display records where bill is greater than 15 and tip is less than 5
filtered_data = data[(data['total_bill'] > 15) & (data['tip'] < 5)]
print(filtered_data)

# 15. Find the highest and lowest amount of tip
highest_tip = data['tip'].max()
lowest_tip = data['tip'].min()
highest_tip, lowest_tip

# 16. Display the information of dataframe
data.info()

# 17. Create a chart to show male and female customer count
plt.plot(gender_counts.index,gender_counts.values)
# or
# import matplotlib.pyplot as plt
# gender_counts.plot(kind='bar', color=['blue', 'pink'])
# plt.title('Male and Female Customer Count')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# 18. Display female smoker customers
female_smokers = data[(data['sex'] == 'Female') & (data['smoker'] == 'Yes')]
female_smokers

# 19. Find total bill on weekends (Saturday and Sunday)
total_bill_weekends = data[data['day'].isin(['Sat', 'Sun'])]['total_bill'].sum()
total_bill_weekends

# 20. Draw a triangle using line chart
sex_count = data.value_counts("sex")
plt.plot(sex_count.index, sex_count.values , marker="^")