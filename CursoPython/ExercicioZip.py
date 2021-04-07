
lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4]

somaLista = zip(lista1,lista2)
novalista = [x+y for x,y in zip(lista1,lista2)]
print(novalista)

# for i in range(len(lista2)):
#     novalista.append(lista1[i]+lista2[i])
# for valor in somaLista:
#     novalista.append(valor[0]+ valor[1])
# print(novalista)