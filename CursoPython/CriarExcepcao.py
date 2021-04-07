class TaErradoError(Exception):
    pass

def testa():
    raise TaErradoError("Errado!")
try:
    testa()
except TaErradoError as error:
    print(f"Erro: {error}")