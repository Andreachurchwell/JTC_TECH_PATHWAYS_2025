# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()


# import matplotlib.pyplot as plt

# years = [1983, 1984, 1985, 1986, 1987]
# total_populations = [8939007, 8954518, 8960387, 8956741, 8943721]

# plt.plot(years, total_populations)
# plt.title("Year vs Population in Bulgaria")
# plt.xlabel("Year")
# plt.ylabel("Total Population")
# plt.show()



# import matplotlib.pyplot as plt

# temp = [30, 32, 33, 28.5, 35, 29, 29]
# ice_creams_count = [100, 115, 115, 75, 125, 79, 89]

# plt.scatter(temp, ice_creams_count)
# plt.title("Temperature vs. Sold ice creams")
# plt.xlabel("Temperature")
# plt.ylabel("Sold ice creams count")
# plt.show()

# import matplotlib.pyplot as plt

# numbers = [0.1, 0.5, 1, 1.5, 2, 4, 5.5, 6, 8, 9]

# plt.hist(numbers, bins = 3)
# plt.xlabel("Number")
# plt.ylabel("Frequency")
# plt.show()

# values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]

# plt.boxplot(values)
# plt.yticks(range(1, 22))
# plt.ylabel("Value")
# plt.show()

# Our data
# labels = ["JavaScript", "Java", "Python", "C#"]
# usage = [69.8, 45.3, 38.8, 34.4]

# # Generating the y positions. Later, we'll use them to replace them with labels.
# y_positions = range(len(labels))

# # Creating our bar plot
# plt.bar(y_positions, usage)
# plt.xticks(y_positions, labels)
# plt.ylabel("Usage (%)")
# plt.title("Programming language usage")
# plt.show()


# sizes = [25, 20, 45, 10]
# labels = ["Cats", "Dogs", "Tigers", "Goats"]

# plt.pie(sizes, labels = labels, autopct = "%.2f")
# plt.axes().set_aspect("equal")
# plt.show()

# import requests
# import matplotlib.pyplot as plt

# # Step 1: Fetch the list of all breeds
# url = "https://dog.ceo/api/breeds/list/all"
# response = requests.get(url)
# data = response.json()

# # Step 2: Count sub-breeds as a proxy for popularity
# breed_data = data["message"]
# breed_popularity = {breed: len(subbreeds) for breed, subbreeds in breed_data.items()}

# # Optional: Sort by "popularity"
# sorted_breeds = dict(sorted(breed_popularity.items(), key=lambda item: item[1], reverse=True))

# # Step 3: Pick top 10
# top_breeds = list(sorted_breeds.keys())[:10]
# popularity_counts = [sorted_breeds[breed] for breed in top_breeds]

# plt.figure(figsize=(10, 6))
# plt.bar(top_breeds, popularity_counts, color='skyblue')
# plt.title("Top 10 Dog Breeds by Number of Sub-Breeds (Simulated Popularity)")
# plt.xlabel("Dog Breed")
# plt.ylabel("Number of Sub-Breeds")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns

# # Data
# teams = ['Oklahoma City Thunder', 'Boston Celtics', 'Cleveland Cavaliers', 'Denver Nuggets', 'Minn Timberwolves']
# probabilities = [35.7, 35.1, 16.7, 5.6, 5.6]

# # Set style
# sns.set(style="whitegrid")
# plt.figure(figsize=(10, 6))
# colors = sns.color_palette("muted", len(teams))

# # Create barplot
# # sns.barplot(x=probabilities, y=teams, palette=colors)
# sns.barplot(x=probabilities, y=teams, hue=teams, palette=colors, legend=False)

# # Add titles and labels
# plt.title("🏀 Predicted 2025 NBA Finals Winners", fontsize=16, weight='bold')
# plt.xlabel("Implied Probability (%)", fontsize=12)
# plt.ylabel("Team", fontsize=12)

# # Annotate bars with probability values
# for index, value in enumerate(probabilities):
#     plt.text(value + 0.5, index, f"{value}%", va='center', fontsize=10)

# plt.xlim(0, max(probabilities) + 10)
# plt.tight_layout()
# plt.show()


# Load your cleaned weather dataset from yesterday's session
# Create at least three different types of plots:
# A line plot showing temperature over time
# A scatter plot showing the relationship between temperature and humidity
# A histogram or box plot showing the distribution of a weather variable
# Apply appropriate customization to each plot:
# Meaningful titles and axis labels
# Custom colors, markers, and line styles
# Grid lines and legends as needed
# Save at least one plot as a PNG file

# import matplotlib.pyplot as plt
# import pandas as pd
# cleaned_data = {
# 'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
# 'temperature': [32.5, 31.8, 33.4, 89.6, 31.2], # All in °F (converted 32°C to 89.6°F)
# 'humidity': [65, 70, 68, 67, 66], # All as percentages
# 'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5] # All in mm (converted inches to mm)
# }
# # Convert the dictionary to a DataFrame
# df = pd.DataFrame(cleaned_data)
# df['date'] = pd.to_datetime(df['date'])  # Convert date strings to datetime objects

# # --- Line Plot: Temperature Over Time ---
# plt.figure(figsize=(10, 5))
# plt.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='tomato', label='Temperature (°F)')
# plt.title('Temperature Over Time')
# plt.xlabel('Date')
# plt.ylabel('Temperature (°F)')
# plt.grid(True)
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('temperature_over_time.png')  # Save the line plot
# plt.show()

# # --- Scatter Plot: Temperature vs. Humidity ---
# plt.figure(figsize=(8, 5))
# plt.scatter(df['temperature'], df['humidity'], color='dodgerblue', marker='x')
# plt.title('Temperature vs. Humidity')
# plt.xlabel('Temperature (°F)')
# plt.ylabel('Humidity (%)')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # --- Box Plot: Precipitation Distribution ---
# plt.figure(figsize=(6, 4))
# plt.boxplot(df['precipitation'], patch_artist=True,
#             boxprops=dict(facecolor='lightgreen', color='darkgreen'),
#             medianprops=dict(color='red'))
# plt.title('Precipitation Distribution')
# plt.ylabel('Precipitation (mm)')
# plt.grid(True, axis='y')
# plt.tight_layout()
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Teams and data
# teams = ['Oklahoma City Thunder', 'Boston Celtics', 'Cleveland Cavaliers', 'Denver Nuggets', 'Minn Timberwolves']
# prob_2024 = [10.2, 30.5, 12.0, 25.0, 22.3]
# prob_2025 = [35.7, 35.1, 16.7, 5.6, 5.6]

# # Set bar positions and width
# bar_width = 0.4
# index = np.arange(len(teams))

# # Plotting
# sns.set(style="whitegrid")
# plt.figure(figsize=(12, 6))
# colors = sns.color_palette("muted")

# # Bars for 2024 and 2025
# plt.barh(index - bar_width/2, prob_2024, height=bar_width, color=colors[0], label='2024')
# plt.barh(index + bar_width/2, prob_2025, height=bar_width, color=colors[1], label='2025')

# # Labels and title
# plt.xlabel("Implied Probability (%)", fontsize=12)
# plt.title("🏀 NBA Finals Predictions: 2024 vs 2025", fontsize=16, weight='bold')
# plt.yticks(index, teams)
# plt.legend()

# # Add data labels
# for i in range(len(teams)):
#     plt.text(prob_2024[i] + 0.5, i - bar_width/2, f"{prob_2024[i]}%", va='center', fontsize=9)
#     plt.text(prob_2025[i] + 0.5, i + bar_width/2, f"{prob_2025[i]}%", va='center', fontsize=9)

# plt.xlim(0, max(prob_2025 + prob_2024) + 10)
# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt
# import seaborn as sns

# # Data
# teams = ['Oklahoma City Thunder', 'Boston Celtics', 'Cleveland Cavaliers', 'Denver Nuggets', 'Minnesota Timberwolves', 'Golden State Warriors', 'New York Knicks', 'Indiana Pacers']
# prob_2024 = [9.1,25.0,2.8,11.8,10.5,2.8,5.9,2.0]
# prob_2025 = [43.5,22.2,10.0, 5.6, 9.1,3.8,3.4,6.7]

# # Set style
# sns.set(style="whitegrid")
# fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# # --- Plot for 2024 ---
# sns.barplot(x=prob_2024, y=teams, palette="pastel", ax=axes[0])
# axes[0].set_title("2024 NBA Finals Predictions", fontsize=14, weight='bold')
# axes[0].set_xlabel("Implied Probability (%)")
# axes[0].set_ylabel("Team")

# # Annotate 2024 bars
# for i, v in enumerate(prob_2024):
#     axes[0].text(v + 0.5, i, f"{v}%", va='center', fontsize=9)

# # --- Plot for 2025 ---
# colors = sns.color_palette("muted", len(teams))
# sns.barplot(x=prob_2025, y=teams, hue=teams, palette=colors, ax=axes[1], legend=False)
# axes[1].set_title("2025 NBA Finals Predictions", fontsize=14, weight='bold')
# axes[1].set_xlabel("Implied Probability (%)")
# axes[1].set_ylabel("")

# # Annotate 2025 bars
# for i, v in enumerate(prob_2025):
#     axes[1].text(v + 0.5, i, f"{v}%", va='center', fontsize=9)

# # Set x-limits for consistency
# max_val = max(max(prob_2024), max(prob_2025))
# axes[0].set_xlim(0, max_val + 10)
# axes[1].set_xlim(0, max_val + 10)

# plt.tight_layout()
# plt.show()


# Breakout Session 2:
# Load your cleaned weather dataset from yesterday's session
# Create a multi-panel visualization with at least three subplots that together tell a meaningful story about your data
# Use different plot types for different aspects of the data:
# Consider time series, distributions, relationships between variables
# Use appropriate plot types for each (line, scatter, bar, histogram, etc.)
# cleaned_data = {
# 'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
# 'temperature': [32.5, 31.8, 33.4, 89.6, 31.2], # All in °F
# 'humidity': [65, 70, 68, 67, 66], # All as percentages
# 'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5] # All in mm
# }

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# # Your cleaned data
# cleaned_data = {
#     'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'temperature': [32.5, 31.8, 33.4, 89.6, 31.2],  # in °F
#     'humidity': [65, 70, 68, 67, 66],  # in percentage
#     'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5]  # in mm
# }

# # Convert data to pandas DataFrame
# df = pd.DataFrame(cleaned_data)
# df['date'] = pd.to_datetime(df['date'])
# df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')  # Fix for barplot axis

# # Set up the figure with subplots
# fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharex=False)

# # --- Plot 1: Time series plot for temperature ---
# sns.lineplot(x='date', y='temperature', data=df, ax=axes[0], color='blue', lw=2)
# axes[0].set_title("Temperature Over Time (°F)", fontsize=14)
# axes[0].set_ylabel("Temperature (°F)")

# # --- Plot 2: Scatter plot for humidity vs. temperature with color gradient for precipitation ---
# scatter = axes[1].scatter(df['temperature'], df['humidity'], c=df['precipitation'], cmap='viridis', s=100)
# axes[1].set_title("Humidity vs Temperature (Color = Precipitation)", fontsize=14)
# axes[1].set_xlabel("Temperature (°F)")
# axes[1].set_ylabel("Humidity (%)")
# fig.colorbar(scatter, ax=axes[1], label="Precipitation (mm)")

# # --- Plot 3: Bar plot for precipitation using string dates ---
# sns.barplot(x='date_str', y='precipitation', data=df, ax=axes[2], color='green')
# axes[2].set_title("Precipitation on Each Day (mm)", fontsize=14)
# axes[2].set_xlabel("Date")
# axes[2].set_ylabel("Precipitation (mm)")
# axes[2].tick_params(axis='x', rotation=45)  # Rotate for readability

# # Adjust layout and show the plot
# plt.tight_layout()
# plt.show()

