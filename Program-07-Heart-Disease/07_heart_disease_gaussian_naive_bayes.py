# Program 7: Heart Disease Classification using Gaussian Naive Bayes
# Note: The supplied implementation uses GaussianNB, not a true Bayesian Network.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

data = pd.read_csv("heart_disease.csv")

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\nEnter New Patient Details:")
patient_data = []

for column in X.columns:
    value = float(input("Enter " + column + ": "))
    patient_data.append(value)

patient = pd.DataFrame([patient_data], columns=X.columns)

result = model.predict(patient)

if result[0] == 1:
    print("Patient may have Heart Disease")
else:
    print("Patient may not have Heart Disease")

actual = int(input("Enter actual result (1 = Disease, 0 = No Disease): "))

if result[0] == actual:
    print("Prediction is Correct")
else:
    print("Prediction is Wrong")
