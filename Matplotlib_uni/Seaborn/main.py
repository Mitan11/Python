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

