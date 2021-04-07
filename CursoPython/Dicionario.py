print()

perguntas = {
    "Pergunta 1":{
        "pergunta": "Quanto é 2+2? ",
        "respostas": {"a": "1", "b": "4", "c": "5"},
        "resposta_certa": "b",
    },
"Pergunta 2":{
        "pergunta": "Quanto é 3*2? ",
        "respostas": {"a": "4", "b": "8", "c": "6"},
        "resposta_certa": "c",
    },
}

print()

resposta_certa = 0
for pergunta_key, pergunta_valor in perguntas.items():
    print("\n{}: {} ".format(pergunta_key, pergunta_valor["pergunta"]))

    print("Rspostas...")
    for respostas_chave, resposta_valor in pergunta_valor["respostas"].items():
        print("{}: {}".format(respostas_chave, resposta_valor))

    resposta_user = input("Sua resposta: ")

    if resposta_user == pergunta_valor["resposta_certa"]:
        print("Voce acertou na resposta")
        resposta_certa+=1
    else:
        print("Voce errou na resposta")

qtd_pergunta = len(perguntas)
porcentagem_acerto = resposta_certa / qtd_pergunta * 100

print("Você acertou {} respostas".format(resposta_certa))
print("Sua percentagem foi de {}%".format(porcentagem_acerto))