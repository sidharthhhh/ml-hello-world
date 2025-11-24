# predict.py
import joblib
import numpy as np

# 1. LOAD THE ARTIFACT
# Notice we are NOT importing pandas, NOT splitting data, and NOT training.
# We are just loading the frozen brain from the disk.
print("Loading model artifact...")
model = joblib.load('iris_model.pkl')

# 2. MOCK INPUT (Simulate an API request)
# Let's say a user sends this JSON:
# { "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2 }
user_input = [[5.1, 3.5, 1.4, 0.2]]

# 3. PREDICT
prediction_index = model.predict(user_input)[0]

# Map the index (0, 1, 2) back to human names (we have to know these hardcoded or save them too)
class_names = ['setosa', 'versicolor', 'virginica']
result = class_names[prediction_index]

print(f"The model predicts this is a: {result}")