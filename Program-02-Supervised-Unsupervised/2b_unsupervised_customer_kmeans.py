# Program 2(b): Unsupervised Learning using K-Means

import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("customer_segmentation.csv")

X = data[["Age", "Income", "SpendingScore"]]

model = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = model.fit_predict(X)

print("Customer Segmentation:\n", data)

age = float(input("Enter customer Age: "))
income = float(input("Enter customer Income: "))
score = float(input("Enter Spending Score: "))

new_customer = pd.DataFrame(
    [[age, income, score]],
    columns=["Age", "Income", "SpendingScore"]
)

result = model.predict(new_customer)
print("Customer belongs to Cluster:", result[0])
