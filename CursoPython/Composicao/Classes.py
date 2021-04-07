class Clientes:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def inserirEndereco(self, cidade, distrito):
        self.endereco.append(Enderecos(cidade, distrito))

    def listarEndereco(self):
        for ender in self.endereco:
            print(ender.cidade, ender.distrito)


class Enderecos:
    def __init__(self, cidade, distrito):
        self.cidade = cidade
        self.distrito = distrito




c1 = Clientes("Adilson", 35)
c1.inserirEndereco("Trindade", "Me-zochi")
print(c1.nome, c1.idade)
c1.listarEndereco()

print()

c2 = Clientes("Benvindo", 56)
c2.inserirEndereco("Caixao Grand", "Me-zochi")
print(f"{c2.nome} tem {c2.idade} de idade")
c2.listarEndereco()