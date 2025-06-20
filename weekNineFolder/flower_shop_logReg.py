"""code along for a pretend flower shop, i have 4 different flowers: Rose, Hydrangea, Lily, and Hibiscus. To create the data, i measured each flower by: Petal length, Petal width, and Stem thickness"""


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Features: [petal length, petal width, stem thickness]
X = np.array([
    [5.0, 2.0, 1.2],  # Rose
    [5.2, 2.1, 1.3],
    [4.9, 1.9, 1.1],
    
    [6.0, 5.5, 0.8],  # Hydrangea
    [6.1, 5.7, 0.9],
    [5.9, 5.6, 0.7],
    
    [3.0, 1.0, 0.5],  # Lily
    [3.1, 1.2, 0.6],
    [2.9, 0.9, 0.5],
    
    [7.0, 3.5, 1.5],  # Hibiscus
    [7.1, 3.4, 1.6],
    [6.9, 3.6, 1.4],
])

# Labels: 0 = Rose, 1 = Hydrangea, 2 = Lily, 3 = Hibiscus
y = np.array([
    0, 0, 0,   # Rose
    1, 1, 1,   # Hydrangea
    2, 2, 2,   # Lily
    3, 3, 3    # Hibiscus
])

# New: Prices for each flower (in dollars)
# These are just made-up values, slightly tied to petal/stem size
flower_prices = np.array([
    10.0, 10.5, 9.8,   # Rose
    12.0, 12.5, 11.8,  # Hydrangea
    7.0, 7.5, 6.8,     # Lily
    15.0, 15.2, 14.8   # Hibiscus
])

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Split features and price
X_train_price, X_test_price, y_train_price, y_test_price = train_test_split(X, flower_prices, test_size=0.25)

# Step 2: Build the regression model
reg_model = LinearRegression()
reg_model.fit(X_train_price, y_train_price)

# Step 3: Predict flower prices
price_predictions = reg_model.predict(X_test_price)

# Step 4: Print predictions vs actual
print("\n--- Linear Regression (Predicting Price) ---")
for pred, actual in zip(price_predictions, y_test_price):
    print(f"Predicted: ${pred:.2f} — Actual: ${actual:.2f}")

# Step 5: Evaluate model performance
mae = mean_absolute_error(y_test_price, price_predictions)
r2 = r2_score(y_test_price, price_predictions)
print(f"\nMean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# one prediction was dead-on 14.80 and the other 2 were very close. the mean_absolute_error was .37 so that means i was less that 40 cents off and my r2 was.94, which means 94% of the price variation is explained by my features


# So now the model has:
# 12 flowers with 3 measurements each
# Labels telling it what type each one is


#Step 2: Split and Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# model is now studying 9 of the flowers and will be tested on the remaining 3.

# Step 3: Predict
# so the first time i ran this, it was 1 for three, it correctly guessed hibiscus but thought 2 roses were lilies. 

predictions = model.predict(X_test)
print("Predicted:", predictions)
print("Actual:   ", y_test)
# Predicted: [2 3 2]
# Actual:    [0 3 0]
flower_names = ['Rose', 'Hydrangea', 'Lily', 'Hibiscus']

for i in range(len(predictions)):
    print(f"Predicted: {flower_names[predictions[i]]} — Actual: {flower_names[y_test[i]]}")

# First Run (1/3 correct)
# Maybe your model trained on weak examples for Roses, or tested on a Rose it had never seen anything like.

# Later Runs (3/3 correct)
# It got luckier:
# Better, more balanced training samples
# Easier test flowers that looked like ones it had studied



# so i keep testing it, and i notice, its skipping roses, its always just the other 3, so i ask why:

# 1. Small dataset = not enough to learn from
# You only gave it 3 examples of each flower.
# That’s like giving a student 3 math problems and expecting them to master the topic.
# Logistic Regression needs more data to find good patterns, especially when classes are close in feature values.

# 2. Feature overlap
# The Rose and Lily examples may have very close values in petal length/width or stem thickness.
# The model may be seeing something like:
# “Hey, this petal is kind of short and the stem is kinda thin... that feels like a Lily, not a Rose.”

# i also wanted to create a visual to plot two features since were covering features tonight. so i decided to do a scatter plot using 2 features, petal length, and petal width and i wanted to highlight test data points

import matplotlib.pyplot as plt

# Just for labeling
flower_names = ['Rose', 'Hydrangea', 'Lily', 'Hibiscus']
colors = ['red', 'blue', 'green', 'purple']

# Choose the two features to plot (e.g., petal length = 0, petal width = 1)
x_index = 0  # petal length
y_index = 1  # petal width

# Plot all training data
for label in np.unique(y_train):
    plt.scatter(
        X_train[y_train == label, x_index],
        X_train[y_train == label, y_index],
        label=f"{flower_names[label]} (train)",
        c=colors[label],
        edgecolor='k',
        alpha=0.7,
        marker='o'
    )

# Plot test data with predicted labels
for i in range(len(X_test)):
    plt.scatter(
        X_test[i, x_index],
        X_test[i, y_index],
        c=colors[predictions[i]],
        marker='X',
        edgecolor='black',
        s=100,
        label=f"{flower_names[predictions[i]]} (pred)" if f"{flower_names[predictions[i]]} (pred)" not in plt.gca().get_legend_handles_labels()[1] else None
    )

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Flower Prediction Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()



# Circles → training flowers (true label)
# X markers → test flowers (predicted label)
# Color = flower type
# how close test points are to similar training ones



# so my next question is how can i make this better?
# Option 1: Add more fake flowers
# Give it 5–10 examples per flower to learn better patterns. Want help making those?
# Option 2: Use clearer differences
# Make sure Roses and Lilies don’t have overlapping numbers — exaggerate the differences so the model gets a cleaner signal.
# Option 3: Try a different model
# Something like KNeighborsClassifier works better with small datasets sometimes. 


# visuals for actual vs predicted prices

import matplotlib.pyplot as plt

# Scatter plot: Actual vs Predicted Prices
# Each dot is one flower.
# Dots on the diagonal line = perfect predictions
# Dots near the line = close predictions
# Far from the line = model missed
plt.figure(figsize=(6, 6))
plt.scatter(y_test_price, price_predictions, color='teal', edgecolor='black', s=80)
plt.plot([min(y_test_price), max(y_test_price)],
         [min(y_test_price), max(y_test_price)],
         color='gray', linestyle='--')

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Linear Regression: Actual vs Predicted Prices")
plt.grid(True)
plt.tight_layout()
plt.show()


# now the next step i wanna see plot price vs stem thickness(single feature)
# See a trend line (how price rises/falls with stem thickness)
# Understand feature impact
# Connect real values to prediction patterns

# Plot: Stem Thickness vs. Price with Regression Line

# Use only stem thickness (index 2)
stem_thickness = X[:, 2].reshape(-1, 1)
prices = flower_prices

# Train regression on just stem thickness
simple_reg = LinearRegression()
simple_reg.fit(stem_thickness, prices)

# Predict line
x_line = np.linspace(min(stem_thickness), max(stem_thickness), 100).reshape(-1, 1)
y_line = simple_reg.predict(x_line)




# Dots = actual flower prices
# Blue line = what the model “learned”
# If the dots hug the line → this feature is a strong predictor
# Plot
plt.figure(figsize=(8, 5))
plt.scatter(stem_thickness, prices, color='darkorange', edgecolor='black', s=80, label='Actual')
plt.plot(x_line, y_line, color='blue', linewidth=2, label='Regression Line')
plt.xlabel("Stem Thickness")
plt.ylabel("Price ($)")
plt.title("Flower Price vs. Stem Thickness")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# at this point, i have done classifiers(logReg and KNN) to predict a flower type, a regressor(linearReg) to predict flower price, and made visuals for all. To now wrap it all together, i want to lock it in with side by side comparisons of all of my features impact on price(bar chart of coefficients)


# Show how much each feature affects price
feature_names = ["Petal Length", "Petal Width", "Stem Thickness"]
coefficients = reg_model.coef_



# Which feature mattered most for price prediction
# Which features had small or negative impact
# This is called interpreting model weights — essential in machine learning

plt.figure(figsize=(6, 4))
bars = plt.bar(feature_names, coefficients, color='seagreen', edgecolor='black')
plt.title("Feature Impact on Price (Linear Regression)")
plt.ylabel("Coefficient (Effect on Price)")
plt.grid(axis='y')

# Label bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f"{yval:.2f}", va='bottom', ha='center')

plt.tight_layout()
plt.show()

# What the chart shows:
# The x-axis lists your features: Petal Length, Petal Width, Stem Thickness.

# The y-axis shows the coefficient values your linear regression model learned for each feature.

# Each bar height tells you how much that feature affects the price prediction, holding the other features constant.

# What the coefficients mean:
# Positive coefficient: The feature increases the predicted price when its value goes up.

# Negative coefficient: The feature decreases the predicted price when its value goes up.

# Larger absolute value means stronger impact on price.

# Smaller or near-zero means the feature doesn't affect price much.

# How to interpret it practically:
# If the bar for Petal Length is around 2.5, it means:

# For each additional unit increase in petal length (like 1 cm longer petals), the model predicts the price to go up by roughly $2.50, assuming other features stay the same.

# If Stem Thickness has a coefficient close to zero or negative:

# Changes in stem thickness don’t really change the price much (or might slightly decrease it).

# Why is this useful?
# You can understand which features are most important for predicting price.

# Helps in interpreting your model — which is critical in real life where you want to explain why the model makes predictions.

# If a feature has a negative coefficient but you expect a positive impact, maybe you need more data or to check for feature correlation.

# Summary in your case:
# Your chart showed that Petal Length and Petal Width likely have a strong positive impact on price.

# Stem Thickness had some impact but less than petal size.

# So flowers with bigger petals tend to be pricier in your model.













