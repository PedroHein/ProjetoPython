#Pedro Henrique Sant Anna Hein
#RA:20.00134-7

import streamlit as st

class UserController():
    def __init__(self):
        self._lista_usuarios_cadastrados = []

    def buscar_usuario_email(self, email_usuario):
        for i, usuario in enumerate(self._lista_usuarios_cadastrados):
            if(email_usuario == usuario.username):
                return [usuario, i]
        return []
    
    def adicionar_usuario(self, novo_usuario):
        self._lista_usuarios_cadastrados.append(novo_usuario)

    def reinserir_usuario(self, posicao, novo_usuario):
        self._lista_usuarios_cadastrados.insert(posicao, novo_usuario)
    
    def remover_usuario(self, usuario):
        posicao_user = self._lista_usuarios_cadastrados.index(usuario)
        self._lista_usuarios_cadastrados.remove(usuario)
        return posicao_user
    
    def update_usuario_compra(self, produto):
        lista_info_usuario = self.buscar_usuario_email(st.session_state["Logado"])
        self._lista_usuarios_cadastrados.remove(lista_info_usuario[0])
        lista_info_usuario[0].adicionar_compra_carrinho(produto)
        self._lista_usuarios_cadastrados.insert(lista_info_usuario[1], lista_info_usuario[0])
    
    def update_usuario_venda(self, produto):
        lista_info_usuario = self.buscar_usuario_email(st.session_state["Logado"])
        self._lista_usuarios_cadastrados.remove(lista_info_usuario[0])
        lista_info_usuario[0].remover_compra_carrinho(produto)
        self._lista_usuarios_cadastrados.insert(lista_info_usuario[1], lista_info_usuario[0])
    
                
