import csv

with open("clientes.csv", "r") as arquivo:
    dados = csv.reader(arquivo)

    for dado in dados:
        print(dado[0], dado[1], dado[2], dado[3])

print("#############################")

with open("clientes.csv", "r") as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

    for dado in dados:
        print(dado["Nome"], dado["Sobrenome"], dado["E-mail"], dado["Telefone"])


print("#############################")

with open("Cliente2.csv", "w") as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado["Nome"],
                dado["Sobrenome"],
                dado["E-mail"],
                dado["Telefone"]
            ]
        )