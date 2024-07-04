# Diabetes Prediction ML Model

This project is a Streamlit web application for predicting diabetes using a machine learning model.

## Project Overview

This project aims to predict diabetes using a machine learning model deployed on a Streamlit app. The model is trained on a dataset of patient information, including features like age, BMI, and other relevant medical measurements.

## Files in the Repository

- **`index.py`**: Main file to run the Streamlit app.
- **`model.pkl`**: Pre-trained machine learning model saved using joblib.
- **`requirements.txt`**: List of Python packages required to run the app.
- **`README.md`**: Project documentation.
- **`diabetes.csv`**: The dataset and any other necessary data files.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/subham-behera/diabetes-prediction.git
    cd diabetes-prediction
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the App

To run the Streamlit app, execute the following command in your terminal:
```bash
streamlit run app.py
