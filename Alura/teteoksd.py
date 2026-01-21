import pandas as pd

df = pd.read_csv("C:/Users/rafael.silva/Desktop/Alura/Especialista_IA/docs/produtos_vendidos_numpy.csv")

#Filtrando arquivo csv por categoria x e avaliação
"""
filtro = df[(df["Categoria"] == "Brinquedos") & (df["Avaliação"] > 2.0)]

print(filtro) """


#Método iloc, para puxar por [valor da linha : quantidade], também podemos usar [0, 3] com vírgula, que significa [valor da linha, coluna]
""" filtro = df[(df["Categoria"] == "Brinquedos") & (df["Avaliação"] > 2.0)]

eletronicos = filtro.iloc[0:3]

print(eletronicos) """

