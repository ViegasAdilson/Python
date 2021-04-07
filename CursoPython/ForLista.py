
texto = "Python"
#
for letra in texto:
    print(letra)


# lista = ["A", "B", "C", "D", "E", 10.5]
# print(lista[3])
# print(lista[::2])#[inici : fim : salto]
#
# print(lista[::-1]) # inverter a lista

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
l1.insert(0, "Banana")
l2.extend(l1)
l1.extend("a")#adiciona no ultimo indice
l1.append("B")#adiciona no ultimo indice
print("lista 1",l1)
l1.pop()#elimina o ultimo indice
del(l1[0])
#print(l3)
print(l2)
print(l1)