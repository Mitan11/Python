import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# SET 1 – K-Nearest Neighbor (KNN)
# Questions :
# 1. Load the dataset and display shape and column names.

df = pd.read_csv('iris.csv')
print("Shape of the dataset:", df.shape)
print("Column names:", df.columns)

# 2. Display first 5 records.

print("First 5 records:")
print(df.head(5))

# 3. Check for missing values.
print("Missing values:")
print(df.isnull().sum())

# 4. Split dataset into features and target.
X = df.drop('species', axis=1)
y = df['species']

# 5. Split data into 80% training and 20% testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Apply KNN with K = 3.
model = KNeighborsClassifier(n_neighbors=3)

# 7. Predict test data.
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 8. Calculate accuracy score.
accuracy = accuracy_score(y_test, y_pred)

# 9. Display confusion matrix.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 10. Predict species for a flower with values [5.1, 3.5, 1.4, 0.2].
pred = model.predict([[5.1, 3.5, 1.4, 0.2]])
print("Predicted species for [5.1, 3.5, 1.4, 0.2]:", pred[0])


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# SET 2 – Decision Tree Classifier
# Questions:
# 1. Load dataset and display summary.
df = pd.read_csv('wine.csv')
df.info()
# or 
df.describe()

# 2. Display first 10 records.
print("First 10 records:")
print(df.head(10))

# 3. Separate features and target.
X = df.drop('Customer_Segment', axis=1)  # Replace 'target' with the actual target column name
y = df['Customer_Segment']

# 4. Split dataset into training and testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Apply Decision Tree Classifier (max_depth=4).
model = DecisionTreeClassifier(max_depth=4, random_state=42)

# 6. Predict test data.
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 7. Calculate accuracy.
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 8. Display confusion matrix.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 9. Display classification report.
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 10. Predict wine class for input sample values.
pred = model.predict([[13.0, 2.0, 2.5, 16.0, 100.0, 2.5, 1.5, 0.5, 1.0, 3.0, 1.0, 2.0, 100.0]])  # Replace with actual feature values
print("Predicted wine class for input sample values:", pred[0])


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# SET 3 – Logistic Regression
# Questions:
# 1. Load dataset and display info.
df = pd.read_csv('Titanic-Dataset.csv')
df.info()

# 2. Handle missing values.
new_df = df.fillna(df.mean(numeric_only=True))  # Fill numeric columns with mean
print(new_df)

# 3. Convert categorical columns (Sex) into numeric.
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. Select input features and target (Survived).
x = df.drop('Survived', axis=1)  # Replace 'Survived' with the actual target column name
y = df['Survived']

# 5. Split the dataset into training and testing.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 6. Apply Logistic Regression.
model = LogisticRegression(random_state=42)

# 7. Predict test data.
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# 8. Calculate accuracy.
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 9. Display confusion matrix.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 10. Predict survival of a passenger (Age=30, Fare=50000, Sex=Male).
pred = model.predict([[30, 50000, 0]])  # Replace with actual feature values
print("Predicted survival for a passenger (Age=30, Fare=50000, Sex=Male):", pred[0])

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# SET 4 – Support Vector Machine (SVM)
# Questions:
# 1. Load dataset and display columns.
df = pd.read_csv('Social_Network_Ads.csv')
print("Columns in the dataset:", df.columns.tolist())

# 2. Select Age and EstimatedSalary as features.
X = df[['Age', 'EstimatedSalary']]

# 3. Select Purchased as target.
y = df['Purchased']  # Replace 'Purchased' with the actual target column name

# 4. Split the dataset into training and testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Apply SVM (linear kernel).
model = SVC(kernel='linear', random_state=42)

# 6. Predict test data.
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 7. Calculate accuracy.
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 8. Display confusion matrix.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 9. Display classification report.
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 10. Predict purchase for (Age=35, Salary=60000).
pred = model.predict([[35, 60000]])  # Replace with actual feature values
print("Predicted purchase for (Age=35, Salary=60000):", pred[0])


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# SET 5 – K-Means Clustering
# Questions:
# 1. Load dataset and display first 5 records.
df = pd.read_excel('Mall Customers.csv')
print("First 5 records:")
print(df.head())

# 2. Select Annual Income and Spending Score.
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]  # Replace with actual column names

# 3. Apply K-Means clustering (K=5).
model = KMeans(n_clusters=5, random_state=42)
model.fit(X)

# 4. Add a cluster column.
# df['Cluster'] = model.labels_
# or 
df['Cluster'] = model.predict(X)
print("Data with Cluster column:")

# 5. Display clustered data.
print(df.head())

# 6. Plot clusters using scatter plot.
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-Means Clustering of Mall Customers')
plt.show()

# 7. Change K value and observe changes.
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)
df['Cluster'] = model.predict(X)

# 8. USe different markers for each cluster and plot a graph.
markers = ['o', 's', 'D', '^', 'v']
# plt.figure(figsize=(8,6))

plt.scatter(df[df['Cluster']==0]['Annual Income (k$)'],
            df[df['Cluster']==0]['Spending Score (1-100)'],
            marker='o', label='Cluster 0')

plt.scatter(df[df['Cluster']==1]['Annual Income (k$)'],
            df[df['Cluster']==1]['Spending Score (1-100)'],
            marker='s', label='Cluster 1')

plt.scatter(df[df['Cluster']==2]['Annual Income (k$)'],
            df[df['Cluster']==2]['Spending Score (1-100)'],
            marker='^', label='Cluster 2')

plt.scatter(df[df['Cluster']==3]['Annual Income (k$)'],
            df[df['Cluster']==3]['Spending Score (1-100)'],
            marker='D', label='Cluster 3')

plt.scatter(df[df['Cluster']==4]['Annual Income (k$)'],
            df[df['Cluster']==4]['Spending Score (1-100)'],
            marker='*', label='Cluster 4')

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means Clustering")

plt.legend()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#  SET 6 – Hierarchical Clustering
# Questions:
# 1. Load dataset and display summary.
df = pd.read_csv('Mall Customers.csv')
print("Summary of the dataset:")
print(df.describe())

# 2. Select required features.
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]  # Replace with actual column names

# 3. Create a dendrogram.
plt.figure(figsize=(10, 7))
dend = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

# 4. Determine the number of clusters.
n_clusters = 5

# 5. Apply Agglomerative Clustering.
model = AgglomerativeClustering(n_clusters=n_clusters)
clusters = model.fit_predict(X)

# 6. Add cluster column.
df['Cluster'] = clusters
print("\nClustered Data:")
print(df.head())

# 7. Plot clusters using scatter plot.
plt.figure(figsize=(8,6))

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Hierarchical Clustering Result")

plt.show()

# 8. Compare with K-Means result.
from sklearn.cluster import KMeans

# Apply K-Means
kmeans = KMeans(n_clusters=5, random_state=0)
k_clusters = kmeans.fit_predict(X)

# Add to dataframe
df['KMeans_Cluster'] = k_clusters

# Plot K-Means clusters
plt.figure(figsize=(8,6))
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['KMeans_Cluster'], cmap='rainbow')
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clustering Result")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

#  SET 7 – Density-Based Clustering (DBSCAN)
# Questions:
# 1. Load dataset and display first 5 records.
df = pd.read_csv('Mall Customers.csv')
print("First 5 records:")

# 2. Select features for clustering.
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# 3. Scale the data.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply DBSCAN (eps, min_samples).
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# 5. Display cluster labels.
df['Cluster'] = clusters
print("Cluster labels assigned by DBSCAN:")
print(df['Cluster'].value_counts())

# 6. Identify noise points (-1).
noise_points = df[df['Cluster'] == -1]
print("\nNoise points identified by DBSCAN:")
print(noise_points)

# 7. Plot clusters.
plt.figure(figsize=(8,6))
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("DBSCAN Clustering Result")
plt.show()

# 8. Change eps value and observe results.
dbscan = DBSCAN(eps=0.3, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)
df['Cluster'] = clusters
print("\nCluster labels with eps=0.3:")
print(df['Cluster'].value_counts())

# 9. Compared with K-Means.
kmeans = KMeans(n_clusters=5, random_state=0)
k_clusters = kmeans.fit_predict(X_scaled)
df['KMeans_Cluster'] = k_clusters
print("\nCluster labels from K-Means:")
print(df['KMeans_Cluster'].value_counts())

# 10. Explain noise points.



#  SET 8 – Model Evaluation (Common)
# Dataset: Use any above dataset
# Questions:
# 1. Train any classification model.
# 2. Predict test data.
# 3. Calculate accuracy.
# 4. Display confusion matrix.
# 5. Generate classification report.
# 6. Explain precision and recall.
# 7. Compare two models.
# 8. Identify the best model.
# 9. Interpret results.