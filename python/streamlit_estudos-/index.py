import streamlit as st
import random 

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma página!",
    ["Home", "Gráfico"],
)

#Home
if pagina == "Home":
    st.title("Pagina Home")
    st.write("Sistema usando o Streamlit")

    #input
    nome = st.text_input("Digite seu nome")

    #selectbox
    curso = st.selectbox(
        "Escolha um curso",
        ["Python", "JS", "Banco de dados"]
    )
    #Slider
    nota = st.slider(
        "Esolha a sua nota",
        0,
        10,
        5
    )
    #Checkbox
    mostrar = st.checkbox("Mostrar mensagem")
    if mostrar:
        st.success("Checkbox marcado")
    else:
        st.error("Marca a Checkbox")
    
    #Butão
    if st.button("Enviar"):
        st.write(f"Nome : {nome}")
        st.write(f"Curso : {curso}")
        st.write(f"Nota : {nota}")

    #Colunas
    st.subheader("Colunas")
    col1, col2 = st.columns(2)

    with col1:
        st.info("Informações coluna 1")
    with col2:
        st.warning("Informação coluna 2")

#Grafico
elif pagina == "Gráfico":
    st.title("Pagina de Gráficos")
    valores = []
    for i in range(5):
        valores.append(random.randint(1,100))
    st.bar_chart(valores)
