import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weather_data = pd.read_csv('weekFiveFolder/w5d2inclassweather.csv.csv')
# print(weather_data.head())

weather_data['date'] = pd.to_datetime(weather_data['date'])
weather_data['month'] = weather_data['date'].dt.month
# print(weather_data.head())

monthly_temp = weather_data.groupby('month')['temperature'].mean()
# print('monthly temp==',monthly_temp)

# visuals for mean temperature
# plt.figure(figsize=(10,6))
# monthly_temp.plot(kind='bar')
# plt.title('Average Mthly Temp')
# plt.xlabel('Month')
# plt.ylabel('Temp')
# plt.xticks(rotation=0)
# plt.show()

monthly_stats = weather_data.groupby('month')['temperature'].agg(['min','max', 'mean'])
# print(monthly_stats)

# visuals
# plt.figure(figsize=(12,6))
# monthly_stats[['min','max','mean']].plot(kind='bar')
# plt.title('Mthly Temp Stats')
# plt.xlabel('Month')
# plt.ylabel('Temp')
# plt.legend(['Min','Max','Avg'])
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

# set up custom aggerate
def temp_range(series):
    return series.max() - series.min()

monthly_range = weather_data.groupby('month')['temperature'].agg(temp_range)
# print(monthly_range)
weather_data['location'] = np.random.choice(['Urban', 'Suburban', 'Rural'], size=len(weather_data))
location_monthly_temp = weather_data.groupby(['month', 'location'])['temperature'].mean()
# print(location_monthly_temp)
# print(weather_data.head())

location_monthly_df = location_monthly_temp.unstack()
# print(location_monthly_df)

# plt.figure(figsize=(12,6))
# location_monthly_df.plot(kind='bar')
# plt.title('Avg temp by location')
# plt.xlabel('month')
# plt.ylabel('temp')
# plt.legend(title='Location')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# # plt.xticks(rotation='vertical')
# plt.show()

monthly_complex = weather_data.groupby('month').agg({
    'temperature': ['mean', 'min'],
    'humidity': ['mean', 'max'],
    'precipitation': ['sum', 'mean', lambda x: (x > 0).sum()]
})
# print(monthly_complex)

# print(monthly_complex[('temperature', 'mean')])
# print(monthly_complex[('precipitation', 'sum')])

pivot_basic = pd.pivot_table(weather_data, 
                           values='temperature',
                           index='month',
                           columns='location',
                           aggfunc='mean')
# print(pivot_basic)
print("Basic Pivot Table - Average Temperature by Month and Location:")
print(pivot_basic)

# Visualize the pivot table
# plt.figure(figsize=(12, 6))
# sns.heatmap(pivot_basic, annot=True, cmap='YlOrRd', fmt='.1f')
# plt.title('Average Temperature by Month and Location')
# plt.show()

pivot_multi = pd.pivot_table(weather_data,
                             values=['temperature','humidity','precipitation'],
                             index='month',
                             columns='location',
                             aggfunc={
                                 'temperature': 'mean',
                                 'humidity':'mean',
                                 'precipitation': 'sum'
                             })
print(pivot_multi)


"With multiple values and aggregations, pivot tables become even more powerful. We can analyze several variables simultaneously across different dimensions."
# Hierarchical Indices in Pivot Tables:
"Pivot tables create hierarchical (multi-level) indices. Let's explore how to work with them:"
# Add a 'season' column
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

weather_data['season'] = weather_data['month'].apply(get_season)

# Create a pivot table with a hierarchical index
pivot_hierarchical = pd.pivot_table(weather_data, 
                                  values='temperature',
                                  index=['season', 'month'],
                                  columns='location',
                                  aggfunc='mean')

print("Pivot Table with Hierarchical Index:")
# print(pivot_hierarchical)

# Accessing data from the hierarchical pivot table
print("\nSummer temperatures:")
print(pivot_hierarchical.loc['Summer'])

print("\nWinter temperatures in Urban areas:")
print(pivot_hierarchical.loc['Winter', 'Urban'])

# Pivot table with fill values and margins
pivot_advanced = pd.pivot_table(weather_data, 
                               values=['temperature', 'precipitation'],
                               index=['season', 'month'],
                               columns='location',
                               aggfunc={'temperature': 'mean', 'precipitation': 'sum'},
                               fill_value=0,      # Replace NaN with 0
                               margins=True,      # Add row and column totals
                               margins_name='All')  # Name for the totals

print("Advanced Pivot Table:")
print(pivot_advanced)
















# import csv

# # Store temperature and humidity in separate lists
# temperature_data = []
# humidity_data = []

# with open('weekFiveFolder/w5d2inclassweather.csv.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)  # Using DictReader to access by column names
#     for row in reader:
#         temperature_data.append(float(row['temperature']))
#         humidity_data.append(float(row['humidity']))

# # Calculate the averages
# avg_temp = sum(temperature_data) / len(temperature_data)
# avg_humidity = sum(humidity_data) / len(humidity_data)

# print(f"Average Temperature: {avg_temp:.2f} °C")
# print(f"Average Humidity: {avg_humidity:.2f}%")