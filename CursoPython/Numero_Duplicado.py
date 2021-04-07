lista_inteiro = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
]
num_check = set()
primeiro_check = -1
for primeira in lista_inteiro:
    for num in primeira:
        if num in num_check:
            primeiro_check = num
            break
        num_check.add(num)
    print(primeira, primeiro_check)

# def encontra_primeiro_duplicado(param_lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1
#
#     for numero in param_lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break
#
#         numeros_checados.add(numero)
#
#     return primeiro_duplicado
#
#
# for lista_de_inteiros in lista_inteiro:
#     print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))