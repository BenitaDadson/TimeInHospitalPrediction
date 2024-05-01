import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
from requests.exceptions import RequestException

st.set_page_config(page_title="What are your chances of being readmitted?", page_icon="nauseated_face")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/0daaa1ba-5899-4daa-bad3-b423937c71a5/jrDZyqPokR.json")

with st.container():
    st.subheader("Business Analytics Capstone Project 2024")
    st.title("A Diabetic Readmission Analysis")
    st.write("This website is meant to help  diabetic patients predict their chances of Early Readmission")
    st.write("[Learn More on how we generated this machine >](https://diabetesreadmissioncapstone.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What this does")
        st.write("##")
        st.write(
            """
            Using our test dataset, we have been able to generate the chances of a patient being readmitted. All they need to do is:
            Select your age, &
            Select any additional information during the hospital encounter

            And Voila! We predict your chances of being readmitted within 30 days of discharge
            """
        )
        st.write("My chances of Early Readmission >](https://hospitalreadmission/c/WePredictForYou")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st

# Define the coefficients from your logistic regression results
coefficients = {
    # Define the test model coefficients

    'Intercept': 2.854e-01,
    'agenumeric': 3.896e-03,
    'admission_type_idEmergency': -1.366e-01,
    'admission_type_idUrgent': -1.700e-01,
    'admission_type_idElective': -2.382e-01,
    'admission_type_idTraumaCenter': -1.184e+01,
    'A1Cresult>8': -5.587e-02,
    'A1CresultNorm': -4.111e-02,
    'A1CresultNot Tested': 1.347e-01,
    'diabetesMedYes': 1.516e-01,
    'PrimaryDiagnosesCirculatory': 2.975e-02,
    'PrimaryDiagnosesCongenital Anomalies': 4.922e-02,
    'PrimaryDiagnosesDiabetes': -6.261e-02,
    'PrimaryDiagnosesDigestive': -1.996e-01,
    'PrimaryDiagnosesEndocrine': 9.541e-02,
    'PrimaryDiagnosesExternal': 2.295e-01,
    'PrimaryDiagnosesGenitourinary': -2.250e-01,
    'PrimaryDiagnosesIll Defined Conditions': -2.000e-01,
    'PrimaryDiagnosesInfectious Disease': -1.295e-01,
    'PrimaryDiagnosesInjury': -4.321e-02,
    'PrimaryDiagnosesMental Disorders': 8.367e-02,
    'PrimaryDiagnosesMusculoskeletal': -2.261e-01,
    'PrimaryDiagnosesNeoplasms': -1.270e-01,
    'PrimaryDiagnosesNervous System': -2.032e-01,
    'PrimaryDiagnosesOther': -1.445e-01,
    'PrimaryDiagnosesPregnancy/Childbirth Complications': -6.290e-01,
    'PrimaryDiagnosesRespiratory': -3.121e-01,
    'PrimaryDiagnosesSense Organ': -5.943e-01,
    'PrimaryDiagnosesSkin Disease': -3.693e-01,
    'SecondaryDiagnosesCirculatory': 1.733e-01,
    'SecondaryDiagnosesCongenital Anomalies': 3.597e-01,
    'SecondaryDiagnosesDiabetes': 2.570e-01,
    'SecondaryDiagnosesDigestive': 2.296e-01,
    'SecondaryDiagnosesEndocrine': 1.652e-01,
    'SecondaryDiagnosesExternal': 2.705e-01,
    'SecondaryDiagnosesGenitourinary': 1.837e-01,
    'SecondaryDiagnosesIll Defined Conditions': -2.908e-03,
    'SecondaryDiagnosesInfectious Disease': 2.491e-01,
    'SecondaryDiagnosesInjury': 1.252e-01,
    'SecondaryDiagnosesMental Disorders': 5.881e-02,
    'SecondaryDiagnosesMusculoskeletal': -6.196e-02,
    'SecondaryDiagnosesNeoplasms': 4.210e-01,
    'SecondaryDiagnosesNervous System': 2.641e-01,
    'SecondaryDiagnosesOther': 6.420e-01,
    'SecondaryDiagnosesPregnancy/Childbirth Complications': 1.265e-01,
    'SecondaryDiagnosesRespiratory': 9.969e-02,
    'SecondaryDiagnosesSense Organ': -4.602e-01,
    'SecondaryDiagnosesSkin Disease': 7.883e-02,
    'ThirdDiagnosesCirculatory': 4.645e-02,
    'ThirdDiagnosesCongenital Anomalies': -1.742e-01,
    'ThirdDiagnosesDiabetes': 1.149e-01,
    'ThirdDiagnosesDigestive': 1.373e-01,
    'ThirdDiagnosesEndocrine': 7.153e-02,
    'ThirdDiagnosesExternal': -2.895e-02,
    'ThirdDiagnosesGenitourinary': 1.127e-01,
    'ThirdDiagnosesIll Defined Conditions': 1.352e-01,
    'ThirdDiagnosesInfectious Disease': -1.586e-02,
    'ThirdDiagnosesInjury': 8.364e-02,
    'ThirdDiagnosesMental Disorders': 1.936e-01,
    'ThirdDiagnosesMusculoskeletal': 9.923e-02,
    'ThirdDiagnosesNeoplasms': 4.265e-01,
    'ThirdDiagnosesNervous System': 4.054e-01,
    'ThirdDiagnosesOther': 3.471e-01,
    'ThirdDiagnosesPregnancy/Childbirth Complications': -1.241e+00,
    'ThirdDiagnosesRespiratory': 1.702e-01,
    'ThirdDiagnosesSense Organ': -8.173e-02,
    'ThirdDiagnosesSkin Disease': 1.114e-01,
    'time_in_hospital': 5.103e-02,
    'Discharge_StatusDischarged to home': -1.483e+00,
    'Discharge_StatusDischarged/transferred': -1.018e+00,
    'Discharge_StatusHospice / home': -2.779e+00,
    'Discharge_StatusHospice / medical facility': -2.109e+00,
    'Discharge_StatusLeft AMA': -1.027e+00,
    'Discharge_StatusStill patient/Expected Return': 1.050e+01,
    'Hospital_Service': 1.535e-01,
    'number_diagnoses': 3.527e-02,
    'metforminSteady': -1.548e-01,
    'metforminUp': -3.688e-01,
    'metforminDown': 6.611e-02,
    'glyburideSteady': -6.373e-02,
    'glyburideUp': 7.837e-02,
    'glyburideDown': -1.762e-01,
    'glipizideSteady': -1.885e-02,
    'glipizideUp': 8.768e-02,
    'glipizideDown': 1.969
}



# Define the function to calculate the predicted probability
def calculate_probability(inputs):
    probability = coefficients['Intercept']
    for feature, value in inputs.items():
        if feature in coefficients:
            probability += coefficients[feature] * value
    return 1 / (1 + np.exp(-probability))

# Streamlit app
st.title('Readmission Probability Generator')

# Sidebar for user inputs
with st.sidebar:
    st.title('Please Enter your Information Here')
    agenumeric = st.number_input("Age", min_value=0, max_value=100, value=50)
    admission_type = st.radio("Admission Type", ["None", "Emergency", "Urgent", "Elective", "Trauma Center"])
    a1c_result = st.radio("A1C Result", ["NA", ">8", "Norm", "Not Tested"])
    diabetes_med = st.radio("Diabetes Medication", ["Yes", "No", "NA"])
    primary_diagnoses = st.selectbox("Primary Diagnosis", ["None","Circulatory", "Congenital Anomalies", "Diabetes", "Digestive", "Endocrine", "External", "Genitourinary", "Ill Defined Conditions", "Infectious Disease", "Injury", "Mental Disorders", "Musculoskeletal", "Neoplasms", "Nervous System", "Other", "Pregnancy/Childbirth Complications", "Respiratory", "Sense Organ", "Skin Disease"])
    secondary_diagnoses = st.selectbox("Secondary Diagnosis", ["None","Circulatory", "Congenital Anomalies", "Diabetes", "Digestive", "Endocrine", "External", "Genitourinary", "Ill Defined Conditions", "Infectious Disease", "Injury", "Mental Disorders", "Musculoskeletal", "Neoplasms", "Nervous System", "Other", "Pregnancy/Childbirth Complications", "Respiratory", "Sense Organ", "Skin Disease"])
    third_diagnoses = st.selectbox("Third Diagnosis", ["None","Circulatory", "Congenital Anomalies", "Diabetes", "Digestive", "Endocrine", "External", "Genitourinary", "Ill Defined Conditions", "Infectious Disease", "Injury", "Mental Disorders", "Musculoskeletal", "Neoplasms", "Nervous System", "Other", "Pregnancy/Childbirth Complications", "Respiratory", "Sense Organ", "Skin Disease"])
    time_in_hospital = st.slider("Time in Hospital", min_value=0, max_value=14, value=7)
    discharge_status = st.selectbox("Discharge Status", ["None", "Discharged to home", "Discharged/transferred", "Hospice / home", "Hospice / medical facility", "Left AMA", "Still patient/Expected Return"])
    hospital_service = st.sidebar.slider('Hospital Service', 0, 7, key='hospital_service_input')
    number_diagnoses = st.slider("Number of Diagnoses", min_value=0, max_value=15, value=5)
    metformin = st.radio("Metformin", ["Steady", "Up", "Down", "No", "NA"])
    glyburide = st.radio("Glyburide", ["Steady", "Up", "Down", "No", "NA"])
    glipizide = st.radio("Glipizide", ["Steady", "Up", "Down", "No", "NA"])
    insulin = st.radio("Insulin", ["Steady", "Up", "Down", "No", "NA"])
    glimepiride = st.radio("Glimepiride", ["Steady", "Up", "Down", "No", "NA"])

# Define the feature dictionary
inputs = {
    'agenumeric': agenumeric,
    'admission_type_idUrgent': 1 if admission_type == "Urgent" else 0,
    'admission_type_idElective': 1 if admission_type == "Elective" else 0,
    'admission_type_idEmergency': 1 if admission_type == "Emergency" else 0,
    'admission_type_idTraumaCenter': 1 if admission_type == "TraumaCenter" else 0,
    'A1Cresult>8': 1 if a1c_result == ">8" else 0,
    'A1CresultNorm': 1 if a1c_result == "Norm" else 0,
    'A1CresultNot Tested': 1 if a1c_result == "Not Tested" else 0,
    'diabetesMed1': 1 if diabetes_med == "Yes" else 0,
    'PrimaryDiagnosesCirculatory': 1 if primary_diagnoses == "Circulatory" else 0,
    'PrimaryDiagnosesCongenital Anomalies': 1 if primary_diagnoses == "Congenital Anomalies" else 0,
    'PrimaryDiagnosesDiabetes': 1 if primary_diagnoses == "Diabetes" else 0,
    'PrimaryDiagnosesDigestive': 1 if primary_diagnoses == "Digestive" else 0,
    'PrimaryDiagnosesEndocrine': 1 if primary_diagnoses == "Endocrine" else 0,
    'PrimaryDiagnosesExternal': 1 if primary_diagnoses == "External" else 0,
    'PrimaryDiagnosesGenitourinary': 1 if primary_diagnoses == "Genitourinary" else 0,
    'PrimaryDiagnosesIll Defined Conditions': 1 if primary_diagnoses == "Ill Defined Conditions" else 0,
    'PrimaryDiagnosesInfectious Disease': 1 if primary_diagnoses == "Infectious Disease" else 0,
    'PrimaryDiagnosesInjury': 1 if primary_diagnoses == "Injury" else 0,
    'PrimaryDiagnosesMental Disorders': 1 if primary_diagnoses == "Mental Disorders" else 0,
    'PrimaryDiagnosesMusculoskeletal': 1 if primary_diagnoses == "Musculoskeletal" else 0,
    'PrimaryDiagnosesNeoplasms': 1 if primary_diagnoses == "Neoplasms" else 0,
    'PrimaryDiagnosesNervous System': 1 if primary_diagnoses == "Nervous System" else 0,
    'PrimaryDiagnosesOther': 1 if primary_diagnoses == "Other" else 0,
    'PrimaryDiagnosesPregnancy/Childbirth Complications': 1 if primary_diagnoses == "Pregnancy/Childbirth Complications" else 0,
    'PrimaryDiagnosesRespiratory': 1 if primary_diagnoses == "Respiratory" else 0,
    'PrimaryDiagnosesSense Organ': 1 if primary_diagnoses == "Sense Organ" else 0,
    'PrimaryDiagnosesSkin Disease': 1 if primary_diagnoses == "Skin Disease" else 0,
    'SecondaryDiagnosesCirculatory': 1 if secondary_diagnoses == "Circulatory" else 0,
    'SecondaryDiagnosesCongenital Anomalies': 1 if secondary_diagnoses == "Congenital Anomalies" else 0,
    'SecondaryDiagnosesDiabetes': 1 if secondary_diagnoses == "Diabetes" else 0,
    'SecondaryDiagnosesDigestive': 1 if secondary_diagnoses == "Digestive" else 0,
    'SecondaryDiagnosesEndocrine': 1 if secondary_diagnoses == "Endocrine" else 0,
    'SecondaryDiagnosesExternal': 1 if secondary_diagnoses == "External" else 0,
    'SecondaryDiagnosesGenitourinary': 1 if secondary_diagnoses == "Genitourinary" else 0,
    'SecondaryDiagnosesIll Defined Conditions': 1 if secondary_diagnoses == "Ill Defined Conditions" else 0,
    'SecondaryDiagnosesInfectious Disease': 1 if secondary_diagnoses == "Infectious Disease" else 0,
    'SecondaryDiagnosesInjury': 1 if secondary_diagnoses == "Injury" else 0,
    'SecondaryDiagnosesMental Disorders': 1 if secondary_diagnoses == "Mental Disorders" else 0,
    'SecondaryDiagnosesMusculoskeletal': 1 if secondary_diagnoses == "Musculoskeletal" else 0,
    'SecondaryDiagnosesNeoplasms': 1 if secondary_diagnoses == "Neoplasms" else 0,
    'SecondaryDiagnosesNervous System': 1 if secondary_diagnoses == "Nervous System" else 0,
    'SecondaryDiagnosesOther': 1 if secondary_diagnoses == "Other" else 0,
    'SecondaryDiagnosesPregnancy/Childbirth Complications': 1 if secondary_diagnoses == "Pregnancy/Childbirth Complications" else 0,
    'SecondaryDiagnosesRespiratory': 1 if secondary_diagnoses == "Respiratory" else 0,
    'SecondaryDiagnosesSense Organ': 1 if secondary_diagnoses == "Sense Organ" else 0,
    'SecondaryDiagnosesSkin Disease': 1 if secondary_diagnoses == "Skin Disease" else 0,
    'ThirdDiagnosesCirculatory': 1 if third_diagnoses == "Circulatory" else 0,
    'ThirdDiagnosesCongenital Anomalies': 1 if third_diagnoses == "Congenital Anomalies" else 0,
    'ThirdDiagnosesDiabetes': 1 if third_diagnoses == "Diabetes" else 0,
    'ThirdDiagnosesDigestive': 1 if third_diagnoses == "Digestive" else 0,
    'ThirdDiagnosesEndocrine': 1 if third_diagnoses == "Endocrine" else 0,
    'ThirdDiagnosesExternal': 1 if third_diagnoses == "External" else 0,
    'ThirdDiagnosesGenitourinary': 1 if third_diagnoses == "Genitourinary" else 0,
    'ThirdDiagnosesIll Defined Conditions': 1 if third_diagnoses == "Ill Defined Conditions" else 0,
    'ThirdDiagnosesInfectious Disease': 1 if third_diagnoses == "Infectious Disease" else 0,
    'ThirdDiagnosesInjury': 1 if third_diagnoses == "Injury" else 0,
    'ThirdDiagnosesMental Disorders': 1 if third_diagnoses == "Mental Disorders" else 0,
    'ThirdDiagnosesMusculoskeletal': 1 if third_diagnoses == "Musculoskeletal" else 0,
    'ThirdDiagnosesNeoplasms': 1 if third_diagnoses == "Neoplasms" else 0,
    'ThirdDiagnosesNervous System': 1 if third_diagnoses == "Nervous System" else 0,
    'ThirdDiagnosesOther': 1 if third_diagnoses == "Other" else 0,
    'ThirdDiagnosesPregnancy/Childbirth Complications': 1 if third_diagnoses == "Pregnancy/Childbirth Complications" else 0,
    'ThirdDiagnosesRespiratory': 1 if third_diagnoses == "Respiratory" else 0,
    'ThirdDiagnosesSense Organ': 1 if third_diagnoses == "Sense Organ" else 0,
    'ThirdDiagnosesSkin Disease': 1 if third_diagnoses == "Skin Disease" else 0,
    'time_in_hospital': time_in_hospital,
    'Discharge_StatusDischarged to home': 1 if discharge_status == "Discharged to home" else 0,
    'Discharge_StatusDischarged/transferred': 1 if discharge_status == "Discharged/transferred" else 0,
    'Discharge_StatusHospice / home': 1 if discharge_status == "Hospice / home" else 0,
    'Discharge_StatusHospice / medical facility': 1 if discharge_status == "Hospice / medical facility" else 0,
    'Discharge_StatusLeft AMA': 1 if discharge_status == "Left AMA" else 0,
    'Hospital_Service': hospital_service,
    'number_diagnoses': number_diagnoses,
    'metformin1': 1 if metformin == "Steady" else 0,
    'metformin2': 1 if metformin == "Up" else 0,
    'metformin3': 1 if metformin == "Down" else 0,
    'glyburide1': 1 if glyburide == "Steady" else 0,
    'glyburide2': 1 if glyburide == "Up" else 0,
    'glyburide3': 1 if glyburide == "Down" else 0,
    'glipizide1': 1 if glipizide == "Steady" else 0,
    'glipizide2': 1 if glipizide == "Up" else 0,
    'glipizide3': 1 if glipizide == "Down" else 0,
    'insulin1': 1 if insulin == "Steady" else 0,
    'insulin2': 1 if insulin == "Up" else 0,
    'insulin3': 1 if insulin == "Down" else 0,
    'glimepiride1': 1 if glimepiride == "Steady" else 0,
    'glimepiride2': 1 if glimepiride == "Up" else 0,
    'glimepiride3': 1 if glimepiride == "Down" else 0

}

# Calculate predicted probability
probability = calculate_probability(inputs)

# Input cost of readmission
cost_of_readmission = st.number_input((("Enter the cost of readmission: $")))

# Calculate expected cost of readmission
expected_cost = probability * cost_of_readmission


#Display results

st.write('## :hospital: Your Results Are In')
st.write(f'Your Chances of Early Readmission: {probability:.2%}')
st.write(f'Your Expected Cost of Readmission: ${expected_cost:.2f}')


# Progress bar
progress_bar = st.progress(0)

# Animate the progress bar
progress_increment = 0.1
progress_value = 0

while progress_value <= probability:
    progress_bar.progress(progress_value)
    progress_value += progress_increment
    if progress_value > 100:
        break
    if progress_value > probability:
        progress_value = probability

    time.sleep(0.05)  # Adjust the sleep time to control the animation speed

# Display the predicted probability
st.success(f"Predicted probability of readmission: {probability * 100:.2f}%")