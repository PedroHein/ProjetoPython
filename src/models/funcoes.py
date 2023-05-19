#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

import streamlit as st
import datetime as dt
from models.abas import Abas
from PIL import Image as img
import os
import time

class Funcao():
    @staticmethod
    def calcular_idade(data_nascimento):
        today = dt.date.today()
        idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
        return idade

    @staticmethod
    # Retorna True se campo diferete de vazio
    def validar_string(campo_str):
        return(campo_str != None and campo_str!="")

    @staticmethod
    # Retorna True se dicionario diferente de vazio
    def validar_dicionario(dict):
        return len(dict.keys()) != 0

    @staticmethod
    def validar_lista(lista):
        for valor in lista:
            if not(Funcao.validar_string(valor)):
                return False
        return True

    @staticmethod
    def limpar_tela():
        os.system('cls')

    @staticmethod
    def ajustar_imagem(path_imagem,x,y):
        imagem = img.open(path_imagem)
        return imagem.resize((x, y))

    @staticmethod
    def converter_float_str_decimal_BR(valor):
        result = str("{:.2f}".format(valor))
        return result.replace(".",",")

    @staticmethod
    def setar_ambiente_pagina_login():
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Pagina"]      = Abas.LOGIN.name
    
    @staticmethod
    def setar_ambiente_pagina_cadastro():
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Pagina"]      = Abas.CADASTRO.name
    
    @staticmethod
    def escrever_mensagem_aviso():
        if(Funcao.validar_string(st.session_state["Caption"])):
            st.error(st.session_state["Caption"], icon="⚠️")

    @staticmethod
    def exibir_spinner(tempo, msg, msg_sucesso):
        with st.spinner(msg):
            time.sleep(tempo)
            st.success(msg_sucesso)


    

