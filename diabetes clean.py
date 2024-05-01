import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Read the dataset
diabetes_10_year = pd.read_excel("/Users/benitadadson/Downloads/diabetes 10 year.xlsx")

# Replace '?' with NaN
diabetes_10_year.replace("?", pd.NA, inplace=True)

# Drop columns that are not relevant
drop_columns = ["id", "patient_nbr", "discharge_disposition_id", "admission_source_id",
                "payer_code", "medical_specialty", "examide", "citoglipton", "weight"]
diabetes_10_year.drop(columns=drop_columns, inplace=True)

# Drop rows with 'Unknown/Invalid' gender
diabetes_10_year = diabetes_10_year[diabetes_10_year['gender'] != 'Unknown/Invalid']

# Drop rows with missing values
diabetes_10_year.dropna(inplace=True)

# Convert 'readmitted' to binary variable
diabetes_10_year['readmitted'] = diabetes_10_year['readmitted'].apply(lambda x: 1 if x == '<30' else 0)

# Visualizations
# Gender and Readmission
sns.countplot(data=diabetes_10_year, x='gender', hue='readmitted')
plt.title('Gender and Readmission')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Age vs Readmission
sns.countplot(data=diabetes_10_year, x='age', hue='readmitted')
plt.title('Age vs Readmission')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Race and Readmission
sns.countplot(data=diabetes_10_year, x='race', hue='readmitted')
plt.title('Race and Readmission')
plt.xlabel('Race')
plt.ylabel('Count')
plt.show()

# Readmission by A1C Test Result
sns.countplot(data=diabetes_10_year, x='A1Cresult', hue='readmitted')
plt.title('Readmission by A1C Test Result')
plt.xlabel('A1C Test Result')
plt.ylabel('Count')
plt.show()

# Readmission by Max Glucose Serum Result
sns.countplot(data=diabetes_10_year, x='max_glu_serum', hue='readmitted')
plt.title('Readmission by Max Glucose Serum Result')
plt.xlabel('Max Glucose Serum Result')
plt.ylabel('Count')
plt.show()

# Define functions for creating visualizations

import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc, html
from dash.dependencies import Input, Output


def make_bar_chart(data, x, y, title):
    fig = px.bar(data, x=x, y=y, title=title)
    return fig

def make_pie_chart(data, labels, values, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title=title)
    return fig

# Sidebar
st.sidebar.title("Filter Data")
# Add sidebar filters based on your diabetes data columns
selected_age = st.sidebar.slider("Select age", min_value=0, max_value=100, value=50)
selected_gender = st.sidebar.selectbox("Select gender", ["Male", "Female"])

# Filter data based on sidebar inputs
filtered_data = diabetes_10_year[(diabetes_10_year['age'] == selected_age) & (diabetes_10_year['gender'] == selected_gender)]

# Main content
st.title("Diabetes Data Analysis")

# Calculate count of readmission for each age group
readmission_counts = filtered_data.groupby('age')['readmitted'].sum().reset_index()

# Display visualizations
st.subheader("Bar Chart by Age")
# Replace 'Some_Variable' with the column name you want to visualize
bar_chart = make_bar_chart(readmission_counts, x='age', y='readmitted', title='Age groups and readmission status')
st.plotly_chart(bar_chart)


st.subheader("Pie Chart by Gender")
# Replace 'Another_Variable' with the column name you want to visualize
pie_chart = make_pie_chart(filtered_data, labels=['Male', 'Female'], values=[100, 200], title='Readmission by Gender')
st.plotly_chart(pie_chart)

# Display metrics or summary statistics based on the filtered data
st.subheader("Summary Statistics")
# Calculate and display summary statistics (e.g., average, count) based on the filtered data
average_variable = filtered_data['time_in_hospital'].mean()
total_records = len(filtered_data)
st.write(f"Average Some Variable: {average_variable}")
st.write(f"Total Records: {total_records}")





#kip
readmission_status = df_selection["readmitted"].value_counts()

gender_male = df_selection["gender" == 'Male'].value_counts()
gender_female = df_selection["gender" == 'Female'].value_counts()

age_0 = df_selection["age" == '[0-10)'].value_counts()
age_1 = df["age" == '[10-20)'].value_counts()
age_2 = df["age" == '[20-30)'].value_counts()
age_3 = df["age" == '[30-40)'].value_counts()
age_4 = df["age" == '[40-50)'].value_counts()
age_5 = df["age" == '[50-60)'].value_counts()
age_6 = df["age" == '[60-70)'].value_counts()
age_7 = df["age" == '[70-80)'].value_counts()
age_8 = df["age" == '[80-90)'].value_counts()
age_9 = df["age" == '[90-100)'].value_counts()

race_black = df["race" == 'AfricanAmerican'].value_counts()
race_white = df["race" == 'Caucasian'].value_counts()
race_asian = df["race" == 'Asian'].value_counts()
race_hispanic = df["race" == 'Hispanic'].value_counts()
race_other = df["race" == 'Other'].value_counts()

average_time_in_hospital = round(df["time_in_hospital"].mean(), 1)
average_lab_procedures = round(df["num_lab_procedures"].mean(), 1)
average_num_medications = round(df["num_medications"].mean(), 1)


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Readmission:")
    st.subheader("{accidental_readmission_status:}")

with middle_column:
    st.subheader("Gender:")
    st.subheader("{gender}")

with right_column:
    st.subheader("Race:")
    st.subheader("{race}")



#top kpi

readmission_status = df_selection["readmitted"].value_counts()

gender = df_selection["gender"].value_counts()


age = df_selection["age"].value_counts()


race = df_selection["race"].value_counts()


average_time_in_hospital = round(df_selection["time_in_hospital"].mean(), 1)
average_lab_procedures = round(df_selection["num_lab_procedures"].mean(), 1)
average_num_medications = round(df_selection["num_medications"].mean(), 1)


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Readmission:")
    st.subheader("{accidental_readmission_status:}")

with middle_column:
    st.subheader("Gender:")
    st.subheader("{gender}")

with right_column:
    st.subheader("Race:")
    st.subheader("{race}")

st.markdown("---")

#readmission by race [bar chart]





