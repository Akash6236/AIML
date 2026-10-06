import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data=pd.read_csv("news_dataset.csv")
print("Dataset")
print(data.head())

X=data["Document"]
y=data["Category"]

Vectorizer=CountVectorizer()

X=Vectorizer.fit_transform(X)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)
model=MultinomialNB()
model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("\n Actual Categories")
print(y_test.values)
print("\n Predicted Categories")
print(prediction)

accuracy=accuracy_score(y_test,prediction)
precision=precision_score(y_test,prediction,average="weighted")
recall=recall_score(y_test,prediction,average="weighted")

print("\n Model Performance")
print("------")
print(f"Accuracy:{accuracy*100:.2f}%")
print(f"Precision:{precision*100:.2f}%")
print(f"Recall:{recall*100:.2f}%")

print("\n------")

print("News Articel classification")

print("\n------")

news=input("enter the news article:")
news_vector=Vectorizer.transform([news])
predicted=model.predict(news_vector)[0]

print("\n Predicted category:",predicted)
actual=input("enter actual category(Sports/technology/politics):")

print("\n------")

print("\nPrediction result")

print("\n------")

print("actual category:",actual)
print("Predicted Category:",predicted)

if predicted.lower()==actual.lower():
    print("\n predicted Status:Correct")
    print("Accuracy for this sample:100%")

else:
    print("\n predicted Status:incorrect")
    print("Accuracy for this sample:0%")









