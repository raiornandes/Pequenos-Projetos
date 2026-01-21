import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dados = pd.read_excel('C:/Users/rafael.silva/Desktop/Alura/FIAPHandsOn/data/gaf_esp.xlsx')

#print(dados.head())
#print(dados.describe())

### visualizando grafico com matplotlib, comparando
#dados.plot.scatter(x='Comprimento do Abdômen', y='Comprimento das Antenas')
#plt.show()

x = dados[['Comprimento do Abdômen', 'Comprimento das Antenas']]
y = dados['Espécie']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=42)
#print("Total base de treino: ", len(x_train))
#print("Total base de teste: ", len(y_test))

modelo_classificador = KNeighborsClassifier(n_neighbors=3)
modelo_classificador.fit(x_train, y_train)

print(modelo_classificador())