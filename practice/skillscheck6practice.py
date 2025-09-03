# ✅ Ready to Start?
# Let’s jump in with this one:

# 🧪 Prompt 1:
# Write a function that takes a list of numbers and returns a new list of only the even numbers.
# psudeo code
# function called is_even()
# takes in a list
# return new list [] of only the evens

# def is_even(listOfN):
#     result = []
#     for num in listOfN:
#         if num % 2 == 0:
#             result.append(num)
#     return result
# print(is_even([1,2,3,4,5,6,7,8,9]))


# 💥 Let’s Do One More Prompt (Practice w/ Try/Except)
# Prompt 2:

# Write a function that asks the user to enter a temperature. 
# If they enter something that’s not a number, show a message saying “Invalid input, please enter a number.”


# function called is_valid 
# takes in input as param
# if the num is not valid ill show a msg saying invalid input please enter a num

# def check_temp():
#     user_input = input('Please enter a temp:')
#     try:
#         temp = float(user_input)
#         print('valid temp', temp)
#     except ValueError:
#         print('invalid input, please enter a number')

# print(check_temp())


# 🧪 Prompt 3:
# You have a list of cities and their temperatures in a dictionary.
# Write a function that prints only the cities where the temp is over 85°F.

# temps = {
#     "selmer": 95,
#     'atlanta': 76,
#     'new york': 85,
#     'la': 92
# }

# def hot_cities(temps):
#     result = []
#     for city,temp in temps.items():
#         if temp > 85:
#             result.append(city)
#     return result

# print(hot_cities(temps))

# 🔑 Tip:
# Use a set() to help — it automatically removes duplicates.

# Want to try it?
# Make a function called remove_dupes(city_list) that returns a list of unique cities.

# Go ahead and type it out — I’ll be right here to check!

# cities = ['Selmer', 'Atlanta', 'Queens', 'Selmer', 'Atlanta']


# def remove_dupes(city_list):
#     unique_list = list(set(city_list))
#     return unique_list
# print(remove_dupes(cities))



# 🧪 Prompt 5: CSV Filtering
# You have a CSV file called weather.csv with the following columns:
# city, temperature, date

# Some rows are missing the temperature (it's blank).
# 👉 Write a function that filters only valid entries and prints the cities with temperatures over 85°F.

# import csv

# def filter_hot_cities():
#     with open('weather_csv', newline='') as file:
#         reader = csv.reader(file)
#         next(reader)

#         for row in reader:
#             city = row[0]
#             temp = row[1]

#             if temp: 
#                 if float(temp) > 85:
#                     print(city)

# filter_hot_cities()

# def read_file_lines(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             print(line.strip())


# ❓Q7.
# You have a list of cities from a file, but some appear more than once.
# How would you remove duplicates before displaying the list in a GUI dropdown?

# Go ahead and talk me through your thinking or start coding — I’ll follow your lead.

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# city_list = ['selmer', 'atlanta', 'miami', 'dallas', 'selmer']

# unique_city = []

# for city in city_list:
#     print('city=', city)
#     if city not in unique_city:
#         unique_city.append(city)
# print('unique_city==', unique_city)

# dropdown = ttk.Combobox(root, values=unique_city)
# dropdown.pack()

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# with open('cities.txt', 'r') as f:
#     city_list = [line.strip() for line in f]


# city_list = ['selmer', 'houston', 'miami', 'Selmer', 'dallas']

# titled_cities = [city.title() for city in city_list]
# # print(titled_cities)
# uniques = list(set(titled_cities))
# print('result==', sorted(uniques))



# import requests

# from config import api_key

# def fetch_weather(city):
#     url = f'http://api.openweathermapq={city}&apiid={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     print('data=', data)

# city = 'Selmer'
# weather = fetch_weather(city)
# print(weather)

# ❓Q9.
# The user enters a temperature in a Tkinter form.
# Make sure it's a valid number before saving it to a file.

# You can go ahead and talk it out, or start coding.
# Let me know what you’re thinking — I’ll follow along and guide where needed.

# psudeocode: i would need to import tkinter and have an input and btn 
# with an onclick that has try and except also maybe import messagebox
# my try and except would need to make sure its a valid num and if not, give a error msg 
# as well as except a val error so it dont crash

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title('temp entry')

# entry = tk.Entry(root)
# entry.pack()


# def on_click():
#     temp = entry.get()
#     try:
#         float(temp)
#         messagebox.showinfo('yay',f'{temp} is good!!')
#     except ValueError:
#         messagebox.showerror('invalid please enter a number')

# tk.Button(root, text='save temp', command=on_click).pack()


# root.mainloop()



# ❓Q10.
# You're collecting weather data for multiple cities and want to store it in a dictionary.
# Show how you would organize and later access the data.


# i would import pandas and organize w key value pairs 
# then when accessing i would call what i needed in square brackets

# weather_data = {
#     'Selmer': {'temp': 85, 'wind': 5, 'humidity': 70},
#     'Atlanta': {'temp': 82, 'wind': 2, 'humidity': 60},
#     'Miami': {'temp': 95, 'wind': 8, 'humidity': 75},
# }

# print('Selmer Temp:', weather_data['Selmer']['temp'])

# for city, data in weather_data.items():
#     # print('city=', city, 'data=', data)
#     print(f"{city}: temp: {data['temp']} wind:{data['wind']} humidity: {data['humidity']}")


# ❓Q11.
# You want to add a new feature — calculating humidity range — to your project.
# Organize this logic in a separate module and connect it to main.py.

# okay, lets say i want humidity range to show up in my mainwindow, first i would prob
# create a folder called features or utils and in it make humitity.py with all the logic
# then inside lets say my main window, i would import from features humidity.py then i would call it when i need it

# from features.humidity import huidity_range

# humid_vals = [33,44,55,66,77]

# range_val = huidity_range(humid_vals)
# print(f'Humidity range:', {range_val})