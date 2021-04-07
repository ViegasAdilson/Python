carrinho = []

carrinho.append(("produto1", 30))
carrinho.append(("produto2", 20))
carrinho.append(("produto3", 50))

print(sum([float(valor) for produto,valor in carrinho]))

