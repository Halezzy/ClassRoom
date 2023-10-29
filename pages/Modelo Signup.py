import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Página de Cadastro de Usuário",
    layout="wide"
)

# Título da página
st.title("Bem-vindo à Nossa Página de Cadastro de Usuário")

# Subtítulo
st.header("Registre-se para fazer parte da nossa comunidade!")

# Informação adicional criativa
st.markdown("![Streamlit](https://upload.wikimedia.org/wikipedia/commons/6/69/Streamlit_logo_with_name.png)")

# Formulário de cadastro de usuário
st.subheader("Cadastro de Usuário")

# Nome do usuário
nome = st.text_input("Nome")

# E-mail do usuário
email = st.text_input("E-mail")

# Senha do usuário
senha = st.text_input("Senha", type="password")

# Botão de envio
if st.button("Registrar"):
    # Exibindo os dados informados
    st.subheader("Dados informados:")
    st.write("Nome:", nome)
    st.write("E-mail:", email)
    st.write("Senha: *** (não exibida por motivos de segurança)")

# Rodapé criativo
st.markdown("---")
st.write("Seja bem-vindo à nossa comunidade! 🚀")

# Executar o aplicativo com 'streamlit run nome_do_arquivo.py'

st.subheader("Código deste modelo")
st.code("""import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Página de Cadastro de Usuário",
    layout="wide"
)

# Título da página
st.title("Bem-vindo à Nossa Página de Cadastro de Usuário")

# Subtítulo
st.header("Registre-se para fazer parte da nossa comunidade!")

# Informação adicional criativa
st.markdown("![Streamlit](https://upload.wikimedia.org/wikipedia/commons/6/69/Streamlit_logo_with_name.png)")

# Formulário de cadastro de usuário
st.subheader("Cadastro de Usuário")

# Nome do usuário
nome = st.text_input("Nome")

# E-mail do usuário
email = st.text_input("E-mail")

# Senha do usuário
senha = st.text_input("Senha", type="password")

# Botão de envio
if st.button("Registrar"):
    # Exibindo os dados informados
    st.subheader("Dados informados:")
    st.write("Nome:", nome)
    st.write("E-mail:", email)
    st.write("Senha: *** (não exibida por motivos de segurança)""")

# Rodapé criativo
st.markdown("---")
st.write("Seja bem-vindo à nossa comunidade! 🚀")

# Executar o aplicativo com 'streamlit run nome_do_arquivo.py')
