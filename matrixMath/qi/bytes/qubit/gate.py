###########################################################

from matrixMath.qi.bytes.qubit.qubity import isUnitary
import numpy as np
import math

####################################

# t h e  G a t e s

#################################

# the X Matrix
x = np.array([[0, 1], [1, 0]])
# a flippable one state
state1 = [1,0]
flipped = np.dot(x,state1)
print(flipped)

###################################


# The Z Gate

z = np.array([[1, 0], [0, -1]])


################################



##############################

# # Dirac Hadamard
# #       | 0 } + | 1 }
# #       _____________
# #           root2
#
# # matrix   [[1, 1],
# #          [ 1,-1]])
#
#
# # create the basic matrix
# h = np.array([[1, 1],
#               [1, -1]])
# # get the matrix transpose
# htranspose = h.transpose()
# # get the haddy coefficient
# hcoefficient = 1/(math.sqrt(2))
# # dot the matrix with its transpose
# dot = np.dot(h,htranspose)
# # square the coefficient
# hcoefficientmul = hcoefficient*hcoefficient
# # print the squared coefficient with the dot
# print(hcoefficientmul*dot)


#############################################

