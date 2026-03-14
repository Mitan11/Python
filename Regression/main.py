"""
===========================================================
Practical Implementation of Supervised Learning:
LINEAR REGRESSION (Using Python)
===========================================================
#Linear regression
#a type of supervised machine-learning algorithm that learns from the labelled datasets and
maps the data points with most optimized linear functions which can be used for prediction on
new datasets.
#It assumes that there is a linear relationship between the input and output, meaning the output
changes at a constant rate as the input changes.
#This relationship is represented by a straight line.
#For example: predict a student's exam score based on study hours
#Independent variable (input): Hours studied
#Dependent variable (output): Exam score
# Image of slop
#Types:
#1. Simple Linear Regression
#2. Multiple Linear Regression: more than one independent variable and one dependent
variable
"""
# -----------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# -----------------------------------------------------------
# NumPy is used for numerical operations
import numpy as np
# Pandas is used for handling datasets
import pandas as pd
# Matplotlib is used for data visualization
import matplotlib.pyplot as plt
# train_test_split is used to split dataset
from sklearn.model_selection import train_test_split
# LinearRegression model is imported from sklearn
from sklearn.linear_model import LinearRegression
# Metrics to evaluate model performance
from sklearn.metrics import mean_squared_error, r2_score
# -----------------------------------------------------------
# 2. CREATE DATASET (SUPERVISED LEARNING)
# -----------------------------------------------------------
"""
Supervised learning means:
- We have INPUT (X)
- We have OUTPUT (Y)
- Model learns relationship between X and Y
Example:
Study Hours -> Exam Score
"""
# Creating input feature (X)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# Creating target output (Y)
y = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
# Convert to DataFrame for better understanding
data = pd.DataFrame({
 'Study_Hours': X.flatten(),
 'Marks': y
})
print("Dataset:")
print(data)
# -----------------------------------------------------------
# 3. VISUALIZE THE DATA
# -----------------------------------------------------------
"""
We plot the data to see relationship between X and Y
"""
plt.scatter(X, y)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
# -----------------------------------------------------------
# 4. SPLIT DATA INTO TRAINING AND TESTING
# -----------------------------------------------------------
"""
Why split?
- Training data: model learns from it
- Testing data: model is evaluated on unseen data
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))
# -----------------------------------------------------------
# 5. CREATE LINEAR REGRESSION MODEL
# -----------------------------------------------------------
"""
Linear Regression Equation:
y = mX + c
where,
m = slope (coefficient)
c = intercept
"""
model = LinearRegression()
# -----------------------------------------------------------
# 6. TRAIN THE MODEL
# -----------------------------------------------------------
"""
Model learns slope and intercept from training data
"""
model.fit(X_train, y_train)
# -----------------------------------------------------------
# 7. GET MODEL PARAMETERS
# -----------------------------------------------------------
print("\nModel Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)
# -----------------------------------------------------------
# 8. MAKE PREDICTIONS
# -----------------------------------------------------------
"""
Model predicts marks for test data
"""
y_pred = model.predict(X_test)
print("\nActual Marks:", y_test)
print("Predicted Marks:", y_pred)
# -----------------------------------------------------------
# 9. EVALUATE THE MODEL
# -----------------------------------------------------------
"""
Evaluation Metrics:
1. Mean Squared Error (MSE)
2. R-squared score (R^2)
"""
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nMean Squared Error:", mse)
print("R2 Score:", r2)
# -----------------------------------------------------------
# 10. VISUALIZE REGRESSION LINE
# -----------------------------------------------------------
"""
Plot:
- Blue dots = actual data
- Red line = predicted regression line
"""
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression Model")
plt.legend()
plt.show()
# -----------------------------------------------------------
# 11. PREDICT FOR NEW INPUT
# -----------------------------------------------------------
"""
Predict marks if student studies for 12 hours
"""
new_hours = np.array([[12]])
predicted_marks = model.predict(new_hours)
print("\nPredicted marks for 12 study hours:", predicted_marks[0])