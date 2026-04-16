import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

# Display columns and their data types
print("Columns in file:", df.columns.tolist())
print("\nData types of each column:")
print(df.dtypes)
