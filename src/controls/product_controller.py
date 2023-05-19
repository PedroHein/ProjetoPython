#Pedro Henrique Sant Anna Hein
#RA:20.00134-7

from models.products.product import Product

class ProductController():
    def __init__(self):
        self._lista_itens_cadastrados = [
            Product(nome="Nike Dunk Black and White", descricao="", valor=1199.99, imagem="assets/tenis1.jpg"),
            Product(nome="Nike Dunk Low Next Nature Blue", descricao="", valor=899.99, imagem="assets/tenis2.jpg"),
            Product(nome="Nike Dunk Low Next Nature", descricao="", valor=899.99, imagem="assets/tenis3.jpg"),
            Product(nome="Nike Dunk Low Vast Grey", descricao="", valor=999.99, imagem="assets/tenis4.jpg"),
            Product(nome="Nike Dunk Low LA Dodgers", descricao="", valor=999.99, imagem="assets/tenis5.jpg"),
            Product(nome="Nike Dunk Low Court Purple", descricao="", valor=1399.99, imagem="assets/tenis6.jpg"),
            Product(nome="Nike Dunk Low Pro Black x Neckface", descricao="", valor=1499.99, imagem="assets/tenis7.jpg"),
            Product(nome="Nike SB Dunk Low Strangelove", descricao="", valor=9999.99, imagem="assets/tenis8.jpg"),
            Product(nome="Nike SB Dunk Low Elephant", descricao="", valor=1999.99, imagem="assets/tenis9.jpg"),
        ]

    def get_item_pelo_nome(self, nome):
        for item in self._lista_itens_cadastrados:
            if item.get_nome() == nome:
                return item
        return None

    def gerar_lista_nomes_produtos(self):
        lista_retorno=[]
        for item in self._lista_itens_cadastrados:
            lista_retorno.append(item.get_nome())
        return lista_retorno


    def get_lista_itens_cadastrados(self):
        return self._lista_itens_cadastrados
    
    def montar_lista_nomes_itens(self):
        lista=[]
        for item in self._lista_itens_cadastrados:
            lista.append(item.get_nome())
        return lista
