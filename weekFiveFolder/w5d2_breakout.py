# # Choose appropriate aggregation functions
# # Interpret the results
# # Create a visualization if time permits
# # Prepare to share your most interesting finding with the class
# # Expected Output:
# # At least three different GroupBy analyses
# # Written interpretations of what each analysis reveals
# # (Optional) Visualizations to illustrate findings
# # Discussion Points:
# # What unexpected patterns did you discover in the data?
# # Which grouping variables provided the most interesting insights?
# # What challenges did you encounter when implementing GroupBy operations?
# # How might these techniques be useful in your weather project?



# import pandas as pd
# import matplotlib.pyplot as plt

# # Step 1: Load the dataset
# weather_data = pd.read_csv('weekFiveFolder/w5d2inclassweather.csv.csv')  # Replace with your actual filename

# # Step 2: Convert 'date' column to datetime format
# weather_data['date'] = pd.to_datetime(weather_data['date'])
# print(weather_data.head())
# # Step 3: Extract month from date
# weather_data['month'] = weather_data['date'].dt.month

# # Step 4: Map each month to a season
# def get_season(month):
#     if month in [12, 1, 2]:
#         return 'Winter'
#     elif month in [3, 4, 5]:
#         return 'Spring'
#     elif month in [6, 7, 8]:
#         return 'Summer'
#     elif month in [9, 10, 11]:
#         return 'Fall'

# weather_data['season'] = weather_data['month'].apply(get_season)

# # ------------------------------
# # GroupBy Analysis 1: Average Temperature by Season
# avg_temp_by_season = weather_data.groupby('season')['temperature'].mean().sort_values()
# print("Average Temperature by Season:")
# print(avg_temp_by_season)

# # Optional plot
# avg_temp_by_season.plot(kind='bar', title='Average Temperature by Season', ylabel='Temperature')
# plt.show()

# # ------------------------------
# # GroupBy Analysis 2: Total Precipitation by Season
# precip_by_season = weather_data.groupby('season')['precipitation'].sum().sort_values(ascending=False)
# print("\nTotal Precipitation by Season:")
# print(precip_by_season)

# # Optional plot
# precip_by_season.plot(kind='bar', title='Total Precipitation by Season', ylabel='Precipitation')
# plt.show()

# # ------------------------------
# # GroupBy Analysis 3: Average Wind Speed by Season
# wind_by_season = weather_data.groupby('season')['wind_speed'].mean().sort_values()
# print("\nAverage Wind Speed by Season:")
# print(wind_by_season)

# # Optional plot
# wind_by_season.plot(kind='bar', title='Average Wind Speed by Season', ylabel='Wind Speed')
# plt.show()


# Instructions:
# Using the provided weather dataset:
# Create at least two different pivot tables that reveal interesting patterns
# Include at least one pivot table with a hierarchical index
# Try both wide and long format transformations
# For each pivot table:
# Create a visualization to illustrate the findings
# Write a brief explanation of what insights can be gleaned from the analysis
# Prepare to share your most effective pivot table with the class
# Expected Output:
# At least two pivot tables with different structures
# Visualizations for each pivot table
# Written interpretations of findings


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
weather_data = pd.read_csv('weekFiveFolder/w5d2inclassweather.csv.csv')

# Convert 'date' column to datetime
weather_data['date'] = pd.to_datetime(weather_data['date'], errors='coerce')

# Drop rows with invalid or missing dates
weather_data = weather_data.dropna(subset=['date'])

# Extract 'month' and 'year' for grouping
weather_data['month'] = weather_data['date'].dt.month
weather_data['year'] = weather_data['date'].dt.year

# Drop rows with missing temperature or precipitation data
weather_data = weather_data.dropna(subset=['temperature', 'precipitation'])

# ===========================
# Pivot Table 1: Avg Temp by Month
# ===========================
pivot_temp = weather_data.pivot_table(
    index='month',
    values='temperature',
    aggfunc='mean'
).sort_index()

print("Pivot Table 1: Average Temperature by Month")
print(pivot_temp)

# Plot: Avg Temp by Month
pivot_temp.plot(
    kind='bar',
    figsize=(8, 5),
    color='orange',
    legend=False,
    title='Average Temperature by Month'
)
plt.ylabel('Avg Temperature')
plt.xlabel('Month')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================
# Pivot Table 2: Avg Temp & Precip by Year and Month
# ===========================
pivot_multi = weather_data.pivot_table(
    index=['year', 'month'],
    values=['temperature', 'precipitation'],
    aggfunc='mean'
)

print("\nPivot Table 2: Average Temp & Precipitation by Year and Month")
print(pivot_multi.head(12))  # Display 1 year for quick view

# Plot: Monthly Avg Temperature Over Years
pivot_multi_unstacked = pivot_multi.unstack()

pivot_multi_unstacked['temperature'].plot(
    figsize=(10, 6),
    title='Monthly Average Temperature Over Years'
)
plt.ylabel('Avg Temperature')
plt.grid(True)
plt.tight_layout()
plt.show()

# # Plot: Monthly Avg Precipitation Over Years
pivot_multi_unstacked['precipitation'].plot(
    figsize=(10, 6),
    title='Monthly Average Precipitation Over Years'
)
plt.ylabel('Avg Precipitation')
plt.grid(True)
plt.tight_layout()
plt.show()





