from time import time, sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print("\nA funcao '{}' levou {}ms para ser executa.".format(funcao.__name__, tempo))
        return resultado
    return interna()

@velocidade
def demora():
    for i in range(10000):
        print(i, end="")