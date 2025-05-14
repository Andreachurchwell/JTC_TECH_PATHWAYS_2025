import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# speeds = pd.DataFrame(
#         [
#            ("bird", "Falconiformes", 389.0),
#             ("bird", "Psittaciformes", 24.0),
#             ("mammal", "Carnivora", 80.2),
#             ("mammal", "Primates", np.nan),
#             ("mammal", "Carnivora", 58),
#         ],
#         index=["falcon", "parrot", "lion", "monkey", "leopard"],
#         columns=("class", "order", "max_speed"),
#     )
    
# grouped = speeds.groupby("class")

# grouped = speeds.groupby(["class", "order"])
# print(speeds)

# import pandas as pd

# data = {
#     'fruit': ['apple', 'apple', 'orange', 'orange', 'banana'],
#     'price': [1.0, 1.2, 0.8, 1.0, 0.5],
#     'quantity': [5, 3, 6, 2, 9]
# }

# df = pd.DataFrame(data)
# result = df.groupby('fruit')['quantity'].sum()

# result =df.groupby('fruit').agg({
#     'price': 'mean',
#     'quantity': 'sum'
# })
# print(result)


# # 🔢 Want to Sort by Quantity (Biggest First)?
# sorted_result = df.groupby('fruit').agg({
#     'price': 'mean',
#     'quantity': 'sum'
# }).sort_values('quantity', ascending=False)

# print(sorted_result)

# # 🔎 Want to Filter Fruits with Quantity Over 8?
# filtered_result = df.groupby('fruit').agg({
#     'price': 'mean',
#     'quantity': 'sum'
# })

# # Keep only rows where quantity is greater than 8
# filtered_result = filtered_result[filtered_result['quantity'] > 8]

# print(filtered_result)


# data = {
#     'category': ['tech', 'tech', 'books', 'books', 'clothing', 'clothing', 'tech'],
#     'item': ['laptop', 'phone', 'novel', 'comic', 'shirt', 'jeans', 'tablet'],
#     'price': [1200, 800, 15, 10, 25, 40, 600],
#     'units_sold': [3, 5, 10, 7, 8, 6, 4]
# }

# df = pd.DataFrame(data)

# 🧠 Task 1: For each category, find:
# Average price

# Total units sold

# result = df.groupby('category').agg({
#     'price': 'mean',
#     'units_sold': 'sum'
# })

# print(result)

# #  Task 2: Sort by units_sold, most sold at the top
# sorted_result = result.sort_values('units_sold', ascending=False)
# print(sorted_result)

# # 🧠 Task 3: Filter to only include categories that sold more than 15 units total
# popular = result[result['units_sold'] > 15]
# print(popular)

# 5-13-25 OFFICE HOURS W PATRICK

# data = {
#     'date': ['2025-01-01','2025-01-02','2025-01-03','2025-02-01','2025-02-02'],
#     'temp': [30,32,28,40,42],
#     'humid': [55,60,58,65,63],
#     'prec': [0.1,0.0,0.0,0.2,0.3]
# }
# weather = pd.DataFrame(data)
# weather['date'] = pd.to_datetime(weather['date'])
# weather['month'] = weather['date'].dt.month

# # print(weather)

# # monthly_avg_temp = weather.groupby('month')['temp'].mean()
# # # print(monthly_avg_temp)
# # plt.figure(figsize=(8,5))
# # monthly_avg_temp.plot(kind='line', marker='o')
# # plt.title('Avg Monthly Temp')
# # plt.xlabel('Month')
# # plt.ylabel('Temp')
# # plt.grid(True)
# # plt.tight_layout()
# # plt.show()


# mon_total_prec = weather.groupby('month')['prec'].sum()
# # print(mon_total_prec)


# # plt.figure(figsize=(8,5))
# # mon_total_prec.plot(kind='bar')
# # plt.title('Avg Monthly Precip')
# # plt.xlabel('Month')
# # plt.ylabel('Temp')
# # # plt.grid(True)
# # plt.tight_layout()
# # plt.show()


# summary = weather.groupby('month').agg({
#     'temp': ['mean', 'min', 'max'],
#     'prec': 'sum'
# })

# print(summary)


# 🔄 What Is Reshaping in Pandas?
# Reshaping refers to changing the structure of your DataFrame 
# — like pivoting, unpivoting, stacking, or unstacking data — to better analyze or visualize it.
# import pandas as pd

# # Original data
# data = {
#     'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
#     'fruit': ['apple', 'orange', 'apple', 'orange'],
#     'sales': [5, 3, 8, 6]
# }

# # Create DataFrame
# df = pd.DataFrame(data)
# print("Original DataFrame:\n")
# print(df)
# print("\n---\n")

# # Pivot the DataFrame
# pivot_df = df.pivot(index='date', columns='fruit', values='sales')
# print("Pivoted DataFrame:\n")
# print(pivot_df)
# # Reset index so 'date' is a column again
# pivot_reset = pivot_df.reset_index()

# # Use melt to unpivot the wide data
# melted = pd.melt(pivot_reset, id_vars='date', var_name='fruit', value_name='sales')

# print("Melted DataFrame:\n")
# print(melted)

# # Stack the columns into a new row level
# stacked = pivot_df.stack()

# print("Stacked DataFrame:\n")
# print(stacked)


# 🧠 Key Takeaways: Hierarchical Indexing (MultiIndex)
# MultiIndex allows you to have multiple levels (indexes) on an axis.

# You can think of it like having a table within a table, useful for higher-dimensional data in a 2D DataFrame.


# import pandas as pd
# import numpy as np

# # Step 1: Create MultiIndex with teams and player positions
# teams = ['Lakers', 'Lakers', 'Bulls', 'Bulls', 'Warriors', 'Warriors', 'Celtics', 'Celtics']
# positions = ['Guard', 'Forward', 'Guard', 'Forward', 'Guard', 'Forward', 'Guard', 'Forward']

# arrays = [teams, positions]
# index = pd.MultiIndex.from_arrays(arrays, names=['Team', 'Position'])

# # Step 2: Create DataFrame with random performance stats (Points and Assists)
# df = pd.DataFrame(np.random.randint(10, 30, size=(8, 2)), index=index, columns=['Points', 'Assists'])

# print("\nOriginal DataFrame (Player Stats):")
# print(df)

# # Step 3: Use .loc[] to access specific parts of the DataFrame
# print("\nAccess rows where Team == 'Lakers':")
# print(df.loc['Lakers'])

# print("\nAccess row where Team == 'Bulls' and Position == 'Guard':")
# print(df.loc[('Bulls', 'Guard')])

# # Step 4: Swap index levels
# print("\nAfter swapping index levels (Team <-> Position):")
# print(df.swaplevel('Team', 'Position'))

# # Step 5: Sort by Position (index level 1)
# print("\nAfter sorting by 'Position' level:")
# print(df.sort_index(level=1))

# # Step 6: Group by Position and sum the performance stats
# print("\nGroup by 'Position' and sum the stats:")
# print(df.groupby(level='Position').sum())

# import numpy as np
# from collections import Counter

# cups = [1, 2, 3, 2, 2, 4, 3, 5, 2, 6, 100]

# print("Mean:", np.mean(cups))       # Affected by the outlier
# print("Median:", np.median(cups))   # More stable
# print("Standard Deviation:", np.std(cups))  # Shows spread

# # Mode (using Counter since NumPy doesn’t have mode)
# counts = Counter(cups)
# mode = counts.most_common(1)[0][0]
# print("Mode:", mode)


