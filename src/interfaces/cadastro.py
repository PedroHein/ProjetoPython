#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

import streamlit as st
from models.dados.dadosusuarios import DadosUsuario
from models.user.user import User
from models.funcoes import Funcao
import datetime as dt

class AbaCadastro:
    def __init__(self, controller) -> None:
        self.controller = controller

        data_min = dt.date(1900, 1, 1)
        data_max = dt.date.today() 
        
        st.title("Cadastre-se")
        

        col1, col2 = st.columns(2)
        with col1:
            self.nome_contato = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo", value="")
        with col2:
            self.email_contato = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value="")
            
        self.senha_usuario = st.text_input(label="Senha", placeholder ="Digite uma senha", value="",  type='password')
        self.senha_usuario_check = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value="", type='password')

        self.lista_campos_cadastro = [self.nome_contato, self.email_contato, self.senha_usuario, self.senha_usuario_check]

        col1, col2 = st.columns([8, 1])

        with col1:
            self.btt_confirmar_cadastro = st.button(
                label="Confirmar Cadastro", 
                    on_click=self.autenticar_cadastro
            )

            Funcao.escrever_mensagem_aviso()

        with col2:
            self.btt_voltar_login = st.button(
                    label='Voltar',
                    on_click=Funcao.setar_ambiente_pagina_login
                    )
    
    def autenticar_cadastro(self):
        if not self.checar_lista_cadastro():
                st.session_state["Caption"] = "Preencher todos os campos!"
        elif self.senha_usuario != self.senha_usuario_check:
                st.session_state["Caption"] = "As senhas não conferem!"
        elif len(self.controller.buscar_usuario_email(self.email_contato))!=0:
                st.session_state["Caption"] = "Usuário já Cadastrado!"
        else:
            contato_user = DadosUsuario(name=self.nome_contato, email=self.email_contato)
            user_novo = User(contato_user, self.senha_usuario)
            self.controller.adicionar_usuario(user_novo)
            Funcao.setar_ambiente_pagina_login()

        
    def checar_lista_cadastro(self):
        for campo in self.lista_campos_cadastro:
            if not Funcao.validar_string(campo):
                return False
        return True
