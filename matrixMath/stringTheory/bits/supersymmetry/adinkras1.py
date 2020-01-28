import numpy as np

#######################################

# String Theory

#######################################

#
l2 = np.array([[ 0, 1, 0,  0],
               [-1, 0, 0,  0],
               [ 0, 0, 0, -1],
               [ 0, 0, 1,  0]])

l3 = np.array([[ 0, 0, 1,  0],
               [ 0, 0, 0,  1],
               [-1, 0, 0,  0],
               [ 0,-1, 0,  0]])

r4 = np.array([[ 0, 0, 0, -1],
               [ 0, 0, 1,  0],
               [ 0,-1, 0,  0],
               [ 1, 0, 0,  0]])

l2cm = np.array([[ 0, 1, 0,  0],
                 [ 0, 0, 1,  0],
                 [-1, 0,  0, 0],
                 [ 0, 0, 0, -1]])


def isUnitary(matrix):
    tmatrix = matrix.transpose()
    i = np.matmul(matrix, tmatrix)
    print(i)
    return i


isUnitary(l2)
isUnitary(l3)
isUnitary(r4)
isUnitary(l2cm)
