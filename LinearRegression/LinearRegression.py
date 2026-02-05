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
# from sklearn.metrics import mean_squared_error, r2_score

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

# or 

# df = pd.read_csv('data.csv')

# x = df['Study_Hours'].values.reshape(-1, 1)
# y = df['Marks'].values

plt.scatter(X, y)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

y_pred = model.predict(X_test)
print("\nActual Marks:", y_test)
print("Predicted Marks:", y_pred)


# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("\nMean Squared Error:", mse)
# print("R2 Score:", r2)


plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression Model")
plt.legend()
plt.show()


new_hours = np.array([[12]])
predicted_marks = model.predict(new_hours)
print("\nPredicted marks for 12 study hours:", predicted_marks[0])