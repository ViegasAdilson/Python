
# file = open("abc.txt", "w+")
# file.write("Linha1\n")
# file.write("Linha2\n")
# file.write("Linha3\n")
#
# file.seek(0, 0)
# print("Lendo linha: ")
# print(file.read())
#
# print("############")
# file.seek(0, 0)
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
#
# print("############")
# file.seek(0, 0)
# for linha in file:
#     print(linha, end="")
# file.close()

############################ Ler e escrever e apaga tudo que esta no ficheiro ###################################
# with open("abc.txt", "w+") as file:
#     file.write("linha1\n")
#     file.write("linha2\n")
#     file.write("linha3\n")
#
#     file.seek(0)
#     print(file.read())

######################################## Ler ###############################

# with open("abc.txt", "r") as file:
#     print(file.read())

######################### adiciona coisa no arqui sem apagar nada ##########################
with open("abc.txt", "a+") as file:
    file.write("Outra linha\n")
    print(file.read())