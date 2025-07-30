import pandas as pd
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

# === CONFIGURAÇÃO DE URLS ===
url_base = 'https://docs.google.com/spreadsheets/d/1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg/export?format=csv&gid='

# GIDs das abas (confirmados)
gid_vmais = '0'             # Aba "V+"
gid_estoque = '442396298'   # Aba "Estoque"
gid_epmais = '2119602860'   # Aba "Ep+"

# === IMPORTAÇÃO DOS DADOS ===
df_vmais = pd.read_csv(url_base + gid_vmais)
df_estoque = pd.read_csv(url_base + gid_estoque)
df_epmais = pd.read_csv(url_base + gid_epmais)

# === IMAGEM CENTRALIZADA ===
image = Image.open("quero.png").resize((150, 150))
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_str}" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# === CSS PERSONALIZADO ===
st.markdown("""
    <style>
    /* Aumentar tamanho da fonte dos botões */
    button[kind="secondary"] {
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 0.75em 1em !important;
    }

    /* Cor verde ao focar/hover no botão */
    button[kind="secondary"]:focus-visible {
        outline: 2px solid #00C851 !important;
        box-shadow: 0 0 0 0.25rem rgba(0, 200, 81, 0.25) !important;
    }
    button[kind="secondary"]:hover {
        border-color: #00C851 !important;
    }

    /* Títulos e textos maiores */
    .stTitle h1 {
        font-size: 40px !important;
    }
    .stMarkdown h3 {
        font-size: 28px !important;
    }
    </style>
""", unsafe_allow_html=True)

# === TÍTULO CENTRALIZADO COM FONTE MAIOR ===
st.markdown("""
    <h1 style="text-align: center; font-size: 40px; margin-top: 0;">
        Sorteio Campanha de Aniversário
    </h1>
""", unsafe_allow_html=True)


# === CONTROLE DE ABA SIMULADA ===
if "aba" not in st.session_state:
    st.session_state.aba = "V+"

# === BOTÕES DE NAVEGAÇÃO ===
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📄 V+", use_container_width=True):
        st.session_state.aba = "V+"
with col2:
    if st.button("📦 Estoque", use_container_width=True):
        st.session_state.aba = "Estoque"
with col3:
    if st.button("📝 Ep+", use_container_width=True):
        st.session_state.aba = "Ep+"

# === CONTEÚDO DAS "ABAS" ===
st.markdown("---")
if st.session_state.aba == "V+":
    st.subheader("📄 Sorteio V+")
    st.dataframe(df_vmais)
elif st.session_state.aba == "Estoque":
    st.subheader("📦 Sorteio Estoque")
    st.dataframe(df_estoque)
elif st.session_state.aba == "Ep+":
    st.subheader("📝 Sorteio Ep+")
    st.dataframe(df_epmais)
