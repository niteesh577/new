import streamlit as st
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# Load the heart disease prediction model
heart_dis_model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Streamlit UI
st.header("Disease Detection Page")

# Input fields
age = st.number_input('Age', min_value=1, max_value=100, step=1)
sex = st.radio('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type (cp)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure (trestbps)', min_value=80, max_value=200, step=1)
chol = st.number_input('Cholesterol (chol)', min_value=100, max_value=600, step=1)
fbs = st.radio('Fasting Blood Sugar (fbs)', ['<= 120 mg/dl', '> 120 mg/dl'])
restecg = st.selectbox('Resting Electrocardiographic Results (restecg)', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved (thalach)', min_value=60, max_value=220, step=1)
exang = st.radio('Exercise Induced Angina (exang)', ['No', 'Yes'])
oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest (oldpeak)', min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox('Slope of the ST Segment (slope)', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels (0-3) Colored by Fluoroscopy (ca)', [0, 1, 2, 3])
thal = st.selectbox('Thalassemia (thal)', [0, 1, 2, 3])

# Convert categorical variables to numeric values
sex_numeric = 1 if sex == 'Male' else 0
fbs_numeric = 1 if fbs == '> 120 mg/dl' else 0
exang_numeric = 1 if exang == 'Yes' else 0

# Visualization based on inputs
if st.button('Diagnosis Test Result'):
    # Display input values as a bar chart
    input_data = pd.DataFrame({
        'Input': ['Age', 'Sex', 'Chest Pain Type', 'Resting Blood Pressure', 'Cholesterol', 'Fasting Blood Sugar',
                  'Resting Electrocardiographic Results', 'Maximum Heart Rate', 'Exercise Induced Angina',
                  'ST Depression', 'Slope of the ST Segment', 'Number of Major Vessels', 'Thalassemia'],
        'Value': [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    })
    st.bar_chart(input_data.set_index('Input'))

    # Make predictions and display the result as a pie chart
    heart_prediction = heart_dis_model.predict_proba([[age, sex_numeric, cp, trestbps, chol, fbs_numeric, restecg, thalach,
                                                       exang_numeric, oldpeak, slope, ca, thal]])[0]

    result_df = pd.DataFrame({
        'Prediction': ['Heart Disease', 'No Heart Disease'],
        'Probability': [heart_prediction[1], heart_prediction[0]]
    })

    fig, ax = plt.subplots()
    ax.pie(result_df['Probability'], labels=result_df['Prediction'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Provide guidance and links based on the prediction
    if heart_prediction[1] > 0.5:  # If the probability of heart disease is higher
        st.info("It's recommended to consult a healthcare professional. Here are some resources for guidance:")
        st.markdown("[American Heart Association](https://www.heart.org/)")
        st.markdown("[Mayo Clinic - Heart Disease](https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118)")
    else:
        st.success("No heart disease detected. Maintain a healthy lifestyle!")

# You can add more sections with relevant information based on the user's input and the model's prediction.
