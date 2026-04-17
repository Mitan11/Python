import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score

# SET – 1 
# 1. Load the Churn_Modelling dataset and display dataset shape and column names.
df = pd.read_csv('Churn_Modelling.csv')
print("Dataset Shape:", df.shape)
print("Column Names:", df.columns.tolist())

# 2. Display random 8 customer records.
print("Random 8 Customer Records:")
print(df.sample(8))

# 3. Identify customers whose Balance is above the dataset average.
cust_above_avg_balance = df[df['Balance'] > df['Balance'].mean()]
print("Customers with Balance above Average:")
print(cust_above_avg_balance)

# 4. Count customers by Geography and display the result.
print("Customer Count by Geography:")
print(df.groupby('Geography').size())

# 5. Calculate mean, median, and variance of CreditScore.
print("CreditScore Statistics:")
print("Mean:", df['CreditScore'].mean())
print("Median:", df['CreditScore'].median())
print("Variance:", df['CreditScore'].var())

# 6. Draw a scatter plot showing Age vs Balance colored by Gender.
plt.scatter(df['Age'], df['Balance'], c=df['Gender'].map({'Male': 'blue', 'Female': 'red'}))
plt.xlabel('Age')
plt.ylabel('Balance')
plt.title('Age vs Balance by Gender')
plt.show()

# 7. Apply Linear Regression to predict customer Balance using Age.
X = df[['Age']]
y = df['Balance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Linear Regression Results:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared Score:", r2_score(y_test, y_pred))

# 8. Predict the Balance of a customer whose Age is 40.
predicted_balance = model.predict([[40]])
print("Predicted Balance for a 40-year-old customer:", predicted_balance[0])

# SET – 2

# 1. Load the students dataset and display column names.
df = pd.read_csv('students.csv')
print("Column Names:", df.columns.tolist())

# 2. Show first 6 records of the dataset.
print("First 6 Records:")
print(df.head(6))

# 3. Check for duplicate records and remove them if any.
duplicates = df.duplicated().sum()
print("Number of Duplicate Records:", duplicates)
df = df.drop_duplicates()


# 4. Calculate average math, reading, and writing scores.
print("Average Scores:")
print("Math:", df['math score'].mean())
print("Reading:", df['reading score'].mean())
print("Writing:", df['writing score'].mean())

# 5. Find students whose math score is below class average.
math_avg = df['math score'].mean()
below_avg_students = df[df['math score'] < math_avg]
print("Students with Math Score below Average:")
print(below_avg_students)

# 6. Count students by gender and parental level of education.
print("Student Count by Gender:")
print(df.groupby('gender').size())
print("Student Count by Parental Level of Education:")
print(df.groupby('parental level of education').size())

# 7. Create a new column Total_Score.
df['Total_Score'] = df['math score'] + df['reading score'] + df['writing score']

# 8. Display top 10 students based on Total_Score.
print("Top 10 Students by Total Score:")
print(df.nlargest(10, 'Total_Score'))

# 9. Plot a histogram of math scores.
plt.hist(df['math score'], bins=10, edgecolor='black')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.title('Distribution of Math Scores')
plt.show()

# SET – 3

# 1. Load the Housing dataset and display the dataset summary.
df = pd.read_csv('Housing.csv')
print("Dataset Summary:")
print(df.info())

# 2. Select Area as input variable and Price as output variable.
X = df[['area']]
y = df['price']

# 3. Handle missing values using mean imputation.
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# 4. Visualize Area vs Price using scatter plot.
plt.scatter(X['area'], y, color='blue')
plt.xlabel('area')
plt.ylabel('price')
plt.title('Area vs Price')
plt.show()

# 5. Split the dataset into 80% training and 20% testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train a Simple Linear Regression model.
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Display regression equation.
print("Regression Equation:")
print("y = {:.2f} + {:.2f} * x".format(model.intercept_, model.coef_[0]))
# regression_equation = model.coef_[0] * x + model.intercept_

# 8. Predict prices for test data.
y_pred = model.predict(X_test)

# 9. Predict house price for Area = 2500 sq.ft.
predicted_price = model.predict([[2500]])
print("Predicted Price for 2500 sq.ft. Area:", predicted_price[0])

# SET – 4

# 1. Load the Movie dataset and display dataset info.
df = pd.read_csv('IMDB-Movie-Data.csv - IMDB-Movie-Data.csv')
print("Dataset Info:")

# 2. Display the last 5 movie records.
df_last_5 = df.tail(5)
print("Last 5 Movie Records:")
print(df_last_5)

# 3. Find movies released after 2015.
movies_after_2015 = df[df['Year'] > 2015]
print("Movies Released After 2015:")

# 4. Calculate average IMDB rating.
average_rating = df['Rating'].mean()
print("Average IMDB Rating:", average_rating)

# 5. Identify the top 5 highest-rated movies.
top_5_movies = df.nlargest(5, 'Rating')
print("Top 5 Highest-Rated Movies:")
print(top_5_movies)

# 6. Find the director with the maximum number of movies.
director_counts = df.groupby('w').size()
top_director = director_counts.idxmax()
print("Director with Maximum Number of Movies:", top_director)

# 7. Calculate standard deviation of movie runtime.
std_runtime = df['Runtime (Minutes)'].std()
print("Standard Deviation of Movie Runtime:", std_runtime)

# 8. Display movies with revenue greater than dataset average.
revenue_avg = df['Revenue (Millions)'].mean()
high_revenue_movies = df[df['Revenue (Millions)'] > revenue_avg]
print("Movies with Revenue greater than Average:")
print(high_revenue_movies)

# 9. Draw a scatter plot of runtime vs rating.
plt.scatter(df['Runtime (Minutes)'], df['Rating'], color='green')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Rating')
plt.title('Runtime vs Rating')
plt.show()

# 10. Plot a bar chart showing top 5 directors by movie count.
plt.bar(director_counts.nlargest(5).index, director_counts.nlargest(5).values, color='orange')
plt.xlabel('Director')
plt.ylabel('Number of Movies')
plt.title('Top 5 Directors by Movie Count')
plt.xticks(rotation=45)
plt.show()


# SET – 5

# 1. Load the E-Commerce dataset and display the first 5 records.
df = pd.read_csv('E-Commerce.csv')
print("First 5 Records:")
print(df.head())

# 2. Remove records with missing CustomerID.
df = df.dropna(subset=['CustomerID'])

# 3. Convert the InvoiceDate column to datetime format.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 4. Create a new column TotalAmount using Quantity × UnitPrice.
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# 5. Find the total sales for each country.
sales_by_country = df.groupby('Country')['TotalAmount'].sum()
print("Total Sales by Country:")
print(sales_by_country)

# 6. Identify the top 10 customers based on total purchase value.
top_10_customers = df.groupby('CustomerID')['TotalAmount'].sum().nlargest(10)
print("Top 10 Customers by Purchase Value:")
print(top_10_customers)

# 7. Display all invoices having negative quantity values.
negative_quantity_invoices = df[df['Quantity'] < 0]
print("Invoices with Negative Quantity:")
print(negative_quantity_invoices)

# 8. Calculate the average TotalAmount.
average_total_amount = df['TotalAmount'].mean()
print("Average Total Amount:", average_total_amount)

# 9. Find transactions where TotalAmount is greater than the average.
high_value_transactions = df[df['TotalAmount'] > average_total_amount]
print("Transactions with Total Amount greater than Average:")
print(high_value_transactions)

# 10. Plot a box plot of TotalAmount.
plt.boxplot(df['TotalAmount'])
plt.xlabel('Total Amount')
plt.title('Distribution of Total Amount')
plt.show()
