# ---------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ---------------------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ---------------------------------------------------------
# 2. LOAD DATASET
# ---------------------------------------------------------

data = pd.read_csv("/content/sample_data/employee_promotion_dataset.csv")

print("Dataset Preview:")
print(data.head())


# ---------------------------------------------------------
# 3. DEFINE FEATURES AND TARGET
# ---------------------------------------------------------

# Input features
X = data.drop("performance", axis=1)

# Target variable
y = data["performance"]


# ---------------------------------------------------------
# 4. SPLIT DATASET INTO TRAINING AND TESTING
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print("\nTraining Data Size:", X_train.shape)
print("Testing Data Size:", X_test.shape)


# ---------------------------------------------------------
# 5. CREATE DECISION TREE MODEL
# ---------------------------------------------------------

model = DecisionTreeClassifier(max_depth=4)

# Train the model
model.fit(X_train, y_train)


# ---------------------------------------------------------
# 6. MAKE PREDICTIONS
# ---------------------------------------------------------

y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)


# ---------------------------------------------------------
# 7. MODEL EVALUATION
# ---------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ---------------------------------------------------------
# 8. NEW SAMPLE PREDICTION
# ---------------------------------------------------------

# Example employee data
new_employee = [[35, 70000, 8, 3, 45]]

prediction = model.predict(new_employee)

print("\nPredicted Performance:", prediction[0])
