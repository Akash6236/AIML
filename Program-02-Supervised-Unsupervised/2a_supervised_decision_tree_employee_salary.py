# Program 2(a): Supervised Learning using Decision Tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("emp_salary.csv")

X = data[["Age", "Experience", "Education"]]
y = data["Salary"]

# If Education contains text labels, encode them before training.
# This example expects numeric feature columns.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

age = float(input("Enter Age: "))
experience = float(input("Enter Experience: "))
education = float(input("Enter Education value: "))

new_employee = pd.DataFrame(
    [[age, experience, education]],
    columns=["Age", "Experience", "Education"]
)

result = model.predict(new_employee)
print("Predicted Salary Category:", result[0])
