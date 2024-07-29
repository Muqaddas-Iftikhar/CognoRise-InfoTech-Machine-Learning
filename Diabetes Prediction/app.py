import streamlit as st
import pickle
from sklearn.ensemble import AdaBoostClassifier

try:
    boosting = pickle.load(open('boosting.pkl', 'rb'))
    df1 = pickle.load(open('diabetes.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")
    st.stop()

st.write("Columns in df1:", df1.columns)

required_columns = ['age', 'hypertension', 'heart_disease', 
                   'bmi', 'HbA1c_level', 'blood_glucose_level',
                   'gender_Female', 'gender_Male', 'gender_Other',
                   'smoking_history_No Info', 'smoking_history_current',
                   'smoking_history_ever', 'smoking_history_former',
                   'smoking_history_never', 'smoking_history_not current']

st.write("Data preview:", df1.head())

for column in required_columns:
    if column not in df1.columns:
        st.error(f"Column '{column}' is missing from the data.")
        st.stop()

st.title('Diabetes Predictor')

age = st.number_input('Age', min_value=int(df1['age'].min()), max_value=int(df1['age'].max()), value=int(df1['age'].median()))
hypertension = st.selectbox('Hypertension', df1['hypertension'].unique())
heart_disease = st.selectbox('Heart Disease', df1['heart_disease'].unique())
gender_Female = st.selectbox('Gender_Female', df1['gender_Female'].unique())
gender_Male = st.selectbox('Gender_Male', df1['gender_Male'].unique())
gender_Other = st.selectbox('Gender_Other', df1['gender_Other'].unique())
smoking_history_No_Info = st.selectbox('Smoking History_No Info', df1['smoking_history_No Info'].unique())
smoking_history_current = st.selectbox('Smoking History_current', df1['smoking_history_current'].unique())
smoking_history_ever = st.selectbox('Smoking History_ever', df1['smoking_history_ever'].unique())
smoking_history_former = st.selectbox('Smoking History_former', df1['smoking_history_former'].unique())
smoking_history_never = st.selectbox('Smoking History_never', df1['smoking_history_never'].unique())
smoking_history_not_current = st.selectbox('Smoking History_not_current', df1['smoking_history_not current'].unique())
bmi = st.number_input('BMI', min_value=float(df1['bmi'].min()), max_value=float(df1['bmi'].max()), value=float(df1['bmi'].median()))
hba1c_level = st.number_input('HbA1c Level', min_value=float(df1['HbA1c_level'].min()), max_value=float(df1['HbA1c_level'].max()), value=float(df1['HbA1c_level'].median()))
blood_glucose_level = st.number_input('Blood Glucose Level', min_value=int(df1['blood_glucose_level'].min()), max_value=int(df1['blood_glucose_level'].max()), value=int(df1['blood_glucose_level'].median()))

input_data = [[age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level,
               gender_Female, gender_Male, gender_Other,
               smoking_history_No_Info, smoking_history_current, smoking_history_ever,
               smoking_history_former, smoking_history_never, smoking_history_not_current]]

if st.button('Predict'):
    prediction = boosting.predict(input_data)
    result = 'has diabetes' if prediction[0] else 'does not have diabetes'
    st.write(f'The predicted diabetes status is: The patient {result}')