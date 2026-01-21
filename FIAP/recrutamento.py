import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_excel('FIAPHandsOn/data/Recrutamento.xlsx')

#print(data.head())
#print(data.shape)
#print(data.isnull().sum())

data.fillna({'salary': 0}, inplace=True)
print(data.isnull().sum())

dummy_hsc_s=pd.get_dummies(data['hsc_s'], prefix='dummy')
dummy_degree_t=pd.get_dummies(data['degree_t'], prefix='dummy')

data_coeded = pd.concat([data,dummy_hsc_s,dummy_degree_t],axis=1)
data_coeded.drop(['hsc_s','degree_t','salary'],axis=1, inplace=True)

x = data_coeded[['ssc_p', 'hsc_p', 'degree_p', 'workex', 'mba_p']]
y = data_coeded['status']