# ML Hello World

A simple, end-to-end Machine Learning project demonstrating the complete lifecycle of an ML application: training, visualization, prediction, and deployment via a REST API.

## Project Overview

This project uses the classic **Iris dataset** to classify flowers into three species: *setosa*, *versicolor*, and *virginica*. It demonstrates how to:
1.  **Train** a K-Nearest Neighbors (KNN) model using `scikit-learn`.
2.  **Visualize** the data using `matplotlib`.
3.  **Predict** new samples using the trained model.
4.  **Serve** the model via a `FastAPI` web server.
5.  **Containerize** the application using `Docker`.

## Features

-   **`train_model.py`**: Loads data, trains a KNN model, evaluates accuracy, and saves the model artifact (`iris_model.pkl`).
-   **`visualize.py`**: Generates a scatter plot (`iris_plot.png`) of the dataset features.
-   **`predict.py`**: Loads the saved model and runs a prediction on sample input.
-   **`main.py`**: A FastAPI application that serves the model as a REST endpoint.
-   **`Dockerfile`**: Defines the container environment for the API.

## Prerequisites

-   **Python 3.11+**
-   **Docker** (Optional, for containerization)

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    -   **Windows**:
        ```powershell
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Train the Model
This script trains the model and saves it as `iris_model.pkl`.
```bash
python train_model.py
```
*Output: Prints model accuracy and saves the artifact.*

### 2. Visualize Data
Generates a plot of Petal Length vs. Petal Width.
```bash
python visualize.py
```
*Output: Saves `iris_plot.png`.*

### 3. Run a Prediction
Tests the saved model with a sample input.
```bash
python predict.py
```
*Output: Prints the predicted species.*

### 4. Start the API Server
Runs the FastAPI server locally.
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

-   **Health Check**: `GET http://127.0.0.1:8000/health`
-   **Predict Endpoint**: `POST http://127.0.0.1:8000/predict`
    -   **Body**:
        ```json
        {
          "sepal_length": 5.1,
          "sepal_width": 3.5,
          "petal_length": 1.4,
          "petal_width": 0.2
        }
        ```

## Docker Instructions

### Build the Image
```bash
docker build -t ml-hello-world .
```

### Run the Container
```bash
docker run -p 8000:8000 ml-hello-world
```
The API is now accessible at `http://localhost:8000`.
