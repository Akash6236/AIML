import pandas as pd
data={
    "Name":["Abhiram","raju","shyam","raghu"],
    "Marks":[45,23,32,34],
    "Department":["CSE","MCA","BCA","ECE"]
}
df=pd.DataFrame(data)
print(df)
print("\n average marks")
print(df["Marks"].mean())

print("\n higest marks")
print(df["Marks"].max())

print("\n student above 80")
print(df["Marks"]>80)

print("\n Department wise average")
print(df.groupby("Department")["Marks"].mean())
