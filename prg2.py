import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("emp_salary.csv")
print("Employee Salary Dataset")
print(data)

X = data[["Age", "Experience", "Education"]]
y = data["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("\nActual Values")
print(y_test.values)
print("\nPredicted Values")
print(prediction)
print("\nAccuracy : {:.2f}%".format(accuracy_score(y_test, prediction) * 100))
print("\nEmployee Salary Prediction")

age = int(input("Enter Age : "))
exp = int(input("Enter Experience : "))
edu = int(input("Enter Education Years : "))
employee = pd.DataFrame([[age, exp, edu]], columns=X.columns)
result = model.predict(employee)

print("\nPrediction")
if result[0] == "High":
    print("High Salary Employee")
else:
    print("Low Salary Employee")