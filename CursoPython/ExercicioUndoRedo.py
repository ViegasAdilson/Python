
lista = []
lista_apagada = []

def desfazer():
    if not lista:
        print("Nada a desfazer")
    else:
        l1 = lista.pop()
        lista_apagada.append(l1)
        print(lista)


def refazer():
    if not lista_apagada:
        print("Nada a refazer")
    else:
        l1 = lista_apagada.pop()
        lista.append(l1)
        print(lista)


def entrada(a):
    digitado = input(a)
    return digitado



while True:
    opcoe = entrada("O que deseja? Desfazer 'd' ou Refazer 'r'ou Adicinar 'a'?: ").lower()
    if opcoe == "d":
        desfazer()
    elif opcoe == "r":
       refazer()
    elif opcoe == "a":
        tarefa = entrada("Adicione uma tarefa: ")
        lista.append(tarefa)
        print(lista)
