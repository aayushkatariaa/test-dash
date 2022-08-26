import time  

import numpy as np  
import pandas as pd  
import plotly.express as px  
import streamlit as st  
dataset_url="https://github.com/aayushkatariaa/dataset-1/blob/main/Country_clean.csv"
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, on_bad_lines='skip')

df = get_data()
st.set_page_config(
    page_title="testing dashboard",,
    layout="wide",
)
st.title("Real-Time / Live Data Science Dashboard")
job_filter = st.selectbox("Select the Job", pd.unique(df["Country Name"]))
df = df[df["Country Name"] == job_filter]
