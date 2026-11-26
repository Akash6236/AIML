# Program 1(g): Student Marks Analysis using Pandas

import pandas as pd

data = {
    "Name": ["Anu", "Ravi", "Kiran", "Meena", "John"],
    "Marks": [85, 72, 91, 66, 78],
    "Department": ["MCA", "BCA", "MCA", "BCA", "MCA"]
}

df = pd.DataFrame(data)

print("Student Data:\n", df)
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())

print("\nStudents scoring above 80:\n", df[df["Marks"] > 80])

print("\nDepartment-wise Average Marks:\n",
      df.groupby("Department")["Marks"].mean())
