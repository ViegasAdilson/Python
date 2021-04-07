
secreto = "perfume"
digitado = []

chances = 3

while True:
    if chances <= 0:
        print("Você perdeu!!!")
        break

    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Isso nao vale, digite apenas uma letra")
        continue
    digitado.append(letra)

    if letra in secreto:
        print("Voce acertou a letra {} existe na palavra secreta".format(letra))
    else:
        print("A letra '{}' nao existe na palavra secreta".format(letra))
        digitado.pop()
        chances-=1

    secreta_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreta_temporario = secreta_temporario + letra_secreta
        else:
            secreta_temporario+="*"
    if secreta_temporario == secreto:
        print("Voce venceu, a palavra secreta era {}".format(secreto))
        break
    else:
        print("A palavra secreta esta assim: {}".format(secreta_temporario))
    

    print("Voce ainda tem {} chances".format(chances))