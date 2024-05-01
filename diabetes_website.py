import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time
from requests.exceptions import RequestException

st.set_page_config(page_title="How long will I spend in a hospital?", page_icon="face_with_thermometer")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/5198932a-6296-4061-943b-9ac6f685f851/uPvSCY3RLQ.json")

with st.container():
    st.subheader("Business Analytics Capstone Project 2024")
    st.title("A Diabetic Readmission Analysis")
    st.write("This website is meant to help  diabetic patients predict their Length of Stay in a hospital encounter")
    st.write("[Learn More on how we generated this machine >](https://diabetesreadmissionLOH.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What this does")
        st.write("##")
        st.write(
            """
            Using our coefficients, we have been able to determine the Patient's Length of Stay. All they need to do is:
            Select your age, &
            Select any additional information during the hospital encounter

            And Voila! We predict the number of days you will spend in the hospital
            """
        )
        st.write("My chances of Early Readmission >](https://hospitalreadmission/c/WePredictForYou")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Import necessary libraries
import numpy as np
import streamlit as st

# Define the coefficients from your linear regression results
coefficients = {
    # Define the test model coefficients

    "Intercept": -0.1165811,
    "genderFemale": 0.0722780,
    "raceAfricanAmerican": 0.3595985,
    "raceAsian": 0.0385531,
    "raceHispanic": 0.1266658,
    "raceOther": 0.0705608,
    "agenumeric": 0.0182218,
    "admission_type_idUrgent": 0.2779292,
    "admission_type_idElective": -0.2175178,
    "admission_type_idNewborn": 0.3541172,
    "admission_type_idTrauma Center": 0.5142868,
    "A1Cresult>8": -0.0174505,
    "A1CresultNorm": -0.0109581,
    "A1CresultNot Tested": -0.0840652,
    "max_glu_serum>300": -0.2766725,
    "max_glu_serumNorm": -0.4803551,
    "max_glu_serumNot Tested": -1.1997983,
    "diabetesMedYes": -0.1019981,
    "PrimaryDiagnosesCirculatory": -0.0017551,
    "PrimaryDiagnosesCongenital Anomalies": 0.4585131,
    "PrimaryDiagnosesDiabetes": 0.2800787,
    "PrimaryDiagnosesDigestive": 0.2182519,
    "PrimaryDiagnosesEndocrine": 0.0382062,
    "PrimaryDiagnosesExternal": 2.9232316,
    "PrimaryDiagnosesGenitourinary": 0.1328503,
    "PrimaryDiagnosesIll Defined Conditions": 0.0355325,
    "PrimaryDiagnosesInfectious Disease": 0.4924979,
    "PrimaryDiagnosesInjury": 0.2267050,
    "PrimaryDiagnosesMental Disorders": 2.1574311,
    "PrimaryDiagnosesMusculoskeletal": -0.0754015,
    "PrimaryDiagnosesNeoplasms": 0.7439182,
    "PrimaryDiagnosesNervous System": 0.7847566,
    "PrimaryDiagnosesOther": -0.0904839,
    "PrimaryDiagnosesPregnancy/Childbirth Complications": 0.6636691,
    "PrimaryDiagnosesRespiratory": 0.0008939,
    "PrimaryDiagnosesSense Organ": -0.2231363,
    "PrimaryDiagnosesSkin Disease": 0.6750721,
    "SecondaryDiagnosesCirculatory": -0.0033022,
    "SecondaryDiagnosesCongenital Anomalies": -0.2996125,
    "SecondaryDiagnosesDiabetes": 0.0413385,
    "SecondaryDiagnosesDigestive": 0.3057481,
    "SecondaryDiagnosesEndocrine": 0.1881888,
    "SecondaryDiagnosesExternal": -0.1413270,
    "SecondaryDiagnosesGenitourinary": 0.0658257,
    "SecondaryDiagnosesIll Defined Conditions": 0.2172200,
    "SecondaryDiagnosesInfectious Disease": 0.5457403,
    "SecondaryDiagnosesInjury": 0.2948847,
    "SecondaryDiagnosesMental Disorders": 0.2060830,
    "SecondaryDiagnosesMusculoskeletal": 0.2102344,
    "SecondaryDiagnosesNeoplasms": 0.1207049,
    "SecondaryDiagnosesNervous System": 0.4357768,
    "SecondaryDiagnosesOther": 0.0365997,
    "SecondaryDiagnosesPregnancy/Childbirth Complications": 0.0421482,
    "SecondaryDiagnosesRespiratory": 0.2215365,
    "SecondaryDiagnosesSense Organ": 0.0331245,
    "SecondaryDiagnosesSkin Disease": 0.7528389,
    "ThirdDiagnosesCirculatory": -0.1893504,
    "ThirdDiagnosesCongenital Anomalies": -0.2675107,
    "ThirdDiagnosesDiabetes": -0.2025693,
    "ThirdDiagnosesDigestive": -0.0873241,
    "ThirdDiagnosesEndocrine": -0.0717677,
    "ThirdDiagnosesExternal": -0.3893981,
    "ThirdDiagnosesGenitourinary": 0.0369607,
    "ThirdDiagnosesIll Defined Conditions": 0.0612609,
    "ThirdDiagnosesInfectious Disease": 0.3430703,
    "ThirdDiagnosesInjury": 0.1225794,
    "ThirdDiagnosesMental Disorders": -0.1789362,
    "ThirdDiagnosesMusculoskeletal": 0.1524617,
    "ThirdDiagnosesNeoplasms": 0.1423942,
    "ThirdDiagnosesNervous System": 0.0126887,
    "ThirdDiagnosesOther": 0.1379407,
    "ThirdDiagnosesPregnancy/Childbirth Complications": -0.2674730,
    "ThirdDiagnosesRespiratory": 0.1086108,
    "ThirdDiagnosesSense Organ": 0.0215907,
    "ThirdDiagnosesSkin Disease": 0.6776750,
    "metforminSteady": -0.0971052,
    "metforminUp": 0.4047743,
    "metforminDown": 0.1182940,
    "repaglinideSteady": 0.2838814,
    "repaglinideUp": 1.0683652,
    "repaglinideDown": 1.9337989,
    "glimepirideSteady": -0.0616602,
    "glimepirideUp": 0.8730866,
    "glimepirideDown": 0.3362973,
    "glipizideSteady": -0.0995633,
    "glipizideUp": 0.7781544,
    "glipizideDown": 0.5266018,
    "glyburideSteady": 0.0138374,
    "glyburideUp": 0.7749670,
    "glyburideDown": 0.5046890,
    "tolbutamideSteady": -0.1638107,
    "pioglitazoneSteady": -0.1330535,
    "pioglitazoneUp": 1.3368613,
    "pioglitazoneDown": 0.0242772,
    "rosiglitazoneSteeady": -0.1575677,
    "rosiglitazoneUp": 0.8976580,
    "rosiglitazoneDown": 0.2025151,
    "acarboseSteady": -0.4573987,
    "acarboseUp": 1.1102345,
    "acarboseDown": -0.6413337,
    "insulinSteady": -0.0399199,
    "insulinUp": 0.2234517,
    "insulinDown": -0.0642068,
    "glyburidemetforminSteady": 0.1345505,
    "glyburidemetforminUp": -0.7747722,
    "glyburidemetforminDown": 3.4357264,
    "glipizidemetforminSteady": -0.3191890,
    "num_lab_procedures": 0.0283200,
    "num_procedures": 0.1368773,
    "num_medications": 0.1356525,
    "Hospital_Service": -0.0245299,
    "number_diagnoses": 0.0629639
}



# Define the function to calculate the predicted time_in_hospital
def calculate_time_in_hospital(features):
    time_in_hospital = coefficients['Intercept']
    for feature, coef in coefficients.items():
        if feature != 'Intercept' and feature in features:
            time_in_hospital += coef * features[feature]
    return time_in_hospital

# Streamlit app
st.title('Predicted Time in Hospital')


with st.sidebar:
    agenumeric = st.slider('Age', min_value=0, max_value=100, value=0)

    # Gender
    gender = st.selectbox('Gender', ['Male', 'Female', "NA"])
    gender_val = 1 if gender == 'Female' else 0

    # Race
    race = st.selectbox('Race', ['Caucasian', 'AfricanAmerican', 'Asian', 'Hispanic', 'Other', "NA"])
    race_val = [0, 0, 0, 0, 0]
    if race == 'AfricanAmerican':
        race_val[1] = 1
    elif race == 'Asian':
        race_val[2] = 1
    elif race == 'Hispanic':
        race_val[3] = 1
    elif race == 'Other':
        race_val[4] = 1
    else:
        race_val[0] = 1

    # Admission Type ID
    admission_type = st.selectbox('Admission Type ID', ['Emergency', 'Urgent', 'Elective', 'Newborn', 'TraumaCenter', "NA"])
    admission_type_val = [0, 0, 0, 0, 0]
    if admission_type == 'Urgent':
        admission_type_val[1] = 1
    elif admission_type == 'Elective':
        admission_type_val[2] = 1
    elif admission_type == 'Newborn':
        admission_type_val[3] = 1
    elif admission_type == 'TraumaCenter':
        admission_type_val[4] = 1
    else:
        admission_type_val[0] = 1

    # A1C Result
    a1c_result = st.selectbox('A1C Result', ['None', 'Norm', '>8', 'Not Tested'])
    a1c_result_val = [0, 0, 0, 0]
    if a1c_result == '>8':
        a1c_result_val[2] = 1
    elif a1c_result == 'Norm':
        a1c_result_val[1] = 1
    elif a1c_result == 'Not Tested':
        a1c_result_val[3] = 1
    else:
        a1c_result_val[0] = 1

    # Max Glu Serum
    max_glu_serum = st.selectbox('Max Glu Serum', ['None', '>300', 'Norm', 'Not Tested'])
    max_glu_serum_val = [0, 0, 0, 0]
    if max_glu_serum == '>300':
        max_glu_serum_val[1] = 1
    elif max_glu_serum == 'Norm':
        max_glu_serum_val[2] = 1
    elif max_glu_serum == 'Not Tested':
        max_glu_serum_val[3] = 1
    else:
        max_glu_serum_val[0] = 1

    # Diabetes Medication
    diabetes_med = st.selectbox('Diabetes Medication', ['No', 'Yes', "NA"])
    diabetes_med_val = 1 if diabetes_med == 'Yes' else 0

    # Primary Diagnosis
    primary_diagnoses = st.selectbox("Primary Diagnosis",
                                     ["None", "Circulatory", "Congenital Anomalies", "Diabetes", "Digestive",
                                      "Endocrine", "External", "Genitourinary", "Ill Defined Conditions",
                                      "Infectious Disease", "Injury", "Mental Disorders", "Musculoskeletal",
                                      "Neoplasms", "Nervous System", "Other", "Pregnancy/Childbirth Complications",
                                      "Respiratory", "Sense Organ", "Skin Disease"])
    secondary_diagnoses = st.selectbox("Secondary Diagnosis",
                                       ["None", "Circulatory", "Congenital Anomalies", "Diabetes", "Digestive",
                                        "Endocrine", "External", "Genitourinary", "Ill Defined Conditions",
                                        "Infectious Disease", "Injury", "Mental Disorders", "Musculoskeletal",
                                        "Neoplasms", "Nervous System", "Other", "Pregnancy/Childbirth Complications",
                                        "Respiratory", "Sense Organ", "Skin Disease"])
    third_diagnoses = st.selectbox("Third Diagnosis",
                                   ["None", "Circulatory", "Congenital Anomalies", "Diabetes", "Digestive", "Endocrine",
                                    "External", "Genitourinary", "Ill Defined Conditions", "Infectious Disease",
                                    "Injury", "Mental Disorders", "Musculoskeletal", "Neoplasms", "Nervous System",
                                    "Other", "Pregnancy/Childbirth Complications", "Respiratory", "Sense Organ",
                                    "Skin Disease"])

    # Medication
    st.subheader("Medication")

    metformin = st.radio("Metformin", ["Steady", "Up", "Down", "No", "NA"])
    glyburide = st.radio("Glyburide", ["Steady", "Up", "Down", "No", "NA"])
    glipizide = st.radio("Glipizide", ["Steady", "Up", "Down", "No", "NA"])
    insulin = st.radio("Insulin", ["Steady", "Up", "Down", "No", "NA"])
    glimepiride = st.radio("Glimepiride", ["Steady", "Up", "Down", "No", "NA"])
    repaglinide = st.radio("Repaglinide", ["Steady", "Up", "Down", "No", "NA"])
    tolbutamide = st.radio("Tolbutamide", ["Steady", "Up", "Down", "No", "NA"])
    pioglitazone = st.radio("Pioglitazone", ["Steady", "Up", "Down", "No", "NA"])
    rosiglitazone = st.radio("Rosiglitazone", ["Steady", "Up", "Down", "No", "NA"])
    acarbose = st.radio("Acarbose", ["Steady", "Up", "Down", "No", "NA"])
    glyburidemetformin = st.radio("Glyburide Metformin", ["Steady", "Up", "Down", "No", "NA"])
    glipizidemetformin = st.radio("Glipizide Metformin", ["Steady", "Up", "Down", "No", "NA"])



    # Number of Lab Procedures
    num_lab_procedures = st.slider('Number of Lab Procedures', min_value=0, max_value=100, value=0)



    # Number of Procedures
    num_procedures = st.slider('Number of Procedures', min_value=0, max_value=10, value=0)

    # Number of Medications
    num_medications = st.slider('Number of Medications', min_value=0, max_value=100, value=0)

    # Number of Diagnoses
    number_diagnoses = st.slider('Number of Diagnoses', min_value=0, max_value=20, value=0)

    hospital_service = st.slider('Number of Hospital Services', min_value=0, max_value=20, value=0)



st.write('## :⏳: Your Results Are In')


# Function to calculate the predicted time in hospital
# Animated progress bar to show the predicted time in hospital
progress_bar = st.progress(0)

# Define the function to calculate the predicted time_in_hospital
def calculate_time_in_hospital(features):
    time_in_hospital = coefficients['Intercept']
    for feature, coef in coefficients.items():
        if feature != 'Intercept' and feature in features:
            time_in_hospital += coef * features[feature]
    return time_in_hospital

# Animated progress bar to show the predicted time in hospital
progress_bar = st.progress(0)

# Function to calculate the predicted time in hospital
def calculate_and_show_time_in_hospital():
    # Calculate features here
    features = {
        'Intercept': 1,
        'genderFemale': gender_val,
        'raceAfricanAmerican': race_val[1],
        'raceAsian': race_val[2],
        'raceHispanic': race_val[3],
        'raceOther': race_val[4],
        'admission_type_idUrgent': admission_type_val[1],
        'admission_type_idElective': admission_type_val[2],
        'admission_type_idNewborn': admission_type_val[3],
        'admission_type_idTraumaCenter': admission_type_val[4],
        'A1Cresult>8': a1c_result_val[2],
        'A1CresultNorm': a1c_result_val[1],
        'A1CresultNotTested': a1c_result_val[3],
        'max_glu_serum>300': max_glu_serum_val[1],
        'max_glu_serumNorm': max_glu_serum_val[2],
        'max_glu_serumNotTested': max_glu_serum_val[3],
        'diabetesMedYes': diabetes_med_val,
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
        'metforminSteady': 1 if metformin == "Steady" else 0,
        'metforminUp':  1 if metformin == "Up" else 0,
        'metforminDown': 1 if metformin == "Down" else 0,
        'repaglinideSteady': 1 if repaglinide == "Steady" else 0,
        'repaglinideUp': 1 if repaglinide == "Up" else 0,
        'repaglinideDown': 1 if repaglinide == "Down" else 0,
        'glimepirideSteady': 1 if glimepiride == "Steady" else 0,
        'glimepirideUp': 1 if glimepiride == "Up" else 0,
        'glimepirideDown': 1 if glimepiride == "Down" else 0,
        'glipizideSteady': 1 if glipizide == "Steady" else 0,
        'glipizideUp': 1 if glipizide == "Up" else 0,
        'glipizideDown': 1 if glipizide == "Down" else 0,
        'glyburideSteady': 1 if glyburide == "Steady" else 0,
        'glyburideUp': 1 if glyburide == "Up" else 0,
        'glyburideDown': 1 if glyburide == "Down" else 0,
        'tolbutamideSteady': 1 if tolbutamide == "Steady" else 0,
        'pioglitazoneSteady': 1 if pioglitazone == "Steady" else 0,
        'pioglitazoneUp': 1 if pioglitazone == "Up" else 0,
        'pioglitazoneDown': 1 if pioglitazone == "Down" else 0,
        'rosiglitazoneSteady': 1 if rosiglitazone == "Steady" else 0,
        'rosiglitazoneUp': 1 if rosiglitazone == "Up" else 0,
        'rosiglitazoneDown': 1 if rosiglitazone == "Down" else 0,
        'acarboseSteady': 1 if acarbose == "Steady" else 0,
        'acarboseUp': 1 if acarbose == "Up" else 0,
        'acarboseDown': 1 if acarbose == "Down" else 0,
        'insulinSteady': 1 if insulin == "Steady" else 0,
        'insulinUp': 1 if insulin == "Up" else 0,
        'insulinDown': 1 if insulin == "Down" else 0,
        'glyburidemetforminSteady': 1 if glyburidemetformin == "Steady" else 0,
        'glyburidemetforminUp': 1 if glyburidemetformin == "Up" else 0,
        'glyburidemetforminDown': 1 if glyburidemetformin == "Down" else 0,
        'glipizidemetforminSteady': 1 if glipizidemetformin == "Steady" else 0,
        'num_lab_procedures': num_lab_procedures,
        'num_procedures': num_procedures,
        'num_medications': num_medications,
        'Hospital_Service': hospital_service,
        'number_diagnoses': number_diagnoses,
        'agenumeric': agenumeric
    }



    # Perform prediction here
    predicted_time_in_hospital = calculate_time_in_hospital(features)

    # Show prediction result
    st.success(f'Predicted Time in Hospital: {predicted_time_in_hospital:.3f} days')

# Show progress bar
with st.spinner('Calculating...'):
    # Update progress bar while calculating
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)

    # Calculate and show the predicted time in hospital
    calculate_and_show_time_in_hospital()


