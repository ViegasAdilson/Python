num1 = input("Digite um numero inteiro: ")

if num1.isdigit():
    if int(num1) % 2 == 0:
        print("O {} introduzidos é par".format(num1))
    else:
        print("O {} introduzido é impar".format(num1))
else:
    print("o valor que digitou não é um numero")

