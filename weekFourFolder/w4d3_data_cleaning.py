# # 💀 The Boring Title: Working with Missing Data
# # What it really means:
# # How to deal with things like NaN or None in your data.

# # 🔍 1. What's considered “missing”?
# # In pandas, missing values are typically represented as:

# # np.nan (Not a Number)

# # None (Python’s version of null)

# # Mini example:


# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'name': ['Alice', 'Bob', None],
#     'score': [9.5, np.nan, 7.0]
# })
# print(df)
# # ✅ 2. How to check what’s missing
# # Use:

# # df.isna() – returns True where values are missing

# # df.notna() – returns True where values are not missing

# # Example:

# print(df.isna())
# # 🧹 3. How to drop missing data
# # Use dropna():


# df.dropna()  # Drops rows with ANY missing values
# df.dropna(axis=1)  # Drops columns instead
# # 🩹 4. How to fill missing data
# # Use fillna():

# df.fillna(0)  # Replace NaNs with 0
# df['score'].fillna(df['score'].mean())  # Replace with column average
# # 🔄 5. More advanced options
# # method='ffill' – forward fill (fills with the value above)

# # method='bfill' – backward fill (fills with the value below)


# df.fillna(method='ffill')
# # TL;DR Cheat Sheet:
# # Task	                Function
# # Find missing	         df.isna()
# # Remove missing	         df.dropna()
# # Replace missing	          df.fillna(value)
# # Forward fill	         df.fillna(method='ffill')
# # Backward fill	         df.fillna(method='bfill')




# import pandas as pd

# # Your original data
# data = {
#     'customer_id': [101, 102, 103, 104, 102, 106, 107, 108, 109, 110],
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', 'Eve', 'Allice', 'Frank', 'Grace', None],
#     'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Los Angeles', 'San Diego', 'new york', 'Austin', 'Miami', 'Boston'],
#     'signup_date': ['2021-01-10', '2021/01/15', '15-01-2021', '2021.01.20', None, '2021-01-25', '2021-01-25', '2021-02-01', '2021-02-01', '2021-02-05'],
#     'age': [25, 30, -1, 45, 30, None, 29, 33, 40, 50],
#     'amount': ['100', '200', '300', '400', '200', '500', 'invalid', '700', '800', '900']
# }

# df = pd.DataFrame(data)

# # 1️⃣ Remove Duplicates
# df.drop_duplicates(inplace=True)
# df = df.drop_duplicates(subset='customer_id')

# # 2️⃣ Spelling Errors
# print(df['name'].value_counts())  # Look for weird spellings
# df['name'] = df['name'].replace({'Allice': 'Alice'})  # Fix typo
# df['city'] = df['city'].str.title()  # Fix capitalization

# # 3️⃣ Highlight Errors
# print(df[df['age'] < 0])  # Age shouldn't be negative

# # Optional: add a column for invalid age
# df['invalid_age'] = df['age'] < 0

# # 4️⃣ Null Values
# print(df.isna().sum())  # Count nulls

# # Fill missing names and ages with placeholders
# df['name'] = df['name'].fillna('Unknown')
# df['age'] = df['age'].fillna(df['age'].median())  # Median is good for age

# # 5️⃣ Fix Data Types
# df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Turn 'invalid' to NaN
# df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

# # 6️⃣ Replication (no email, so let's check by name and signup_date)
# duplicates = df[df.duplicated(subset=['name', 'signup_date'], keep=False)]
# print(duplicates)


import pandas as pd

# Load the data from the URL
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
df = pd.read_csv(url, header=None)  # Read without any header

# Assign column names manually
df.columns = ['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip']

# Inspect the first few rows and columns
print(df.head())
print(df.columns)

# Now you can perform cleaning tasks, for example:
# Fill missing values for 'Address' column
df['Address'] = df['Address'].fillna('Unknown')

# Drop duplicates if needed
df.drop_duplicates(inplace=True)

# Remove unnecessary columns, if any
df.drop(['State'], axis=1, inplace=True)  # Example of removing a column

# Save the cleaned data
df.to_csv('cleaned_data.csv', index=False)


