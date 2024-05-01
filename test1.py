
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
from requests.exceptions import RequestException
st.set_page_config(page_title="What are your chances of being readmitted?", page_icon="nauseated_face")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
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
        st_lottie(lottie_coding, height = 300, key="coding")


# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st

# Load the DataFrame 'df' (assuming it contains user data)
# Replace 'your_dataframe.csv' with the path to your DataFrame file
df = pd.read_excel("/Users/benitadadson/Downloads/test_data.xlsx")

# Define the test model coefficients
test_log1_coefficients = {
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
    'glipizideDown': 1.969e-01,
    'insulinSteady': 4.615e-02,
    'insulinUp': 9.594e-02,
    'insulinDown': 2.357e-01,
    'glimepirideSteady': -6.089e-02,
    'glimepirideUp': 6.528e-01,
    'glimepirideDown': 3.271e-01,
    'agenumeric:time_in_hospital': -4.724e-04
}



# Define function to predict readmission probability
def predict_readmission_probability(inputs):
    # Calculate the linear combination of coefficients and input values
    log_odds = test_log1_coefficients['Intercept']
    for variable, coefficient in test_log1_coefficients.items():
        if variable != 'Intercept':
            log_odds += coefficient * inputs.get(variable, 0)  # Set to 0 if variable not provided

    # Convert log-odds to probability
    probability = 1 / (1 + np.exp(-log_odds))
    return probability

# Create Streamlit web application
def main():
    st.title('Readmission Likelihood Predictor')
    st.sidebar.title('Enter Your Information')

    # Collect user inputs
    agenumeric = st.sidebar.number_input('Age', key='agenumeric_input')
    admission_type_id = st.sidebar.radio('Admission Type ID', ['Emergency', 'Urgent', 'Elective', 'Newborn', 'Trauma Center'], key='admission_type_input')
    A1Cresult = st.sidebar.radio('A1Cresult', ['>8', 'Normal', 'Not Tested'], key='A1Cresult_input')
    diabetesMed = st.sidebar.radio('Diabetes Medication', ['No', 'Yes'], key='diabetesMed_input')
    primary_diagnosis = st.sidebar.selectbox('Primary Diagnosis', df['PrimaryDiagnoses'].unique(),
                                             key='primary_diagnosis_input')
    secondary_diagnosis = st.sidebar.selectbox('Secondary Diagnosis', df['SecondaryDiagnoses'].unique(),
                                               key='secondary_diagnosis_input')
    third_diagnosis = st.sidebar.selectbox('Third Diagnosis', df['ThirdDiagnoses'].unique(),
                                           key='third_diagnosis_input')
    time_in_hospital = st.sidebar.slider('Time in Hospital', 1, 14, key='time_in_hospital_input')
    discharge_status = st.sidebar.radio('Discharge Status', df['Discharge_Status'].unique(),
                                        key='discharge_status_input')
    hospital_service = st.sidebar.slider('Hospital Service', 0, 7,
                                        key='hospital_service_input')
    number_diagnoses = st.sidebar.slider('Number of Diagnoses', 1, 16, key='number_diagnoses_input')
    metformin = st.sidebar.radio('Metformin', ['No', 'Steady', 'Up', 'Down'], key='metformin_input')
    glyburide = st.sidebar.radio('Glyburide', ['No', 'Steady', 'Up', 'Down'], key='glyburide_input')
    glipizide = st.sidebar.radio('Glipizide', ['No', 'Steady', 'Up', 'Down'], key='glipizide_input')
    insulin = st.sidebar.radio('Insulin', ['No', 'Steady', 'Up', 'Down'], key='insulin_input')
    glimepiride = st.sidebar.radio('Glimepiride', ['No', 'Steady', 'Up', 'Down'], key='glimepiride_input')
    # Collect inputs for other variables

    inputs = {
    'agenumeric': agenumeric,
    'admission_type_id': admission_type_id,
    'A1Cresult': A1Cresult,
    'diabetesMed': diabetesMed,
    'primary_diagnosis': primary_diagnosis,
    'secondary_diagnosis': secondary_diagnosis,
    'third_diagnosis': third_diagnosis,
    'time_in_hospital': time_in_hospital,
    'discharge_status': discharge_status,
    'hospital_service': hospital_service,
    'number_diagnoses': number_diagnoses,
    'metformin': metformin,
    'glyburide': glyburide,
    'glipizide': glipizide,
    'insulin': insulin,
    'glimepiride': glimepiride
}

    # Calculate readmission probability
    probability = predict_readmission_probability(inputs)

    # Calculate the expected cost of readmission
    expected_cost = probability * 15200  # $15,200 is the average cost of readmission



    # Display results

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


# Run the app
if __name__ == "__main__":
    main()


