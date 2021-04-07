secreta = "perfume"
digitada = []


while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('So pode digitar uma letra.')
        continue

    digitada.append(letra)
    
    if letra in secreta:
        print('Acertou! a letra "{}" existe na palavra secreta'.format(letra))
    else:
        print('A letra "{}" nao existe na palavra secreta'.format(letra))
        digitada.pop()
    secreta_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitada:
            secreta_temporario += letra_secreta
        else:
            secreta_temporario += '*'

