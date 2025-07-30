import pandas as pd
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

# === CONFIGURAÇÃO DE URLS ===
url_base = 'https://docs.google.com/spreadsheets/d/1AQNVp1AlD3XqrOxILCCWa6ULgsW6ZLhpB5ODndTDrlg/export?format=csv&gid='

# GIDs das abas (confirmados)
gid_vmais = '0'             # Aba "V+"
gid_estoque = '1445310468'   # Aba "Estoque"
gid_epmais = '329262931'   # Aba "Ep+"

# === IMPORTAÇÃO DOS DADOS ===
df_vmais = pd.read_csv(url_base + gid_vmais)
df_estoque = pd.read_csv(url_base + gid_estoque)
df_epmais = pd.read_csv(url_base + gid_epmais)



# ========================================= DATA CLEANING ==============================================
# === FORMATAÇÃO FINAL E REORDENAÇÃO ===

# === df_vmais ===
df_vmais["Filial"] = df_vmais["Filial"].astype(str) + " - " + df_vmais["Nome FIlial"]
df_vmais["Região"] = df_vmais["Núm. Região"].astype(str) + " - " + df_vmais["Nome Região"].str.upper()
df_vmais["Colaborador Sorteado"] = df_vmais["matricula"].astype(str) + " - " + df_vmais["Colab. Ganhador"]
df_vmais.drop(columns=["Nome FIlial", "Nome Região", "Núm. Região", "matricula", "Colab. Ganhador"], inplace=True)
df_vmais = df_vmais[["Data", "Região", "Filial", "Colaborador Sorteado"]]

# === df_estoque ===
df_estoque["Filial"] = df_estoque["Filial"].astype(str) + " - " + df_estoque["Nome FIlial"]
df_estoque["Região"] = df_estoque["Núm. Região"].astype(str) + " - " + df_estoque["Nome Região"].str.upper()
df_estoque["Colaborador Sorteado"] = df_estoque["matricula"].astype(str) + " - " + df_estoque["Colab. Ganhador"]
df_estoque.drop(columns=["Nome FIlial", "Nome Região", "Núm. Região", "matricula", "Colab. Ganhador"], inplace=True)
df_estoque = df_estoque[["Data", "Região", "Filial", "Colaborador Sorteado"]]

# === df_epmais ===
df_epmais["Filial"] = df_epmais["Filial"].astype(str) + " - " + df_epmais["Nome FIlial"]
df_epmais["Região"] = df_epmais["Núm. Região"].astype(str) + " - " + df_epmais["Nome Região"].str.upper()
df_epmais["Colaborador Sorteado"] = df_epmais["matricula"].astype(str) + " - " + df_epmais["Colab. Ganhador"]
df_epmais.drop(columns=["Nome FIlial", "Nome Região", "Núm. Região", "matricula", "Colab. Ganhador"], inplace=True)
df_epmais = df_epmais[["Data", "Região", "Filial", "Colaborador Sorteado"]]
# ========================================= DATA CLEANING ==============================================




# ========================================= LAYOUT STREAMLIT ==============================================
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
    button[kind="secondary"] {
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 0.75em 1em !important;
    }
    button[kind="secondary"]:focus-visible {
        outline: 2px solid #00C851 !important;
        box-shadow: 0 0 0 0.25rem rgba(0, 200, 81, 0.25) !important;
    }
    button[kind="secondary"]:hover {
        border-color: #00C851 !important;
    }
    .stTitle h1 {
        font-size: 40px !important;
    }
    .stMarkdown h3 {
        font-size: 28px !important;
    }
    </style>
""", unsafe_allow_html=True)

# === TÍTULO CENTRALIZADO ===
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
