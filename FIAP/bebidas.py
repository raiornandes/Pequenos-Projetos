import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score #avaliar acuracia, mede a proporção de previsões feitas pelo modelo
from sklearn.tree import DecisionTreeClassifier #modelo de arvore de decisão, pra criar regras se -> então
from sklearn.tree import plot_tree #visualizar graficamente o modelo
from sklearn.ensemble import RandomForestClassifier #modelo de floresta aleatoria, cria varias arvores, cada árvore vê uma parte diferente dos dados
from sklearn.tree import export_graphviz #exporta a arvore para o formato .dot, e melhora a visualização do grafico

from imblearn.over_sampling import SMOTE

dados = pd.read_csv('FIAPHandsOn\data\caffeine.csv')

#print(dados.shape) #quantas linhas e colunas tem
#print(dados.head())

#print(set(dados['type']))

#print(dados.isnull().sum())

x = dados.drop(columns=['type', 'drink'])
y = dados['type']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=7)

#criterion = 'gini', mede a impureza do nó, quanto maior, mais impuro está, a arvore tenta diminuir a cada divisão
dt = DecisionTreeClassifier(random_state = 7, criterion = 'gini', max_depth = 3)

dt.fit(x_train, y_train)

y_predito = dt.predict(x_test)

print(accuracy_score(y_test, y_predito))

oversample = SMOTE()
x_train_os, y_train_os, = oversample.fit_resample(x_train, y_train)

rf = RandomForestClassifier(criterion= 'entropy', n_estimators=80, max_depth = 7, random_state=7) 
rf.fit(x_train_os, y_train_os) 

estimator_rf = rf.estimators_

y_predito_random_forest = rf.predict(x_test)

print(accuracy_score(y_test, y_predito_random_forest))
print(rf.score(x_train,y_train))
print(rf.score(x_test, y_test))