import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('diabetes_nonlinear.csv')

X = df[['BMI']]
y = df['Disease_Progression']

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

print("MSE:", mean_squared_error(y, y_pred))
print("R2:", r2_score(y, y_pred))

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.show()

# New prediction
new_X = [[0.05],[0.1],[0.15],[0.2],[0.25]]
new_X_poly = poly.transform(new_X)
pred = model.predict(new_X_poly)

print("Predicted Disease Progression:", pred)