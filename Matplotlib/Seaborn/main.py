# Seaborn

# Importing Libraries
import matplotlib.pyplot as plt
import seaborn as sns

'''
We use distribution plots to visualize the distribution of quantitative data.
Let's discuss some plots that allow us to visualize the distribution of a data set. These plots are:
        distplot/histplot
        jointplot
        pairplot
        rugplot
'''
# Loading of seaborn inbuilt dataset
df = sns.load_dataset('tips')
df

# Distribution Plot
sns.histplot(df['total_bill'])
sns.histplot(df['total_bill'], bins=30) # specifying number of bins for histogram (number of bars)
sns.histplot(df['total_bill'], bins=30 , kde=True)  # it adds a kde (kernel density estimate) plot on top of the histogram for better visualization

# Subplots
plt.subplot(2,2,1)
sns.histplot(df['total_bill'], bins=30 , kde=True)
plt.subplot(2,2,2)
sns.histplot(df['tip'], bins=30 , kde=True)

# Joint Plot
sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter')  # scatter plot

# pairplot
sns.pairplot(df)  # pairwise relationships in a dataset

# pairplot with hue it adds color based on a categorical variable
sns.pairplot(df, hue='sex')  # pairwise relationships in a dataset with hue based on 'sex'

# Rug Plot
sns.rugplot(df['total_bill'])  # it draws small vertical lines at each data point along the x-axis to show the distribution of data points

