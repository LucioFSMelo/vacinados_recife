import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Variável para o link de acesso ao arquivo csv do portal
data_url = 'http://dados.recife.pe.gov.br/dataset/7ccb3816-0d62-49e1-b39a-3159870883b0/resource/99b42b09-95af-47de-8411-ab99c380c3ef/download/vacinados.csv'

@st.cache_data
def load_data():
    data = pd.read_csv(data_url, sep=';')
    return data

data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

st.header('Perfil das pessoas vacinadas - 2021')
st.text('Fonte: http://dados.recife.pe.gov.br/group/covid')
st.write(data)