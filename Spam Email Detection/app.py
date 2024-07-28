import streamlit as st
import pickle

# Load the model and data
try:
    lr = pickle.load(open('lr.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")
    st.stop()

st.write("Columns in df:", df.columns)

# Define the required columns for input and prediction
required_columns = ['Category', 'Message']

# Display the first few rows of df1 for inspection
st.write("Data preview:", df.head())

# Ensure the necessary columns are present
for column in required_columns:
    if column not in df.columns:
        st.error(f"Column '{column}' is missing from the data.")
        st.stop()

st.title('Email Spam Detector')

# User input for the message
message = st.text_area('Message')

# Preprocess the input message
# Here, you can add any preprocessing steps like tokenization, stemming, vectorization, etc.
# For simplicity, we assume the input data is directly fed into the model.

if st.button('Predict'):
    input_data = [message]  # Modify this if your model expects different input
    prediction = lr.predict(input_data)
    result = 'spam' if prediction[0] == 1 else 'ham'
    st.write(f'The predicted category is: The email is {result}')
