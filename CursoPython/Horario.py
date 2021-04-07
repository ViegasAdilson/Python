"""
Bom dia 0 - 11, Boa tarde 12 - 17 e Boa noite 18 - 23.

"""
horario = input("Digite um horario (0 - 23: ")

if horario.isdigit():
    horario = int (horario)
    if horario < 0 or horario > 23:
        print("Horario de estar entre 0 e 23.")
    else:
        if horario <= 11:
            print("Bom dia!")
        elif horario <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
else:
    print("Por favor, digite um horario entre 0 e 23. ")