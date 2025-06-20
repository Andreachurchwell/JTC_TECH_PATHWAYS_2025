"""So i wanted to use my same flower data and swap from logistic regression to k-neighbors-classifier, this model will make predictions based on closeness and not formulas"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Your original flower data
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

y = np.array([
    0, 0, 0,   # Rose
    1, 1, 1,   # Hydrangea
    2, 2, 2,   # Lily
    3, 3, 3    # Hibiscus
])

flower_names = ['Rose', 'Hydrangea', 'Lily', 'Hibiscus']
colors = ['red', 'blue', 'green', 'purple']

# Split data into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Create and train the KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions on the test set
predictions = knn.predict(X_test)

print("Predicted:", predictions)
print("Actual:   ", y_test)

for i in range(len(predictions)):
    print(f"Predicted: {flower_names[predictions[i]]} — Actual: {flower_names[y_test[i]]}")

# just like logReg it went 1 for 3 on the first run.
# Predicted: [0 0 0]
# Actual:    [3 0 3]
# Predicted: Rose — Actual: Hibiscus
# Predicted: Rose — Actual: Rose
# Predicted: Rose — Actual: Hibiscus

# the next 2 times was 3 for 3, then the 4th was 1 of 3, and the 5th was 3 for 3


from sklearn.metrics import accuracy_score
# Calculate accuracy for your KNN model
accuracy = accuracy_score(y_test, predictions)
print(f"KNN Accuracy: {accuracy * 100:.2f}%")


for k in [1, 3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"K={k} --> Accuracy: {acc * 100:.2f}%")

#     At k=1, your KNN got 100% accuracy on the test set — that means it’s basically looking at the closest single neighbor, which works perfectly here.

# At k=3, accuracy dropped to 33.33%, and even worse at k=5 and 7.

# Your test set is small (only 3 samples), so changing k affects predictions a lot.


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
#  Confusion matrix to see detailed results
# Suppose y_test and predictions are your test and predicted labels

labels = [0, 1, 2, 3]  # all flower classes by their numeric labels

cm = confusion_matrix(y_test, predictions, labels=labels)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=flower_names)

disp.plot(cmap='Blues')
plt.show()

# The model struggles distinguishing Hibiscus from Rose here — it misclassified Hibiscus as Rose twice.

# It correctly identified the Hydrangea flower once.

# Your model's accuracy changes a lot depending on K (number of neighbors considered):

# K=1 gave perfect accuracy (but with such small data, this could just be lucky).

# Higher Ks (3, 5, 7) lowered accuracy, meaning considering more neighbors confuses it more in this small dataset.








# Plotting the data using petal length and petal width (features 0 and 1)
x_index, y_index = 0, 1

# Plot training data
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
plt.title("Flower Prediction Scatter Plot with KNN")
plt.legend()
plt.grid(True)
plt.show()


# so after running these and seeing the visuals, what really stood out was they seem very similar even though they "think" differently.

# Logistic Regression tries to draw straight-ish lines (boundaries) to separate flowers based on the features it learned from the training data. It’s like fitting a formula.

# KNN just looks around for the closest neighbors and says “this test flower looks most like these training flowers.” No formula, just direct comparison.

# so my next step is actually plugging in what weve covered this week and what i can try to get a better grasp of. i ask chat what i should do.
# ✅ Build a Simple Linear Regression Example (Flower Price)
# Why?
# It connects your existing flower features to new ML concepts like regression, error, and trendlines.
# It teaches how regression predicts values, not labels.
# You'll get to compare: classification (type of flower) vs regression (price of flower).

# Here’s what we’ll do:
# Add a fake “price” to each flower based on features (like longer petals = more expensive)
# Train a LinearRegression model
# Plot the prediction line
# Show how well it did with MAE or R²

# so im jumping back to logReg file






