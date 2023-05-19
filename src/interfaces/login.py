#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

import streamlit as st
from models.abas import Abas
from models.funcoes import Funcao

class AbaLogin:
    def __init__(self, controller) -> None:
        self.controller = controller

        st.title("PH SNKRS🔥")
        st.header("Login")

        col1, col2 = st.columns(2)
        with col1:
            self.login_email = st.text_input(label = "E-mail", placeholder ="Digite seu E-mail", value="")
        with col2:
            self.login_senha = st.text_input(label = "Senha", placeholder ="Digite sua senha", type='password', value="")

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 3.35, 1.1])
        with col1:
            self.btt_fazer_login = st.button(
                label="Entrar", 
                on_click=self.autenticar_login
                )
        with col5:
            self.btt_fazer_cadastro = st.button(
                label="Cadastre-se",
                on_click=Funcao.setar_ambiente_pagina_cadastro
                )

        Funcao.escrever_mensagem_aviso()
    
    def autenticar_login(self):
        if not(Funcao.validar_string(self.login_email) and Funcao.validar_string(self.login_senha)):
            st.session_state["Caption"] = "Preencha todas as informações"
        else:
            usuario = self.controller.buscar_usuario_email(self.login_email)
            if (len(usuario) != 0 and usuario[0].get_senha() == self.login_senha):
                st.session_state["Logado"] = usuario[0].get_nome_de_usuario()
                st.session_state["Pagina"] = Abas.HOME.name
            else:
                st.session_state["Caption"] = "Usuário ou senha incorretos!"
   