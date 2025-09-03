# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("API_KEY")

# if api_key:
#     print("✅ API Key loaded successfully!")
# else:
#     print("⚠️ API Key not found. Please check your .env file.")



# import tkinter as tk
# from tkinter import ttk
# from tkintermapview import TkinterMapView
# from dotenv import load_dotenv
# import requests
# import os
# from datetime import datetime

# # Load API Key
# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# if not API_KEY:
#     raise Exception("API_KEY not found. Add it to your .env or hardcode it.")

# # --- Weather Fetch ---
# def fetch_current_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def fetch_forecast(city):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # --- UI Update ---
# def update_ui():
#     city = city_entry.get().strip()
#     if not city:
#         status_label.config(text="Please enter a city name.")
#         return

#     status_label.config(text="Fetching weather...")
#     root.update()

#     current_data = fetch_current_weather(city)
#     if not current_data:
#         status_label.config(text="City not found or API error.")
#         clear_weather()
#         clear_forecast()
#         return

#     # Update current weather info
#     city_label.config(text=current_data["name"])
#     temp = round(current_data["main"]["temp"])
#     desc = current_data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {desc}")
#     detail_labels["Humidity"].config(text=f"{current_data['main']['humidity']}%")
#     detail_labels["Wind"].config(text=f"{current_data['wind']['speed']} mph")
#     detail_labels["Cloudiness"].config(text=f"{current_data['clouds']['all']}%")
#     detail_labels["Visibility"].config(text=f"{current_data.get('visibility', 0)/1000:.1f} km")

#     # Update map
#     lat = current_data["coord"]["lat"]
#     lon = current_data["coord"]["lon"]
#     map_widget.set_position(lat, lon)
#     map_widget.set_marker(lat, lon, text=current_data["name"])
#     map_widget.set_zoom(8)

#     # Update forecast
#     forecast_data = fetch_forecast(city)
#     if not forecast_data or "list" not in forecast_data:
#         status_label.config(text="Failed to fetch forecast.")
#         clear_forecast()
#         return

#     show_forecast(forecast_data)
#     status_label.config(text="Weather updated successfully.")

# def clear_weather():
#     city_label.config(text="--")
#     temp_label.config(text="--")
#     for key in detail_labels:
#         detail_labels[key].config(text="--")

# def clear_forecast():
#     for widget in forecast_frame.winfo_children():
#         widget.destroy()

# def show_forecast(forecast_data):
#     clear_forecast()

#     days = {}
#     for item in forecast_data["list"]:
#         day = item["dt_txt"].split()[0]
#         temp = item["main"]["temp"]
#         desc = item["weather"][0]["description"].title()

#         if day not in days:
#             days[day] = {"temps": [], "descs": []}
#         days[day]["temps"].append(temp)
#         days[day]["descs"].append(desc)

#     # Show next 5 days
#     for day, data in sorted(days.items())[:5]:
#         dt = datetime.strptime(day, "%Y-%m-%d")
#         day_name = dt.strftime("%a, %b %d")
#         temp_max = round(max(data["temps"]))
#         temp_min = round(min(data["temps"]))
#         desc = max(set(data["descs"]), key=data["descs"].count)

#         day_frame = ttk.Frame(forecast_frame, padding=8, relief="ridge")
#         day_frame.pack(side="left", padx=6, pady=6, expand=True, fill="y")

#         ttk.Label(day_frame, text=day_name, font=("Segoe UI", 11, "bold")).pack(pady=(0,4))
#         ttk.Label(day_frame, text=f"High: {temp_max}°F").pack()
#         ttk.Label(day_frame, text=f"Low: {temp_min}°F").pack()
#         ttk.Label(day_frame, text=desc).pack(pady=(4,0))

# # --- Tkinter Setup ---

# root = tk.Tk()
# root.title("Weather + Map + Forecast")
# root.geometry("820x720")
# root.configure(bg="#2E2E2E")

# style = ttk.Style(root)
# style.theme_use("default")
# style.configure("TFrame", background="#2E2E2E")
# style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
# style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

# # --- Top Search ---
# top_frame = ttk.Frame(root)
# top_frame.pack(pady=10)

# city_entry = ttk.Entry(top_frame, width=30, font=("Segoe UI", 12))
# city_entry.pack(side="left", padx=5)
# city_entry.insert(0, "Selmer")

# search_button = ttk.Button(top_frame, text="Search", command=update_ui)
# search_button.pack(side="left", padx=5)

# status_label = ttk.Label(root, text="", font=("Segoe UI", 10, "italic"), foreground="white")
# status_label.pack(pady=(0,10))

# # --- City + Condition ---
# main_frame = ttk.Frame(root)
# main_frame.pack(pady=10)

# city_label = ttk.Label(main_frame, text="City Name", style="Header.TLabel")
# city_label.grid(row=0, column=0, sticky="w", padx=10)

# temp_label = ttk.Label(main_frame, text="Temperature + Condition", style="TLabel")
# temp_label.grid(row=1, column=0, sticky="w", padx=10)

# # --- Weather Cards ---
# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10)

# detail_labels = {}
# for i, key in enumerate(["Humidity", "Wind", "Cloudiness", "Visibility"]):
#     card = ttk.Frame(details_frame, style="TFrame", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, style="TLabel").pack()
#     val = ttk.Label(card, text="--", style="TLabel")
#     val.pack()
#     detail_labels[key] = val

# # --- Map Frame ---
# map_outer_frame = tk.Frame(root, bg="#444", bd=2, relief="sunken")
# map_outer_frame.pack(pady=15)

# map_widget = TkinterMapView(map_outer_frame, width=780, height=300, corner_radius=5)
# map_widget.pack()

# # --- Forecast Frame ---
# forecast_frame = ttk.Frame(root)
# forecast_frame.pack(pady=10, fill="x")

# # Start with default city weather loaded
# update_ui()

# root.mainloop()




# import tkinter as tk
# from tkinter import ttk
# from tkintermapview import TkinterMapView
# from dotenv import load_dotenv
# import requests
# import os
# from datetime import datetime
# import io
# from PIL import Image, ImageTk

# # Load API Key
# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# if not API_KEY:
#     raise Exception("API_KEY not found. Add it to your .env or hardcode it.")

# # Global to hold references to images so Tkinter doesn't GC them
# forecast_icon_refs = {}

# # --- Weather Fetch ---
# def fetch_current_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def fetch_forecast(city):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # --- UI Update ---
# def update_ui():
#     city = city_entry.get().strip()
#     if not city:
#         status_label.config(text="Please enter a city name.")
#         return

#     status_label.config(text="Fetching weather...")
#     root.update()

#     current_data = fetch_current_weather(city)
#     if not current_data:
#         status_label.config(text="City not found or API error.")
#         clear_weather()
#         clear_forecast()
#         return

#     # Update current weather info
#     city_label.config(text=current_data["name"])
#     temp = round(current_data["main"]["temp"])
#     desc = current_data["weather"][0]["description"].title()
#     temp_label.config(text=f"{temp}°F, {desc}")

#     # Load and display current weather icon
#     icon_code = current_data["weather"][0]["icon"]
#     icon_image = get_icon_image(icon_code)
#     if icon_image:
#         icon_label.config(image=icon_image)
#         icon_label.image = icon_image  # keep reference
#     else:
#         icon_label.config(image='')
#         icon_label.image = None

#     detail_labels["Humidity"].config(text=f"{current_data['main']['humidity']}%")
#     detail_labels["Wind"].config(text=f"{current_data['wind']['speed']} mph")
#     detail_labels["Cloudiness"].config(text=f"{current_data['clouds']['all']}%")
#     detail_labels["Visibility"].config(text=f"{current_data.get('visibility', 0)/1000:.1f} km")

#     # Update map
#     lat = current_data["coord"]["lat"]
#     lon = current_data["coord"]["lon"]
#     map_widget.set_position(lat, lon)
#     map_widget.set_marker(lat, lon, text=current_data["name"])
#     map_widget.set_zoom(8)

#     # Update forecast
#     forecast_data = fetch_forecast(city)
#     if not forecast_data or "list" not in forecast_data:
#         status_label.config(text="Failed to fetch forecast.")
#         clear_forecast()
#         return

#     show_forecast(forecast_data)
#     status_label.config(text="Weather updated successfully.")

# def clear_weather():
#     city_label.config(text="--")
#     temp_label.config(text="--")
#     icon_label.config(image='')
#     icon_label.image = None
#     for key in detail_labels:
#         detail_labels[key].config(text="--")

# def clear_forecast():
#     global forecast_icon_refs
#     forecast_icon_refs.clear()  # clear previous references
#     for widget in forecast_frame.winfo_children():
#         widget.destroy()

# def get_icon_image(icon_code):
#     try:
#         url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
#         response = requests.get(url)
#         if response.status_code == 200:
#             image_data = response.content
#             image = Image.open(io.BytesIO(image_data))
#             return ImageTk.PhotoImage(image)
#     except Exception as e:
#         print("Error loading icon:", e)
#     return None

# def show_forecast(forecast_data):
#     clear_forecast()

#     days = {}
#     for item in forecast_data["list"]:
#         day = item["dt_txt"].split()[0]
#         temp = item["main"]["temp"]
#         desc = item["weather"][0]["description"].title()
#         icon = item["weather"][0]["icon"]

#         if day not in days:
#             days[day] = {"temps": [], "descs": [], "icons": []}
#         days[day]["temps"].append(temp)
#         days[day]["descs"].append(desc)
#         days[day]["icons"].append(icon)

#     for idx, (day, data) in enumerate(sorted(days.items())[:5]):
#         dt = datetime.strptime(day, "%Y-%m-%d")
#         day_name = dt.strftime("%a, %b %d")
#         temp_max = round(max(data["temps"]))
#         temp_min = round(min(data["temps"]))
#         desc = max(set(data["descs"]), key=data["descs"].count)
#         icon_code = max(set(data["icons"]), key=data["icons"].count)

#         day_frame = ttk.Frame(forecast_frame, padding=8, relief="ridge")
#         day_frame.pack(side="left", padx=6, pady=6, expand=True, fill="y")

#         # Icon for forecast day
#         icon_img = get_icon_image(icon_code)
#         if icon_img:
#             icon_label_f = ttk.Label(day_frame, image=icon_img)
#             icon_label_f.image = icon_img  # keep reference
#             icon_label_f.pack()

#             # Keep reference globally to prevent GC
#             forecast_icon_refs[f"{day}_{idx}"] = icon_img

#         ttk.Label(day_frame, text=day_name, font=("Segoe UI", 11, "bold")).pack(pady=(4,2))
#         ttk.Label(day_frame, text=f"High: {temp_max}°F").pack()
#         ttk.Label(day_frame, text=f"Low: {temp_min}°F").pack()
#         ttk.Label(day_frame, text=desc).pack(pady=(4,0))

# # --- Tkinter Setup ---

# root = tk.Tk()
# root.title("Weather + Map + Forecast")
# root.geometry("820x720")
# root.configure(bg="#2E2E2E")

# style = ttk.Style(root)
# style.theme_use("default")
# style.configure("TFrame", background="#2E2E2E")
# style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
# style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

# # --- Top Search ---
# top_frame = ttk.Frame(root)
# top_frame.pack(pady=10)

# city_entry = ttk.Entry(top_frame, width=30, font=("Segoe UI", 12))
# city_entry.pack(side="left", padx=5)
# city_entry.insert(0, "Selmer")

# search_button = ttk.Button(top_frame, text="Search", command=update_ui)
# search_button.pack(side="left", padx=5)

# status_label = ttk.Label(root, text="", font=("Segoe UI", 10, "italic"), foreground="white")
# status_label.pack(pady=(0,10))

# # --- City + Condition ---
# # main_frame = ttk.Frame(root)
# # main_frame.pack(pady=10)

# # city_label = ttk.Label(main_frame, text="City Name", style="Header.TLabel")
# # city_label.grid(row=0, column=0, sticky="w", padx=10)

# # temp_label = ttk.Label(main_frame, text="Temperature + Condition", style="TLabel")
# # temp_label.grid(row=1, column=0, sticky="w", padx=10)

# # icon_label = ttk.Label(main_frame, background="#2E2E2E")
# # icon_label.grid(row=1, column=1, sticky="w", padx=5)

# main_card = tk.Frame(root, bg="#3A3A3A", bd=2, relief="ridge", padx=15, pady=15)
# main_card.pack(pady=10, fill="x", padx=20)

# city_label = tk.Label(main_card, text="City Name", font=("Segoe UI", 18, "bold"), fg="white", bg="#3A3A3A")
# city_label.grid(row=0, column=0, sticky="w")

# temp_label = tk.Label(main_card, text="Temperature + Condition", font=("Segoe UI", 14), fg="white", bg="#3A3A3A")
# temp_label.grid(row=1, column=0, sticky="w", pady=(8, 0))

# icon_label = tk.Label(main_card, bg="#3A3A3A")
# icon_label.grid(row=1, column=1, sticky="w", padx=15)




# # --- Weather Cards ---
# details_frame = ttk.Frame(root)
# details_frame.pack(pady=10)

# detail_labels = {}
# for i, key in enumerate(["Humidity", "Wind", "Cloudiness", "Visibility"]):
#     card = ttk.Frame(details_frame, style="TFrame", padding=10)
#     card.grid(row=0, column=i, padx=5)
#     ttk.Label(card, text=key, style="TLabel").pack()
#     val = ttk.Label(card, text="--", style="TLabel")
#     val.pack()
#     detail_labels[key] = val

# # --- Map Frame ---
# map_outer_frame = tk.Frame(root, bg="#444", bd=2, relief="sunken")
# map_outer_frame.pack(pady=15)

# map_widget = TkinterMapView(map_outer_frame, width=780, height=300, corner_radius=5)
# map_widget.pack()

# # --- Forecast Frame ---
# forecast_frame = ttk.Frame(root)
# forecast_frame.pack(pady=10, fill="x")

# # Load initial data
# update_ui()

# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from dotenv import load_dotenv
import requests
import os
from datetime import datetime
import io
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv  # <-- Added for CSV writing

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise Exception("API_KEY not found. Add it to your .env or hardcode it.")

forecast_icon_refs = {}

def fetch_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_detail_icon(name):
    icons = {
        "Humidity": "\U0001F4A7",
        "Wind": "\U0001F32C",
        "Cloudiness": "\u2601",
        "Visibility": "\U0001F441",
    }
    return icons.get(name, "")

# --- New CSV saving functions ---

def save_current_weather_to_csv(data):
    filename = "current_weather.csv"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        data.get("name", ""),
        now_str,
        data["main"].get("temp", ""),
        data["main"].get("humidity", ""),
        data["wind"].get("speed", ""),
        data["clouds"].get("all", ""),
        data.get("visibility", ""),
        data["weather"][0].get("description", ""),
    ]
    header = ["City", "Datetime", "Temp(F)", "Humidity(%)", "Wind Speed(mph)", "Cloudiness(%)", "Visibility(m)", "Description"]
    
    write_header = not os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow(row)

def save_forecast_to_csv(data):
    filename = "forecast.csv"
    header = ["City", "DateTime", "Temp(F)", "Description"]
    city = data.get("city", {}).get("name", "")
    write_header = not os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        for item in data.get("list", []):
            dt_txt = item.get("dt_txt", "")
            temp = item.get("main", {}).get("temp", "")
            desc = item.get("weather", [{}])[0].get("description", "")
            writer.writerow([city, dt_txt, temp, desc])

# --- UI update function with CSV saving calls ---

def update_ui():
    city = city_entry.get().strip()
    if not city:
        status_label.config(text="Please enter a city name.")
        return

    status_label.config(text="Fetching weather...")
    root.update()

    current_data = fetch_current_weather(city)
    if not current_data:
        status_label.config(text="City not found or API error.")
        clear_main_card()
        clear_forecast()
        clear_plot()
        return

    # Save current weather to CSV
    save_current_weather_to_csv(current_data)

    city_label.config(text=current_data["name"])
    temp = round(current_data["main"]["temp"])
    desc = current_data["weather"][0]["description"].title()
    temp_label.config(text=f"{temp}°F, {desc}")

    icon_code = current_data["weather"][0]["icon"]
    icon_image = get_icon_image(icon_code)
    if icon_image:
        icon_label.config(image=icon_image)
        icon_label.image = icon_image
    else:
        icon_label.config(image='')
        icon_label.image = None

    detail_labels["Humidity"].config(text=f"{current_data['main']['humidity']}%")
    detail_labels["Wind"].config(text=f"{current_data['wind']['speed']} mph")
    detail_labels["Cloudiness"].config(text=f"{current_data['clouds']['all']}%")
    detail_labels["Visibility"].config(text=f"{current_data.get('visibility', 0)/1000:.1f} km")

    lat = current_data["coord"]["lat"]
    lon = current_data["coord"]["lon"]
    map_widget.set_position(lat, lon)
    map_widget.set_marker(lat, lon, text=current_data["name"])
    map_widget.set_zoom(8)

    forecast_data = fetch_forecast(city)
    if not forecast_data or "list" not in forecast_data:
        status_label.config(text="Failed to fetch forecast.")
        clear_forecast()
        clear_plot()
        return

    # Save forecast data to CSV
    save_forecast_to_csv(forecast_data)

    show_forecast(forecast_data)
    status_label.config(text="Weather updated successfully.")

def clear_main_card():
    city_label.config(text="--")
    temp_label.config(text="--")
    icon_label.config(image='')
    icon_label.image = None
    for key in detail_labels:
        detail_labels[key].config(text="--")

def clear_forecast():
    global forecast_icon_refs
    forecast_icon_refs.clear()
    for widget in forecast_frame.winfo_children():
        widget.destroy()

def clear_plot():
    ax.clear()
    canvas.draw()

def get_icon_image(icon_code):
    try:
        url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            return ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error loading icon:", e)
    return None

def show_forecast(forecast_data):
    clear_forecast()

    days = {}
    for item in forecast_data["list"]:
        day = item["dt_txt"].split()[0]
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"].title()
        icon = item["weather"][0]["icon"]

        if day not in days:
            days[day] = {"temps": [], "descs": [], "icons": []}
        days[day]["temps"].append(temp)
        days[day]["descs"].append(desc)
        days[day]["icons"].append(icon)

    for idx, (day, data) in enumerate(sorted(days.items())[:5]):
        dt = datetime.strptime(day, "%Y-%m-%d")
        day_name = dt.strftime("%a, %b %d")
        temp_max = round(max(data["temps"]))
        temp_min = round(min(data["temps"]))
        desc = max(set(data["descs"]), key=data["descs"].count)
        icon_code = max(set(data["icons"]), key=data["icons"].count)

        day_frame = ttk.Frame(forecast_frame, padding=8, relief="ridge")
        day_frame.pack(side="left", padx=6, pady=6, expand=True, fill="y")

        icon_img = get_icon_image(icon_code)
        if icon_img:
            icon_label_f = ttk.Label(day_frame, image=icon_img)
            icon_label_f.image = icon_img
            icon_label_f.pack()
            forecast_icon_refs[f"{day}_{idx}"] = icon_img

        ttk.Label(day_frame, text=day_name, font=("Segoe UI", 11, "bold")).pack(pady=(4,2))
        ttk.Label(day_frame, text=f"High: {temp_max}°F").pack()
        ttk.Label(day_frame, text=f"Low: {temp_min}°F").pack()
        ttk.Label(day_frame, text=desc).pack(pady=(4,0))

    days_list = []
    highs = []
    lows = []

    for day, data in sorted(days.items())[:5]:
        dt = datetime.strptime(day, "%Y-%m-%d")
        days_list.append(dt.strftime("%a"))
        highs.append(round(max(data["temps"])))
        lows.append(round(min(data["temps"])))

    ax.clear()
    ax.plot(days_list, highs, label="High", marker='o', color='orange')
    ax.plot(days_list, lows, label="Low", marker='o', color='skyblue')

    ax.set_title("5-Day Temperature Forecast")
    ax.set_ylabel("Temperature (°F)")
    ax.set_xlabel("Day")
    ax.legend()
    ax.grid(True, color='gray', linestyle='--', alpha=0.5)

    ax.set_facecolor('#2E2E2E')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    canvas.draw()

# --- Tkinter Setup ---

root = tk.Tk()
root.title("Weather + Map + Forecast")
root.geometry("820x820")
root.configure(bg="#2E2E2E")

style = ttk.Style(root)
style.theme_use("default")
style.configure("TFrame", background="#2E2E2E")
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

top_frame = ttk.Frame(root)
top_frame.pack(pady=10)

city_entry = ttk.Entry(top_frame, width=30, font=("Segoe UI", 12))
city_entry.pack(side="left", padx=5)
city_entry.insert(0, "Selmer")

search_button = ttk.Button(top_frame, text="Search", command=update_ui)
search_button.pack(side="left", padx=5)

status_label = ttk.Label(root, text="", font=("Segoe UI", 10, "italic"), foreground="white")
status_label.pack(pady=(0,10))

main_card = tk.Frame(root, bg="#3A3A3A", bd=2, relief="ridge", padx=20, pady=15)
main_card.pack(pady=10, fill="x", padx=20)

left_frame = tk.Frame(main_card, bg="#3A3A3A")
left_frame.grid(row=0, column=0, sticky="w")

city_label = tk.Label(left_frame, text="City Name", font=("Segoe UI", 20, "bold"), fg="white", bg="#3A3A3A")
city_label.pack(anchor="w")

temp_label = tk.Label(left_frame, text="Temperature + Condition", font=("Segoe UI", 16), fg="white", bg="#3A3A3A")
temp_label.pack(anchor="w", pady=(4,0))

icon_label = tk.Label(left_frame, bg="#3A3A3A")
icon_label.pack(anchor="w", pady=(4,0))

right_frame = tk.Frame(main_card, bg="#3A3A3A")
right_frame.grid(row=0, column=1, sticky="ne", padx=(40,0))

detail_labels = {}
for key in ["Humidity", "Wind", "Cloudiness", "Visibility"]:
    card = tk.Frame(right_frame, bg="#2E2E2E", padx=10, pady=6)
    card.pack(pady=4, fill="x")

    icon_lbl = tk.Label(card, text=get_detail_icon(key), font=("Segoe UI", 14), fg="white", bg="#2E2E2E")
    icon_lbl.pack(side="left")

    lbl_key = tk.Label(card, text=f" {key}:", font=("Segoe UI", 12, "bold"), fg="white", bg="#2E2E2E")
    lbl_key.pack(side="left")

    val = tk.Label(card, text="--", font=("Segoe UI", 14), fg="white", bg="#2E2E2E")
    val.pack(side="left", padx=(5,0))
    detail_labels[key] = val

map_outer_frame = tk.Frame(root, bg="#444", bd=2, relief="sunken")
map_outer_frame.pack(pady=15)

map_widget = TkinterMapView(map_outer_frame, width=780, height=180, corner_radius=5)
map_widget.pack()

forecast_frame = ttk.Frame(root)
forecast_frame.pack(pady=10, fill="x")

fig = Figure(figsize=(8, 2.5), dpi=100)
ax = fig.add_subplot(111)
ax.set_facecolor('#2E2E2E')
ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')
ax.title.set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=(10, 20), fill="x")

update_ui()

root.mainloop()


