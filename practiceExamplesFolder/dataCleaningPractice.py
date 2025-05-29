# import pandas as pd
# import numpy as np

# data = {
#     'customer_id': [101, 102, 103, 104, 102, 106, 107, 108, 109, 110],
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', 'Eve', 'Allice', 'Frank', 'Grace', None],
#     'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Los Angeles', 'San Diego', 'new york', 'Austin', 'Miami', 'Boston'],
#     'signup_date': ['2021-01-10', '2021/01/15', '15-01-2021', '2021.01.20', None, '2021-01-25', '2021-01-25', '2021-02-01', '2021-02-01', '2021-02-05'],
#     'age': [25, 30, -1, 45, 30, None, 29, 33, 40, 50],
#     'purchase_amount': ['100', '200', '300', '400', '200', '500', 'invalid', '700', '800', '900'],
#     'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com', 'bob@email.com', 'eve@email.com', 'allice@email.com', 'frank@email.com', 'grace@email.com', ''],
# }

# df = pd.DataFrame(data)
# # print('data==',data)
# # print(df.head())
# # print(df.info())
# # print(df.describe())
# # print('missing vals=',df.isna())

# # df['age'].fillna(df['age'].median())
# print('Missing values per column:', df.isna().sum())
# df['name'] = df['name'].fillna('Unknown')
# df['age'] = df['age'].fillna(df['age'].median())
# # Step 1: Standardize 'signup_date' to datetime
# df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
# # Step 2: Clean 'purchase_amount' to numeric, invalid values become NaN
# df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')
# # Step 3: Handle negative age by setting it to NaN
# df['age'] = df['age'].apply(lambda x: np.nan if x < 0 else x)
# print('Cleaned Data Frame: ')
# print('dataframe=',df)





# import pandas as pd

# # Sample weather data
# data = {
#     "date": ["2025-05-10", "2025-05-11", "2025-05-12", "2025-05-13", "2025-05-14"],
#     "temp_max": [78, 85, 80, 90, 75],
#     "temp_min": [60, 65, 62, 70, 58],
#     "condition": ["sunny", "rain", "cloudy", "sunny", "rain"],
#     "precipitation": [0.0, 1.2, 0.0, 0.0, 0.8]
# }

# weather_df = pd.DataFrame(data)
# # print(weather_df)

# # Practice Questions for You
# # Try answering these by writing pandas code that uses weather_df:

# # Get all days where the max temperature was above 80 degrees.
# hot_days = weather_df[weather_df['temp_max'] > 80]
# # print(hot_days)
# # Find the average minimum temperature for days that had rain.
# avg_min_temp = weather_df[weather_df['condition'] == 'rain']
# # print(avg_min_temp.mean())
# # print(avg_min_temp)
# avg_min_temp_rainy_days = avg_min_temp['temp_min'].mean()
# print(avg_min_temp_rainy_days)
# # Get the date(s) when the precipitation was 0.0 (no rain).
# no_rain_dates = weather_df[weather_df['precipitation']==0.0]
# print(no_rain_dates)
# # Add a new column called temp_range which is the difference between max and min temperatures.
# weather_df['temp_range'] =weather_df['temp_max'] - weather_df['temp_min']
# print(weather_df[['date','temp_max','temp_min','temp_range']])
# # Find the day with the largest temperature range.



# # New Practice Questions:
# # Get all days where the minimum temperature was below 60 degrees.
# cold_days = weather_df[weather_df['temp_min'] < 60]
# print(cold_days)
# # Find the total precipitation over all days.
# rain_total = weather_df[weather_df["condition"] == 'rain']
# sum_rain_total = rain_total['precipitation'].sum()
# print(sum_rain_total)
# List the unique weather conditions in the DataFrame.

# Sort the DataFrame by max temperature in descending order.

# Create a new column is_hot that is True if max temp is over 85, otherwise False.