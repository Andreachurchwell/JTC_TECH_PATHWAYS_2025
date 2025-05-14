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

# Convert temperature and precipitation to numeric (in case of string issues)
weather_data['temperature'] = pd.to_numeric(weather_data['temperature'], errors='coerce')
weather_data['precipitation'] = pd.to_numeric(weather_data['precipitation'], errors='coerce')

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

# ===========================
# FIXED Plot: Monthly Avg Temperature Over Years
# ===========================
pivot_multi_reset = pivot_multi.reset_index()
pivot_temp_pivoted = pivot_multi_reset.pivot(
    index='month', columns='year', values='temperature'
)

pivot_temp_pivoted.plot(
    figsize=(10, 6),
    title='Monthly Average Temperature Over Years'
)
plt.ylabel('Avg Temperature')
plt.xlabel('Month')
plt.grid(True)
plt.tight_layout()
plt.show()

# ===========================
# Plot: Monthly Avg Precipitation Over Years
# ===========================
pivot_precip_pivoted = pivot_multi_reset.pivot(
    index='month', columns='year', values='precipitation'
)

pivot_precip_pivoted.plot(
    figsize=(10, 6),
    title='Monthly Average Precipitation Over Years'
)
plt.ylabel('Avg Precipitation')
plt.xlabel('Month')
plt.grid(True)
plt.tight_layout()
plt.show()