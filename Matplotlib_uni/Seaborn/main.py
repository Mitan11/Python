# Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# To see all available seaborn datasets
sns.get_dataset_names()

# Loading of seaborn inbuilt dataset
df = sns.load_dataset('diamonds')
df.head()

# Distribution Plot
plt.scatter(df.carat , df.color)
# sns.set() #style this plot using the set funtion

# Changing the style of the plot
plt.scatter(df.carat , df.color)
sns.set_style("whitegrid")

# Loading another seaborn inbuilt dataset
df1 = sns.load_dataset('car_crashes')
df1
# Scatter Plot
plt.scatter(df1.speeding , df1.alcohol)

# Changing the style of the plot
param = sns.axes_style()
param

# Changing the style of the plot
df1 = sns.load_dataset('car_crashes')
df1

# Scatter Plot
plt.scatter('speeding' , 'alcohol', data=df1)
sns.set_style("darkgrid",{'grid.color' : '0.8'})
plt.show()

# Changing the context of the plot
plt.scatter('speeding' , 'alcohol', data=df1)
# sns.set_context("notebook")
sns.set_context("poster")
plt.show()

# Changing the style and context of the plot
plt.scatter('speeding' , 'alcohol', data=df1)
sns.set_style("dark")
sns.set_context("poster")
plt.show()

df2 = sns.load_dataset("tips")
df2

# Scatter Plot
plt.scatter("total_bill","tip" , data=df2)
sns.scatterplot("total_bill","tip" , data=df2)

# Changing the style and context of the plot
# relplot is used to make a scatter plot with multiple categories
sns.relplot(data=df2 , x = "total_bill" ,y = "tip" , hue="time" , col = "day" , col_wrap = 4)

# Line Plot
sns.relplot(data=df2 , x = "total_bill" ,y = "tip" , kind = 'line')

# Changing the confidence interval of the line plot
sns.relplot(data=df2 , x = "size" ,y = "tip" , kind = 'line' , ci = 65)

# Point Plot
sns.pointplot(x='day' , y = "tip" , data = df2)

# Changing the style and context of the plot hue is used to differentiate the categories in the plot
sns.pointplot(x='day' , y = "tip" , data = df2 , hue = "smoker" , palette = "Accent")

# Joint Plot
sns.jointplot(x="total_bill" ,  y= "tip" , data=df2)

# Changing the kind of the joint plot
sns.jointplot(x="total_bill" ,  y= "tip" , data=df2 , kind = "reg")

# Box Plot
sns.boxplot(x="day" ,  y= "tip" , data=df2)


flight = sns.load_dataset("flights")
# Heatmap
flight_pvt = flight.pivot(
index = "month",
columns = "year",
values = "passengers"
)
# annot = True is used to show the values in the heatmap
sns.heatmap(flight_pvt , cmap = "YlGnBu" , annot = True , fmt = "d")

corr_matrix = df1.corr()
print(corr_matrix)

sns.heatmap(corr_matrix, 
            cmap="YlGnBu",      
            annot=True,         
            fmt=".2f",          
            linewidths=0.5,      
            cbar_kws={'label': 'Correlation'},
            square=True) 

# Pair Plot
sns.pairplot(df2 , hue = 'day')

