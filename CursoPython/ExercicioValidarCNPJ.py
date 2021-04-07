import re

cpnj = "04.252.011/0001"

regressivo = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
regressivo1 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
b = []
c = []


def remover_caracter(valor):
    valor = valor.replace("/", "")
    valor = valor.replace(".", "")
    valor = valor.replace("-", "")
    return valor


def calcula_Digito(valor):
    formula = 11 - (valor % 11)
    return formula


def listagem(valor, valor1):
    resultado = zip(valor1, valor)
    l1 = list(resultado)
    ex = [(x * r) for x, r in l1]
    cpnj_resultado = sum(ex)
    return cpnj_resultado


cpnj_removido = remover_caracter(cpnj)
cpnj_removido = list(cpnj_removido)
for i in cpnj_removido:
    i = int(i)
    b.append(i)
formula_primeiro = calcula_Digito(listagem(regressivo, b))
formula_primeiro = str(formula_primeiro)
penultimo_digito = cpnj + "-" + formula_primeiro
print(penultimo_digito)

cpnj_removido1 = remover_caracter(penultimo_digito)
cpnj_removido1 = list(cpnj_removido1)
for j in cpnj_removido1:
    j = int(j)
    c.append(j)
formula_segundo = calcula_Digito(listagem(regressivo1, c))
formula_segundo = str(formula_segundo)

ultimo_digito = cpnj + "-" + formula_segundo
print(ultimo_digito)
