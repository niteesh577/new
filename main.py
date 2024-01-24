import streamlit as st
import pickle
st.header("Disease Detection Page")
heart_dis_model = pickle.load(open('heart_disease_model.pkl', 'rb'))
age = None
try:
    age = float(st.text_input('Age'))
except ValueError:
    pass

sex = None
try:
     sex = float(st.text_input('Sex'))
except ValueError:
     pass

cp = None
try:
    cp = float(st.text_input('Chest Pain Type (cp)'))
except ValueError:
    pass

trestbps = None
try:
    trestbps = float(st.text_input('Resting Blood Pressure (trestbps)'))
except ValueError:
    pass

chol = None
try:
    chol = float(st.text_input('Cholesterol (chol)'))
except ValueError:
    pass

fbs = None
try:
    fbs = float(st.text_input('Fasting Blood Sugar (fbs)'))
except ValueError:
    pass

restecg = None
try:
    restecg = float(st.text_input('Resting Electrocardiographic Results (restecg)'))
except ValueError:
    pass

thalach = None
try:
    thalach = float(st.text_input('Maximum Heart Rate Achieved (thalach)'))
except ValueError:
    pass

exang = None
try:
    exang = float(st.text_input('Exercise Induced Angina (exang)'))
except ValueError:
    pass

oldpeak = None
try:
    oldpeak = float(st.text_input('ST Depression Induced by Exercise Relative to Rest (oldpeak)'))
except ValueError:
    pass

slope = None
try:
    slope = float(st.text_input('Slope of the ST Segment (slope)'))
except ValueError:
    pass

ca = None
try:
    ca = float(st.text_input('Number of Major Vessels (0-3) Colored by Fluoroscopy (ca)'))
except ValueError:
    pass
thal = None
try:
    thal = float(st.text_input('Thalassemia (thal)'))
except ValueError:
    pass

heart_diagnosis = ''
if st.button('Diagnosis Test Result'):
    if (
                    age is not None and sex is not None and cp is not None and trestbps is not None and chol is not None
                    and fbs is not None and restecg is not None and thalach is not None and exang is not None
                    and oldpeak is not None and slope is not None and ca is not None and thal is not None
            ):
                heart_prediction = heart_dis_model.predict(
                    [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
                )
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person has heart disease.'
                else:
                    heart_diagnosis = 'The person does not have heart disease.'
    else:
                heart_diagnosis = 'Please provide valid input for all fields.'
    st.success(heart_diagnosis)
