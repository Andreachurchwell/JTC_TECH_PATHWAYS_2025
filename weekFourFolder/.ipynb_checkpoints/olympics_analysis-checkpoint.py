import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('olympics.csv')

# Inspect the first few rows
print(df.head())

# Example: Filter countries with more than 10 gold medals
filtered_df = df[df['Gold'] > 10]
print(filtered_df)

# Create a simple plot of gold medals by country
# sns.barplot(data=df, x='Country', y='Gold')
# plt.xticks(rotation=90)  # Rotate the x-axis labels if needed
# plt.show()
