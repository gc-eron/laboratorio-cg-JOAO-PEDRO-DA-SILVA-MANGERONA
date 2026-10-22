# import streamlit as st

# st.title("Computação Gráfica - 2026/10")
# st.header("Aluno: João Pedro da Silva Mangerona")
# st.write("Ambiente configurado com sucesso via uv e Streamlit!")


import streamlit as st
import numpy as np

st.title("Atv 1 - Computação Gráfica - 2026/10")
st.write("Aluno: João Pedro da Silva Mangerona")
st.write("Ambiente configurado com sucesso via uv e Streamlit!")
n = st.slider("Tamanho", 2, 64, 8)
img = np.full((n, n), 128, dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)