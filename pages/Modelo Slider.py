import streamlit as st

st.title("Tutorial Slider ")
# Lista de URLs das imagens
imagens = [
    "Images/StLogo1.png",
    "Images/PyLogo.jpg", 
    "Images/TutSlider.png"
]

# Slider interativo para navegar entre as imagens
slide_idx = st.slider("Navegar pelas Imagens", 0, len(imagens) - 1, 0, format="%d")

# Exibir a imagem de acordo com o slide selecionado
st.image(imagens[slide_idx], caption=f"Imagem {slide_idx + 1}", use_column_width=True)
