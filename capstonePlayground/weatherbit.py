import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("wbio")

# Set location (city or lat/lon)
city = "Selmer, TN"
# Optionally: use latitude & longitude
lat = 35.17
lon = -88.59

def fetch_air_quality(lat, lon):
    url = f"https://api.weatherbit.io/v2.0/current/airquality?lat={lat}&lon={lon}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            air_data = data["data"][0]
            print("\n✅ Air Quality Data:")
            print(f"AQI: {air_data['aqi']}")
            print(f"PM2.5: {air_data['pm25']}")
            print(f"PM10: {air_data['pm10']}")
            print(f"O3: {air_data['o3']}")
            print(f"CO: {air_data['co']}")
            print(f"SO2: {air_data['so2']}")
            print(f"NO2: {air_data['no2']}")
        else:
            print("⚠️ No air quality data found.")
    else:
        print(f"❌ Request failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if not API_KEY:
        print("❌ WEATHERBIT_API_KEY not found in .env")
    else:
        fetch_air_quality(lat, lon)

import os
import requests
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
API_KEY = os.getenv("wbio")

def run_test(name, url):
    print(f"\n➡️ Testing {name} endpoint")
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("✅ Success:")
        print(response.json())
    else:
        print("❌ Failed or Restricted:")
        print(response.text)

if __name__ == "__main__":
    if not API_KEY:
        print("❌ API key not found. Check your .env file for 'wbio'.")
    else:
        base_params = f"&key={API_KEY}"
        lat = 35.17
        lon = -88.59
        city = "Selmer"
        country = "US"

        # Current Weather
        run_test("Current Weather", f"https://api.weatherbit.io/v2.0/current?city={city}&country={country}{base_params}")

        # Air Quality
        run_test("Air Quality", f"https://api.weatherbit.io/v2.0/current/airquality?lat={lat}&lon={lon}{base_params}")

        # Pollen Forecast (if available to your plan)
        run_test("Pollen Forecast", f"https://api.weatherbit.io/v2.0/forecast/pollen?city={city}&country={country}{base_params}")

        # Agriculture/Soil Data
        run_test("Soil & Agriculture", f"https://api.weatherbit.io/v2.0/current/agweather?lat={lat}&lon={lon}{base_params}")


# import customtkinter as ctk

# # Dummy data (replace with real API response later)
# dummy_air_data = {
#     "aqi": 47,
#     "pm25": 11,
#     "pm10": 16,
#     "o3": 101.2,
#     "co": 251.9,
#     "so2": 3.85,
#     "no2": 5.42,
#     "pollen_level_tree": 4,
#     "pollen_level_grass": 2,
#     "pollen_level_weed": 2,
#     "mold_level": 0,
#     "predominant_pollen_type": "Trees"
# }

# # Map pollen level number to words and color
# def pollen_level_text(level):
#     levels = ["None", "Low", "Moderate", "High", "Very High"]
#     return levels[level] if 0 <= level < len(levels) else "Unknown"

# def create_air_quality_card(parent, data):
#     card = ctk.CTkFrame(parent, corner_radius=15, fg_color="#3A3A3A")
#     card.pack(pady=10, padx=20, fill="x")

#     # AQI big text
#     aqi_label = ctk.CTkLabel(card, text=f"AQI: {data['aqi']}", font=("Arial", 24, "bold"), text_color="white")
#     aqi_label.pack(pady=(10, 5))

#     pollutant_text = f"PM2.5: {data['pm25']}  |  PM10: {data['pm10']}\nO₃: {data['o3']}  |  NO₂: {data['no2']}\nCO: {data['co']}  |  SO₂: {data['so2']}"
#     pollutants = ctk.CTkLabel(card, text=pollutant_text, font=("Arial", 14), text_color="#DDDDDD")
#     pollutants.pack(pady=5)

#     # Pollen Levels
#     pollen_text = (
#         f"🌳 Trees: {pollen_level_text(data['pollen_level_tree'])}   "
#         f"🌾 Grass: {pollen_level_text(data['pollen_level_grass'])}   "
#         f"🌿 Weed: {pollen_level_text(data['pollen_level_weed'])}\n"
#         f"🦠 Mold: {pollen_level_text(data['mold_level'])}   "
#         f"Predominant: {data['predominant_pollen_type']}"
#     )
#     pollen_label = ctk.CTkLabel(card, text=pollen_text, font=("Arial", 13), text_color="#AAAAAA")
#     pollen_label.pack(pady=(5, 15))

#     return card

# # Test preview
# if __name__ == "__main__":
#     ctk.set_appearance_mode("dark")
#     app = ctk.CTk()
#     app.geometry("400x300")
#     app.title("Air Quality Card Preview")

#     create_air_quality_card(app, dummy_air_data)

#     app.mainloop()