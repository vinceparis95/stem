##################################

import pandas as pd
import matplotlib.pyplot as plt


################################


# Load realdata from your csv

df = pd.read_csv("~/Documents/test.csv")
print(df)


########################################


# plot the realdata from the

plot = df.plot(x='x', y='y')
plt.show()


############################



