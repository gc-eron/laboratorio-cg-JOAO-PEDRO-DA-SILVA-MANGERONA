import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Bandeira Rússia")

# imagem = np.zeros((8, 8), dtype=np.uint8)
# imagem[2, 5] = 255
# imagem[4:, :] = 128
# st.image(ampliar(imagem))
# st.write(imagem)

bandeira = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira[:2,:] = (0, 0, 255)
bandeira[2:4,:] = (255, 255, 255)
bandeira[4:, :] = (255, 0, 0)
st.image(ampliar(bandeira))