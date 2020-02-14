from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


######################################################################

# Linear Regression

#####################################################################

# import the data
data = pd.read_csv("~/Desktop/databit2b.csv")
data2 = pd.read_csv("~/Desktop/databit2btest.csv")


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
X2 = data['flight'].values.reshape(-1,1)
y2 = data['mind'].values.reshape(-1,1)

############################################

# create clone

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=9, random_state=0)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=23, random_state=0)


############################################

# train the algorithm
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred2 = regressor.predict(X_test2)

df = pd.DataFrame({'Actual': y_test2.flatten(), 'Predicted': y_pred2.flatten()})
print(df)

plt.scatter(X_test2, y_test2,  color='gray')
plt.plot(X_test2, y_pred2, color='red', linewidth=2)
plt.show()
