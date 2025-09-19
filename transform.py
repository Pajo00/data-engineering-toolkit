import pandas as pd
from cleaning import cleaned_df  
print("Data from cleaning.py:")
print(cleaned_df)

# Add a new column for Salary in thousands
cleaned_df["Salary_K"] = cleaned_df["Salary"] / 1000

# Add a column that categorizes Age groups
cleaned_df["Age_Group"] = pd.cut(
    cleaned_df["Age"],
    bins=[0, 20, 30, 40, 100],
    labels=["<20", "20-30", "30-40", "40+"]
)

print("\n✅ Transformation complete in transform.py")
print(cleaned_df)

# Save transformed dataset for loading step
cleaned_df.to_csv("transformed_data.csv", index=False)