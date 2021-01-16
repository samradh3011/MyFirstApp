import pandas as pd
import numpy as np
import streamlit as st

data = pd.read_csv('C:\\Users\\HP DB0186AU\\Desktop\\Data_Science\\Assignments\\Multiple Linear Regression\\Multiple Linear Regression\\Cars.csv')
uploader = st.file_uploader('browse file')
st.dataframe(uploader)

