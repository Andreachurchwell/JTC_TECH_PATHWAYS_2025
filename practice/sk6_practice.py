# 🔹 Practice Q1: Filtering Clean Data
# Scenario Recap:
# You have a CSV file with city, temperature, and date. Some rows are missing temperature values.
# You want to filter:

# Only valid rows (no missing temps)

# Cities where temperature is over 85°F

# # ANSWER

# # I would import pandas
# import pandas as pd

# # load csv
# df = pd.read_csv('weather.csv')
# # drop missing temps
# df = df.dropna(subset=['temperature'])
# # filter temps > 85
# hot_cities = df[df['temperature'] > 85]
# # display just the city and temp
# print(hot_cities[['city', 'temperature']])






# Scenario Recap:
# You're building a Tkinter GUI form where:

# The user enters a city and a temperature

# They click a button

# That button saves the data to a CSV file

# ✅ What your code needs to do:
# Grab input from Entry fields

# Validate that temperature is a number

# Append the city and temp to a .csv file

# Handle errors using try/except

# Optional: Show a messagebox if data is saved or invalid


# import tkinter as tk
# from tkinter import messagebox
# import csv

# def save_entry():
#     city = city_entry.get()
#     temp = temp_entry.get()
    
#     try:
#         temp = float(temp)
#         with open('weather.csv', 'a', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow([city, temp])
#         messagebox.showinfo('Success', 'Ur INfo is saved')
#     except ValueError:
#         messagebox.showerror('Error', "please enter a valid number")

# root = tk.Tk()
# root.title('Weather Entry FOrm')

# tk.Label(root, text='City').pack()
# city_entry = tk.Entry(root)
# city_entry.pack()

# tk.Label(root, text='Temp').pack()
# temp_entry = tk.Entry(root)
# temp_entry.pack()

# tk.Button(root, text='Save', command=save_entry).pack()
# root.mainloop()

