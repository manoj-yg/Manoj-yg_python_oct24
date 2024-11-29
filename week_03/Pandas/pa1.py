import pandas as pd

# Create a DataFrame
data = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Monitor"],
    "Price": [800, 300, 500, 200],
    "Quantity": [5, 8, 10, 6]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Initial DataFrame:")
print(df)

# Calculate total sales (Price * Quantity)
df["Total Sales"] = df["Price"] * df["Quantity"]
print("\nDataFrame with Total Sales:")
print(df)

# Filter products with Total Sales > 3000
high_sales = df[df["Total Sales"] > 3000]
print("\nProducts with Total Sales > 3000:")
print(high_sales)

# Calculate summary statistics
print("\nSummary Statistics:")
print(df.describe())
