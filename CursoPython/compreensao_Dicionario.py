l1 =[1,2,3,4,5,6,7,8]
l2 = [v*2 for v in l1]
n=4
l3 = [l1[i:i+n] for i in range(0, len(l1),n)]
print(l3)
print(l2)

lista = [
    ("chave", "valor"),
    ("chave2", "valor2")
]

d1 = {x: y for x, y in lista}
print(d1)