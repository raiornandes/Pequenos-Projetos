import pandas as pd

dados = [
    {"nome": "Ana Paula", "idade": 29, "cidade": "São Paulo"},
    {"nome": "Carlos Henrique", "idade": 35, "cidade": "Belo Horizonte"},
    {"nome": "Mariana Silva", "idade": 22, "cidade": "Curitiba"},
    {"nome": "Rafael Gomes", "idade": 41, "cidade": "Salvador"},
    {"nome": "Juliana Souza", "idade": 30, "cidade": "Porto Alegre"}
]

df = pd.DataFrame(dados)

df.to_csv("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/dados.csv")