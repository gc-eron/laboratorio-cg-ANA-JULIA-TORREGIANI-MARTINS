import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

st.header("1. Saturação")
fator_sat = st.slider("Saturação", 0.0, 2.0, 1.0)
hsv_sat = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv_sat = hsv_sat.astype(np.float32)
hsv_sat[:, :, 1] *= fator_sat
hsv_sat[:, :, 1] = np.clip(hsv_sat[:, :, 1], 0, 255)
hsv_sat = hsv_sat.astype(np.uint8)
img_sat = cv2.cvtColor(hsv_sat, cv2.COLOR_HSV2RGB)
st.image(img_sat, caption="Saturação ajustada")

st.header("2. Brilho")
fator_brilho = st.slider("Brilho", 0.0, 2.0, 1.0)
hsv_brilho = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv_brilho = hsv_brilho.astype(np.float32)
hsv_brilho[:, :, 2] *= fator_brilho
hsv_brilho[:, :, 2] = np.clip(hsv_brilho[:, :, 2], 0, 255)
hsv_brilho = hsv_brilho.astype(np.uint8)
img_brilho = cv2.cvtColor(hsv_brilho, cv2.COLOR_HSV2RGB)
st.image(img_brilho, caption="Brilho ajustado")

st.header("3. Matiz girada")
giro = st.slider("Giro da matiz (graus)", 0, 179, 0)
hsv_matiz = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv_matiz[:, :, 0] = (hsv_matiz[:, :, 0].astype(int) + giro) % 180
img_matiz = cv2.cvtColor(hsv_matiz, cv2.COLOR_HSV2RGB)
st.image(img_matiz, caption="Matiz girada")

st.header("8. Negativo")
negativo = 255 - img
st.image(negativo, caption="Negativo")

st.header("11. Espelhamento")
horizontal = img[:, ::-1]
vertical = img[::-1, :]
col1, col2 = st.columns(2)
col1.image(horizontal, caption="Espelhada na horizontal")
col2.image(vertical, caption="Espelhada na vertical")