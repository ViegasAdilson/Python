
"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print("abrir arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("retornando arquivo")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando arquivo")
        self.arquivo.close()

with Arquivo("abc.txt", "w") as arquivo:
    arquivo.write("Alguma coisa\n")

"""
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print("Abrir arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()

with abrir("abc.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")