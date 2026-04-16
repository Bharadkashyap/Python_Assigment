import pandas as pd

df = pd.read_excel("students.xlsx")

# List of students from Rajkot City
print("\nStudents from Rajkot City:")
print(df[df["City"] == "Rajkot"])

# List of Male students
print("\nMale Students:")
print(df[df["Gender"] == "Male"])

# List of Male students from Rajkot City
print("\nMale Students from Rajkot City:")
print(df[(df["Gender"] == "Male") & (df["City"] == "Rajkot")])

# List of students whose age >= 20
print("\nStudents with Age >= 20:")
print(df[df["Age"] >= 20])
