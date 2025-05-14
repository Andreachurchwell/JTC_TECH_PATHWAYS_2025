# import pandas as pd
# import matplotlib.pyplot as plt


# # Load the data
# df = pd.read_csv('C:/Users/achur/desktop/python/techPathwayNotes/.venv/weekFourFolder/selmerWeather.csv')

# # Convert 'DATE' to datetime so matplotlib handles it better
# df['DATE'] = pd.to_datetime(df['DATE'])

# # Plotting
# plt.figure(figsize=(12, 5))  # wider figure for more room
# plt.plot(df['DATE'], df['PRCP'], label='Daily Precipitation', color='#f77f00', linewidth=2)  # Tennessee orange

# # Style the plot
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Precipitation (inches)', fontsize=12)
# plt.title('Daily Precipitation in Selmer, TN (2025)', fontsize=14, fontweight='bold')
# plt.xticks(rotation=45)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.legend()
# plt.tight_layout()
# plt.show()


# # 1. Find the average high and low temperature

# print("Average high (TMAX):", df["TMAX"].mean())
# print("Average low (TMIN):", df["TMIN"].mean())
# # 2. Find the hottest and coldest days

# hottest_day = df.loc[df["TMAX"].idxmax()]
# coldest_day = df.loc[df["TMIN"].idxmin()]

# print("Hottest day:\n", hottest_day)
# print("Coldest day:\n", coldest_day)
# # 3. Count how many days have missing data

# missing_tmax = df["TMAX"].isna().sum()
# missing_tmin = df["TMIN"].isna().sum()
# missing_tobs = df["TOBS"].isna().sum()

# print("Missing TMAX values:", missing_tmax)
# print("Missing TMIN values:", missing_tmin)
# print("Missing TOBS values:", missing_tobs)




# import pandas as pd
# import matplotlib.pyplot as plt

# # Load and prepare data
# df = pd.read_csv('C:/Users/achur/desktop/python/techPathwayNotes/.venv/weekFourFolder/selmerWeather.csv')
# df['DATE'] = pd.to_datetime(df['DATE'])

# # Set tornado date and period
# tornado_date = pd.to_datetime('2025-04-03')
# tornado_week_start = pd.to_datetime('2025-03-30')
# tornado_week_end = pd.to_datetime('2025-04-06')

# # Plotting Precipitation
# plt.figure(figsize=(12, 6))
# plt.plot(df['DATE'], df['PRCP'], label='Daily Precipitation', color='#f77f00', linewidth=2)

# # Plotting Temperature (TMAX and TMIN)
# plt.plot(df['DATE'], df['TMAX'], label='Max Temp (°F)', color='#ff6f00', linestyle='-', linewidth=2)
# plt.plot(df['DATE'], df['TMIN'], label='Min Temp (°F)', color='#0066cc', linestyle='-', linewidth=2)

# # Highlight the tornado week (shaded region)
# plt.axvspan(tornado_week_start, tornado_week_end, color='gray', alpha=0.2, label="Tornado Week (April 3)")

# # Highlight the tornado day
# plt.axvline(x=tornado_date, color='red', linestyle='--', linewidth=2)
# plt.text(tornado_date, df['PRCP'].max(), 'Tornado - Apr 3', color='red', fontsize=10, rotation=90, verticalalignment='bottom')

# # Labels and style
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Precipitation (inches) and Temperature (°F)', fontsize=12)
# plt.title('Weather Data in Selmer, TN (2025) - Including Tornado on April 3', fontsize=14, fontweight='bold')
# plt.xticks(rotation=45)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.legend()
# plt.tight_layout()
# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# # Load and prepare data
# df = pd.read_csv('C:/Users/achur/desktop/python/techPathwayNotes/.venv/weekFourFolder/selmerWeather.csv')
# df['DATE'] = pd.to_datetime(df['DATE'])

# # Set tornado date and period
# tornado_date = pd.to_datetime('2025-04-03')
# tornado_week_start = pd.to_datetime('2025-03-30')
# tornado_week_end = pd.to_datetime('2025-04-06')

# # Plotting with bar chart for Precipitation and line plot for Temperature
# fig, ax1 = plt.subplots(figsize=(12, 6))

# # Bar chart for Precipitation with thinner bars and different color
# ax1.bar(df['DATE'], df['PRCP'], color='#4CAF50', label='Precipitation (inches)', width=0.7, align='center')

# # Creating a second y-axis for Temperature (TMAX, TMIN)
# ax2 = ax1.twinx()
# ax2.plot(df['DATE'], df['TMAX'], label='Max Temp (°F)', color='#FF9800', linestyle='-', linewidth=2)
# ax2.plot(df['DATE'], df['TMIN'], label='Min Temp (°F)', color='#2196F3', linestyle='-', linewidth=2)

# # Highlight the tornado week (shaded region with pattern)
# ax1.axvspan(tornado_week_start, tornado_week_end, color='gray', alpha=0.3, hatch='//', label="Tornado Week (April 3)")

# # Highlight the tornado day with a bold red line
# ax1.axvline(x=tornado_date, color='red', linestyle='-', linewidth=3, label='Tornado Day')

# # Annotations for Tornado Day
# ax1.text(tornado_date, df['PRCP'].max() + 0.1, 'Tornado - Apr 3', color='red', fontsize=12, rotation=90, verticalalignment='bottom')

# # Labels and style
# ax1.set_xlabel('Date', fontsize=12)
# ax1.set_ylabel('Precipitation (inches)', fontsize=12)
# ax2.set_ylabel('Temperature (°F)', fontsize=12)

# # Title and Legend
# plt.title('Weather Data in Selmer, TN (2025) - Including Tornado on April 3', fontsize=14, fontweight='bold')
# ax1.grid(True, linestyle='--', alpha=0.5)

# # Place legend outside the plot for clarity
# ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
# ax2.legend(loc='upper right', bbox_to_anchor=(1, 1))

# # Finalize and show plot
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()





