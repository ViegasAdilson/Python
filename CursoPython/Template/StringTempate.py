from string import Template
from datetime import datetime
from Template.dados import meu_email, minha_senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


with open("Template.html", "r")as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.safe_substitute(nome="Adilson Viegas", data=data_atual)

msg = MIMEMultipart()
msg["from"] = "Adilson Viegas"
msg["to"] = meu_email
msg["subject"]= "Atencao: este é um email de teste"


corpo = MIMEText(corpo_msg, "html")
msg.attach(corpo)

with open("imagem.jpg", "rb") as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print("email enviado com sucesso")
