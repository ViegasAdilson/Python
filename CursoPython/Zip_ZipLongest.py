from itertools import zip_longest

#cidades = ["Trindade", "Guadalupe", "Santana", "Neves", "Lemba"]

#distrito = ["Me-zochi", "Lobata", "Cantagalo"]
cidades = [1,2,3,4,5,5]
distrito = [1,2,3,4,5,]
distrito_cidade = zip(distrito, cidades)

#print(dict(distrito_cidade))
print(list(distrito_cidade))

distrito_cidade = zip_longest(distrito, cidades, fillvalue="Distrito")

print(list(distrito_cidade))