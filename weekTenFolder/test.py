# import tkinter as tk
# from tkinter import ttk
# import requests
# from dotenv import load_dotenv
# import os

# # Load API key from .env
# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# # Set up root window
# root = tk.Tk()
# root.title("Weather Dashboard")
# root.geometry("1000x700")
# root.configure(bg="#2E2E2E")

# icon_img = tk.PhotoImage(file="sunny.png")

# # Style setup
# style = ttk.Style(root)
# style.theme_use("default")
# style.configure("TFrame", background="#2E2E2E")
# style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
# style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
# style.configure("Card.TFrame", background="#3C3F41", relief="raised", borderwidth=1)
# style.configure("Card.TLabel", background="#3C3F41", foreground="white")

# # Search bar
# top_frame = ttk.Frame(root)
# top_frame.pack(fill="x", pady=10, padx=20)

# search_entry = ttk.Entry(top_frame, width=40)
# search_entry.pack(side="left", padx=(0, 10))

# def fetch_weather():
#     city = search_entry.get()
#     if not city:
#         return
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         update_weather(data)
#     else:
#         city_label.config(text="City not found.")
#         temp_label.config(text="")

# search_button = ttk.Button(top_frame, text="Search", command=fetch_weather)
# search_button.pack(side="left")

# # Main weather display
# main_weather_frame = ttk.Frame(root)
# main_weather_frame.pack(pady=10, padx=20, fill="x")

# city_label = ttk.Label(main_weather_frame, text="City Name", style="Header.TLabel")
# city_label.grid(row=0, column=0, sticky="w")

# temp_label = ttk.Label(main_weather_frame, text="Temperature + Condition")
# temp_label.grid(row=1, column=0, sticky="w")

# # Weather detail cards
# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10, padx=20, fill="x")

# detail_labels = {}
# for i, key in enumerate(["Visibility", "Dew Point", "Wind", "Humidity", "Cloudiness"]):
#     card = ttk.Frame(details_frame, style="Card.TFrame", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, style="Card.TLabel").pack()
#     val_label = ttk.Label(card, text="--", style="Card.TLabel")
#     val_label.pack()
#     detail_labels[key] = val_label

# # Function to update UI
# def update_weather(data):
#     city_label.config(text=data["name"])
#     temp = round(data["main"]["temp"])
#     condition = data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {condition}")

#     visibility = f"{data.get('visibility', 0) / 1000:.1f} km"
#     wind = f"{data['wind']['speed']} mph"
#     humidity = f"{data['main']['humidity']}%"
#     clouds = f"{data['clouds']['all']}%"
#     dew_point = "--"  # Not in standard endpoint, leave as placeholder

#     detail_labels["Visibility"].config(text=visibility)
#     detail_labels["Wind"].config(text=wind)
#     detail_labels["Humidity"].config(text=humidity)
#     detail_labels["Cloudiness"].config(text=clouds)
#     detail_labels["Dew Point"].config(text=dew_point)



#     # Display icon under main weather frame
# icon_label = tk.Label(root, image=icon_img, bg="#2E2E2E")
# icon_label.image = icon_img  # Keep a reference!


# icon_label.pack(pady=10)


# from PIL import Image, ImageTk
# from io import BytesIO

# # Create radar label inside the existing root window
# radar_label = tk.Label(root, bg="#2E2E2E")
# radar_label.pack(pady=20)


# def update_radar():
#     url = "https://tilecache.rainviewer.com/v2/radar/nowcast/256/10/511/382/8/1_1.png"
#     try:
#         response = requests.get(url)
#         print(f"Radar fetch status code: {response.status_code}")
#         if response.status_code == 200:
#             img_data = response.content
#             img = Image.open(BytesIO(img_data))
#             img = img.resize((256, 256))
#             radar_img = ImageTk.PhotoImage(img)
#             radar_label.config(image=radar_img)
#             radar_label.image = radar_img
#             print("Radar image updated successfully.")
#         else:
#             print("Failed to fetch radar image.")
#     except Exception as e:
#         print(f"Radar update failed: {e}")

#     root.after(300000, update_radar)  # Refresh every 5 minutes

# radar_label = tk.Label(root, bg="#2E2E2E", bd=2, relief="solid")
# radar_label.pack(pady=20)

# update_radar()  # Start updating radar image


# root.mainloop()





# import tkinter as tk
# from tkinter import ttk
# import requests
# from dotenv import load_dotenv
# import os
# from PIL import Image, ImageTk
# from io import BytesIO
# import math

# # Load API key from .env
# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# # Convert lat/lon to tile x,y at zoom level (Web Mercator)
# def deg2num(lat_deg, lon_deg, zoom):
#     lat_rad = math.radians(lat_deg)
#     n = 2.0 ** zoom
#     xtile = int((lon_deg + 180.0) / 360.0 * n)
#     ytile = int((1.0 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2.0 * n)
#     return (xtile, ytile)

# # Get latest radar timestamp from RainViewer API
# def get_latest_radar_timestamp():
#     url = "https://api.rainviewer.com/public/weather-maps.json"
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             latest = data['radar']['past'][-1]['time']
#             return latest
#         else:
#             print("Failed to get radar timestamps:", response.status_code)
#     except Exception as e:
#         print("Error fetching radar timestamps:", e)
#     return None

# # Tkinter setup
# root = tk.Tk()
# root.title("Weather Dashboard")
# root.geometry("1000x700")
# root.configure(bg="#2E2E2E")

# # Styles
# style = ttk.Style(root)
# style.theme_use("default")
# style.configure("TFrame", background="#2E2E2E")
# style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
# style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
# style.configure("Card.TFrame", background="#3C3F41", relief="raised", borderwidth=1)
# style.configure("Card.TLabel", background="#3C3F41", foreground="white")

# # Frames
# top_frame = ttk.Frame(root)
# top_frame.pack(fill="x", pady=10, padx=20)

# search_entry = ttk.Entry(top_frame, width=40)
# search_entry.pack(side="left", padx=(0, 10))

# search_button = ttk.Button(top_frame, text="Search")
# search_button.pack(side="left")

# main_weather_frame = ttk.Frame(root)
# main_weather_frame.pack(pady=10, padx=20, fill="x")

# city_label = ttk.Label(main_weather_frame, text="City Name", style="Header.TLabel")
# city_label.grid(row=0, column=0, sticky="w")

# temp_label = ttk.Label(main_weather_frame, text="Temperature + Condition")
# temp_label.grid(row=1, column=0, sticky="w")

# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10, padx=20, fill="x")

# detail_labels = {}
# for i, key in enumerate(["Visibility", "Dew Point", "Wind", "Humidity", "Cloudiness"]):
#     card = ttk.Frame(details_frame, style="Card.TFrame", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, style="Card.TLabel").pack()
#     val_label = ttk.Label(card, text="--", style="Card.TLabel")
#     val_label.pack()
#     detail_labels[key] = val_label

# # Radar label
# radar_label = tk.Label(root, bg="#2E2E2E", bd=2, relief="solid")
# radar_label.pack(pady=20)

# # Placeholder icon image - replace with your own icon if you want
# # icon_img = tk.PhotoImage(file="sunny.png")
# # icon_label = tk.Label(root, image=icon_img, bg="#2E2E2E")
# # icon_label.image = icon_img
# # icon_label.pack(pady=10)

# # Global to keep radar image reference
# radar_img_ref = None

# # Update radar tile image
# def update_radar(lat, lon, zoom=7):
#     global radar_img_ref
#     timestamp = get_latest_radar_timestamp()
#     if not timestamp:
#         print("No radar timestamp available.")
#         return

#     x, y = deg2num(lat, lon, zoom)
#     tile_url = f"https://tilecache.rainviewer.com/v2/radar/{timestamp}/256/{zoom}/{x}/{y}/8/1_1.png"
#     print("Radar tile URL:", tile_url)

#     try:
#         response = requests.get(tile_url)
#         print(f"Radar fetch status code: {response.status_code}")
#         if response.status_code == 200:
#             img_data = response.content
#             img = Image.open(BytesIO(img_data))
#             img = img.resize((256, 256))
#             radar_img_ref = ImageTk.PhotoImage(img)
#             radar_label.config(image=radar_img_ref)
#         else:
#             print("Failed to fetch radar image.")
#     except Exception as e:
#         print("Radar update failed:", e)

#     root.after(300000, lambda: update_radar(lat, lon, zoom))  # Refresh every 5 mins

# # Update weather and start radar update
# def update_weather(data):
#     city_label.config(text=data["name"])
#     temp = round(data["main"]["temp"])
#     condition = data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {condition}")

#     visibility = f"{data.get('visibility', 0) / 1000:.1f} km"
#     wind = f"{data['wind']['speed']} mph"
#     humidity = f"{data['main']['humidity']}%"
#     clouds = f"{data['clouds']['all']}%"
#     dew_point = "--"  # Placeholder

#     detail_labels["Visibility"].config(text=visibility)
#     detail_labels["Wind"].config(text=wind)
#     detail_labels["Humidity"].config(text=humidity)
#     detail_labels["Cloudiness"].config(text=clouds)
#     detail_labels["Dew Point"].config(text=dew_point)

#     # Optionally update icon here if you want

#     # Start radar updates for this location
#     lat = data["coord"]["lat"]
#     lon = data["coord"]["lon"]
#     update_radar(lat, lon)

# def fetch_weather():
#     city = search_entry.get()
#     if not city:
#         return
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         update_weather(data)
#     else:
#         city_label.config(text="City not found.")
#         temp_label.config(text="")

# search_button.config(command=fetch_weather)

# root.mainloop()



# import tkinter as tk
# from tkinter import ttk
# import requests
# from dotenv import load_dotenv
# import os
# from PIL import Image, ImageTk, ImageDraw
# import math

# # Load your API key
# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# # GUI setup
# root = tk.Tk()
# root.title("Weather + World Map")
# root.geometry("1000x700")
# root.configure(bg="#2E2E2E")

# # ---------- Styles ----------
# style = ttk.Style(root)
# style.theme_use("default")
# style.configure("TFrame", background="#2E2E2E")
# style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
# style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
# style.configure("Card.TFrame", background="#3C3F41", relief="raised", borderwidth=1)
# style.configure("Card.TLabel", background="#3C3F41", foreground="white")

# # ---------- Top search frame ----------
# top_frame = ttk.Frame(root)
# top_frame.pack(fill="x", pady=10, padx=20)

# search_entry = ttk.Entry(top_frame, width=40)
# search_entry.pack(side="left", padx=(0, 10))

# # ---------- Main weather info ----------
# main_weather_frame = ttk.Frame(root)
# main_weather_frame.pack(pady=10, padx=20, fill="x")

# city_label = ttk.Label(main_weather_frame, text="City Name", style="Header.TLabel")
# city_label.grid(row=0, column=0, sticky="w")

# temp_label = ttk.Label(main_weather_frame, text="Temperature + Condition")
# temp_label.grid(row=1, column=0, sticky="w")

# # ---------- Detail cards ----------
# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10, padx=20, fill="x")

# detail_labels = {}
# for i, key in enumerate(["Visibility", "Dew Point", "Wind", "Humidity", "Cloudiness"]):
#     card = ttk.Frame(details_frame, style="Card.TFrame", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, style="Card.TLabel").pack()
#     val_label = ttk.Label(card, text="--", style="Card.TLabel")
#     val_label.pack()
#     detail_labels[key] = val_label

# # ---------- Load world map image ----------
# try:
#     original_img = Image.open("C:/Users/achur/desktop/python/techPathwayNotes/weekTenFolder/world2.png").resize((800, 400), Image.Resampling.LANCZOS)
# except Exception as e:
#     print("Image load error:", e)
#     root.destroy()

# map_img = original_img.copy()
# map_tk = ImageTk.PhotoImage(map_img)
# map_label = tk.Label(root, image=map_tk, bg="#2E2E2E")
# map_label.pack(pady=20)

# # ---------- Map conversion function ----------
# def latlon_to_xy(lat, lon, width, height):
#     x = int((lon + 180) * (width / 360))
#     lat = max(min(lat, 85.0511), -85.0511)  # clamp latitude
#     lat_rad = math.radians(lat)
#     merc_n = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
#     y = int((1 - merc_n / math.pi) / 2 * height)
#     return x, y

# # ---------- Weather update function ----------
# def update_weather(data):
#     city_label.config(text=data["name"])
#     temp = round(data["main"]["temp"])
#     condition = data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {condition}")

#     visibility = f"{data.get('visibility', 0) / 1000:.1f} km"
#     wind = f"{data['wind']['speed']} mph"
#     humidity = f"{data['main']['humidity']}%"
#     clouds = f"{data['clouds']['all']}%"
#     dew_point = "--"

#     detail_labels["Visibility"].config(text=visibility)
#     detail_labels["Wind"].config(text=wind)
#     detail_labels["Humidity"].config(text=humidity)
#     detail_labels["Cloudiness"].config(text=clouds)
#     detail_labels["Dew Point"].config(text=dew_point)

#     # Plot on map
#     lat = data["coord"]["lat"]
#     lon = data["coord"]["lon"]

#     # Copy original to redraw clean map
#     new_img = original_img.copy()
#     draw = ImageDraw.Draw(new_img)
#     x, y = latlon_to_xy(lat, lon, new_img.width, new_img.height)
#     draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill="red")
    
#     global map_tk
#     map_tk = ImageTk.PhotoImage(new_img)
#     map_label.config(image=map_tk)
#     map_label.image = map_tk

# # ---------- Weather fetch ----------
# def fetch_weather():
#     city = search_entry.get()
#     if not city:
#         return
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         update_weather(data)
#     else:
#         city_label.config(text="City not found.")
#         temp_label.config(text="")

# # Connect button
# search_button = ttk.Button(top_frame, text="Search", command=fetch_weather)
# search_button.pack(side="left")

# root.mainloop()



import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from dotenv import load_dotenv
import requests
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# --- Weather Fetch ---
def fetch_weather():
    city = city_entry.get()
    if not city:
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        update_ui(data)
    else:
        city_label.config(text="City not found.")
        temp_label.config(text="")
        for label in detail_labels.values():
            label.config(text="--")

# --- UI Update ---
def update_ui(data):
    city = data["name"]
    temp = round(data["main"]["temp"])
    condition = data["weather"][0]["description"].title()

    city_label.config(text=f"{city}")
    temp_label.config(text=f"{temp}°F, {condition}")

    detail_labels["Humidity"].config(text=f"{data['main']['humidity']}%")
    detail_labels["Wind"].config(text=f"{data['wind']['speed']} mph")
    detail_labels["Cloudiness"].config(text=f"{data['clouds']['all']}%")
    detail_labels["Visibility"].config(text=f"{data.get('visibility', 0) / 1000:.1f} km")

    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]
    map_widget.set_position(lat, lon)
    map_widget.set_marker(lat, lon, text=city)
    map_widget.set_zoom(6)

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Weather + Map")
root.geometry("800x620")
root.configure(bg="#2E2E2E")

style = ttk.Style(root)
style.theme_use("default")
style.configure("TFrame", background="#2E2E2E")
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

# --- Top Search ---
top_frame = ttk.Frame(root)
top_frame.pack(pady=10)

city_entry = ttk.Entry(top_frame, width=30)
city_entry.pack(side="left", padx=5)

search_button = ttk.Button(top_frame, text="Search", command=fetch_weather)
search_button.pack(side="left", padx=5)

# --- City + Condition ---
main_frame = ttk.Frame(root)
main_frame.pack(pady=10)

city_label = ttk.Label(main_frame, text="City Name", style="Header.TLabel")
city_label.grid(row=0, column=0, sticky="w", padx=10)

temp_label = ttk.Label(main_frame, text="Temperature + Condition", style="TLabel")
temp_label.grid(row=1, column=0, sticky="w", padx=10)

# --- Weather Cards ---
details_frame = ttk.Frame(root)
details_frame.pack(pady=10)

detail_labels = {}
for i, key in enumerate(["Humidity", "Wind", "Cloudiness", "Visibility"]):
    card = ttk.Frame(details_frame, style="TFrame", padding=10)
    card.grid(row=0, column=i, padx=5)
    ttk.Label(card, text=key, style="TLabel").pack()
    val = ttk.Label(card, text="--", style="TLabel")
    val.pack()
    detail_labels[key] = val

# --- Map Frame ---
map_outer_frame = tk.Frame(root, bg="#444", bd=2, relief="sunken")
map_outer_frame.pack(pady=15)

map_widget = TkinterMapView(map_outer_frame, width=500, height=300, corner_radius=5)
map_widget.pack()

root.mainloop()












# import tkbootstrap as ttk  # Replaces both tkinter and ttk
# import requests
# from dotenv import load_dotenv
# import os

# # Load API key from .env
# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# # Set up root window with a modern theme
# root = ttk.Window(themename="darkly")  # Try "darkly", "superhero", "flatly", "cyborg", etc.
# root.title("Weather Dashboard")
# root.geometry("1000x700")

# # Top search bar
# top_frame = ttk.Frame(root)
# top_frame.pack(fill="x", pady=10, padx=20)

# search_entry = ttk.Entry(top_frame, width=40)
# search_entry.pack(side="left", padx=(0, 10))

# def fetch_weather():
#     city = search_entry.get()
#     if not city:
#         return
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         update_weather(data)
#     else:
#         city_label.config(text="City not found.")
#         temp_label.config(text="")

# search_button = ttk.Button(top_frame, text="Search", bootstyle="primary", command=fetch_weather)
# search_button.pack(side="left")

# # Main weather display
# main_weather_frame = ttk.Frame(root)
# main_weather_frame.pack(pady=10, padx=20, fill="x")

# city_label = ttk.Label(main_weather_frame, text="City Name", font=("Segoe UI", 18, "bold"))
# city_label.grid(row=0, column=0, sticky="w")

# temp_label = ttk.Label(main_weather_frame, text="Temperature + Condition", font=("Segoe UI", 14))
# temp_label.grid(row=1, column=0, sticky="w")

# # Weather detail cards
# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10, padx=20, fill="x")

# detail_labels = {}
# for i, key in enumerate(["Visibility", "Dew Point", "Wind", "Humidity", "Cloudiness"]):
#     card = ttk.Frame(details_frame, bootstyle="secondary", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, font=("Segoe UI", 10, "bold")).pack()
#     val_label = ttk.Label(card, text="--", font=("Segoe UI", 10))
#     val_label.pack()
#     detail_labels[key] = val_label

# # Function to update UI
# def update_weather(data):
#     city_label.config(text=data["name"])
#     temp = round(data["main"]["temp"])
#     condition = data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {condition}")

#     visibility = f"{data.get('visibility', 0) / 1000:.1f} km"
#     wind = f"{data['wind']['speed']} mph"
#     humidity = f"{data['main']['humidity']}%"
#     clouds = f"{data['clouds']['all']}%"
#     dew_point = "--"  # Not in standard endpoint, leave as placeholder

#     detail_labels["Visibility"].config(text=visibility)
#     detail_labels["Wind"].config(text=wind)
#     detail_labels["Humidity"].config(text=humidity)
#     detail_labels["Cloudiness"].config(text=clouds)
#     detail_labels["Dew Point"].config(text=dew_point)

# root.mainloop()


