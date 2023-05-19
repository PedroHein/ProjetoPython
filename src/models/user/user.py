#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

from models.cart.cart import Cart

class User():
    def __init__(self, contato, senha):
        self.contato = contato
        self.username = self.contato.get_email()
        self.senha = senha
        self.cart = Cart()
    
    def adicionar_compra_carrinho(self, product):
        self.cart.adicionar_product(product)
    
    def remover_compra_carrinho(self, product):
        self.cart.remover_product(product)
    
    def get_contato(self):
        return self.contato
    
    def get_nome_de_usuario(self):
        return self.username
        
    def get_senha(self):
        return self.senha

    def get_carrinho_de_compras(self):
        return self.cart
    
    def __str__(self) -> str:
        return f'Nome de Usuário:{self.username} Contato:{self.senha} Contato:{self.contato} Carrinho de Compra:{self.cart}'



    
    
    
