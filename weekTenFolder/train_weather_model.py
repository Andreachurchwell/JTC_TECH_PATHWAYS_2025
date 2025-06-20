import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample data (temp, humidity, pressure, next_day_temp)
data = {
    "temp": [70, 75, 80, 85, 78, 82, 90, 68, 72],
    "humidity": [50, 55, 45, 60, 52, 48, 40, 65, 53],
    "pressure": [1012, 1010, 1015, 1008, 1011, 1013, 1014, 1009, 1010],
    "next_day_temp": [72, 77, 83, 86, 79, 83, 89, 70, 74]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["temp", "humidity", "pressure"]]
y = df["next_day_temp"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to file
joblib.dump(model, "weather_model.joblib")
print("Model trained and saved as weather_model.joblib")
