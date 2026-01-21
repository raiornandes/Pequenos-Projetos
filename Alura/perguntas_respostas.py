import openai
import pandas as pd
import os
import time
from dotenv import load_dotenv
 
load_dotenv("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

caminho = 'Especialista_IA/docs/perguntas_e_respostas.csv'
perguntas= []

with open(caminho, "r", encoding="utf-8") as arquivo:
    perguntas = [linha.strip() for linha in arquivo]

respostas = []

for pergunta in perguntas:
    prompt = f"Responda de forma clara e concisa a seguinte pergunta:\n{pergunta}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente especialista em ciências."},
            {"role": "user", "content": prompt}
        ]
    )
    
    resposta_texto = response.choices[0].message.content.strip()
    respostas.append(resposta_texto)
    
    time.sleep(1)

df = pd.DataFrame({
    "Pergunta": perguntas,
    "Resposta": respostas
})

print(df.to_string(index=False))

caminho_csv = "C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/perguntas_e_respostas.csv"
df.to_csv(caminho_csv, index=False, encoding="utf-8-sig", quotechar='"')

print(f"\nCSV criado com sucesso em: {caminho_csv}")