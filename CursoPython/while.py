# x = 0
# while x < 5:
#     y = 0
#
#     while y < 5:
#         print("{},{}".format(x,y))
#         y+=1
#
#     x+=1
#
# print("Acabou")
def entrada(a):
    num = input(a)
    return num

while True:
    num_1 = entrada("Digite um numero: ")
    operador = entrada("Digite o operador: ")
    num_2 = entrada("Digite um numero: ")

    sair = entrada("Deseja sair, [s]im ou [n]ão: ").lower()

    if not num_1.isdigit() or not num_2.isdigit():
        print("Voce precisa digitar um numero")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print("A soma de {}+{}={}".format(num_1, num_2,(num_1 + num_2)))
    elif operador == "-":
        print("A subtracao de {}-{}={}".format(num_1, num_2, num_1-num_2))
    elif operador == "*":
        print("A multiplicacao de {}-{}={}".format(num_1, num_2, num_1*num_2))
    elif operador == "/":
        print("A divisao de {}-{}={}".format(num_1, num_2, num_1/num_2))

    if sair == "s":
        print("Você saiu da calculadora")
        break