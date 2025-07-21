import streamlit as st
import pandas as pd
from pathlib import Path

# Arquivo onde os usuários serão salvos
USUARIOS_CSV = Path("usuarios.csv")

# Função para salvar os dados no CSV
def salvar_usuario(nome, email, senha):
    if USUARIOS_CSV.exists():
        usuarios = pd.read_csv(USUARIOS_CSV)
    else:
        usuarios = pd.DataFrame(columns=["Nome", "Email", "Senha"])

    # Verificar se o e-mail já está cadastrado
    if email in usuarios["Email"].values:
        st.error("Este e-mail já está cadastrado. Use outro.")
        return False

    # Adicionar novo usuário
    novo_usuario = pd.DataFrame({"Nome": [nome], "Email": [email], "Senha": [senha]})
    usuarios = pd.concat([usuarios, novo_usuario], ignore_index=True)
    usuarios.to_csv(USUARIOS_CSV, index=False)
    return True

st.title("📋 Cadastro de Usuário")
st.write("Preencha os campos abaixo para criar sua conta.")

# Campos do formulário
nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
confirma_senha = st.text_input("Confirme a senha", type="password")

if st.button("Cadastrar"):
    if not nome or not email or not senha or not confirma_senha:
        st.error("Por favor, preencha todos os campos.")
    elif senha != confirma_senha:
        st.error("As senhas não coincidem.")
    else:
        if salvar_usuario(nome, email, senha):
            st.success("Usuário cadastrado com sucesso! Vá para a tela de login.")
