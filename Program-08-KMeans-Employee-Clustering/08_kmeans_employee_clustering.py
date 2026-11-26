# Program 8: K-Means Clustering using Employee Salary Dataset

import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("employee_salary.csv")

X = data[["Age", "Experience", "Salary"]]

model = KMeans(n_clusters=3, random_state=42, n_init=10)
data["Cluster"] = model.fit_predict(X)

print("Clustered Employee Data:\n", data)
print("\nCluster Centers:\n", model.cluster_centers_)

age = float(input("Enter Age: "))
experience = float(input("Enter Experience: "))
salary = float(input("Enter Salary: "))

new_employee = pd.DataFrame(
    [[age, experience, salary]],
    columns=["Age", "Experience", "Salary"]
)

result = model.predict(new_employee)
print("Employee belongs to Cluster:", result[0])

# Cluster numbers are arbitrary. Check cluster centres before assigning
# business labels such as Junior, Mid-Level, or Senior.
