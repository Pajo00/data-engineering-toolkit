import pandas as pd

# Read transformed data
df = pd.read_csv("transformed_data.csv")

print("Data ready for loading:")
print(df)

# Save to CSV
df.to_csv("clean_data.csv", index=False)
print("✅ Data successfully loaded to clean_data.csv")

# Save to Parquet
df.to_parquet("clean_data.parquet", index=False)
print("✅ Data successfully loaded to clean_data.parquet")