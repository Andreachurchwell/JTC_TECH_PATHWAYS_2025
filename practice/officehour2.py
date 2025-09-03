# Practice Q1: Filtering Clean Data
# Scenario:
# You have a CSV file with weather data, including city, temperature, and date. Some rows have missing temperatures. You want to filter only valid entries and display all cities with temperatures over 85°F.

# Questions:
# What steps would you take to clean the data?
# How would you filter only high-temperature rows?
# What structure would you use to display the result?




# 🔹 Practice Q2: Button to Append New Entry

# Scenario:
# You’re building a GUI with a form: the user enters a city and temperature, and clicks a button to save that data to a CSV file.

# Proctor Questions:
# What does the button function need to do?
# How would you collect the input from the form?
# How would you store the entry in the file?

# What does the button function need to do?
# Trigger an on click function called save-to-csv, try except  float value error, message box 
# How would you collect the input from the form?
# Entry, get
# How would you store the entry in the file?
# Open csv in append mode, save the file, save to css function



# Practice Q3: Count Weather Events

# Scenario:
# You have a list of weather descriptions from an API, like [‘Rain’, ‘Clear’, ‘Rain’, ‘Clouds’]. You want to count how often each type appears.

# Questions:
# How would you structure the code to count each type?
# What Python tools could help you do this?
# Where would you show the results in the GUI? w charts/matplotlib

# my_weather_list = ['Rain', 'Clear', 'Rain', 'Clouds']

# counts = {}
# for weather in my_weather_list:
#     if weather in counts:
#         counts[weather] += 1
#     else: 
#         counts[weather] = 1
# print(counts)



# 🔹 Practice Q4: Show Forecast from API

# Scenario:
# You want to call an API that gives a 3-day forecast and show those 3 days and temperatures in the GUI.
# import requests
# import os
# from dotenv import_dotenv
# load_dotenv()

# api_key = os.getenv('api_key')
# city = 'Selmer'

# url = f'https: api.openweather/data/2.5/forecast?q={city}&appid={api_key}'
# response = requests.get(url)
# data = response.json()

# # Proctor Questions:
# # What Python tools would you use to get and parse the data?

# # How would you extract just the date and temperature values?

# # How would you display them?


# QUESTIONS 5 & 6 COMING 2mw!!!!!8-2-25 @ 12
# Q5. You build a GUI with a field for date input. You want to check that the user enters the date in YYYY-MM-DD format before saving.
# Q6. You have an SQLite table of temperatures by city. You want to calculate and show the average temperature for a city entered by the user.


# Q7. You have a list of cities from a file, but some appear more than once. Remove duplicates before displaying the list in a GUI dropdown.

# Q8. Store your API key in a separate configuration file. Write logic to read that key and use it in your request function.

# Q9. The user enters a temperature in a Tkinter form. Make sure it's a valid number before saving it to a file.

# Q10. You're collecting weather data for multiple cities and want to store it in a dictionary. Show how you would organize and later access the data.

# Q11. You want to add a new feature—calculating humidity range—to your project. Organize this logic in a separate module and connect it to `main.py`.

# Q12. After fetching weather data for three cities, save a plain-text report summarizing the results in a readable format.

# Q13. Display weather records (city, date, temperature) in a grid layout inside a GUI using Tkinter.

# Q14. You have a sorted list of temperatures. Use binary search to find out whether a specific value is in the list.

# Q15. Your API fetch sometimes fails or returns the wrong format. Use `try/except` to prevent your app from crashing and show an error message instead.

# Q16. You calculate an average temperature and want to save it in a database table called `averages`. Write the logic to insert it using SQL.






# 1. You have a CSV file with weather data, including city, temperature, and date. Some rows have missing temperatures. You want to filter only valid entries and display all cities with temperatures over 85°F.
# What steps would you take to clean the data?
# How would you filter only high-temperature rows?
# What structure would you use to display the result?



# 2. You’re building a GUI with a form: the user enters a city and temperature, and clicks a button to save that data to a CSV file.
# What does the button function need to do?
# How would you collect the input from the form?
# How would you store the entry in the file?



# 3. You have a list of weather descriptions from an API, like [‘Rain’, ‘Clear’, ‘Rain’, ‘Clouds’]. You want to count how often each type appears.
# How would you structure the code to count each type?
# What Python tools could help you do this?
# Where would you show the results in the GUI?



# 4. You want to call an API that gives a 3-day forecast and show those 3 days and temperatures in the GUI.
# What Python tools would you use to get and parse the data?
# How would you extract just the date and temperature values?
# How would you display them?


# Q5. You build a GUI with a field for date input. You want to check that the user enters the date in YYYY-MM-DD format before saving.
# How would you check if the input is valid?
# What would you do if the input is wrong?
# Where would you show a helpful message?


# Q6. You have an SQLite table of temperatures by city. You want to calculate and show the average temperature for a city entered by the user.
# What query would you write to get the average?
# How would you handle a city that has no entries?
# How would the user trigger this in your app?



# Q7. You have a list of cities from a file, but some appear more than once. Remove duplicates before displaying the list in a GUI dropdown.


# Q8. Store your API key in a separate configuration file. Write logic to read that key and use it in your request function.


# Q9. The user enters a temperature in a Tkinter form. Make sure it's a valid number before saving it to a file.


# Q10. You're collecting weather data for multiple cities and want to store it in a dictionary. Show how you would organize and later access the data.

# Q11. You want to add a new feature—calculating humidity range—to your project. Organize this logic in a separate module and connect it to `main.py`.


# Q12. After fetching weather data for three cities, save a plain-text report summarizing the results in a readable format.


# Q13. Display weather records (city, date, temperature) in a grid layout inside a GUI using Tkinter.


# Q14. You have a sorted list of temperatures. Use binary search to find out whether a specific value is in the list.


# Q15. Your API fetch sometimes fails or returns the wrong format. Use `try/except` to prevent your app from crashing and show an error message instead.


# Q16. You calculate an average temperature and want to save it in a database table called `averages`. Write the logic to insert it using SQL.

