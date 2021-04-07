from dados import produtos, pessoas, lista

#nova_lista = map(lambda x: x*2, lista)
nova_lista = [x*2 for x in lista]
print(list(nova_lista))

# def aumenta_idade(p):
#     p["nova_idade"] = round(p["idade"]*1.20)
#     return p
#
# nomes = map(aumenta_idade, pessoas)
#
# for pessoas in nomes:
#     print(pessoas)