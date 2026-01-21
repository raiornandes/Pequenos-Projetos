import openai
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

emails = ("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/emails.txt")
leitura = []

with open (emails, "r", encoding="utf-8") as arquivo:
        leitura = [linha.strip() for linha in arquivo]

def resumidor_de_emails(lista_de_emails):
    lista_de_resumos = []

    for email in lista_de_emails:
        prompt=f"Resuma este email em **uma única linha**, apenas o **intuito do email**, sem comentários adicionais: {email}"
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                 {"role": "system", "content": "Sua função é resumir emails, sem perder o contexto."},
                 {"role": "user", "content": prompt}
            ]
        )
        resposta_texto = response.choices[0].message.content.strip()
        lista_de_resumos.append(resposta_texto)

    return lista_de_resumos

resumos = resumidor_de_emails(leitura)

caminho_resumos = ("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/resumos_emails.txt")

with open(caminho_resumos, "w", encoding="utf-8") as doc:
     lista = "\n".join(resumos)
     doc.write(lista)