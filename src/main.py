#Pedro Henrique Sant Anna Hein
# RA:20.00134-7
#PH SNEAKERS

import streamlit as st
from controls.user_controller import UserController
from controls.product_controller import ProductController
from interfaces.login import AbaLogin
from interfaces.cadastro import AbaCadastro
from interfaces.inicio import AbaInicio
from models.funcoes import Funcao
from models.abas import Abas

st.set_page_config(page_title="PH SNKRS", page_icon=":fire:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

if __name__ == "__main__":

    if not(Funcao.validar_dicionario(st.session_state)):
        usercontroller = UserController()
        productcontroller = ProductController()
        Funcao.setar_ambiente_pagina_login()
    else:
        usercontroller = st.session_state["UserController"]
        productcontroller = st.session_state["ProductController"]

    if st.session_state["Pagina"] == Abas.LOGIN.name:
        pagina_atual = AbaLogin(usercontroller)

    elif st.session_state["Pagina"] == Abas.CADASTRO.name:
        pagina_atual = AbaCadastro(usercontroller)

    elif st.session_state["Pagina"] == Abas.HOME.name:
        pagina_atual = AbaInicio(usercontroller, productcontroller)

    st.session_state["UserController"] = usercontroller
    st.session_state["ProductController"] = productcontroller
