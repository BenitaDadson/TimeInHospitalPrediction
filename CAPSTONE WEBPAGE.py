# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import streamlit as sl
import altair as alt
from faker import Faker
import plotly.express as px
import plotly.graph_objects as go
import random
import warnings
warnings.filterwarnings('ignore')
import os

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Step 2: Load the dataset
df = pd.read_excel("/Users/benitadadson/Downloads/diabetes 10 year.xlsx")

# Step 4: Create the web dashboard
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Hospital Readmission Analysis Dashboard"),

    # Dropdown for selecting feature to analyze
    dcc.Dropdown(
        id='feature-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='race',  # Default feature to analyze
        clearable=False
    ),

    # Graph to display analysis
    dcc.Graph(id='feature-graph'),

    # Table to display data
    html.Div(id='data-table')
])


# Define callback to update graph and table based on dropdown selection
@app.callback(
    [Output('feature-graph', 'figure'),
     Output('data-table', 'children')],
    [Input('feature-dropdown', 'value')]
)
def update_dashboard(selected_feature):
    # Visualization
    fig = px.bar(df, x=selected_feature, title=f"Number of Lab Procedures by {selected_feature}")

    # Data table
    table_df = df.groupby(selected_feature)['num_lab_procedures'].mean().reset_index()
    table = html.Table(
        [html.Tr([html.Th(col) for col in table_df.columns])] +
        [html.Tr([html.Td(table_df.iloc[i][col]) for col in table_df.columns]) for i in range(len(table_df))]
    )

    return fig, table


# Step 5: Run the web application
if __name__ == '__main__':
    app.run_server(debug=True)
