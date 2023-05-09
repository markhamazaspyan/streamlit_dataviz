import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import time

st.set_page_config(layout="centered")

st.title('This is my first app!')
st.header('This is a header')

st.write('Streamlit is **_really_ cool**.')



@st.cache_data
def get_data(n_rows):
    time.sleep(3)
    return pd.DataFrame(np.random.randn(n_rows, 20), columns=('col %d' % i for i in range(20)))

n_rows = st.number_input('N rows', 10)
dataframe = get_data(n_rows)
st.write(dataframe)
if st.checkbox('Show line chart'):
    st.line_chart(dataframe)
