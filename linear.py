# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('canada_per_capita_income.csv')
df

df.isnull().sum()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel('year')
plt.ylabel('per capita income (US$)')
plt.scatter(df.year,df["per capita income (US$)"],color='red',marker='+')

area = df.drop('per capita income (US$)',axis=1)
price = df['per capita income (US$)']

reg = linear_model.LinearRegression()
reg.fit(area,price)

accuracy_score = reg.score(area,price)
accuracy_score

reg.predict([[2016]])