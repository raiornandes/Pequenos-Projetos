import pandas as pd
from dotenv import load_dotenv
import os
import openai

load_dotenv("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

reviews = []
df = pd.read_csv('C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/reviews.csv')

reviews = df['reviewText'].tolist()

analises = []

for review in reviews:
    prompt = f"Classifique o sentimento do review como apenas uma das palavras: Positivo, Neutro ou Negativo. Responda apenas com a palavra, sem explicações. Review: {review}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0.1,
        messages=[
            {"role": "system", "content": "Você é um analisador de sentimentos."},
            {"role": "user", "content": prompt}
        ]
    )

    resultado_analise = response.choices[0].message.content.strip()
    analises.append(resultado_analise)

df = pd.DataFrame({
    "Dados": reviews,
    "Analises": analises
})

caminho_csv = "C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/analises.csv"
df.to_csv(caminho_csv, index=False, encoding="utf-8", quotechar='"')

print(f"\nCSV criado com sucesso em: {caminho_csv}")