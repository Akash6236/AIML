# Program 6: Naive Bayesian Classifier for Document Classification
# Official question mentions Java APIs; this is the Python implementation
# used for practical preparation.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv("news_dataset.csv")

X = data["Document"]
y = data["Category"]

cv = CountVectorizer()
X = cv.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average="weighted", zero_division=0))
print("Recall:", recall_score(y_test, y_pred, average="weighted", zero_division=0))

news = input("\nEnter a news document: ")
news_vector = cv.transform([news])
result = model.predict(news_vector)

print("Predicted Category:", result[0])

actual = input("Enter actual category: ")

if result[0] == actual:
    print("Prediction is Correct")
else:
    print("Prediction is Wrong")
