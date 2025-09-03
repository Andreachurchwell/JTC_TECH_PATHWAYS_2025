# import requests
# import json
# import csv
# import os
# from datetime import datetime
# class WeatherDataFetcher:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.base_url = "https://api.weatherbit.io/v2.0/history/daily"
#     def fetch_weather_data(self, city="selmer", country="US",
#                           start_date="2024-01-01", end_date="2024-12-31"):
#         """
#         Fetch weather data from Weatherbit API
#         """
#         params = {
#             'city': city,
#             'country': country,
#             'start_date': start_date,
#             'end_date': end_date,
#             'key': self.api_key
#         }
#         try:
#             print(f"Fetching weather data for {city}, {country}...")
#             response = requests.get(self.base_url, params=params)
#             response.raise_for_status()  # Raises an HTTPError for bad responses
#             # Convert to JSON
#             data = response.json()
#             print(f"Successfully fetched {len(data.get('data', []))} records")
#             return data
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching data: {e}")
#             return None
#     def save_to_csv(self, json_data, filename="weather_data.csv"):
#         """
#         Save JSON data to CSV file (append mode)
#         """
#         if not json_data or 'data' not in json_data:
#             print("No data to save")
#             return
#         weather_records = json_data['data']
#         if not weather_records:
#             print("No weather records found")
#             return
#         # Get all possible field names from the first record
#         fieldnames = list(weather_records[0].keys())
#         try:
#             # Check if file exists and has content to determine if we need to write headers
#             file_exists = os.path.exists(filename)
#             file_has_content = file_exists and os.path.getsize(filename) > 0
#             print(f"File exists: {file_exists}")
#             print(f"File has content: {file_has_content}")
#             with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 # Only write header if file doesn't exist or is empty
#                 if not file_has_content:
#                     print("Writing headers...")
#                     writer.writeheader()
#                 else:
#                     print("Skipping headers - file already has content")
#                 writer.writerows(weather_records)
#             print(f"Data successfully appended to {filename}")
#             print(f"File size: {os.path.getsize(filename)} bytes")
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")
#     def run(self, output_filename="pollen_data_2025.csv"):
#         """
#         Main method to fetch data and save to CSV
#         """
#         # Fetch data from API
#         weather_data = self.fetch_weather_data()
#         if weather_data:
#             # Save raw JSON for reference (optional)
#             json_filename = f"weather_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
#             try:
#                 with open(json_filename, 'w', encoding='utf-8') as f:
#                     json.dump(weather_data, f, indent=2)
#                 print(f"Raw JSON saved to {json_filename}")
#             except Exception as e:
#                 print(f"Warning: Could not save JSON file: {e}")
#             # Convert to CSV (append mode)
#             self.save_to_csv(weather_data, output_filename)
#         else:
#             print("Failed to fetch weather data")
# # Example usage
# if __name__ == "__main__":
#     # Replace with your actual API key
#     API_KEY = ""
#     # Create fetcher instance
#     fetcher = WeatherDataFetcher(API_KEY)
#     # Run the process
#     fetcher.run()
#     # You can also customize the parameters:
#     # fetcher.run("custom_weather_data.csv")
#     # Or fetch data for different location/dates:
#     # custom_data = fetcher.fetch_weather_data(
#     #     postal_code="10001",
#     #     country="US",
#     #     start_date="2024-06-01",
#     #     end_date="2024-06-30"
#     # )
#     # fetcher.save_to_csv(custom_data, "june_weather.csv")'




import requests
import pandas as pd
from datetime import datetime, timedelta



LAT = 35.1701
LON = -88.5923

def generate_month_ranges(start_date, end_date):
    ranges = []
    current = start_date
    while current < end_date:
        next_month = (current.replace(day=1) + timedelta(days=32)).replace(day=1)
        end = min(next_month - timedelta(days=1), end_date)
        ranges.append((current.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))
        current = next_month
    return ranges

start = datetime(2024, 7, 1)
end = datetime(2025, 6, 30)
month_ranges = generate_month_ranges(start, end)

all_data = []

for start_date, end_date in month_ranges:
    print(f"[INFO] Fetching {start_date} to {end_date}")
    url = "https://api.weatherbit.io/v2.0/history/daily"
    params = {
        "lat": LAT,
        "lon": LON,
        "start_date": start_date,
        "end_date": end_date,
        "key": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json().get("data", [])
        all_data.extend(data)
    except Exception as e:
        print(f"[ERROR] Failed for {start_date} - {end_date}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Keep only needed columns
columns_needed = ["datetime", "max_wind_spd", "precip", "max_temp", "min_temp"]
df = df[columns_needed].copy()

# Rename and clean
df.rename(columns={"datetime": "date"}, inplace=True)
df["city"] = "Selmer"

# Reorder columns
df = df[["date", "city", "max_wind_spd", "precip", "max_temp", "min_temp"]]

# Save cleaned CSV
df.to_csv("cleaned_weather_data_selmer.csv", index=False)
print("[DONE] Saved clean file as cleaned_weather_data_selmer.csv")