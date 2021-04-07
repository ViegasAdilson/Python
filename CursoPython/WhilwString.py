
minha_string = "O rato roeu a roupado rei de roma."

# c = 0
# nova_string = ""
# while c < len(minha_string):
#     if minha_string[c] == "r":
#         nova_string = nova_string + minha_string[c].upper()
#     else:
#         nova_string = nova_string+minha_string[c]

#     # print(minha_string[c])
#     c += 1
# print(nova_string)


c = 0
tamanho_string = len(minha_string)

while c < tamanho_string:

    conta = minha_string.count(minha_string[c])
    print(minha_string[c].lower(), conta * "*")

    c += 1

# while True:
#     minha_string = input("Digite uma frase: ")
#     tamanho_frase = len(minha_string)

#     c = 0
#     contagem_atual = 0
#     letra = ""
#     while c < tamanho_frase:
#         qtd_vezes_letra = minha_string.count(minha_string[c])
#         if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
#             letra = minha_string[c]
#             contagem_atual = qtd_vezes_letra

#         c+=1

#    print(letra, contagem_atual)
