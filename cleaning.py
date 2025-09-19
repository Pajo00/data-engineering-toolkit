import pandas as pd

# Create dummy raw data
dummy_data = {
    "Name": ["Alice", "bob", "Charlie", "Alice", "Eve", None],
    "Age": [25, None, 30, 25, 22, 28],
    "Email": [
        "ALICE@example.com",
        "bob@EXAMPLE.com",
        None,
        "alice@example.com",
        "eve@Example.Com",
        "frank@example.com"
    ],
    "Salary": ["50000", "60000", "55000", "50000", "45000", "70000"]
}

raw_df = pd.DataFrame(dummy_data)

# Clean the data
raw_df = raw_df.drop_duplicates()
raw_df["Age"].fillna(raw_df["Age"].mean(), inplace=True)
raw_df["Email"].fillna("no_email_provided@example.com", inplace=True)
raw_df["Name"] = raw_df["Name"].str.strip().str.title()
raw_df["Email"] = raw_df["Email"].str.lower().str.strip()
raw_df["Salary"] = pd.to_numeric(raw_df["Salary"], errors="coerce")

print("✅ Cleaning complete in cleaning.py")

# Export cleaned DataFrame so it can be used in other scripts
cleaned_df = raw_df
