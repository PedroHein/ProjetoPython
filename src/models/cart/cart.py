#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

class Cart():

    def __init__(self):
        self.products = []
    
    def adicionar_product(self, produto_novo):
        for product in self.products:
            if(product["Produto"] == produto_novo):
                product["Quantidade"] += 1
                return
        
        self.products.append({"Produto":produto_novo, "Quantidade": 1})
        return
    
    def remover_product(self, produto):
        for i, item in enumerate(self.products):
            if(item["Produto"] == produto):
                if(item["Quantidade"]==1):
                    self.products.pop(i)
                else:
                    item["Quantidade"] -= 1

    def qtde_total_products(self):
        qtde_total = 0
        for product in self.products:
            qtde_total += product["Quantidade"]

        return qtde_total
    
    def get_products(self):
        return self.products

    def calcular_valor_total(self):
        total = 0
        for product in self.products:
            total += (product["Produto"].get_valor())*product["Quantidade"]
        return total
    
    def retornar_qtd_product(self, product_procurado):
        for product in self.products:
            if(product["Produto"] == product_procurado):
                return product["Quantidade"]
        return 0

    def __str__(self):
        return f'Itens:{self.products}'