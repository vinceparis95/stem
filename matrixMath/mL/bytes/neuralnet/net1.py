from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow import keras
from tensorflow.keras import layers

######################################################################

# Neural Net 1: a Linear Regression

#####################################################################

# import the data
data = "~/Desktop/databit2.csv"

# set the column names
column_names = ['mind', 'flight', 'healing']
raw_dataset = pd.read_csv(data, names=column_names,
                          na_values = "?", comment='\t',
                           skipinitialspace=True)

data = raw_dataset.copy()

print(data)

train_dataset = data.sample(frac=0.8,random_state=0)
test_dataset = data.drop(train_dataset.index)

sns.pairplot(train_dataset[['mind', 'flight', 'healing']])

plt.show()