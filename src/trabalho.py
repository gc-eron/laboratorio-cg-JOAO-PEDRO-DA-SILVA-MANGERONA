import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/senhora.png")
img = np.array(foto)[:, :, :3]

st.header("1. Saturação")

fator_s = st.slider("Saturação", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
s = hsv[:, :, 1].astype(float)
s = s * fator_s
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
saturada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
st.image(saturada, caption="Saturação")

st.header("2. Brilho")

fator_v = st.slider("Brilho", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
v = hsv[:, :, 2].astype(float)
v = v * fator_v
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
brilho = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
st.image(brilho, caption="Brilho")

st.header("11. Espelhamento")

col1, col2 = st.columns(2)
horizontal = img[:, ::-1]
vertical = img[::-1, :]
col1.image(horizontal, caption="Horizontal")
col2.image(vertical, caption="Vertical")

st.header("14. Só uma cor")

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h_min, h_max = st.slider("Faixa de H", 0, 179, (0, 20))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0
st.image(so_cor, caption="Só a cor escolhida")

st.header("19. Moldura")

espessura = st.slider("Espessura", 1, 100, 20)
r = st.slider("R", 0, 255, 255)
g = st.slider("G", 0, 255, 0)
b = st.slider("B", 0, 255, 0)
cor = (r, g, b)
moldura = img.copy()
moldura[:espessura, :] = cor
moldura[-espessura:, :] = cor
moldura[:, :espessura] = cor
moldura[:, -espessura:] = cor
st.image(moldura, caption="Moldura")
