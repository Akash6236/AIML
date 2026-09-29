import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("diabetes.csv")
print("Dataset")
print(data.head())

X = data[["Glucose","BloodPressure","BMI","Age"]]
y = data["Diabetes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(8, activation="relu", input_shape=(4,)))
model.add(Dense(4, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(
 optimizer="adam",
 loss="binary_crossentropy",
 metrics=["accuracy"])

model.fit(
 X_train,
 y_train,
 epochs=100,
 batch_size=4,
 verbose=0)


prediction = model.predict(X_test)
prediction = (prediction > 0.5)
accuracy = accuracy_score(y_test,prediction)

print("\nModel Accuracy : {:.2f}%".format(accuracy*100))
print("\n==============================")
print("Diabetes Prediction")
print("==============================")

glucose = float(input("Enter Glucose Level : "))
bp = float(input("Enter Blood Pressure : "))
bmi = float(input("Enter BMI : "))
age = float(input("Enter Age : "))
new_patient = pd.DataFrame({
 "Glucose":[glucose],
 "BloodPressure":[bp],
 "BMI":[bmi],
 "Age":[age]})
new_patient = scaler.transform(new_patient)
result = model.predict(new_patient)

print("\nPrediction")
if result[0][0] > 0.5:
 print("Patient is Diabetic")
else:
 print("Patient is Non-Diabetic")
