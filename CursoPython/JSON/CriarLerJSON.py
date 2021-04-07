
from JSON.dado import *
import json

# Converter dicionario Pytho em JSON

# with open("Cliente.json", "w") as arquivo:
#     json.dump(clientes_dicionario, arquivo, indent=4)# Converter dicionario Pytho em JSON



# Ler de JSON para Python

with open("Cliente.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)