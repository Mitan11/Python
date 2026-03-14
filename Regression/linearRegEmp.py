import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([1000,2000,3000,4000,5000,60000,70000,80000,9000,100000])

df = pd.DataFrame(
    {'employeeHours' : x.flatten(),
    'salary' : y}
)

plt.scatter(x,y)


xTest, xTrain , yTest, yTrain = train_test_split(x,y,test_size=0.2 , random_state=42)

model = LinearRegression()
model.fit(xTrain, yTrain)

y_predict = model.predict(xTest)

plt.scatter(x,y)
plt.line(x,model.predict(x))

new_hours = np.array([[12]])
predict = model.predict(new_hours)