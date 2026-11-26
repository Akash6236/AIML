# Program 9: K-Nearest Neighbors classification using Iris dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("iris.csv", sep="\t")

print(data.head())
print(data.columns)

X = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

correct = 0
wrong = 0

for actual, predicted in zip(y_test, y_pred):
    if actual == predicted:
        print("Correct Prediction:", actual)
        correct += 1
    else:
        print("Wrong Prediction:", actual, predicted)
        wrong += 1

print("Correct Predictions:", correct)
print("Wrong Predictions:", wrong)
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nEnter New Flower Details:")
sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))
pl = float(input("Enter Petal Length: "))
pw = float(input("Enter Petal Width: "))

new_flower = pd.DataFrame(
    [[sl, sw, pl, pw]], columns=X.columns
)

result = model.predict(new_flower)
print("Predicted Flower Species:", result[0])
