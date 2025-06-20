import tkinter as tk
from tkinter import ttk
import threading
import time
import joblib  # Make sure your model is saved as a .joblib file
import numpy as np

# Load model once when app starts (pretend it's slow)
model = joblib.load("your_model.joblib")  # replace with your actual model path

# Prediction function
def run_prediction(user_input, result_label, progress):
    def task():
        progress.start()
        time.sleep(1)  # simulate delay
        try:
            # Convert input and predict (adjust as needed for your model)
            data = np.array([[float(user_input.get())]])
            prediction = model.predict(data)
            result = f"Prediction: {prediction[0]}"
        except Exception as e:
            result = f"Error: {str(e)}"
        progress.stop()
        result_label.config(text=result)

    threading.Thread(target=task).start()

# GUI Setup
root = tk.Tk()
root.title("ML Predictor")

frame = ttk.Frame(root, padding=20)
frame.grid()

# Input field
ttk.Label(frame, text="Enter value:").grid(row=0, column=0)
user_input = ttk.Entry(frame)
user_input.grid(row=0, column=1)

# Predict button
result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

progress = ttk.Progressbar(frame, mode='indeterminate')
progress.grid(row=3, column=0, columnspan=2, pady=10)

predict_button = ttk.Button(
    frame, text="Predict",
    command=lambda: run_prediction(user_input, result_label, progress)
)
predict_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
