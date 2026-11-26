# Program 5: Naive Bayes Email Spam Classification

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("emailspam.csv")

X = data["Message"]
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

email = input("\nEnter an email message: ")
email_vector = cv.transform([email])

result = model.predict(email_vector)
print("Email Category:", result[0])
