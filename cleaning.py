import pandas as pd

data = {
    "Name": ["Alice", "bob", "Charlie", "Alice", "Eve", None],
    "Age": [25, None, 30, 25, 22, 28],
    "Email": ["ALICE@example.com", "bob@EXAMPLE.com", None, "alice@example.com", "eve@Example.Com", "frank@example.com"],
    "Salary": ["50000", "60000", "55000", "50000", "45000", "70000"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Basic Data Cleaning
# - Drop duplicates
df = df.drop_duplicates()

# - Handle missing values (fill missing Age with mean, Email with placeholder)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Email"].fillna("no_email_provided@example.com", inplace=True)

# - Standardize text columns (lowercase emails and names, strip spaces)
df["Name"] = df["Name"].str.strip().str.title()   
df["Email"] = df["Email"].str.lower().str.strip()

# - Convert Salary to numeric
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Final Clean DataFrame
print("\nCleaned DataFrame:")
print(df)
