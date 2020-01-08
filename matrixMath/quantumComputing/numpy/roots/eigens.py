import numpy as np
from matrixMath.quantumComputing.qiskit.\
    fruits.MatrixGenerator.MatrixGenerator import *

#####################################

# Eigenvalues

####################################


#####################################


# matrix spawning from QMG
print("the matrix is : \n", matrix,"\n")
print("the matrix times its transpose: \n",
      isUnitary(matrix), "\n")
print("the matrix shape is: \n",
      matrix.shape, "\n")


####################################

n = 3

# n x n I matrix * scalar λ (lambda)
i = np.eye(2)

lam = (np.dot(i, n))


######################################


# subtraction of I multiple from A matrix
print("og matrix minus the I multiple: "
      "\n", matrix - lam, "\n")


########################################


# find the determinant and difference

det = matrix
det2 = []
for x in det:
    for y in x:
        det2.append(y)

if (det2[0]*det2[2]) == 0 and (det2[1]*det2[3]) == 0:
    print("cool")

####################################


# values of det(A-λI ) = 0
