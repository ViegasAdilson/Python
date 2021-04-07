from abc import ABC, abstractmethod


class Contas(ABC):

    def __init__(self, agencia, numeroConta, saldo):
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor): pass

    def detalhes(self):
        print(f"Agencia: {self.agencia},"
              f"Conta: {self.numeroConta},"
              f"Saldo: {self.saldo}")



class ContaPoupanca(Contas):

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")

            return

        self.saldo -= valor
        self.detalhes()




class ContaCorrente(Contas):
    def __init__(self, agencia, numeroConta, saldo, limite = 100):
        super().__init__(agencia, numeroConta, saldo)
        self.limite = limite


    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente")

            return
        self.saldo -= valor
        self.detalhes()
