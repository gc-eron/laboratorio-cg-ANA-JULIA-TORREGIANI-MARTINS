import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
a, l = img.shape[0], img.shape[1]

# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)
col1.image(img, caption="Foto")

h_cor = np.zeros((a, l, 3), dtype=np.uint8)
h_cor[:, :, 0] = hsv[:, :, 0]
h_cor[:, :, 1] = 255
h_cor[:, :, 2] = 255
col2.image(cv2.cvtColor(h_cor, cv2.COLOR_HSV2RGB), caption="H em cor")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

sat = col1.slider("Saturação", 0.0, 2.0, 1.0)
bri = col1.slider("Brilho", 0.0, 2.0, 1.0)
copia = hsv.copy().astype(np.float32)
copia[:, :, 1] = np.clip(copia[:, :, 1] * sat, 0, 255)
copia[:, :, 2] = np.clip(copia[:, :, 2] * bri, 0, 255)
col1.image(cv2.cvtColor(copia.astype(np.uint8), cv2.COLOR_HSV2RGB), caption="Saturação e brilho")

giro = col2.slider("Giro da matiz", 0, 179, 0)
girada = hsv.copy()
girada[:, :, 0] = (hsv[:, :, 0].astype(int) + giro) % 180
col2.image(cv2.cvtColor(girada, cv2.COLOR_HSV2RGB), caption="Matiz girada")

# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)