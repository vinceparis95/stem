

import numpy as np
from matrixMath.qi.fruits.matrixGen.MatrixGenerator import matrix


####################################

# E i g e n v a l u e

####################################

# create the matrix

x = np.array([[1, 0], [0, 1]])


######################################

# create the lamda

# set lambda to 1
l = 2

# n x n I matrix * scalar λ (lambda)
i = np.eye(2)

# dot lambda with i matrix for lam diagonal
lam = (np.dot(i, l))

# subtraction of I multiple from A matrix
x = x - lam

#######################################

# find if the determinant is eigenvalue
# det = det(A-λI)=0

def isEigen(matrix):
    det = matrix
    det2 = []
    for x in det:
        for y in x:
            det2.append(y)
    det3 = (det2[0] * det2[3]) - (det2[1] * det2[2])
    if det3 == 0:
        return det3
    elif det3 != 0:
        return det3


# simple aeigenvalue getter
def eigens2(x):
    return np.linalg.eigvals(np.array(matrix))

isEigen(x)

#####################################################

# U n i t a r i t y

#####################################################


def isUnitary(m):
      tmatrix = m.transpose()
      i = np.matmul(m, tmatrix)
      print("if i matrix, then unitary: ")
      return i

