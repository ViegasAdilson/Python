from ExercicioBanco.Conta import ContaPoupanca, ContaCorrente
from ExercicioBanco.Banco import Banco
from ExercicioBanco.Pessoas import Cliente

banco = Banco()

c1 = Cliente("Adilson", 36)
c2 = Cliente("Eanilde", 35)

cp1= ContaPoupanca(2222, 333345, 0)
cp2 = ContaPoupanca(1111, 456773, 0)
cc1 = ContaCorrente(1112, 55545565, 0)

c1.inserirConta(cp1)
c2.inserirConta(cp2)

banco.inserirCliente(c1)
banco.inserirConta(cp1)


if banco.autenticar(c1):
    c1.conta.depositar(40)
    c1.conta.sacar(20)
else:
    print("Cliente nao autenticado")


if banco.autenticar(c2):
    c2.conta.depositar(40)
    c2.conta.sacar(20)
else:
    print("Cliente nao autenticado")