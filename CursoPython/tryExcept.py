def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input("Digite um numero: "))

    if numero is None:
        print("Erro: isso não é um numero")
    elif numero == 0:
        print("numero invalido")
    else:
        print(numero * 2)