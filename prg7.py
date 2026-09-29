import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

data=pd.read_csv("heart_disease.csv")
print("Heart Disease Dataset")
print(data.head())

X=data.iloc[:,:-1]
y=data.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)
model=GaussianNB()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("\n Actual values")
print(y_test.values)

print("\n predicted values")
print(prediction)

accuracy=accuracy_score(y_test,prediction)
precision=precision_score(y_test,prediction)
recall=recall_score(y_test,prediction)

print("------")
print("\n Model Performance")
print("------")

print(f"Accuracy:{accuracy*100:.2f}%")
print(f"Precision:{precision*100:.2f}%")
print(f"Recall:{recall*100:.2f}%")

print("\n Confusion Matrix")

print(confusion_matrix(y_test,prediction))

print("------")
print("\n Heart Disease Prediction")
print("------")

age=int(input("enter the age:"))
bp=int(input("enter blood pressure"))
chol=int(input("enter cholestreol"))
hr=int(input("enter maximum heart rate:"))
cp=int(input("chest pain(0=no,1=yes):"))
patient=pd.DataFrame([[age,bp,chol,hr,cp]],columns=X.columns)
result=model.predict(patient)

print("\n Prediction")
if result[0]==1:
    print("heart disease detected")
else:
    print("No heart disease")

actual=int(input("\n enter actual(0=no disease):"))

print("\n------")

print("\nPrediction result")

print("\n------")
print("actual value:",actual)
print("Predicted value:",result[0])

if actual==result[0]:
    print("\n Prediction correct")
    print("sample accuracy:100%")
else:
    print("\n Prediction incorrect")
    print("sample accuracy:0%")


