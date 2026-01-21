import pandas as pd
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#mpl.rc('axes', labelsize=14)
#mpl.rc('xtick', labelsize=12)
#mpl.rc('ytick', labelsize=12)

dataset = pd.read_csv("C:/Users/rafael.silva/Desktop/Alura/FIAPHandsOn/data/housing.csv")

######## analisando com pandas ########

#print(dataset.head())
#print(dataset.shape)
#print(dataset.info())
#print(set(dataset["ocean_proximity"]))
#print(dataset["ocean_proximity"].value_counts())
#print(dataset.describe())

######## histograma com matplot ########

#print(dataset.hist(bins=50, figsize=(20,15)))
#plt.show()

#dataset_train, dataset_test = train_test_split(dataset, test_size = 0.2, random_state = 7)
#print(len(dataset_train), "treinamento +", len(dataset_test), "teste")

#dataset["income_cat"] = np.ceil(dataset["median_income"] / 1.5)
#dataset["income_cat"].where(dataset["income_cat"] < 5, 5.0, inplace=True)
#dataset["income_cat"] = pd.cut(dataset["median_income"],
#                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
#                               labels=[1, 2, 3, 4, 5])
#dataset["income_cat"].value_counts()
#print(dataset["income_cat"].hist())