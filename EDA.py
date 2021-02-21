import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


##Web app title
st.markdown('''# **EDA App**
This is the EDA app created in **Streamlit** using Pandas Profiling is an Automated tool which is helpful for creating charts,bar graphs also getting all the statistical information etc. of the data Automatically''')

#Upload csv data
with st.sidebar.header('1. Upload CSV Data here'):
    uploaded_file=st.sidebar.file_uploader("Upload yor CSV data",type=['csv'])
    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
    """)



#pandas profiling
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr= ProfileReport(df,explorative=True)
    st.header('**Input DataFrame**')
    st.write(df.head())
    st.write('---')
    st.header('**Pandas Profiling**')
    st_profile_report(pr)

else:
    st.info('Awaiting for CVS file to be uploaded.')
    if st.button('Press to see the Example data'):
        @st.cache
        def load_data():
            a=pd.DataFrame(
                np.random.rand(100,6),columns=['a','b','c','d','e','f'])
            return a

        df=load_data()
        pr=ProfileReport(df,explorative=True)
        st.header('**Input DataFrame**')
        st.write(df.head())
        st.write('---')
        st.header('**Pandas Profiling**')
        st_profile_report(pr)