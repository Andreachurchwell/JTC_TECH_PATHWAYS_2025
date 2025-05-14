# import pandas as pd
# import numpy as np
# # Sample weather data with missing values
# data = {
#     'date': pd.date_range('2023-01-01', periods=7),
#     'temperature': [32.5, 31.8, np.nan, 33.2, 32.7, np.nan, 34.1],
#     'humidity': [65, np.nan, 70, 68, np.nan, 67, 66],
#     'precipitation': [0.0, 0.2, 0.5, np.nan, 0.0, 0.1, 0.0]
# }
# weather_df = pd.DataFrame(data)
# print(weather_df)
# "Now let's check for missing values using different methods:"
# # Check for missing values
# print("Missing values per column:")
# print(weather_df.isna().sum())
# # Percentage of missing values per column
# print("\nPercentage of missing values per column:")
# print(weather_df.isna().mean() * 100)
# # Visual representation of missing values
# print("\nMissing value map:")
# print(weather_df.isna())
# # Total number of missing values
# total_missing = weather_df.isna().sum().sum()
# print(f"\nTotal missing values: {total_missing}")

# # Fill with a specific value
# filled_df = weather_df.fillna(0)
# print("DataFrame after filling missing values with 0:")
# print(filled_df)
# # Fill with column mean
# filled_df2 = weather_df.fillna(weather_df.mean())
# print("\nDataFrame after filling missing values with column means:")
# print(filled_df2)
# # Fill with column median
# filled_df3 = weather_df.fillna(weather_df.median())
# # Fill with different values for different columns
# fill_values = {'temperature': 32.0, 'humidity': 65, 'precipitation': 0.0}
# filled_df4 = weather_df.fillna(value=fill_values)



# Breakout 1:
# Breakout Session 1:
# Compare the results of different approaches

# import pandas as pd
# import numpy as np

# # Step 1: Create the dataset
# data = {
#     'date': pd.date_range('2023-02-01', periods=7),
#     'temperature': [29.5, np.nan, 30.3, 28.8, np.nan, 29.1, 30.7],
#     'humidity': [75, 72, np.nan, 74, 71, np.nan, 73],
#     'precipitation': [0.0, 0.2, 0.0, np.nan, 0.4, 0.0, 0.2]
# }

# df = pd.DataFrame(data)

# # Step 2: Check for missing values
# print("Missing values per column:\n", df.isnull().sum())
# print("\nFull DataFrame with missing values:\n", df)

# # Step 3: Handle missing data

# # Strategy 1: Drop rows with missing values
# df_dropna = df.dropna()

# # Strategy 2: Fill with column mean (fixed warning by avoiding inplace=True on chained assignment)
# df_fill_mean = df.copy()
# df_fill_mean['temperature'] = df_fill_mean['temperature'].fillna(df['temperature'].mean())
# df_fill_mean['humidity'] = df_fill_mean['humidity'].fillna(df['humidity'].mean())
# df_fill_mean['precipitation'] = df_fill_mean['precipitation'].fillna(df['precipitation'].mean())

# # Strategy 3: Forward fill using .ffill() (replaces deprecated method='ffill')
# df_ffill = df.ffill()

# # Step 4: Compare results
# print("\n--- After Dropping Rows ---")
# print(df_dropna)

# print("\n--- After Filling with Mean ---")
# print(df_fill_mean)

# print("\n--- After Forward Fill ---")
# print(df_ffill)

# # Step 5: Recommendation
# print("\nRecommendation:")
# print("Dropping rows is not ideal because we lose data.")
# print("Forward fill can be useful if weather changes slowly day to day.")
# print("Filling with mean keeps all data and is safe for small datasets.")
# print("=> Best approach: Fill with mean values for this specific dataset.")





# # option2
# import pandas as pd
# import numpy as np

# # Step 1: Create the dataset
# data = {
#     'date': pd.date_range('2023-02-01', periods=7),
#     'temperature': [29.5, np.nan, 30.3, 28.8, np.nan, 29.1, 30.7],
#     'humidity': [75, 72, np.nan, 74, 71, np.nan, 73],
#     'precipitation': [0.0, 0.2, 0.0, np.nan, 0.4, 0.0, 0.2]
# }
# df = pd.DataFrame(data)

# # Step 2: Show missing value summary
# print("Missing value count:\n", df.isnull().sum())
# print("\nMissing percentage by column:\n", df.isnull().mean() * 100)

# # Step 3: Different handling strategies

# # Strategy 1: Fill using median (less affected by outliers)
# df_median = df.copy()
# for col in ['temperature', 'humidity', 'precipitation']:
#     df_median[col] = df_median[col].fillna(df_median[col].median())

# # Strategy 2: Fill using a fixed value (custom domain knowledge)
# df_fixed = df.copy()
# df_fixed['temperature'] = df_fixed['temperature'].fillna(29.0)      # assuming 29 is a common expected temp
# df_fixed['humidity'] = df_fixed['humidity'].fillna(73)             # recent average humidity
# df_fixed['precipitation'] = df_fixed['precipitation'].fillna(0.1)  # light rain

# # Strategy 3: Interpolation (linear)
# df_interp = df.copy()
# df_interp[['temperature', 'humidity', 'precipitation']] = df_interp[['temperature', 'humidity', 'precipitation']].interpolate(method='linear')

# # Step 4: Show comparisons
# print("\n--- Median Fill ---")
# print(df_median)

# print("\n--- Fixed Value Fill ---")
# print(df_fixed)

# print("\n--- Interpolation ---")
# print(df_interp)

# # Step 5: Recommend based on context
# print("\nRecommendation:")
# print("Median is safer than mean when outliers are possible.")
# print("Fixed values are risky unless based on domain knowledge.")
# print("Interpolation is great if time-based data has smooth trends.")
# print("=> Recommended: Use interpolation if values change gradually (like weather often does).")




import pandas as pd
import numpy as np
# Sample data with inconsistent types
data = {
    'date': ['2023-01-01', '1/2/2023', 'Jan 3, 2023', '2023-01-04', '1/5/23'],
    'temperature': ['32.5°F', '31.8', '33.4 F', '32°C', 31.2],
    'humidity': ['65%', '70', '68 percent', '67%', '66 %'],
    'precipitation': ['0 mm', '0.2"', '0.5 in', '0', '0.1 inches']
}

# Create DataFrame
messy_df = pd.DataFrame(data)

print("Original messy DataFrame:")
print(messy_df)
print("\nData types:")
print(messy_df.dtypes)

# --- Clean the data ---


# Convert date column to datetime with better format inference

# Add a column with the time part of the datetime

# Clean temperature column
messy_df['temperature'] = messy_df['temperature'].astype(str).str.replace(r'[^\d\.]+', '', regex=True)
messy_df['temperature'] = pd.to_numeric(messy_df['temperature'], errors='coerce').round(1)

# Clean humidity column
messy_df['humidity'] = messy_df['humidity'].astype(str).str.replace(r'[^\d]+', '', regex=True)
messy_df['humidity'] = pd.to_numeric(messy_df['humidity'], errors='coerce').astype('Int64')  # Nullable integer

# Clean precipitation column
messy_df['precipitation'] = messy_df['precipitation'].astype(str).str.replace(r'[^\d\.]+', '', regex=True)
messy_df['precipitation'] = pd.to_numeric(messy_df['precipitation'], errors='coerce').round(2)

# Final output
print("\nCleaned DataFrame:")
print(messy_df)
print("\nData types after cleaning:")
print(messy_df.dtypes)

