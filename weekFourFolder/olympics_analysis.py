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
# 1. How many total athletes are in this Olympic dataset?
# 2. What is the breakdown of male and female athletes?
# 3. What is the average age of all the athletes?
# 4. Who is the tallest athlete in the dataset, and how tall are they?


# 5. Who is the tallest ahtlete to win a medal?
# 6. Who is the shortest athlete?
# 7. How many different sports represented?
# 8. Are there more Summer or Winter Olympic events? How many of each?

# 9. How many athletes have won gold medals?
# 10. What percentage of athletes are missing age information?
# 11. Which event has had the most participants?
# 12. What is the age range (youngest to oldest) of Olympic athletes?
# 13. How many different countries have participated in the Olympics?

# owen's pandas api cheat sheet

## core

# - `df.shape`
# - `df.info()`
# - `df.describe()`
# - `df.head(n)` - first n rows
# - `df.tail(n)` - last n rows
# - `df.sample(n)` - random sample of n rows
# - `df.columns`
# - `df.dtypes`

# ## select

# - `df[['col1', 'col2']]` - select multiple columns
# - `df.loc[row_label, column_label]` - selection by label
# - `df.iloc[row_position, column_position]` - selection by position
# - `df.at[row_label, column_label]` - single value by label
# - `df.iat[row_position, column_position]` - single value by position

# ## filter

# - `df[df['column'] > value]` - filter rows by condition
# - `df[(condition1) & (condition2)]` - filter with multiple conditions
# - `df[(condition1) | (condition2)]` - filter with OR condition
# - `df[~condition]` - negate a condition
# - `df.query('column > value')` - filter using query syntax
# - `df.notna()`
# - `df.isna()`
# - `df.dropna()`

# ## manipulations

# - `df.sort_values(by='column', ascending=False)`
# - `df.sort_index()`
# - `df.reset_index()`
# - `df.set_index('column')`
# - `df.rename(columns={'old': 'new'})`
# - `df.drop('column', axis=1)`
# - `df.drop_duplicates()`
# - `df.fillna(value)`
# - `df.replace(old_value, new_value)`
# - `df.astype({'column': 'type'})` - change data types

# ## stats

# - `df['column'].mean()`
# - `df['column'].median()`
# - `df['column'].min()`
# - `df['column'].max()`
# - `df['column'].sum()`
# - `df['column'].count()` - count non-null values
# - `df['column'].nunique()` - count unique values
# - `df['column'].value_counts()` - count occurrences of each value
# - `df['column'].quantile([0.25, 0.5, 0.75])`
# - `df['column'].std()` - standard deviation
# - `df['column'].var()` - variance
# - `df['column'].corr(df['column2'])` - correlation

# ## groups

# - `df.groupby('column')`
# - `df.groupby(['col1', 'col2'])` - group by multiple columns
# - `df.groupby('column').agg(['mean', 'count'])` - multiple aggregations

# ## pivots

# - `df.pivot(index, columns, values)`
# - `df.pivot_table(values, index, columns, aggfunc)` - more flexible pivot

# ## calcs

# - `df['new_column'] = df['column'] * 2`

# ## joins

# - `pd.concat([df1, df2])`
# - `df1.merge(df2, on='key')` - like SQL join
# - `df1.join(df2)` - join on index


# BELOW IS THE ANSWERS FROM CLASS OUR BREAKOUT ROOM GOT TO NUMBER 9 or 10 !!!

# jtc tp S25 hackaton answer key

# 1. How many total rows are in this Olympic dataset?

# total_athletes = len(df)

# <!-- 271116 -->

# 2. What is the breakdown of male and female athletes?

# gender_breakdown = df['Sex'].value_counts()

# <!--
# M    196594
# F     74522
#  -->

# 3. What is the average age of all the athletes?

# average_age = df['Age'].mean()

# <!-- ~25.6 -->

# 4. Who is the tallest athlete in the dataset, and how tall are they?

# tallest_athlete = df.sort_values(by='Height', ascending=False).head(1)

# <!-- Yao Ming -->

# 5. Who is the tallest ahtlete to win a medal?

# medal_winners = df[df['Medal'].notna()]
# tallest_medalist = medal_winners.sort_values('Height', ascending=False).iloc[0]

# <!-- Arvydas Romas Sabonis -->

# 6. Who is the shortest athlete?

# shortest = df[df['Height'].notna()].sort_values('Height').iloc[0]

# <!-- Lyton Levison Mphande -->

# 7. How many different sports represented?

# unique_sports = df['Sport'].nunique()

# <!-- 66 -->

# 8. Are there more Summer or Winter Olympic events? How many of each?

# season_counts = df['Season'].value_counts()

# <!--
# Summer    222552
# Winter     48564
#  -->

# 9. How many athletes have won gold medals?

# gold_winners = df[df['Medal'] == 'Gold'].shape[0]

# <!-- 13372 -->

# 10. What percentage of athletes are missing age information?

# missing_age = df['Age'].isna().sum()
# percentage = (missing_age / len(df)) \* 100

# <!-- ~3.5% -->

# 11. Which event has had the most participants?

# event_counts = df['Event'].value_counts()
# most_popular_event = event_counts.idxmax()

# <!-- Football Men's Football -->

# 12. What is the age range (youngest to oldest) of Olympic athletes?

# youngest = df['Age'].min()
# oldest = df['Age'].max()

# <!-- 10 - 97 -->

# 13. How many different countries have participated in the Olympics?

# countries = df['NOC'].nunique()

# <!-- 230 -->

# 14. Make a new column for 'BMI' and calculate it for athletes with both height and weight data.

# df['BMI'] = df['Weight'] / ((df['Height']/100) \*\* 2)

# 15. Which country has won the most gold medals throughout Olympic history?

# gold_by_country = df[df['Medal'] == 'Gold']['NOC'].value_counts()
# top_gold_country = gold_by_country.idxmax()

# <!-- 'USA' -->

# 16. Is there a difference in the average age between medal winners and non-medal winners? If so, what is it?

# winners = df[df['Medal'].notna()]
# non_winners = df[df['Medal'].isna()]

# avg_age_winners = winners['Age'].mean()
# avg_age_non_winners = non_winners['Age'].mean()
# difference = avg_age_winners - avg_age_non_winners

# <!-- ~0.4 years -->

# 17. Which sport has the oldest average age of participants?

# sport_avg_age = df.groupby('Sport')['Age'].mean().sort_values(ascending=False)
# oldest_sport = sport_avg_age.index[0]

# <!-- Roque -->

# 18. Create a pivot table showing medal counts by country and sport

# df['Has_Medal'] = df['Medal'].notna().astype(int)

# medal_pivot = df.pivot_table(
# values='Has_Medal',
# index='NOC',
# columns='Sport',
# aggfunc='sum',
# fill_value=0
# )

# 19. What are the top 5 sports with the most female participants?

# female_sports = df[df['Sex'] == 'F']['Sport'].value_counts().head(5)

# <!--
# Athletics               11666
# Swimming                 9850
# Gymnastics               9129
# Alpine Skiing            3398
# Cross Country Skiing     3385
#  -->

# 20. How many athletes competed in each decade (1900s, 1910s, etc.)? (hint: would a column be helpful?)

# df['Decade'] = (df['Year'] // 10) \* 10
# decade_counts = df['Decade'].value_counts().sort_index()

# <!--
# 1890      380
# 1900     8071
# 1910     4040
# 1920    15559
# 1930    10722
# 1940     7480
# 1950    15792
# 1960    29194
# 1970    22461
# 1980    35201
# 1990    36958
# 2000    49357
# 2010    35901
#  -->

# 21. How many athletes have participated in multiple Olympic Games?

# games_per_athlete = df.groupby('Name')['Games'].nunique()
# multi_games_athletes = len(games_per_athlete[games_per_athlete > 1].sort_values(ascending=False))

# <!-- 37415  -->

# 22. Is there a correlation between an athlete's height and the likelihood of winning a medal?

# df['Won_Medal'] = df['Medal'].notna().astype(int)

# height_data = df.dropna(subset=['Height'])
# correlation = height_data['Height'].corr(height_data['Won_Medal'])

# <!-- ~0.09 -->

# 23. Which country has shown the most improvement in medal count from their first Olympics to their most recent?

# medals_by_country_year = df[df['Medal'].notna()].groupby(['NOC', 'Year']).size().reset_index(name='Medal_Count')

# # Get first and last year for each country

# first_medals = medals_by_country_year.sort_values(['NOC', 'Year']).groupby('NOC').first().reset_index()
# last_medals = medals_by_country_year.sort_values(['NOC', 'Year']).groupby('NOC').last().reset_index()

# # Calculate improvement

# improvement = pd.merge(first_medals, last_medals, on='NOC', suffixes=('\_first', '\_last'))
# improvement['Medal_Diff'] = improvement['Medal_Count_last'] - improvement['Medal_Count_first']

# # Show top improvers

# top_improved = improvement.sort_values('Medal_Diff', ascending=False).head(5)

# <!--
#     NOC	Year_first	Medal_Count_first	Year_last	Medal_Count_last	Medal_Diff
# 139	URS	1952	117	1988	366	249
# 141	USA	1896	20	2016	264	244
# 47	GDR	1968	58	1988	213	155
# 46	GBR	1896	9	2016	145	136
# 49	GER	1896	32	2016	159	127
#  -->

# 24. For team sports, which country has the tallest athletes on average?

# team_sports = ['Basketball', 'Volleyball', 'Football', 'Water Polo', 'Handball', 'Hockey', 'Rugby']
# team_heights = df[df['Sport'].isin(team_sports)].groupby('NOC')['Height'].mean().dropna().sort_values(ascending=False)

# <!--
# LTU    200.952381
#  -->

# 25. Which sport has the greatest disparity between male and female participation?

# gender_by_sport = df.groupby(['Sport', 'Sex']).size().unstack(fill_value=0)

# # Calculate absolute and percentage disparity

# gender_by_sport['Difference'] = abs(gender_by_sport['M'] - gender_by_sport['F'])
# gender_by_sport['Total'] = gender_by_sport['M'] + gender_by_sport['F']
# gender_by_sport['Percent_Disparity'] = (gender_by_sport['Difference'] / gender_by_sport['Total'] \* 100)

# # Sort by absolute difference

# top_disparity = gender_by_sport.sort_values('Percent_Difference', ascending=False)

# <!-- Aeronautics -->

# 26. What's the distribution of medals (Gold, Silver, Bronze) across the top 10 countries?

# # Create pivot table of medal types by country

# medal_types = df[df['Medal'].notna()].pivot_table(
# index='NOC',
# columns='Medal',
# values='ID',
# aggfunc='count',
# fill_value=0
# )

# # Add total column

# if 'Gold' in medal_types.columns and 'Silver' in medal_types.columns and 'Bronze' in medal_types.columns:
# medal_types['Total'] = medal_types['Gold'] + medal_types['Silver'] + medal_types['Bronze']
# else: # Handle case where some medal types might be missing
# medal_types['Total'] = medal_types.sum(axis=1)

# # Show top 10 countries

# top_10_medals = medal_types.sort_values('Total', ascending=False).head(10)

# <!--
# Medal	Bronze	Gold	Silver	Total
# NOC
# USA	1358	2638	1641	5637
# URS	689	1082	732	2503
# GER	746	745	674	2165
# GBR	651	678	739	2068
# FRA	666	501	610	1777
# ITA	531	575	531	1637
# SWE	535	479	522	1536
# CAN	451	463	438	1352
# AUS	517	348	455	1320
# RUS	408	390	367	1165
#  -->

