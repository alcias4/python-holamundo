# Protocolo smtp (simpole mail transfer protoclol)
# https://myaccount.google.com/u/1/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje["from"] = "hola mundo"  # quien va a enviar este correo
mensaje["to"] = "camiloandrade.dev@gmail.com"  # a quien mensaje
mensaje["subject"] = "este es una prueba o asuento."
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("camiloandrade.dev@gmail.com", "camilo04")
    smtp.send_message(mensaje)
