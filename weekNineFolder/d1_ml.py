
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier

# # Load data
# data = load_iris()
# X = data.data
# y = data.target

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Choose and train model
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# # Evaluate
# score = model.score(X_test, y_test)
# print("Accuracy:", score)


# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import make_regression

# # Create sample data
# X, y = make_regression(n_samples=100, n_features=1, noise=10)

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Build and train the model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Make predictions
# predictions = model.predict(X_test)

# # Show result
# print(predictions[:5])
