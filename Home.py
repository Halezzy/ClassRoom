import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="WebPages com Python e Streamlit",
    layout="wide"
)

# Título da página
st.title("WebPages com Python e Streamlit")
st.subheader("prof. Hugo Alessi")

# Tópicos disponíveis
topicos = ["Apresentação", "Tutorial de Instalação", "Lista de Elementos e Códigos"]

# Slider para escolher o tópico
topico_selecionado = st.selectbox("Selecione um Tópico", topicos)

# Exibir conteúdo com base no tópico selecionado
if topico_selecionado == "Apresentação":
    # Apresentação
    st.header("Criando Páginas Web com Streamlit")

    # Slides da apresentação
    slides_apresentacao = [
        "O que é o Streamlit?",
        "Por que usar o Streamlit?",
        "Rápido Desenvolvimento",
        "Facilidade de Compartilhamento",
        "Comunidade Ativa",
        "Flexibilidade",
        "Conclusão",
        "Recursos Adicionais"
       
    ]

    # Slider interativo para a exibição dos slides da apresentação
    slide_idx_apresentacao = st.slider(
        "Navegar pelos Slides",
        0, len(slides_apresentacao) - 1, 0,
        format="%d",
        key="slider_apresentacao"
    )

    # Exibir o conteúdo de acordo com o slide selecionado
    st.markdown(f"**Slide: {slides_apresentacao[slide_idx_apresentacao]}**")
    if slide_idx_apresentacao == 0:
        st.markdown("Streamlit é uma biblioteca de código aberto em Python projetada para simplificar o processo de criação de aplicativos da web\n"
                    "interativos e painéis de controle.\n"
                    "Ele permite que desenvolvedores e cientistas de dados criem aplicativos da web de maneira\n"
                    "rápida e fácil, sem a necessidade de conhecimento avançado em desenvolvimento web, HTML, CSS ou JavaScript.")
    elif slide_idx_apresentacao == 1:
        st.markdown("O Streamlit é conhecido por sua abordagem simplificada. Os aplicativos da web são criados diretamente no código Python,\n"
                    "usando uma API Python simples e intuitiva. Isso significa que os desenvolvedores podem focar no desenvolvimento de funcionalidades,\n"
                    "sem se preocupar com a complexidade do desenvolvimento web.")
        
    elif slide_idx_apresentacao == 2:
        st.markdown("O Streamlit é particularmente útil para o desenvolvimento ágil e rápido. Os aplicativos podem ser criados\n"
                    "e iterados rapidamente, o que é valioso para prototipagem e desenvolvimento de MVPs (Mínimo Produto Viável.")
        
    elif slide_idx_apresentacao == 3:
        st.markdown("Os aplicativos criados com o Streamlit podem ser compartilhados facilmente com outras pessoas. Você pode compartilhar\n"
                    "seu aplicativo apenas fornecendo a elas o código Python..")
        
    elif slide_idx_apresentacao == 4:
        st.markdown("O Streamlit tem uma comunidade ativa de usuários e desenvolvedores, o que significa que você pode encontrar recursos,\n"
                    "pacotes personalizados e suporte facilmente.")
        
    elif slide_idx_apresentacao == 5:
        st.markdown("Embora seja simples, o Streamlit é flexível o suficiente para atender a uma variedade de casos de uso, desde painéis de dados\n"
                    "interativos até aplicativos web completos.\n"
                    "Existem opções de hospedagem para implantar seus aplicativos Streamlit na web, facilitando o compartilhamento com outros usuários.")
              
    elif slide_idx_apresentacao == 6:
        st.markdown("Em resumo, o Streamlit é uma ferramenta poderosa para quem deseja criar aplicativos da web interativos com Python de forma rápida \n"
                    "e descomplicada. Ele é amplamente usado por cientistas de dados, desenvolvedores e engenheiros para criar protótipos, painéis de dados\n"
                    "e aplicativos da web de produção. Se você está procurando uma maneira eficaz de criar aplicativos da web sem ter que aprender tecnologias web complexas,\n"
                    "o Streamlit é uma escolha sólida.")
               
    elif slide_idx_apresentacao == 7:
        st.markdown("Recursos Adicionais:")
        st.markdown(" - [Site Oficial do Streamlit](https://streamlit.io)")
        st.markdown(" - [Repositório do Streamlit no GitHub](https://github.com/streamlit/streamlit)")
        st.markdown(" - [Documentação do Streamlit](https://docs.streamlit.io)")
        
    
elif topico_selecionado == "Tutorial de Instalação":
    # Tutorial de Instalação
    st.header("Tutorial: Como Instalar o Streamlit")

    st.markdown("Para começar a usar o Streamlit, siga estas etapas:")

    # Passo 1
    st.subheader("Passo 1: Instale o Streamlit pelo Prompt de comando CMD")
    st.code("pip install streamlit")
    st.write("Em caso de erro pyarrow.")
    st.code("pip install --extra-index-url https://pypi.fury.io/arrow-nightlies/ --prefer-binary --pre pyarrow")
    
    # Passo 2
    st.subheader("Passo 2: Em Desktop, crie o arquivo app.py\n"
                 "Pode-se utilizar o Visual Code")
    
    # Passo 3
    st.subheader("Passo 3: Escreva seu sódigo Streamlit")
    st.code(
        """python
        import streamlit as st
        st.title("Meu Primeiro Aplicativo Streamlit")
        st.header("Meu Primeiro Aplicativo Streamlit")
        st.subheader("Meu Primeiro Aplicativo Streamlit")
        """
    )

    # Passo 4
    st.subheader("Passo 4: Execute o Aplicativo: pelo CMD. obs. deve-se estar no diretório do arquivo")
    st.code("streamlit run app.py")

elif topico_selecionado == "Lista de Elementos e Códigos":
    # Lista de Elementos e Códigos
    st.header("Lista de Elementos e Códigos para Construção de Páginas")

    # Exemplos de elementos e códigos
    st.subheader("Título e Texto")
    st.markdown("```python\nst.title('Título')\nst.write('Texto')\n```")

    st.subheader("Imagem")
    st.markdown("```python\nfrom PIL import Image\nimage = Image.open('imagem.jpg')\nst.image(image, caption='Descrição da Imagem', use_column_width=True)\n```")

    st.subheader("Gráfico")
    st.markdown("```python\nimport matplotlib.pyplot as plt\nplt.plot([1, 2, 3, 4])\nst.pyplot()\n```")

    st.subheader("Botão")
    st.markdown("```python\nif st.button('Clique-me'):\n    st.write('Você clicou no botão!')\n```")

    st.subheader("Entrada de Dados")
    st.markdown("```python\nnome = st.text_input('Nome')\nidade = st.number_input('Idade')\n```")
    
    st.subheader("Saída de Dados")
    st.markdown("```python\n st.write(Nome)\nst.write(Idade)\n```")

    st.subheader("Seleção")
    st.markdown("```python\nopcao = st.selectbox('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'])\n```")

# Rodapé
st.markdown("---")
st.write("Obrigado por explorar nossos recursos! 🚀")

# Executar o aplicativo com 'streamlit run nome_do_arquivo.py'
