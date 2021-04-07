

class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self.idade
    @property
    def nome(self):
        return self.nome


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None


    def inserirConta(self, conta):
        self.conta = conta


