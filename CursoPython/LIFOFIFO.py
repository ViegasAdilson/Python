
# livro = list()
#
# livro.append("Livro 1")
# livro.append("Livro 2")
# livro.append("Livro 3")
# livro.append("Livro 4")
# livro.append("Livro 5")
#
# livro_removido = livro.pop()
# print(livro, livro_removido)

from collections import deque

fila = deque()
fila.append("joao")
fila.append("Adilson")
fila.append("Eanilde")
fila.append("Jasineide")
fila.append("Viegas")

fila.popleft()
for nome in fila:
    print(nome)