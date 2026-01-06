import streamlit as st
from datetime import date

st.set_page_config(page_title="Cadastro de Clientes", layout="centered")

st.title("📋 Cadastro de Clientes")

# Formulário
with st.form("form_cadastro"):
    nome = st.text_input("Nome completo")

    data_nascimento = st.date_input(
        "Data de aniversário", min_value=date(1900, 1, 1), max_value=date.today())

    endereco = st.text_area("Endereço completo")

    tipo_pessoa = st.selectbox(
        "Tipo de pessoa", ("Pessoa Física", "Pessoa Jurídica"))

    submitted = st.form_submit_button("Cadastrar")

# Exibição dos dados
if submitted:
    if nome.strip() == "" or endereco.strip() == "":
        st.error("⚠️ Preencha todos os campos obrigatórios.")
    else:
        st.success("✅ Cliente cadastrado com sucesso!")
        st.write("### Dados do Cliente")
        st.write(f"**Nome:** {nome}")
        st.write(
            f"**Data de aniversário:** {data_nascimento.strftime('%d/%m/%Y')}")
        st.write(f"**Endereço:** {endereco}")
        st.write(f"**Tipo:** {tipo_pessoa}")
