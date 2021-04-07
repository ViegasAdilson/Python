from Associacao.Classes import CarrinhoCompra, Produto

p1 = Produto("Camisa", 50)
p2 = Produto("Telefone", 300)
p3 = Produto("Portatil", 1300)

carrinho = CarrinhoCompra()

carrinho.inserirProduto(p1)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)

carrinho.listarProduto()
print(carrinho.somaTotal())