
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# data = pd.read_csv('nba.csv')
# print(data.head())
# # Your code begins here:
# # 1. Create a box plot of the temperature by month
# plt.figure(figsize=(10,6))
# sns.boxplot(data=data,)

# # 2. Add appropriate labels and title


# # 3. Display the plot
# # plt.savefig('plot.png')
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the dataset
# data = pd.read_csv('nba.csv')

# # Show sample and column names
# print(data.head())
# print(data.columns)

# # Boxplot: Points per Game by Team
# plt.figure(figsize=(12, 6))
# # sns.boxplot(x='Team', y='Points_Per_Game', data=data, palette='Set3')
# sns.boxplot(x='Team', y='Points_Per_Game', hue='Team', data=data, palette='Set3', legend=False)

# plt.xticks(rotation=45)
# plt.title('Points Per Game Distribution by Team')
# plt.xlabel('Team')
# plt.ylabel('Points Per Game')
# plt.tight_layout()
# plt.show()

# # Notes:
# print("Outliers appear as individual dots outside the 'whiskers' of each box.")

# # Questions to Answer Based on the Plot:
# # 1. Which team shows the highest median Points Per Game?
# # 2. Which team has the widest range of scoring (most variability)?
# # 3. Are there any teams with outliers? Which ones?
# # 4. Compare a strong team vs a weaker one — how does their distribution differ?
# # 5. Which team appears to have the most consistent scoring (smallest IQR)?


# # ---- Start of new additions ----

# # Descriptive statistics
# print("\nDescriptive Statistics:")
# # print(data.describe())
# print(data.describe(include='number'))

# # Histogram for Points Per Game
# plt.figure(figsize=(10, 5))
# sns.histplot(data['Points_Per_Game'], bins=10, kde=True, color='skyblue')
# plt.title('Distribution of Points Per Game')
# plt.xlabel('Points Per Game')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

# # # Bar chart: Average Points Per Game by Team
# avg_points = data.groupby('Team')['Points_Per_Game'].mean().sort_values(ascending=False)

# plt.figure(figsize=(10, 6))
# sns.barplot(x=avg_points.index, y=avg_points.values, palette='coolwarm')
# plt.title('Average Points Per Game by Team')
# plt.xlabel('Team')
# plt.ylabel('Avg Points Per Game')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your original data
# data = pd.DataFrame({
#     'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo', 'Nikola Jokic'],
#     'Team': ['Lakers', 'Warriors', 'Suns', 'Bucks', 'Nuggets'],
#     'Games_Played': [55, 60, 58, 61, 63],
#     'Points_Per_Game': [25.4, 27.8, 26.5, 29.1, 24.9],
#     'Assists_Per_Game': [7.9, 6.2, 5.3, 5.8, 9.2],
#     'Rebounds_Per_Game': [7.2, 4.3, 6.1, 11.2, 11.8]
# })

import pandas as pd

data = pd.DataFrame({
    'Player': [
        'LeBron James', 'Luka Doncic',  # Lakers
        'Stephen Curry', 'Jimmy Butler',  # Warriors
        'Kevin Durant', 'Devin Booker',  # Suns
        'Giannis Antetokounmpo', 'Dame Lillard',  # Bucks
        'Nikola Jokic', 'Jamal Murray'  # Nuggets
    ],
    'Team': [
        'Lakers', 'Lakers',
        'Warriors', 'Warriors',
        'Suns', 'Suns',
        'Bucks', 'Bucks',
        'Nuggets', 'Nuggets'
    ],
    'Points_Per_Game': [
        25.4, 31.0,
        27.8, 22.1,
        26.5, 24.3,
        29.1, 20.4,
        24.9, 22.0
    ]
})


# Add outliers
outliers = pd.DataFrame({
    'Player': ['Outlier Player 1', 'Outlier Player 2'],
    'Team': ['Lakers', 'Warriors'],
    'Games_Played': [10, 10],
    'Points_Per_Game': [50.0, 5.0],  # Extreme high and low points
    'Assists_Per_Game': [1.0, 1.0],
    'Rebounds_Per_Game': [1.0, 1.0]
})

# Combine original data with outliers
data = pd.concat([data, outliers], ignore_index=True)

# Plot boxplot again
plt.figure(figsize=(10,6))
sns.boxplot(x='Team', y='Points_Per_Game', data=data, palette='Set3')
plt.title('Points Per Game by Team (with Outliers)')
plt.show()
print(data.groupby('Team')['Points_Per_Game'].describe())


