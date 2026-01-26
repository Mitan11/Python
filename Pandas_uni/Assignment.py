import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Section A: Pandas Assignment

# 1. Load the dataset using pandas and display first 10 rows.
df = pd.read_csv('StudentPerformance.csv')
df.head(10)

# 2. Display last 5 records of dataset.
df.tail(5)

# 3. Print all column names.
df.columns

# 4. Delete Attendance column.
df.drop("Attendance" , axis=1)

# 5. Create a new dataframe with Name, Course and Marks.
newDf = df[["Name" , "Course" , "Marks"]]
newDf

# 6. Find students with marks greater than 80.
marksGreater = df[df["Marks"] > 80]
marksGreater

# 7. Count number of students in each Course.
studentCountByCourse = df.value_counts()
studentCountByCourse

# 8. Check missing values in each column.
missingValues = df.isnull().sum()
missingValues

# 9. Display statistical summary of numeric columns.
stats = df.describe()
stats

# 10. Sort dataset by Marks in descending order.
descSort = df.sort_values("Marks" , ascending=False)
descSort

# Section B: NumPy Assignment

marks = [45, 67, 89, 90, 56, 72, 88, 95, 60, 70]

# 1. Create a NumPy array from given data.
nparray = np.array(marks)

# 2. Find maximum, minimum and average marks.
minimum = nparray.min()
maximum = nparray.max()

minimum , maximum

# 3. Reshape array into 2x5 matrix.
reShape = nparray.reshape(2,5)
reShape

# 4. Find all marks greater than 70.
marksGreater = nparray[nparray > 70]
marksGreater

# 5. Add 5 grace marks to all students.
nparray += 5
nparray

# 6. Sort the array in ascending order.
nparray.sort(axis=0)

# 7. Find standard deviation and variance.
stdd = nparray.std()
vari = nparray.var()

stdd , vari

# 8. Generate first 15 numbers divisible by 3.
dev3 = np.arange(3, 46, 3)
dev3

# 9. Create an array of random numbers between 10 and 100 (size 10).
randomNumber = np.random.randint(10 , 100 , 10)
randomNumber

# 10. Replace all values less than 60 with 60.
nparray[nparray < 60] = 60

# Section C: Matplotlib Assignment

Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Sales = [12000, 15000, 18000, 17000, 21000, 25000]

# 1. Draw a line chart for monthly sales.

plt.plot(Month, Sales, color='b', linestyle='-', marker='o')

# 2. Add title, x-label and y-label to chart.

plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.show()

# 3. Change line style and marker.

plt.plot(Month, Sales, color='b', linestyle='--', marker='s')
plt.title('Monthly Sales Data')

# 4. Draw a bar chart for sales data.

plt.bar(Month, Sales, color='orange')

# 5. Create a pie chart for sales percentage.

plt.pie(Sales, labels=Month, autopct='%1.1f%%', startangle=140)

# 6. Display grid on chart.

plt.plot(Month, Sales, color='b', linestyle='-', marker='o')
plt.grid(True)

# 7. Draw scatter plot between month index and sales.

monthIndex = np.arange(len(Month))
plt.scatter(monthIndex, Sales, color='r', marker='^')

# 8. Create histogram of sales values.

plt.hist(Sales, bins=5, color='g', edgecolor='black')

# 9. Draw multiple lines in one chart.

months = np.array([1, 2, 3, 4, 5, 6])
salesA = np.array([12000, 15000, 18000, 17000, 21000, 25000])
salesB = np.array([10000, 14000, 16000, 15000, 20000, 23000])

plt.plot(months, salesA, label='Sales A')
plt.plot(months, salesB, label='Sales B')

# 10. Save chart as image file.
plt.plot(Month, Sales, color='b', linestyle='-', marker='o')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.savefig('monthly_sales_chart.png')