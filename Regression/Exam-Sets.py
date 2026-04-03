# SET-1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# Creating the dataset
data = {
    'StudentID': range(101, 113),
    'StudyHours': [5, 2, 7, 8, 1, 4, 6, 9, 3, 5, 2, 8],
    'Attendance': [90, 85, 92, 95, 60, 70, 88, 98, 75, 82, 55, 91],
    'Marks': [85, 45, 90, 95, np.nan, 65, 80, 99, np.nan, 78, 40, 92],
    'Result': ['Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass',
    'Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass']
}

df = pd.DataFrame(data)

# Task 1: Save to CSV
df.to_csv('student_performance.csv', index=False)
print("File 'student_performance.csv' created successfully.")

# Task 2: Load the dataset
df_loaded = pd.read_csv('student_performance.csv')

# Task 3: Display the first and last 8 records
print("--- First 8 Records ---")
print(df_loaded.head(8))
print("\n--- Last 8 Records ---")
print(df_loaded.tail(8))

# Task 4: Fill missing values in 'Marks' with 30
df_loaded['Marks'] = df_loaded['Marks'].fillna(30)
print("\nMissing values in 'Marks' filled with 30.")

# Task 5: Plot a box plot for Attendance
plt.figure(figsize=(8, 6))
plt.boxplot(df_loaded['Attendance'])
plt.show()

# 1. Separate features and target (Result)
x = df_loaded[['StudyHours', 'Attendance', 'Marks']]
y = df_loaded['Result']
x_train, x_test, y_train, y_test = train_test_split(x, y,
test_size=0.20, random_state=42)

# 3. Apply KNN (K=3)
pred = KNeighborsClassifier(n_neighbors=3)
pred.fit(x_train, y_train)

# 4. Calculate accuracy and confusion matrix
y_pred = pred.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(accuracy)
print(conf_matrix)

new_student = [[6, 80, 70]]
prediction = pred.predict(new_student)
print(f"The predicted result for the student is : {prediction[0]}")

# SET-2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Create employee_performance.csv with at least 10 records
data = {
    'EmpID': range(1001, 1013),
    'Age': [25, 30, 45, 35, 28, 50, 42, 22, 38, 33, 29, 47],
    'Experience': [2, 5, 20, 10, 4, 25, 18, 1, 12, 8, 3, 22],
    'Salary': [45000, 55000, 120000, 85000, 50000, 150000, 110000, 40000, 95000, 75000, 48000, 130000],
    'Performance': ['Good', 'Average', 'High', 'High', 'Average', 'High', 'High', 'Average', 'Good', 'Average', 'Good', 'High']
}

df = pd.DataFrame(data)
df.to_csv('employee_performance.csv', index=False)
print("File 'employee_performance.csv' created successfully.")

# 2. Load dataset
df_emp = pd.read_csv('employee_performance.csv')

# 3. Display the last 5 records
print("\n--- Last 5 Records ---")
print(df_emp.tail(5))

# 4. Display summary (info and describe)
print("\n--- Dataset Info ---")
df_emp.info()
print("\n--- Dataset Description ---")
print(df_emp.describe())

# 5. Create a bar chart showing average Salary by Performance
avg_salary = df_emp.groupby('Performance')['Salary'].mean()
plt.figure(figsize=(8, 6))
avg_salary.plot(kind='bar')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Separate features and targets
# We drop 'EmpID' as it's not a feature for prediction
X = df_emp[['Age', 'Experience', 'Salary']]
y = df_emp['Performance']

# 2. Split dataset (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.20, random_state=42)

# 3. Apply Decision Tree (max_depth=4)
dt_classifier = DecisionTreeClassifier(max_depth=4,
random_state=42)
dt_classifier.fit(X_train, y_train)

# 4. Display classification report and accuracy
y_pred = dt_classifier.predict(X_test)
acc = accuracy_score(y_test,y_pred)
cr = classification_report(y_test,y_pred)
print(acc)
print(cr)

# 5. Predict Performance for (Age=35, Experience=8, Salary=60000)
new_emp = [[35, 8, 60000]]
emp_prediction = dt_classifier.predict(new_emp)
print(f"\nThe predicted Performance for the employee is: {emp_prediction[0]}")

# SET - 3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Create patient_diagnosis.csv with at least 10 records
data = {
    'PatientID': range(2001, 2013),
    'Age': [45, 50, 35, 60, 28, 55, 40, 30, 48, 52, 33, 47],
    'BloodPressure': [130, 140, 120, 150, 110, 135, 125, 115, 138, 145, 118, 132],
    'GlucoseLevel': [150, 180, 100, 200, 90, 160, 140, 95, 175, 190, 110, 155],
    'BMI': [28, 30, 22, 35, 20, 32, 27, 21, 29, 31, 23, 28.5],
    'Disease': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes']
}

df_patients = pd.DataFrame(data)
df_patients.to_csv('patient_diagnosis.csv', index=False)
print("File 'patient_diagnosis.csv' created successfully.")

# 2. Load dataset using pandas
df = pd.read_csv('patient_diagnosis.csv')

# 3. Display the first 8 records
print(df.head(8))

# 4. Display dataset shape and column names
print(df.shape)
print(df.columns.tolist())

# 5. Draw a scatter plot showing GlucoseLevel vs BMI
plt.figure(figsize=(8, 6))
plt.scatter(df['GlucoseLevel'], df['BMI'])
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Separate features and target (Disease)
X = df[['Age', 'BloodPressure', 'GlucoseLevel', 'BMI']]
y = df['Disease']

# 2. Split dataset into training and testing (Training 30%, Testing 70%)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.70, random_state=42)

# 3. Apply Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

# 4. Predict test data
y_pred = log_model.predict(X_test)

# 5. Display accuracy and confusion matrix
acc = accuracy_score(y_test,y_pred)
con = confusion_matrix(y_test,y_pred)
print(acc)
print(con)

# 6. Predict disease for a patient (Age=45, BP=130, Glucose=150, BMI=28)
new_patient = [[45, 130, 150, 28]]
diagnosis_prediction = log_model.predict(new_patient)
print(f"\nThe predicted result for the patient (Age=45, BP=130, Glucose=150, BMI=28) is: {diagnosis_prediction[0]}")

# SET - 4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 1. Create customer_purchase.csv with at least 10 records
data = {
    'CustomerID': range(3001, 3013),
    'Age': [22, 25, 47, 52, 35, 40, 28, 60, 31, 33, 41, 55],
    'Salary': [20000, 35000, 80000, 110000, 45000, 75000, 30000, 150000, 48000, 52000, 85000, 130000],
    'Purchase': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes']
}
df_customers = pd.DataFrame(data)
df_customers.to_csv('customer_purchase.csv', index=False)
print("File 'customer_purchase.csv' created successfully.")

# 2. Load dataset
df = pd.read_csv('customer_purchase.csv')

# 3. Display dataset shape
print(df.shape)

# 4. Display column names
print(df.columns.tolist())

# 5. Plot a histogram of Salary distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=6, color='skyblue',
edgecolor='black')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Separate features and targets
# Dropping 'CustomerID' since it's not a useful feature for the model
X = df[['Age', 'Salary']]
y = df['Purchase']

# 2. Split dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.20, random_state=42)

# 3. Apply SVM (linear kernel)
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# 4. Predict test data
y_pred = svm_model.predict(X_test)

# 5. Display accuracy and confusion matrix
acc = accuracy_score(y_test,y_pred)
con = confusion_matrix(y_test,y_pred)
print(acc)
print(con)

# 6. Predict purchase for (Age=30, Salary=50000)
new_customer = [[30, 50000]]
purchase_prediction = svm_model.predict(new_customer)
print(f"\nThe predicted result for the customer (Age=30, Salary=50000) is: {purchase_prediction[0]}")

# SET - 5
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Create loan_prediction.csv with at least 10 records
data = { 
    'CustomerID': range(401, 413),
    'Income': [45000, 30000, 85000, 120000, 50000, 25000, 95000, 70000, 40000, 35000, 55000, 110000],
    'CreditScore': [720, 600, 750, 800, 680, 550, 780, 710, 650, 620, 690, 790],
    'LoanAmount': [15000, 10000, 40000, 60000, 20000, 5000, 45000, 30000, 12000, 8000, 25000, 55000],
    'Approved': [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
}
df_loan = pd.DataFrame(data)
df_loan.to_csv('loan_prediction.csv', index=False)
print("File 'loan_prediction.csv' created successfully.")

# 2. Load dataset
df = pd.read_csv('loan_prediction.csv')

# 3. Display the last 4 rows
print(df.tail(4))

# 4. Check for missing values
print(df.isnull().sum())

# 5. Plot a pie chart of Income distribution (categorized)
# To create a pie chart, we'll bin the income into Low, Medium, and High categories
income_bins = [0, 40000, 70000, 150000]
income_labels = ['Low ($<40k)', 'Medium ($40k-70k)', 'High ($>70k)']
df['IncomeCategory'] = pd.cut(df['Income'], bins=income_bins,
labels=income_labels)
income_counts = df['IncomeCategory'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(income_counts, labels=income_counts.index, autopct='%1.1f%%')
plt.title('Loan Applicant Income Distribution')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. Separate features and target (Approved)
X = df[['Income', 'CreditScore', 'LoanAmount']]
y = df['Approved']

# 2. Split dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.20, random_state=42)

# 3. Apply Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

# 4. Predict test data
y_pred = log_model.predict(X_test)

# 5. Display confusion matrix and accuracy
acc = accuracy_score(y_test,y_pred)
con = confusion_matrix(y_test,y_pred)
print(acc)
print(con)

# 6. Predict loan approval for (Income=50000, CreditScore=700, LoanAmount=20000)
new_loan = [[50000, 700, 20000]]
loan_prediction = log_model.predict(new_loan)
status = "Approved" if loan_prediction[0] == 1 else "Rejected"
print(f"\nThe predicted result for the loan application is: {status}")

