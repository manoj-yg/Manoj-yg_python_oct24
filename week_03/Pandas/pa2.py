import pandas as pd

# Sample CSV data (replace 'sample.csv' with your file path)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, None, 35],
    "Salary": [50000, 54000, 61000, None]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values in Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Drop rows with missing Salary values
df = df.dropna(subset=["Salary"])

# Add a new column for Salary after a 10% increment
df["Updated Salary"] = df["Salary"] * 1.1

print("\nCleaned DataFrame:")
print(df)

# Save the cleaned DataFrame to a new CSV file
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved to 'cleaned_data.csv'.")
