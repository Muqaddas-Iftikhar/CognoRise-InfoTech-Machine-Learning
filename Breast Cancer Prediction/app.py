import streamlit as st
import pickle

# Load the model and data
try:
    rfc = pickle.load(open('rfc.pkl', 'rb'))
    df = pickle.load(open('cancer.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")
    st.stop()

st.write("Columns in df:", df.columns)

# Define the required columns for input and prediction
required_columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',
                    'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
                    'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 
                    'fractal_dimension_se', 'radius_worst', 'texture_worst','perimeter_worst', 'area_worst', 'smoothness_worst',
                    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

# Display the first few rows of df1 for inspection
st.write("Data preview:", df.head())

# Ensure the necessary columns are present
for column in required_columns:
    if column not in df.columns:
        st.error(f"Column '{column}' is missing from the data.")
        st.stop()

st.title('Breast Cancer Diagnosis Predictor')

# User inputs based on the actual column names in df1
radius_mean = st.number_input('Radius Mean', min_value=float(df['radius_mean'].min()), max_value=float(df['radius_mean'].max()), value=float(df['radius_mean'].median()))
texture_mean = st.number_input('Texture Mean', min_value=float(df['texture_mean'].min()), max_value=float(df['texture_mean'].max()), value=float(df['texture_mean'].median()))
perimeter_mean = st.number_input('Perimeter Mean', min_value=float(df['perimeter_mean'].min()), max_value=float(df['perimeter_mean'].max()), value=float(df['perimeter_mean'].median()))
area_mean = st.number_input('Area Mean', min_value=float(df['area_mean'].min()), max_value=float(df['area_mean'].max()), value=float(df['area_mean'].median()))
smoothness_mean = st.number_input('Smoothness Mean', min_value=float(df['smoothness_mean'].min()), max_value=float(df['smoothness_mean'].max()), value=float(df['smoothness_mean'].median()))
compactness_mean = st.number_input('Compactness Mean', min_value=float(df['compactness_mean'].min()), max_value=float(df['compactness_mean'].max()), value=float(df['compactness_mean'].median()))
concavity_mean = st.number_input('Concavity Mean', min_value=float(df['concavity_mean'].min()), max_value=float(df['concavity_mean'].max()), value=float(df['concavity_mean'].median()))
concave_points_mean = st.number_input('Concave Points Mean', min_value=float(df['concave points_mean'].min()), max_value=float(df['concave points_mean'].max()), value=float(df['concave points_mean'].median()))
symmetry_mean = st.number_input('Symmetry Mean', min_value=float(df['symmetry_mean'].min()), max_value=float(df['symmetry_mean'].max()), value=float(df['symmetry_mean'].median()))
fractal_dimension_mean = st.number_input('Fractal Dimension Mean', min_value=float(df['fractal_dimension_mean'].min()), max_value=float(df['fractal_dimension_mean'].max()), value=float(df['fractal_dimension_mean'].median()))
radius_se = st.number_input('Radius SE', min_value=float(df['radius_se'].min()), max_value=float(df['radius_se'].max()), value=float(df['radius_se'].median()))
texture_se = st.number_input('Texture SE', min_value=float(df['texture_se'].min()), max_value=float(df['texture_se'].max()), value=float(df['texture_se'].median()))
perimeter_se = st.number_input('Perimeter SE', min_value=float(df['perimeter_se'].min()), max_value=float(df['perimeter_se'].max()), value=float(df['perimeter_se'].median()))
area_se = st.number_input('Area SE', min_value=float(df['area_se'].min()), max_value=float(df['area_se'].max()), value=float(df['area_se'].median()))
smoothness_se = st.number_input('Smoothness SE', min_value=float(df['smoothness_se'].min()), max_value=float(df['smoothness_se'].max()), value=float(df['smoothness_se'].median()))
compactness_se = st.number_input('Compactness SE', min_value=float(df['compactness_se'].min()), max_value=float(df['compactness_se'].max()), value=float(df['compactness_se'].median()))
concavity_se = st.number_input('Concavity SE', min_value=float(df['concavity_se'].min()), max_value=float(df['concavity_se'].max()), value=float(df['concavity_se'].median()))
concave_points_se = st.number_input('Concave Points SE', min_value=float(df['concave points_se'].min()), max_value=float(df['concave points_se'].max()), value=float(df['concave points_se'].median()))
symmetry_se = st.number_input('Symmetry SE', min_value=float(df['symmetry_se'].min()), max_value=float(df['symmetry_se'].max()), value=float(df['symmetry_se'].median()))
fractal_dimension_se = st.number_input('Fractal Dimension SE', min_value=float(df['fractal_dimension_se'].min()), max_value=float(df['fractal_dimension_se'].max()), value=float(df['fractal_dimension_se'].median()))
radius_worst = st.number_input('Radius Worst', min_value=float(df['radius_worst'].min()), max_value=float(df['radius_worst'].max()), value=float(df['radius_worst'].median()))
texture_worst = st.number_input('Texture Worst', min_value=float(df['texture_worst'].min()), max_value=float(df['texture_worst'].max()), value=float(df['texture_worst'].median()))
perimeter_worst = st.number_input('Perimeter Worst', min_value=float(df['perimeter_worst'].min()), max_value=float(df['perimeter_worst'].max()), value=float(df['perimeter_worst'].median()))
area_worst = st.number_input('Area Worst', min_value=float(df['area_worst'].min()), max_value=float(df['area_worst'].max()), value=float(df['area_worst'].median()))
smoothness_worst = st.number_input('Smoothness Worst', min_value=float(df['smoothness_worst'].min()), max_value=float(df['smoothness_worst'].max()), value=float(df['smoothness_worst'].median()))
compactness_worst = st.number_input('Compactness Worst', min_value=float(df['compactness_worst'].min()), max_value=float(df['compactness_worst'].max()), value=float(df['compactness_worst'].median()))
concavity_worst = st.number_input('Concavity Worst', min_value=float(df['concavity_worst'].min()), max_value=float(df['concavity_worst'].max()), value=float(df['concavity_worst'].median()))
concave_points_worst = st.number_input('Concave Points Worst', min_value=float(df['concave points_worst'].min()), max_value=float(df['concave points_worst'].max()), value=float(df['concave points_worst'].median()))
symmetry_worst = st.number_input('Symmetry Worst', min_value=float(df['symmetry_worst'].min()), max_value=float(df['symmetry_worst'].max()), value=float(df['symmetry_worst'].median()))
fractal_dimension_worst = st.number_input('Fractal Dimension Worst', min_value=float(df['fractal_dimension_worst'].min()), max_value=float(df['fractal_dimension_worst'].max()), value=float(df['fractal_dimension_worst'].median()))

# Prepare input for prediction
input_data = [[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
               concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
               perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,
               fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
               compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]]

if st.button('Predict'):
    prediction = rfc.predict(input_data)
    result = 'has breast cancer' if prediction[0] else 'does not have breast cancer'
    st.write(f'The predicted diagnosis is: The patient {result}')
