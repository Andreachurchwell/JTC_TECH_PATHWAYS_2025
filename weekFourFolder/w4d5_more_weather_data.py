# import requests
# import pandas as pd
# import matplotlib.pyplot as plt

# # Your OpenWeather API Key
# API_KEY = "39d51758f6fdfbe1af66a159b7184d6a"

# # Base URL for OpenWeather API
# BASE_URL = 'http://api.openweathermap.org/data/2.5/onecall'

# # Coordinates for Selmer, TN (you can use any city coordinates)
# lat = 35.16442
# lon = -88.59884

# # Set parameters for the API call
# params = {
#     'lat': lat,
#     'lon': lon,
#     'exclude': 'minutely,alerts',  # Exclude unnecessary data
#     'appid': API_KEY,
#     'units': 'imperial'  # Use 'metric' for Celsius
# }

# # Make the API request
# response = requests.get(BASE_URL, params=params)

# if response.status_code == 200:
#     data = response.json()

#     # Extract relevant data
#     daily_data = data['daily']  # Get daily weather data

#     # Create a DataFrame from the data
#     weather_df = pd.DataFrame(daily_data)

#     # Convert timestamps to datetime
#     weather_df['date'] = pd.to_datetime(weather_df['dt'], unit='s')

#     # Extract temperatures and precipitation data
#     weather_df['temp_max'] = weather_df['temp'].apply(lambda x: x['max'])
#     weather_df['temp_min'] = weather_df['temp'].apply(lambda x: x['min'])

#     # Handle missing rain data using .get()
#     weather_df['precipitation'] = weather_df['rain'].apply(lambda x: x.get('1h', 0) if isinstance(x, dict) else 0)

#     # Print out the data for inspection
#     print(weather_df[['date', 'temp_max', 'temp_min', 'precipitation']])

#     # Plotting the data
#     plt.figure(figsize=(12, 6))
#     plt.plot(weather_df['date'], weather_df['temp_max'], label='Max Temp (°F)', color='orange', linestyle='-', linewidth=2)
#     plt.plot(weather_df['date'], weather_df['temp_min'], label='Min Temp (°F)', color='blue', linestyle='-', linewidth=2)
#     plt.bar(weather_df['date'], weather_df['precipitation'], label='Precipitation (inches)', color='green', alpha=0.3)

#     # Adding labels and title
#     plt.xlabel('Date')
#     plt.ylabel('Weather Data')
#     plt.title('Weather Data from OpenWeather API - Selmer, TN')
#     plt.xticks(rotation=45)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

# else:
#     print("Error fetching data:", response.status_code)


# import requests

# API_KEY = "39d51758f6fdfbe1af66a159b7184d6a"
# url = f'http://api.openweathermap.org/data/2.5/weather?q=Selmer,US&appid={API_KEY}&units=imperial'

# response = requests.get(url)

# if response.status_code == 200:
#     print("API request successful")
#     print(response.json())
# else:
#     print("Error fetching data:", response.status_code)


# import requests
# import datetime

# API_KEY = "39d51758f6fdfbe1af66a159b7184d6a"

# # Coordinates for Selmer, TN (You can adjust coordinates for other locations)
# lat = 35.1701
# lon = -88.5923

# # Get the current time (for the past 5 days)
# current_timestamp = int(datetime.datetime.now().timestamp())

# # Make sure your date is within the past 5 days for timemachine
# # You could adjust `current_timestamp` to be 5 days ago if you're testing on an earlier date
# timestamp_5_days_ago = current_timestamp - (5 * 24 * 60 * 60)  # Subtracting 5 days worth of seconds

# # OpenWeather Historical API URL
# BASE_URL = 'http://api.openweathermap.org/data/2.5/onecall/timemachine'

# # Set parameters for the API call
# params = {
#     'lat': lat,
#     'lon': lon,
#     'dt': timestamp_5_days_ago,  # Example for 5 days ago
#     'appid': API_KEY,
#     'units': 'imperial'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
# }

# # Make the API request
# response = requests.get(BASE_URL, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print("API request successful")

#     # Extract data (temperature, humidity, etc.)
#     weather_data = data['current']

#     # Print weather data
#     print(weather_data)
# else:
#     print(f"Error fetching data: {response.status_code}")





# FROM WEATHERBIT
# API Key	Name	
# eafa4bb747ca407b8878f73a0c8dc0b3	Master API Key
# import requests

# API_KEY = "eafa4bb747ca407b8878f73a0c8dc0b3"  # Your API Key
# base_url = "https://api.weatherbit.io/v2.0/history/hourly"  # Endpoint for hourly historical weather data

# # Coordinates for Selmer, TN
# lat = 35.1701
# lon = -88.5923

# # Date format is 'YYYY-MM-DD'
# start_date = "2025-04-03"
# end_date = "2025-04-04"  # One day later than the start date

# # Build the request URL
# url = f"{base_url}?lat={lat}&lon={lon}&key={API_KEY}&start_date={start_date}&end_date={end_date}"

# # Make the API request
# response = requests.get(url)

# # Check the response status
# if response.status_code == 200:
#     print("API request successful")
#     data = response.json()
#     print(data)
# else:
#     print(f"Error fetching data: {response.status_code}")
#     print(response.text)  # Output the full error message for debugging



# import requests
# import csv
# import pandas as pd
# import matplotlib.pyplot as plt
# API_KEY = "eafa4bb747ca407b8878f73a0c8dc0b3"
# base_url = "https://api.weatherbit.io/v2.0/history/hourly"

# lat = 35.1701
# lon = -88.5923
# start_date = "2025-04-03"
# end_date = "2025-04-04"

# url = f"{base_url}?lat={lat}&lon={lon}&key={API_KEY}&start_date={start_date}&end_date={end_date}"

# response = requests.get(url)

# if response.status_code == 200:
#     print("API request successful")
#     data = response.json()
    
#     # Extract hourly data
#     hourly_data = data.get("data", [])

#     # Define the output file and fields
#     output_file = "selmer_tornado_april3_2025.csv"
#     fields = ["timestamp", "temp", "wind_spd", "gust", "pres", "precip", "clouds", "weather_description"]

#     # Write to CSV
#     with open(output_file, mode='w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fields)
#         writer.writeheader()
#         for entry in hourly_data:
#             writer.writerow({
#                 "timestamp": entry.get("timestamp_local"),
#                 "temp": entry.get("temp"),
#                 "wind_spd": entry.get("wind_spd"),
#                 "gust": entry.get("gust"),
#                 "pres": entry.get("pres"),
#                 "precip": entry.get("precip"),
#                 "clouds": entry.get("clouds"),
#                 "weather_description": entry.get("weather", {}).get("description")
#             })

#     print(f"Data saved to {output_file}")
# else:
#     print(f"Error fetching data: {response.status_code}")
#     print(response.text)



# import requests
# import pandas as pd
# from datetime import datetime

# # API key and base URL
# API_KEY = "eafa4bb747ca407b8878f73a0c8dc0b3"
# base_url = "https://api.weatherbit.io/v2.0/history/hourly"

# # Coordinates for Selmer, TN
# lat = 35.1701
# lon = -88.5923

# # Date format is 'YYYY-MM-DD'
# start_date = "2025-04-02"  # Starting from the evening of April 2nd
# end_date = "2025-04-03"  # Ending in the early morning of April 3rd

# # Build the request URL
# url = f"{base_url}?lat={lat}&lon={lon}&key={API_KEY}&start_date={start_date}&end_date={end_date}"

# # Make the API request
# response = requests.get(url)

# # Check the response status
# if response.status_code == 200:
#     print("API request successful")
#     data = response.json()

#     # Check if the expected data is in the response
#     if "data" in data:
#         # Save the data to a CSV file
#         csv_filename = "selmer_tornado_april2_2025_to_april3.csv"
#         df = pd.DataFrame(data["data"])

#         # Print the column names to check for timestamp field
#         print("Columns in the dataset:", df.columns)

#         # Use the correct timestamp field (this can vary based on API response)
#         if 'timestamp_local' in df.columns:
#             df["timestamp_local"] = pd.to_datetime(df["timestamp_local"])
#         elif 'timestamp_utc' in df.columns:
#             df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"])

#         # Save to CSV
#         df.to_csv(csv_filename, index=False)
#         print(f"Data saved to {csv_filename}")
#     else:
#         print("Error: No 'data' key found in the response.")
# else:
#     print(f"Error fetching data: {response.status_code}")
#     print(response.text)

# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data (replace with your full data)
# data = """
# app_temp,azimuth,clouds,datetime,dewpt,dhi,dni,elev_angle,ghi,h_angle,pod,precip,pres,revision_status,rh,slp,snow,solar_rad,temp,timestamp_local,timestamp_utc,ts,uv,vis,weather,wind_dir,wind_gust_spd,wind_spd
# 19.6,274.4,1,2025-04-02:00,6.7,22,155,2.5,20,,d,0,995,final,41,1011,0,42,20.4,2025-04-01 19:00:00,2025-04-02T00:00:00,1743552000,1.7,16,"{'description': 'Clear Sky', 'code': 800, 'icon': 'c01n'}",126,6.4,3.6
# 18.5,283.1,56,2025-04-02:01,7.7,0,0,-9.7,0,,n,0,995,final,47,1011,0,0,19.3,2025-04-01 20:00:00,2025-04-02T01:00:00,1743555600,0.0,16,"{'description': 'Broken clouds', 'code': 803, 'icon': 'c03n'}",128,6.8,4.0
# 17.8,292.8,52,2025-04-02:02,8.1,0,0,-21.4,0,,n,0,994,final,53,1011,0,0,17.8,2025-04-01 21:00:00,2025-04-02T02:00:00,1743559200,0.0,16,"{'description': 'Broken clouds', 'code': 803, 'icon': 'c03n'}",132,7.6,4.0
# """  # Add the rest of your data here (I included just a snippet)

# # Convert the string data into a DataFrame
# from io import StringIO
# df = pd.read_csv(StringIO(data))

# # Convert timestamp columns into datetime objects (if needed)
# df['timestamp_local'] = pd.to_datetime(df['timestamp_local'])

# # Calculate the min and max wind speeds for each timestamp
# min_wind_speed = df.groupby('timestamp_local')['wind_spd'].min()
# max_wind_speed = df.groupby('timestamp_local')['wind_spd'].max()

# # Plotting the min and max wind speeds
# plt.figure(figsize=(10, 6))
# plt.plot(min_wind_speed.index, min_wind_speed.values, marker='o', color='g', label='Min Wind Speed (mph)')
# plt.plot(max_wind_speed.index, max_wind_speed.values, marker='o', color='r', label='Max Wind Speed (mph)')

# plt.title('Min and Max Wind Speed Over Time')
# plt.xlabel('Time')
# plt.ylabel('Wind Speed (mph)')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()


# import requests
# import pandas as pd

# # API key and base URL
# API_KEY = "eafa4bb747ca407b8878f73a0c8dc0b3"
# base_url = "https://api.weatherbit.io/v2.0/history/hourly"

# # Coordinates for Selmer, TN
# lat = 35.1701
# lon = -88.5923

# # Time range: From 1 AM to 3 AM on April 3, 2025 (rounded to the nearest hour)
# start_date = "2025-04-03:01"  # Starting from 1 AM
# end_date = "2025-04-03:03"    # Ending at 3 AM

# # Build the request URL
# url = f"{base_url}?lat={lat}&lon={lon}&key={API_KEY}&start_date={start_date}&end_date={end_date}&tz=local&units=M"

# # Make the API request
# response = requests.get(url)

# # Check the response status
# if response.status_code == 200:
#     print("API request successful")
#     data = response.json()

#     # Check if the expected data is in the response
#     if "data" in data:
#         # Save the data to a CSV file
#         csv_filename = "selmer_tornado_april3_2025_wind.csv"
#         df = pd.DataFrame(data["data"])

#         # Print the column names to check if wind speed is available
#         print("Columns in the dataset:", df.columns)

#         # Check if 'windspeed' is in the data and extract it
#         if 'wind_spd' in df.columns:
#             print("Wind Speed Data:\n", df[['timestamp_local', 'wind_spd']])
            
#         # Save to CSV
#         df.to_csv(csv_filename, index=False)
#         print(f"Data saved to {csv_filename}")
#     else:
#         print("Error: No 'data' key found in the response.")
# else:
#     print(f"Error fetching data: {response.status_code}")
#     print(response.text)































# import requests
# import pandas as pd
# import matplotlib.pyplot as plt

# # Your Weatherbit API Key
# API_KEY = "eafa4bb747ca407b8878f73a0c8dc0b3"  # Replace with your own API key

# # Base URL for Weatherbit API (Current Weather endpoint)
# BASE_URL = 'https://api.weatherbit.io/v2.0/forecast/daily'

# # Coordinates for Selmer, TN (you can adjust coordinates for other locations)
# lat = 35.1701
# lon = -88.5923

# # Set parameters for the API call
# params = {
#     'lat': lat,
#     'lon': lon,
#     'key': API_KEY,
#     'days': 7,  # Get weather for the next 7 days
#     'units': 'I',  # 'I' for imperial (Fahrenheit, miles, inches)
# }

# # Make the API request
# response = requests.get(BASE_URL, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print("API request successful")

#     # Extract the daily weather data
#     daily_data = data['data']

#     # Create a DataFrame from the daily data
#     weather_df = pd.DataFrame(daily_data)

#     # Convert timestamps to datetime format
#     weather_df['date'] = pd.to_datetime(weather_df['timestamp'], unit='s')

#     # Extract temperature and precipitation data
#     weather_df['temp_max'] = weather_df['temp'].apply(lambda x: x['max'])
#     weather_df['temp_min'] = weather_df['temp'].apply(lambda x: x['min'])
#     weather_df['precipitation'] = weather_df['precip'].fillna(0)  # Handle missing rain data

#     # Print the DataFrame for inspection
#     print(weather_df[['date', 'temp_max', 'temp_min', 'precipitation']])

#     # Plotting the data
#     plt.figure(figsize=(12, 6))
#     plt.plot(weather_df['date'], weather_df['temp_max'], label='Max Temp (°F)', color='orange', linestyle='-', linewidth=2)
#     plt.plot(weather_df['date'], weather_df['temp_min'], label='Min Temp (°F)', color='blue', linestyle='-', linewidth=2)
#     plt.bar(weather_df['date'], weather_df['precipitation'], label='Precipitation (inches)', color='green', alpha=0.3)

#     # Adding labels and title
#     plt.xlabel('Date')
#     plt.ylabel('Weather Data')
#     plt.title('Weather Data from Weatherbit API - Selmer, TN')
#     plt.xticks(rotation=45)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

# else:
#     print(f"Error fetching data: {response.status_code}")



