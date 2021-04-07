from itertools import groupby, tee
alunos = [
    {"nome": "Adilson", "nota": "A"},
    {"nome": "Leticia", "nota": "B"},
    {"nome": "Fabricio", "nota": "C"},
    {"nome": "Rosemery", "nota": "D"},
    {"nome": "Joana", "nota": "A"},
    {"nome": "Eduardo", "nota": "C"},
    {"nome": "Joao", "nota": "B"},
    {"nome": "Anderson", "nota": "A"},
    {"nome": "Jose", "nota": "B"},
]

ordena = lambda item: item ["nota"]
alunos.sort(key = ordena)

alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1 , va2 = tee(valores_agrupados)

    print("Agrupamento: {}".format(agrupamento))

    for aluno in va1:
        print(aluno)
    quantidade = len(list(va2))
    print("{} alunos tiraram a nota {}".format(quantidade, agrupamento))
    print()