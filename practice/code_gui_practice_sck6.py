# import tkinter as tk
# from tkinter import ttk, messagebox
# import csv

# # Sample unique city list
# city_list = ["Selmer", "Atlanta", "Miami", "Dallas"]

# # Store weather data in a dictionary
# weather_data = {}

# # GUI setup
# root = tk.Tk()
# root.title("Weather Logger")

# # Dropdown for city selection
# city_var = tk.StringVar()
# dropdown = ttk.Combobox(root, textvariable=city_var, values=city_list)
# dropdown.pack(pady=5)

# # Entry for temperature
# temp_entry = tk.Entry(root)
# temp_entry.pack(pady=5)

# # Function to save data
# def save_weather():
#     city = city_var.get()
#     temp = temp_entry.get()
    
#     try:
#         temp = float(temp)
#         weather_data[city] = {"temperature": temp}
        
#         # Save to CSV
#         with open("weather_log.csv", "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow([city, temp])
        
#         messagebox.showinfo("Saved", f"{city} - {temp}° saved!")
#         temp_entry.delete(0, tk.END)
#         show_records()
#     except ValueError:
#         messagebox.showerror("Invalid input", "Please enter a valid number.")

# # Function to display all records in a grid
# def show_records():
#     for widget in output_frame.winfo_children():
#         widget.destroy()
    
#     tk.Label(output_frame, text="City").grid(row=0, column=0)
#     tk.Label(output_frame, text="Temperature").grid(row=0, column=1)
    
#     for i, (city, data) in enumerate(weather_data.items(), start=1):
#         tk.Label(output_frame, text=city).grid(row=i, column=0)
#         tk.Label(output_frame, text=f"{data['temperature']}°").grid(row=i, column=1)

# # Button to trigger save
# tk.Button(root, text="Save", command=save_weather).pack(pady=5)

# # Frame to show records
# output_frame = tk.Frame(root)
# output_frame.pack(pady=10)

# root.mainloop()


# # ❓Q12.
# # After fetching weather data for three cities,
# # save a plain-text report summarizing the results in a readable format.

# weather_data = {
#     'Selmer': {'Temp': 85, "Wind": 5},
#     'Atlanta': {'Temp': 82, "Wind": 2},
#     'Miami': {'Temp': 95, "Wind": 8}
# }
# print("Weather Report:")

# print('------------')
# for city, data in weather_data.items():
#     print(f"{city} - Temp: {data['Temp']}*F, Wind:{data['Wind']} mph")


# import csv

# with open('weather-data.csv', 'r') as f:
#     reader=csv.DictReader(f)
#     valid_rows = []

#     for row in reader:
#         city = row['city']
#         temp = row['temp']
#         try:
#             temp = float(temp)
#             valid_rows.append((city, temp))
#             print(f'{city} - Temp: {temp}')
#         except (ValueError, TypeError):
#             print(f'Skipping {city} invalid temp: {temp}')
# with open('cleaned_weather.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['city', 'temp'])
#     for city, temp in valid_rows:
#         writer.writerow([city, temp])



# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title('Skills check Practice')

# city_entry = tk.StringVar()
# tk.Entry(root, textvariable=city_entry).pack()

# temp_entry = tk.StringVar()
# tk.Entry(root, textvariable=temp_entry).pack()

# def onClick():
#     city = city_entry.get()
#     temp = temp_entry.get()
#     try:
#         temp = float(temp)
#         messagebox.showinfo('successful entry', f"{city} is {temp}")
#     except ValueError:
#         messagebox.showerror('invalid','Please enter a valid number')

# tk.Button(root, text='clickme', command=onClick).pack()

# root.mainloop()
















