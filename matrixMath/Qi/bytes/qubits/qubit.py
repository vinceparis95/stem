
import numpy as np
import math

##############################

# The Qubit

###########################

# Dirac State 0
# | 0 } = [[ 1,]
#          [ 0 ]]

array = np.array([[1,0]])
array2 = array.transpose()
print(array,"\n", array2)

matrix = np.array([[1,0],
                   [0,1]])


##############################

# Dirac State 1
# | 1 } = [[ 0,]
#          [ 1 ]]
matrixt = matrix.transpose()


# print(matrixt)


#############################################