##################################

import pandas as pd
import matplotlib.pyplot as plt


################################


# Load real_data from your csv

df = pd.read_csv("~/Documents/test.csv")
print(df)


########################################


# plot the real_data from the

plot = df.plot(x='x', y='y')
plt.show()


############################



