import streamlit as st
import pickle
import numpy as np

# Load the model
with open('diabetes_model.pkl', 'rb') as file:
    boosting = pickle.load(file)

# Title of the web app
st.title('Diabetes Prediction App')

# Input fields for the user
st.write('Enter the following details to predict diabetes:')
gender = st.number_input('gender', min_value=0, max_value=20, step=1)
age = st.number_input('age', min_value=0, max_value=120, step=1)
hypertension = st.number_input('hypertension', min_value=0, max_value=150, step=1)
heart_disease = st.number_input('heart_disease', min_value=0, max_value=100, step=1)
smoking_history = st.number_input('smoking_history', min_value=0, max_value=900, step=1)
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1)
HbA1c_level = st.number_input('HbA1c_level', min_value=0.0, max_value=3.0, step=0.01)
blood_glucose_level = st.number_input('blood_glucose_level', min_value=0, max_value=120, step=1)
diabetes = st.number_input('diabetes', min_value=0, max_value=120, step=1)

# Predict button
if st.button('Predict'):
    features = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes]])
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)

    # Display the prediction
    if prediction[0] == 1:
        st.write(f"The model predicts that you have diabetes with a probability of {prediction_proba[0][1]:.2f}")
    else:
        st.write(f"The model predicts that you do not have diabetes with a probability of {prediction_proba[0][0]:.2f}")
