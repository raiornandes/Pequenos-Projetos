import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel('C:/Users/rafael.silva/Desktop/Alura/FIAPHandsOn/data/Frutas.xlsx')

print(df.head())

##### atribuindo valores numeros e armazenando em outra coluna #####
labelencoder = LabelEncoder()
df['CategoriasFrutas'] = labelencoder.fit_transform(df['Fruta'])

print(df.head())