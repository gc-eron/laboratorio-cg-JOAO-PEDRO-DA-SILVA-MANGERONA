import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)
import numpy as np
import streamlit as st
from PIL import Image
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
st.image(img)

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)