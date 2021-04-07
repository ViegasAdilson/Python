"""
from datetime import datetime
nome = 'Adilson'
altura = 1.72
idade = 37
peso = 96
data_actual = datetime.now()
data_actual=data_actual.strftime("%Y")
ano = int(data_actual) - idade
imc = peso/altura**2

print('')
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc: .2f}.')
print(f'{nome} nasceu em {ano}.')
"""

"""
texto = 'O python é fixe'
letra_nova = ''
for letra in texto:
    if letra_nova in texto:
        letra_nova = letra_nova + letra

    print(letra_nova)
    #print('A letra {} {}'.format(letra, (texto.count(letra)*"*")))
"""

string = "O Brasil é o pais de fotebol, o Brasil é penta"

lista_1 = string.split(' ')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor.lower())

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'{palavra} {contagem}')
