import pandas as pd

df = pd.read_excel("students.xlsx")

# Drop rows with missing values
print("\nAfter dropna():")
print(df.dropna())

# Fill missing values with default values
print("\nAfter fillna():")
print(df.fillna("Not Available"))
