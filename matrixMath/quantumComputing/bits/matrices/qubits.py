
import numpy as np
import math


###########################

# Dirac state 0

array = np.array([[1,0]])

array2 = array.transpose()

print(array,"\n", array2)

# | 0 } = [[ 1,]
#          [ 0 ]]


matrix = np.array([[1,0],
                   [0,1]])


##############################

# Dirac state 1

# | 1 } = [[ 0,]
#          [ 1 ]]
matrixt = matrix.transpose()


# print(matrixt)


##############################

# Dirac | 0 } + | 1 }
#       _____________
#           root2

# matrix   [[1, 1],
#          [ 1,-1]])

# create the basic matrix
h = np.array([[1, 1],
              [1, -1]])
# get the matrix transpose
htranspose = h.transpose()
# get the haddy coefficient
hcoefficient = 1/(math.sqrt(2))
# dot the matrix with its transpose
dot = np.dot(h,htranspose)
# square the coefficient
hcoefficientmul = hcoefficient*hcoefficient
# print the squared coefficient with the dot
print(hcoefficientmul*dot)

