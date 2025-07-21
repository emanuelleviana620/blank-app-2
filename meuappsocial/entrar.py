import streamlit as st
import pandas as pd
from pathlib import Path

# Arquivo de usuários
USUARIOS_CSV = Path("usuarios.csv")

# Função para autenticar usuário
def autenticar(email, senha):
    if USUARIOS_CSV.exists():
        usuarios = pd.read_csv(USUARIOS_CSV)
        usuario = usuarios[(usuarios["Email"] == email) & (usuarios["Senha"] == senha)]
        if not usuario.empty:
            return usuario.iloc[0]["Nome"]
    return None

st.title("🔑 Login")
st.write("Digite seu e-mail e senha para acessar o app.")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    usuario = autenticar(email, senha)
    if usuario:
        st.success(f"Bem-vindo(a), {usuario}!")
        st.header("📚 Seus Direitos Sociais")
        st.markdown("""
        ✅ Direito à saúde  
        ✅ Direito à educação  
        ✅ Direito ao trabalho  
        ✅ Direito à assistência social  
        ✅ Direito à previdência social  
        ✅ Direito à moradia
        """)
    else:
        st.error("E-mail ou senha incorretos. Tente novamente.")