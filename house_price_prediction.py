import pandas as pd

# Step 1: Load Dataset
df = pd.read_csv("house_price_data.csv")
print("✅ Dataset Loaded")
print(df.head())

# Step 2: Check & Drop Duplicates
df.drop_duplicates(inplace=True)

# Step 3: Handle Missing Values
df.dropna(inplace=True)  # Alternatively: df.fillna(method='ffill', inplace=True)

# Step 4: Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.dropna(subset=['date'], inplace=True)  # Drop rows where date couldn't be parsed

# Step 5: Drop unnecessary columns (if they exist)
columns_to_drop = ['id', 'zipcode', 'city', 'statezip', 'country', 'street']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], axis=1)

# Step 6: Check for non-numeric values (safety check)
for col in df.columns:
    if df[col].dtype == 'object':
        print(f"⚠️ Column '{col}' has non-numeric values")
        df = df[df[col].str.replace(' ', '').str.isnumeric()]  # Drop rows with text
        df[col] = pd.to_numeric(df[col])

# Step 7: Save Cleaned Data
df.to_csv("cleaned_housing.csv", index=False)
print("✅ Cleaned data saved to 'cleaned_housing.csv'")
