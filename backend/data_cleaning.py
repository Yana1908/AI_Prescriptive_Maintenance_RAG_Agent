import pandas as pd

# ==========================
# Load Dataset
# ==========================

file_path = "data/predictive_maintenance_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("Original Dataset Information")
print("=" * 50)

print("\nShape :", df.shape)

print("\nColumns :")
print(df.columns.tolist())

print("\nData Types :")
print(df.dtypes)

# ==========================
# Check Missing Values
# ==========================

print("\nChecking Missing Values...\n")

print(df.isnull().sum())

# ==========================
# Fill Missing Values
# ==========================

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

text_columns = df.select_dtypes(include=["object"]).columns

for col in text_columns:
    df[col] = df[col].fillna("Unknown")

# ==========================
# Remove Duplicate Records
# ==========================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows :", duplicates)

df = df.drop_duplicates()

# ==========================
# Final Check
# ==========================

print("\nRemaining Missing Values\n")

print(df.isnull().sum())

print("\nFinal Shape :", df.shape)

# ==========================
# Save Clean Dataset
# ==========================

output_path = "data/cleaned_predictive_maintenance_dataset.csv"

df.to_csv(output_path, index=False)

print("\nDataset cleaned successfully.")

print("\nSaved at :", output_path)