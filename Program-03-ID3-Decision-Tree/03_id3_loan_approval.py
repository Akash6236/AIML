# Program 3: ID3-style Decision Tree using Entropy for Loan Approval
# sklearn DecisionTreeClassifier with criterion="entropy" is an
# entropy-based tree implementation; it is not a hand-coded ID3 algorithm.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("loan_approval.csv")

X = data[["Age", "Income", "CreditScore", "Experience"]]
y = data["LoanApproved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

age = float(input("Enter Age: "))
income = float(input("Enter Income: "))
credit_score = float(input("Enter Credit Score: "))
experience = float(input("Enter Experience: "))

new_customer = pd.DataFrame(
    [[age, income, credit_score, experience]],
    columns=["Age", "Income", "CreditScore", "Experience"]
)

result = model.predict(new_customer)
print("Loan Approval Prediction:", result[0])
