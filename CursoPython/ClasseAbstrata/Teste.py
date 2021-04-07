from ClasseAbstrata.ContaPopanca import ContaPoupanca
from ClasseAbstrata.ContaCorrente import ContaCorrente

cp = ContaPoupanca(1111, 22222, 0)
cp.depositar(10)
cp.sacar(5)
cp.depositar(100)
cp.verSaldo()
print("##################################################")

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)