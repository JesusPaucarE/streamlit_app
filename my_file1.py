
import streamlit as st
import pandas as pd
import numpy as np

n = st.slider('n', 5, 100, step = 1)
char_data = pd.DataFrame(np.random.rand(n), columns = ['data'])
st.line_chart(char_data)