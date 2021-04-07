
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os


caminho_pdf = "pdf"
# novo_pdf = PyPDF2.PdfFileMerger()
#
# for root, dirs, files in os.walk(caminho_pdf):
#     for file in files:
#         camininho_completo = os.path.join(root, file)
#
#         arquivo_pdf = open(camininho_completo, "rb")
#         novo_pdf.append(arquivo_pdf)
#
#
# with open(f"{caminho_pdf}/novo_arquivo.pdf", "wb") as meu_novo_pdf:
#     novo_pdf.write(meu_novo_pdf)

with open("pdf/arquivo1.pdf", "rb") as arquivo_pdf:
    leitor = PdfFileReader(arquivo_pdf)
    num_paginhas = leitor.getNumPages()
    for num_paginha in range(num_paginhas):
        escritor = PdfFileWriter()
        pagina_atual = leitor.getPage(num_paginha)
        escritor.addPage(pagina_atual)

        with open(f"novos_pdf/{num_paginha}.pdf", "wb") as novo_pdf:
            escritor.write(novo_pdf)