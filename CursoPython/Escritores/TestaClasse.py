from Escritores.Classes import  Escritor
from Escritores.Classes import Caneta
from Escritores.Classes import MaquinaEscrever

escritor = Escritor("Adilson")
caneta = Caneta("Bic")
maquina = MaquinaEscrever()
# print(escritor.nome)
# print(caneta.marca)
#maquina.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()