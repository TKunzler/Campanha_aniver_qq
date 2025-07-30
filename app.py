import pandas as pd
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

# Importar Dados
url_csv = 'https://docs.google.com/spreadsheets/d/1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg/export?format=csv&id=1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg&gid=0'
df = pd.read_csv(url_csv)


# Página
st.title("Sorteio Campanha de Aniversário")


st.table(df)
