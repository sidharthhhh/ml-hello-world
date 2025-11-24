# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import joblib

# 1. LOAD DATA (The "Database")
# We load a pre-cleaned dataset.
# X = The "Features" (Sepal Length, Width, etc.) -> Inputs
# y = The "Target" (Species Name) -> Output we want to predict
iris = load_iris()
X = iris.data
y = iris.target

# 2. SPLIT DATA (Prod vs. Staging)
# We hide 20% of data (test_size=0.2) to simulate "production" data
# that the model has never seen before.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. INITIALIZE MODEL (The "Algorithm")
# K-Nearest Neighbors (KNN) is simple: "If it looks like a duck, it's a duck."
# It looks at the 3 closest data points to decide the class.
model = KNeighborsClassifier(n_neighbors=3)

# 4. TRAIN (The "Build" Process)
# This is where the math happens. The model learns the patterns in X_train.
print("Training model...")
model.fit(X_train, y_train)

# 5. EVALUATE (The "Unit Test")
# We ask the model to predict the "hidden" production data (X_test)
predictions = model.predict(X_test)

# Compare predictions vs. reality (y_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Extra: Test it with a fake flower we just made up
# [Sepal Length, Sepal Width, Petal Length, Petal Width]
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)
print(f"Prediction for new flower: {iris.target_names[prediction[0]]}")


# SAVE THE ARTIFACT
# We dump the memory state of 'model' into a binary file.
# This is equivalent to creating a .exe or Docker image layer.
model_filename = 'iris_model.pkl'
joblib.dump(model, model_filename)

print(f"Artifact saved to: {model_filename}")