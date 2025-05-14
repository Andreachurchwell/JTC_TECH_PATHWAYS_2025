import pandas as pd
import numpy as np

data = {
    'customer_id': [101, 102, 103, 104, 102, 106, 107, 108, 109, 110],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', 'Eve', 'Allice', 'Frank', 'Grace', None],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Los Angeles', 'San Diego', 'new york', 'Austin', 'Miami', 'Boston'],
    'signup_date': ['2021-01-10', '2021/01/15', '15-01-2021', '2021.01.20', None, '2021-01-25', '2021-01-25', '2021-02-01', '2021-02-01', '2021-02-05'],
    'age': [25, 30, -1, 45, 30, None, 29, 33, 40, 50],
    'purchase_amount': ['100', '200', '300', '400', '200', '500', 'invalid', '700', '800', '900'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com', 'bob@email.com', 'eve@email.com', 'allice@email.com', 'frank@email.com', 'grace@email.com', ''],
}

df = pd.DataFrame(data)
# print('data==',data)
# print(df.head())
# print(df.info())
# print(df.describe())
# print('missing vals=',df.isna())

# df['age'].fillna(df['age'].median())
print('Missing values per column:', df.isna().sum())
df['name'] = df['name'].fillna('Unknown')
df['age'] = df['age'].fillna(df['age'].median())
# Step 1: Standardize 'signup_date' to datetime
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
# Step 2: Clean 'purchase_amount' to numeric, invalid values become NaN
df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')
# Step 3: Handle negative age by setting it to NaN
df['age'] = df['age'].apply(lambda x: np.nan if x < 0 else x)
print('Cleaned Data Frame: ')
print('dataframe=',df)