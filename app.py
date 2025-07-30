import pandas as pd
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

# Importar Dados
url_csv = 'https://docs.google.com/spreadsheets/d/1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg/export?format=csv&id=1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg&gid=0'
df = pd.read_csv(url_csv)

# Carrega e redimensiona
image = Image.open("quero.png").resize((150, 150))

# Converte imagem para base64
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Insere imagem centralizada com HTML
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_str}" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# Página
st.title("Sorteio Campanha de Aniversário")


st.table(df)
