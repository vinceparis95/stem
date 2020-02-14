################################

import pandas as pd
import matplotlib.pyplot as plt


################################

# t h e  D a t a F r a m e

################################


data = "~/Desktop/databit2b.csv"


def createDataFrame(data):
    dataframe = pd.read_csv(data)
    print(dataframe.head())


createDataFrame(data)


###############################



