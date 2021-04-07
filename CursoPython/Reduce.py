from dados import produtos, pessoas, lista

from  functools import reduce

soma_preco = reduce(lambda acumulador, produto: produto["preco"] + acumulador, produtos, 0)

print(round(soma_preco, 2))