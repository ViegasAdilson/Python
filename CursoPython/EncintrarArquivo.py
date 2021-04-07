

import os


caminho_procura = r"C:\Users\OWNVIEGAS\Google Drive"
termo_procura = ""


conta = 0

for raiz, diretorio, arquivo in os.walk(caminho_procura):
    print(f"Arquivo: {arquivo}")
