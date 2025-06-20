from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Fake data (X = input, y = output)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])  # Simple pattern: y = 2 * x

# Train a simple model
model = LinearRegression()
model.fit(X, y)

# Save it to a file
joblib.dump(model, "your_model.joblib")

print("Model saved as your_model.joblib")
