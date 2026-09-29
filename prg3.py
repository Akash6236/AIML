import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("loan_approval.csv")
print("Loan approval Dataset")
print(data)

X = data[["Age", "Income","CreditScore", "Experience"]]
y = data["LoanApproved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = DecisionTreeClassifier(criterion="entropy",random_state=42)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("\nActual Values")
print(y_test.values)
print("\nPredicted Values")
print(prediction)
print("\n Accuracy")
print(accuracy_score(y_test,prediction)*100)

print("\n ------loan approved prediction-------")

age=int(input("enter the age:"))
income=int(input("enter monthly income:"))
credit=int(input("enter credit score:"))
experience = int(input("enter years of experience: ")) 

new_customer = pd.DataFrame( [[age, income, credit, experience]], 
columns=["Age", "Income", "CreditScore", "Experience"]) 
result = model.predict(new_customer) 
if result[0] == "Yes": 
    print("\nLoan Approved") 
else: 
    print("\nLoan Rejected") 
    
prediction = model.predict(X_test) 
accuracy = accuracy_score(y_test, prediction) * 100 
print("\n--------------------------------") 
print("Model Performance") 
print("--------------------------------") 
print(f"Accuracy : {accuracy:.2f}%")