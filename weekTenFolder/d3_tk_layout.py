import tkinter as tk
import requests
from dotenv import load_dotenv
import os
import joblib
import numpy as np
import pandas as pd  


# Load environment variables (like API key)
load_dotenv()
api_key = os.getenv("API_KEY")

scroll_job_id = None

# Load your trained ML model
model = joblib.load("weather_model.joblib")

def scroll_text(label, text, delay=150):
    global scroll_job_id

    def scroll(i=0):
        if not label.winfo_exists():
            return
        display_text = text[i:] + "   " + text[:i]
        label.config(text=display_text)
        scroll_job_id = label.after(delay, scroll, (i + 1) % len(text))

    # Cancel previous scroll if one is running
    if scroll_job_id is not None:
        try:
            label.after_cancel(scroll_job_id)
        except:
            pass  # Ignore if it was already cancelled or invalid

    scroll()




def get_forecast():
    forecast_label.config(text="Loading...")
    scroll_label.config(text="")  # Clear previous scrolling text
    city = city_entry.get().strip()

    if not api_key:
        forecast_label.config(text="Error: API key not set.")
        return

    if not city:
        forecast_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            forecast_label.config(text=f"City not found or API error: {data.get('message', '')}")
            return

        # Get current weather values
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        description = data["weather"][0]["description"]

        # Prepare features for ML model
        features_df = pd.DataFrame([[temp, humidity, pressure]], columns=["temp", "humidity", "pressure"])
        predicted_temp = model.predict(features_df)[0]

        # Static forecast text (everything except predicted temp)
        static_text = (
            f"Weather in {city}:\n"
            f"Now: {temp}°F, {description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Pressure: {pressure} hPa\n"
        )
        forecast_label.config(text=static_text)

        # Scrolling predicted temp line
        predicted_text = f"Predicted Tomorrow: {predicted_temp:.1f}°F 🌡️"
        scroll_text(scroll_label, predicted_text)

    except Exception as e:
        forecast_label.config(text=f"Error fetching data: {e}")
        scroll_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Andrea’s Weather + Prediction App")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#121212")

main_frame = tk.Frame(root, padx=20, pady=20, bg="#121212")
main_frame.pack(fill="both", expand=True)

# City input
city_label = tk.Label(main_frame, text="Enter City:", font=('Arial', 14, 'bold'), fg="#FF6EC7", bg="#121212")
city_label.pack(pady=(0,5))

city_entry = tk.Entry(main_frame, font=('Consolas', 14, 'bold'), fg="#39FF14", bg="#121212",
                      insertbackground="#39FF14", highlightbackground="#39FF14",
                      highlightcolor="#39FF14", highlightthickness=2, bd=0, width=30, justify='center')
city_entry.pack(pady=(0,20))
city_entry.focus()
city_entry.bind('<Return>', lambda event: get_forecast())


# Forecast button
forecast_btn = tk.Button(main_frame, text="Get My Forecast", command=get_forecast,
                         font=('Arial', 14, 'bold'), fg="#FFFF33", bg="#121212",
                         activebackground="#FFFF33", activeforeground="#121212",
                         bd=0, highlightthickness=0)
forecast_btn.pack(pady=(0,30))

# Forecast output (static text)
forecast_label = tk.Label(main_frame, text="Forecast will appear here", wraplength=350,
                          font=("Consolas", 12, 'bold'), fg="#00FFFF", bg="#121212", justify="left")
forecast_label.pack()

# Scrolling predicted temp label
scroll_label = tk.Label(main_frame, text="", font=("Consolas", 12, 'bold'),
                        fg="#00FFFF", bg="#121212", justify="left", wraplength=350)
scroll_label.pack()


# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# def show_accuracy_pie():
#     # Example mock data - just to demo
#     accurate = 70
#     inaccurate = 30
#     labels = ['Accurate Predictions', 'Inaccurate Predictions']
#     sizes = [accurate, inaccurate]
#     colors = ["#84F458", "#E26EEA"] 

#     fig, ax = plt.subplots(figsize=(4, 4), facecolor='#121212')
#     wedges, texts, autotexts = ax.pie(
#         sizes, labels=labels, colors=colors, autopct='%1.1f%%',
#         startangle=90, textprops={'color':"white"}
#     )
#     ax.axis('equal')  # Equal aspect ratio ensures pie is circular
#     ax.set_title('Model Accuracy (Mock Data)', color='white')

#     popup = tk.Toplevel(root)
#     popup.title("Model Accuracy")
#     popup.configure(bg="#121212")

#     canvas = FigureCanvasTkAgg(fig, master=popup)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

#     close_btn = tk.Button(popup, text="Close", command=popup.destroy,
#                           bg="#FF6EC7", fg="#121212", font=('Arial', 12, 'bold'), bd=0)
#     close_btn.pack(pady=10)

# accuracy_btn = tk.Button(main_frame, text="Show Accuracy Chart", command=show_accuracy_pie,
#                          font=('Arial', 12, 'bold'), fg="#FFFF33", bg="#121212",
#                          activebackground="#FFFF33", activeforeground="#121212",
#                          bd=0, highlightthickness=0)
# accuracy_btn.pack(pady=(0, 10))
# Start the GUI app
root.mainloop()




