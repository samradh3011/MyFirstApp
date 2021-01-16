import streamlit as st
import pandas as pd


st.set_page_config(page_icon='📅', page_title='Your Data Frame')
st.title('**Read, Write and Understand Data**')
data = st.file_uploader('Browse files to Open', type=['csv','xlsx'])
if data is None:
    pass
else:
    data = pd.read_csv(data)
    st.write('Your Dataframe:')
    st.dataframe(data)
    st.write('*Number of Columns*: ', len(data.columns))
    st.write('Null Values:', data.isna().sum())
    st.write('Summary:', data.describe())
