from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

######################################################################

# Linear Regression

#####################################################################

# import the data
data = pd.read_csv("~/Desktop/databit2b.csv")

# set the column names
print(data.shape)
print(data.describe())

data.plot(x='flight', y='mind', style='o')
plt.title('test')
plt.xlabel('flight')
plt.ylabel('mind')
plt.show()

X = data['flight'].values.reshape(-1,1)
y = data['mind'].values.reshape(-1,1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=23, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train) #training the algorithm

#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()