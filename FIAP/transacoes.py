import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier #modelo de ML classificação
#accuracy para avaliação do modelo, matriz de confusão
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler


dados = pd.read_csv('FIAPHandsOn/data/card_transdata.csv')

#print(dados.head(3))

#verificando e tratando inconsistencias
#print(dados.isnull().sum())
#dados = dados.dropna()
#dados.describe()

x = dados[['distance_from_home','ratio_to_median_purchase_price', 'online_order']]
y = dados['fraud']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify = y, random_state = 7)

#normalizando
scaler = MinMaxScaler()
scaler.fit(x_train)

x_train_escalonado = scaler.transform(x_train)
x_test_escalonado = scaler.transform(x_test)

print(x_train)

erro = []

for i in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train_escalonado, y_train)
    pred_i = knn.predict(x_test_escalonado)
    erro.append(np.mean(pred_i != y_test))

modelo_classificador = KNeighborsClassifier(n_neighbors=5)

#fazendo o treinamento do modelo de ml
modelo_classificador.fit(x_train_escalonado, y_train)

y_predito = modelo_classificador.predict(x_test_escalonado)

#   print('Score Treino: {:.4f}'.format(modelo_classificador.score(x_train,y_train)))
#print('Score Teste: {:.4f}'.format(modelo_classificador.score(x_test,y_test)))

matriz_confusao = confusion_matrix(y_test, y_predito)
plt.figure(figsize = (8,4))
sns.heatmap(matriz_confusao, annot = True, fmt = "d", cmap = "Blues")
plt.xlabel("Predição");
plt.ylabel("Dados Reais");

print(classification_report(y_test, y_predito))