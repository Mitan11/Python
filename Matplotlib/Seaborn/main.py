# Seaborn

# Importing Libraries
import numpy as np
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


# Catagorical Plots

# Loading of seaborn inbuilt dataset
df = sns.load_dataset('tips')
df

# Count Plot
sns.countplot(df['sex'])

#  Alternative way to write count plot 
sns.countplot(x = df['sex'])

# count plot with hue based on 'smoker' 
sns.countplot(x = df['sex'], hue=df['smoker'])  # count plot with hue based on 'smoker'

# Bar Plot
sns.barplot(x=df['sex'], y = df['total_bill'])  # bar plot showing average total bill for each sex # default estimator is mean

# Changing estimator in bar plot
sns.barplot(x=df['sex'], y = df['tip'] , estimator= np.sum)    # changing estimator to sum

# Box Plot
sns.boxplot(x=df['tip'], y=df['day'] , data=df)  # box plot showing distribution of tip amount for each day

sns.boxplot(x=df['tip'], y=df['day'] , data=df , palette='rainbow')  # box plot showing distribution of tip amount for each day

# Violin Plot
sns.violinplot(x=df['day'], y=df['total_bill'], data=df)

# strip Plot
sns.stripplot(x=df['day'], y=df['total_bill'], data=df)

# Swarm Plot
sns.swarmplot(x=df['day'], y=df['total_bill'], data=df)

# Combining Violin Plot and Swarm Plot
sns.violinplot(x=df['tip'], y=df['day'], data=df)
sns.swarmplot(x=df['tip'], y=df['day'], data=df)



# Matrix Plots

# Loading of seaborn inbuilt dataset
flights = sns.load_dataset('flights')
flights

tips = sns.load_dataset('tips')
tips

# heatmap

tipsCorr = tips[['total_bill', 'tip', 'size']]
tipsCorr

# correlation matrix
tipsCorr.corr()

#  heatmap of correlation matrix
sns.heatmap(tipsCorr.corr())  # heatmap of correlation matrix with annotations

# heatmap with annotations
sns.heatmap(tipsCorr.corr() , annot=True)  # heatmap of correlation matrix with annotations

# Clustermap
sns.clustermap(tipsCorr.corr() , annot=True)  # clustermap of correlation matrix with annotations

# pivot table heatmap
pivotFlight = flights.pivot_table(index='month', columns='year', values='passengers')
pivotFlight

sns.heatmap(pivotFlight)  # heatmap of pivot table


# regression Plots
sns.lmplot(x='total_bill', y='tip', data=df)  # regression plot with scatter plot and regression line 

# regression plot with hue based on 'sex'
sns.lmplot(x='total_bill', y='tip', data=df , hue='sex')  # regression plot with scatter plot and regression line

# palette and markers in regression plot
sns.lmplot(x='total_bill', y='tip', data=df , hue='sex' , palette='rainbow' )  # regression plot with scatter plot and regression line

#   
sns.lmplot(x='total_bill', y='tip', data=df , hue='sex' , palette='rainbow', markers=['o', 'x'])  # regression plot with scatter plot and regression line



# Plotly and cufflinks
import seaborn as sns
import pandas as pd 
import cufflinks as cf 
from plotly.offline import iplot

