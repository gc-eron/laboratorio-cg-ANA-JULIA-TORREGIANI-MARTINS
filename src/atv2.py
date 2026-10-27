import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Imagem como matriz")

bandeira = np.zeros((6, 9, 3), dtype=np.uint8)
bandeira[:,:3] = (0, 140, 69)
bandeira[:,3:6] = (244, 245, 240)
bandeira[:, 6:] = (205, 0, 33)
st.image(ampliar(bandeira))