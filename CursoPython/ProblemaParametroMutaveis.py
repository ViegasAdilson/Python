

def lista_Cliente (cliente_iteraveis, lista = None):
    if lista is None:
        lista = []
    lista.extend(cliente_iteraveis)
    return lista


cliente1 = lista_Cliente(["Adilson", "Eanilde", "Jasineide"])
cliente2 = lista_Cliente(["Benvindo", "Paula", "Remy"])
cliente3 = lista_Cliente(["Manuel"])

print(cliente1)
print(cliente2)
print(cliente3)