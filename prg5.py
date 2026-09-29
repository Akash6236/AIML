import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("emailspam.csv")
print("Dataset")
print(data.head())

X = data[["Message"]]
y = data["Category"]

Vectorizer=CountVectorizer()

X=vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model=multinomialNB()
model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("\n Actual values")
print(y_test.values)

print("\n predicted values")
print(prediction)

accuracy=accuracy_score(y_test,prediction)

print("\nModel Accuracy : {:.2f}%".format(accuracy*100))
print("\n==============================")
print("Email spam Prediction")
print("==============================")

email=input("enter email message:")
email_vector=Vectorizer.transform([email])



result=model.predict(email_vector)

print("\n prediction")

if result[0]=="spam":
    print("spam email")
else:
    print("not spam email")