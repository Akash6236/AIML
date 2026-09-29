import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv("student_performance.csv")
print("Dataset:")
print(data.head(10))

X=data.iloc[:,:-1]
y=data.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
prediction=model.predict(X_test)


print("\nActual values:")
print(y_test.values)

print("\npredicted values")
print(prediction)

print("\n Accuracy:")
print(accuracy_score(y_test,prediction)*100)

