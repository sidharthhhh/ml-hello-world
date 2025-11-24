# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# 1. INITIALIZE APP
app = FastAPI()

# 2. LOAD ARTIFACT (Global State)
# We load this ONCE when the server starts, not per request.
# This prevents latency.
model = joblib.load('iris_model.pkl')
class_names = ['setosa', 'versicolor', 'virginica']

# 3. DEFINE DATA MODEL (Schema Validation)
# This acts like a TypeScript interface or a SQL Schema.
# If a user sends "sepal_length": "banana", the API will reject it automatically.
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 4. DEFINE ENDPOINT (The Route)
@app.post("/predict")
def predict(request: IrisRequest):
    # Convert incoming JSON to the format our model expects (List of Lists)
    input_data = [[
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width
    ]]

    # Make prediction
    prediction_index = model.predict(input_data)[0]
    prediction_name = class_names[prediction_index]

    # Return JSON response
    return {
        "class_id": int(prediction_index),
        "class_name": prediction_name
    }

# Health check route (Standard for Docker/Kubernetes probes)
@app.get("/health")
def health_check():
    return {"status": "ok"}