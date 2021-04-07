#############################Split#########################################
# striing = "O Brasil é o pais de fotebol, o Brasil é penta"
#
# lista_1 = striing.split(' ')# ['O', 'Brasil', 'é', 'o', 'pais', 'de', 'fotebol,', 'o', 'Vrasil', 'é', 'penta']
# lista_2 = striing.split(',')# ['O Brasil é o pais de fotebol', ' o Vrasil é penta']
#
# print(lista_1)
# print(lista_2)
#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print("{} aparece {} ".format(palavra,contagem))

####################################################### Join #######################################################

# string = "o Brasil é penta"
# lista = string.split(' ')# ['o', 'Brasil', 'é', 'penta']
# string_2 = ','.join(lista)# o,Brasil,é,penta
#
# print(string_2)

###################################################Enumerate####################################################

lista = ["Luis", "Joao", "Maria"]

for indice, nome in enumerate(lista):
    print(indice, nome)
