import pandas as pd
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import os
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import graphviz
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


import streamlit_shadcn_ui as ui

# Configure Streamlit page

st.set_page_config(
    page_title="Diabetes Dashboard for Test Data",
    page_icon=":hospital:",
    layout="wide"
)

# Title
st.title(" :hospital: Diabetes Descriptive Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Read data
df = pd.read_excel("/Users/benitadadson/Downloads/test_data.xlsx")

df["A1Cresult"].replace("None", "Not Measured", inplace=True)
df["max_glu_serum"].replace("None", "Not Measured", inplace=True)


# Split page into columns
col1, col2 = st.columns((2))

# Filter by Readmission
with col1:
    readmission_filter = st.checkbox("Filter by Readmission")
    if readmission_filter:
        selected_readmission = st.radio("Select Readmission Status", [0, 1])

# Apply filter
if readmission_filter:
    df = df[df["readmitted"] == selected_readmission].copy()

# Sidebar filters
st.sidebar.header("Please Filter Here")

age = st.sidebar.multiselect("Select the Age:", options=df["age"].unique(), default=df["age"].unique())
gender = st.sidebar.multiselect("Select the Gender:", options=df["gender"].unique(), default=df["gender"].unique())
race = st.sidebar.multiselect("Select the Race:", options=df["race"].unique(), default=df["race"].unique())
admission_type_id = st.sidebar.multiselect("Select the Admission Type:", options=df["admission_type_id"].unique(), default=df["admission_type_id"].unique())
A1Cresult = st.sidebar.multiselect("Select the HBA1C Results:", options=df["A1Cresult"].unique(), default=df["A1Cresult"].unique())
max_glu_serum = st.sidebar.multiselect("Select the Max Glucose Serum:", options=df["max_glu_serum"].unique(), default=df["max_glu_serum"].unique())
PrimaryDiagnoses = st.sidebar.multiselect("Select the Primary Diagnoses:", options=df["PrimaryDiagnoses"].unique(), default=df["PrimaryDiagnoses"].unique())
SecondaryDiagnoses = st.sidebar.multiselect("Select the Second Diagnoses:", options=df["SecondaryDiagnoses"].unique(), default=df["SecondaryDiagnoses"].unique())
ThirdDiagnoses = st.sidebar.multiselect("Select the Third Diagnoses:", options=df["ThirdDiagnoses"].unique(), default=df["ThirdDiagnoses"].unique())
diabetesMed = st.sidebar.multiselect("Select the Diabetes Med Administered Option:", options=df["diabetesMed"].unique(), default=df["diabetesMed"].unique())



st.set_option('deprecation.showPyplotGlobalUse', False)

# Diabetes drugs
diabetes_drugs = [
    "metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride",
    "acetohexamide", "glipizide", "glyburide", "tolbutamide", "pioglitazone",
    "rosiglitazone", "acarbose", "miglitol", "troglitazone", "tolazamide",
     "insulin", "glyburide.metformin", "glipizide.metformin",
    "glimepiride.pioglitazone", "metformin.rosiglitazone", "metformin.pioglitazone"
]

# Add diabetes drugs to multiselect options
drug_selection = {}
for drug in diabetes_drugs:
    drug_selection[drug] = st.sidebar.multiselect(f"Select {drug}:", options=df[drug].unique(), default=df[drug].unique())


# Apply filters
filtered_df = df[
    (df["age"].isin(age)) &
    (df["gender"].isin(gender)) &
    (df["race"].isin(race)) &
    (df["admission_type_id"].isin(admission_type_id)) &
    (df["A1Cresult"].isin(A1Cresult)) &
    (df["max_glu_serum"].isin(max_glu_serum)) &
    (df["PrimaryDiagnoses"].isin(PrimaryDiagnoses)) &
    (df["SecondaryDiagnoses"].isin(SecondaryDiagnoses)) &
    (df["ThirdDiagnoses"].isin(ThirdDiagnoses)) &
    (df["diabetesMed"].isin(diabetesMed))
]


# Additional filtering for drugs
for drug, selection in drug_selection.items():
    filtered_df = filtered_df[filtered_df[drug].isin(selection)]

# Display filtered DataFrame


import graphviz
import streamlit as st

def create_diagram():
    # Create a new graph
    graph = graphviz.Digraph()

    # Add nodes to the graph
    graph.node("Start")
    graph.node("Data Download")
    graph.node("Data Description")
    graph.node("Replace Missing Values")
    graph.node("Data Reduction")
    graph.node("Outlier Removal")
    graph.node("Data Transformation")
    graph.node("Model Training")
    graph.node("Model Evaluation")
    graph.node("Model Deployment")
    graph.node("End")

    # Add edges between nodes
    graph.edge("Start", "Data Download")
    graph.edge("Data Download", "Data Description")
    graph.edge("Data Description", "Replace Missing Values")
    graph.edge("Replace Missing Values", "Data Reduction")
    graph.edge("Data Reduction", "Outlier Removal")
    graph.edge("Outlier Removal", "Data Transformation")
    graph.edge("Data Transformation", "Model Training")
    graph.edge("Model Training", "Model Evaluation")
    graph.edge("Model Evaluation", "Model Deployment")
    graph.edge("Model Deployment", "End")

    return graph

# Main function for Streamlit app
def main():
    st.title("Diabetes Readmission Project Flowchart")

    # Create and display the flowchart diagram
    st.graphviz_chart(create_diagram())

# Run the Streamlit app
if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import plotly.express as px




# Group by readmission and gender, count occurrences
readmission_gender_count = df.groupby(["readmitted", "gender"]).size().reset_index(name="count")

# Pie chart for readmission by gender
st.subheader("Distribution of Readmission by Gender")
fig = px.pie(readmission_gender_count, values="count", names="gender", color="gender",
             hole=0.5, title="Readmission Distribution by Gender")
st.plotly_chart(fig, use_container_width=True)

# Bar graph for readmission by race
readmission_race_count = df.groupby(["readmitted", "race"]).size().reset_index(name="count")

st.subheader("Distribution of Readmission by Race")
fig_race_bar = px.bar(readmission_race_count, x="race", y="count", color="race",
                      title="Readmission Distribution by Race")
st.plotly_chart(fig_race_bar, use_container_width=True)

# Bar graph for readmission by age
readmission_age_count = df.groupby(["readmitted", "age"]).size().reset_index(name="count")
st.subheader("Distribution of Readmission by Age")
fig_age_bar = px.bar(readmission_age_count, x="age", y="count", color="age",
                     title="Readmission Distribution by Age")
st.plotly_chart(fig_age_bar, use_container_width=True)




# Bar graph for readmission by admission type
readmission_admission_type_count = df.groupby(["readmitted", "admission_type_id"]).size().reset_index(name="count")

st.subheader("Distribution of Readmission by Admission Type")
fig_admission_type_bar = px.bar(readmission_admission_type_count, x="admission_type_id", y="count", color="admission_type_id",
                                title="Readmission Distribution by Admission Type")
st.plotly_chart(fig_admission_type_bar, use_container_width=True)


# Grouping the data by discharge status
discharge_status_count = df['Discharge_Status'].value_counts().reset_index()
discharge_status_count.columns = ['Discharge_Status', 'count']

# Plotting the bar graph
st.subheader("Distribution of Discharge Status")
fig_discharge_status = px.bar(discharge_status_count, x="Discharge_Status", y="count",
                              title="Distribution of Discharge Status")
st.plotly_chart(fig_discharge_status, use_container_width=True)



# Grouping by race and calculating the mean length of stay
length_of_stay_race = df.groupby(["race"])["time_in_hospital"].mean().reset_index()

# Plotting the bar graph for length of stay by race
st.subheader("Distribution of Length of Stay by Race")
fig_length_of_stay_race = px.bar(length_of_stay_race, x="race", y="time_in_hospital",
                                 title="Length of Stay Distribution by Race")
st.plotly_chart(fig_length_of_stay_race, use_container_width=True)

# Grouping by gender and calculating the mean length of stay
length_of_stay_gender = df.groupby(["gender"])["time_in_hospital"].mean().reset_index()

# Plotting the bar graph for length of stay by gender
st.subheader("Distribution of Length of Stay by Gender")
fig_length_of_stay_gender = px.bar(length_of_stay_gender, x="gender", y="time_in_hospital",
                                   title="Length of Stay Distribution by Gender")
st.plotly_chart(fig_length_of_stay_gender, use_container_width=True)

# Grouping by age and calculating the mean length of stay
length_of_stay_age = df.groupby(["age"])["time_in_hospital"].mean().reset_index()

# Plotting the bar graph for length of stay by age
st.subheader("Distribution of Length of Stay by Age")
fig_length_of_stay_age = px.bar(length_of_stay_age, x="age", y="time_in_hospital",
                                title="Length of Stay Distribution by Age")
st.plotly_chart(fig_length_of_stay_age, use_container_width=True)


# Grouping by admission type and calculating the mean length of stay
length_of_stay_admission_type = df.groupby(["admission_type_id"])["time_in_hospital"].mean().reset_index()

# Plotting the bar graph for length of stay by admission type
st.subheader("Distribution of Length of Stay by Admission Type")
fig_length_of_stay_admission_type = px.bar(length_of_stay_admission_type, x="admission_type_id", y="time_in_hospital",
                                           title="Length of Stay Distribution by Admission Type")
st.plotly_chart(fig_length_of_stay_admission_type, use_container_width=True)



# Bar graph for HbA1c and Readmission
readmission_hba1c_count = df.groupby(["readmitted", "A1Cresult"]).size().reset_index(name="count")
fig_hba1c_bar = px.bar(readmission_hba1c_count, x="A1Cresult", y="count", color="A1Cresult",
                       title="Readmission Distribution by HbA1c Result")
st.plotly_chart(fig_hba1c_bar, use_container_width=True)

# Bar graph for Max Glucose Serum and Readmission
readmission_max_glu_serum_count = df.groupby(["readmitted", "max_glu_serum"]).size().reset_index(name="count")
fig_max_glu_serum_bar = px.bar(readmission_max_glu_serum_count, x="max_glu_serum", y="count", color="max_glu_serum",
                               title="Readmission Distribution by Max Glucose Serum")
st.plotly_chart(fig_max_glu_serum_bar, use_container_width=True)

# Bar graph for Diabetes Medication and Readmission
readmission_diabetes_med_count = df.groupby(["readmitted", "diabetesMed"]).size().reset_index(name="count")
fig_diabetes_med_bar = px.bar(readmission_diabetes_med_count, x="diabetesMed", y="count", color="diabetesMed",
                              title="Readmission Distribution by Diabetes Medication")
st.plotly_chart(fig_diabetes_med_bar, use_container_width=True)

# Bar graph for Diagnosis 1, 2, 3 and Readmission
readmission_PrimaryDiagnoses_count = df.groupby(["readmitted", "PrimaryDiagnoses"]).size().reset_index(name="count")
fig_PrimaryDiagnoses_bar = px.bar(readmission_PrimaryDiagnoses_count, x="PrimaryDiagnoses", y="count", color="readmitted",
                        title="Readmission Distribution by Diagnosis 1")
st.plotly_chart(fig_PrimaryDiagnoses_bar, use_container_width=True)

readmission_SecondaryDiagnoses_count = df.groupby(["readmitted", "SecondaryDiagnoses"]).size().reset_index(name="count")
fig_SecondaryDiagnoses_bar = px.bar(readmission_SecondaryDiagnoses_count, x="SecondaryDiagnoses", y="count", color="readmitted",
                        title="Readmission Distribution by Diagnosis 2")
st.plotly_chart(fig_SecondaryDiagnoses_bar, use_container_width=True)

readmission_ThirdDiagnoses_count = df.groupby(["readmitted", "ThirdDiagnoses"]).size().reset_index(name="count")
fig_ThirdDiagnoses_bar = px.bar(readmission_ThirdDiagnoses_count, x="ThirdDiagnoses", y="count", color="readmitted",
                        title="Readmission Distribution by Diagnosis 3")
st.plotly_chart(fig_ThirdDiagnoses_bar, use_container_width=True)



def plot_drug_readmission(drug):
    drug_readmission = df.groupby([drug, "readmitted"]).size().reset_index(name="count")
    fig = px.bar(drug_readmission, x=drug, y="count", color="readmitted",
                 title=f"Readmission by {drug.capitalize()} Use",
                 labels={"count": "Count", "readmitted": "Readmitted"})
    st.plotly_chart(fig, use_container_width=True)


# Add the graphs to your existing dashboard
for drug in diabetes_drugs:
    st.subheader(f"Readmission by {drug.capitalize()} Use")
    plot_drug_readmission(drug)


st.subheader(":bar_chart: Explore the Dataset")
df["A1Cresult"].replace("None", "Not Measured", inplace=True)
df["max_glu_serum"].replace("None", "Not Measured", inplace=True)




st.write(df)


import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


# Define features and target variable
X = df[['gender', 'age', 'race', 'admission_type_id', 'A1Cresult', 'max_glu_serum', 'diabetesMed',
        'PrimaryDiagnoses', 'SecondaryDiagnoses', 'ThirdDiagnoses', 'metformin', 'repaglinide',
        'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'tolbutamide',
        'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'tolazamide', 'insulin',
        'glyburide.metformin', 'glipizide.metformin', 'metformin.pioglitazone', 'time_in_hospital',
        'num_lab_procedures', 'num_procedures', 'num_medications', 'Hospital_Service',
         'number_diagnoses', 'Discharge_Status']]
y = df['readmitted']

# Convert categorical variables to dummy variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Calculate ROC curve
y_prob = model.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.grid(True)

# Calculate confusion matrix
y_pred = model.predict(X_test_scaled)
cm = confusion_matrix(y_test, y_pred)

# Display results in Streamlit
st.title('Logistic Regression Model')
st.write('Coefficients:', model.coef_)
st.write('Intercept:', model.intercept_)
st.subheader('ROC Curve')
st.pyplot(plt)

st.subheader('Confusion Matrix')
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, annot_kws={"size": 16})
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
st.pyplot(plt)

st.subheader('Classification Report')
st.text(classification_report(y_test, y_pred))

