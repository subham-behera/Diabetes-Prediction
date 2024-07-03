import streamlit as st
import numpy as np
import joblib

# Load the model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Predict function
def predict_diabetes(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    prediction = model.predict(data)
    return 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'

# Streamlit app
st.title("Diabetes Prediction")

# Collect user input
pregnancies = st.number_input('Pregnancies', 0, 20, step=1)
glucose = st.number_input('Glucose', 0, 200)
blood_pressure = st.number_input('Blood Pressure', 0, 150)
skin_thickness = st.number_input('Skin Thickness', 0, 100)
insulin = st.number_input('Insulin', 0, 900)
bmi = st.number_input('BMI', 0.0, 70.0)
dpf = st.number_input('Diabetes Pedigree Function', 0.0, 3.0)
age = st.number_input('Age', 0, 120)

# Make prediction
if st.button("Predict"):
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    result = predict_diabetes(input_data)
    st.write(f"Prediction: {result}")
