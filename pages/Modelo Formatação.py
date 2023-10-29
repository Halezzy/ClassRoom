import streamlit as st

# Título da página
st.title("Demonstração de Estilos e Formatação de Textos")

# Texto simples em negrito
st.header("Texto em Negrito")

# Texto em itálico
st.subheader("Texto em Itálico")

# Texto com cores personalizadas
st.subheader("Texto Colorido")
st.markdown("<span style='color: blue;'>Texto em Azul</span>", unsafe_allow_html=True)
st.markdown("<span style='color: green;'>Texto em Verde</span>", unsafe_allow_html=True)
st.markdown("<span style='color: red;'>Texto em Vermelho</span>", unsafe_allow_html=True)

# Texto com tamanho personalizado
st.subheader("Texto com Tamanho Personalizado")
st.markdown("<h1 style='color: purple;'>Texto Tamanho H1</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: orange;'>Texto Tamanho H2</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: brown;'>Texto Tamanho H3</h3>", unsafe_allow_html=True)

# Caixa de texto
st.subheader("Caixa de Texto")
texto_caixa = st.text_area("Digite algo aqui:")
if texto_caixa:
    st.write(f"Você digitou: {texto_caixa}")

# Botões com estilos
st.subheader("Botões")
if st.button("Botão Padrão"):
    st.write("Você clicou no botão padrão!")
if st.button("Botão Personalizado", key="custom_button"):
    st.write("Você clicou no botão personalizado!")

# Texto com formatação Markdown
st.subheader("Texto com Formatação Markdown")
st.markdown("**Texto em Negrito**")
st.markdown("*Texto em Itálico*")
st.markdown("Texto com [link](https://www.streamlit.io/)")


st.subheader("Código deste exemplo")

st.code(
    """# Título da página
st.title("Demonstração de Estilos e Formatação de Textos")

# Texto simples em negrito
st.header("Texto em Negrito")

# Texto em itálico
st.subheader("Texto em Itálico")

# Texto com cores personalizadas
st.subheader("Texto Colorido")
st.markdown("<span style='color: blue;'>Texto em Azul</span>", unsafe_allow_html=True)
st.markdown("<span style='color: green;'>Texto em Verde</span>", unsafe_allow_html=True)
st.markdown("<span style='color: red;'>Texto em Vermelho</span>", unsafe_allow_html=True)

# Texto com tamanho personalizado
st.subheader("Texto com Tamanho Personalizado")
st.markdown("<h1 style='color: purple;'>Texto Tamanho H1</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: orange;'>Texto Tamanho H2</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: brown;'>Texto Tamanho H3</h3>", unsafe_allow_html=True)

# Caixa de texto
st.subheader("Caixa de Texto")
texto_caixa = st.text_area("Digite algo aqui:")
if texto_caixa:
    st.write(f"Você digitou: {texto_caixa}")

# Botões com estilos
st.subheader("Botões")
if st.button("Botão Padrão"):
    st.write("Você clicou no botão padrão!")
if st.button("Botão Personalizado", key="custom_button"):
    st.write("Você clicou no botão personalizado!")

# Texto com formatação Markdown
st.subheader("Texto com Formatação Markdown")
st.markdown("**Texto em Negrito**")
st.markdown("*Texto em Itálico*")
st.markdown("Texto com [link](https://www.streamlit.io/)")

""")