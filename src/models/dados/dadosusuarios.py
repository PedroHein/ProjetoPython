#Pedro Henrique Sant Anna Hein
# RA:20.00134-7

class DadosUsuario():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.primeironame = self.name.split()[0]

    def __str__(self) -> str:
        return f'Nome Completo:{self.name} Email:{self.email} Primeiro Nome{self.primeironame}'

    def validar_contato(self):
        return (self.name != '' and self.email != '' and self.primeironame != '')
    
    def get__nome(self):
        return self.name

    def get_email(self):
        return self.email
    
    def get_primeiro_nome(self):
        return self.primeironame

