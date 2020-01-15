import numpy as np
from matrixMath.quantumComputing.toys.matrixGenerator.MatrixGenerator import matrix

#####################################

# Eigenvalues

####################################


# spawn matrix from MatrixGenerator
# print("the matrix is : \n", matrix,"\n")
# print("the matrix times its transpose: \n",
#       isUnitary(matrix), "\n")
# print("the matrix shape is: \n",
#       matrix.shape, "\n")


####################################
#
#
# # the Lambda
#
# # set lambda to 1
# l = 1
# print("lamda: \n", l, "\n")
#
# # n x n I matrix * scalar λ (lambda)
# i = np.eye(2)
# print("the i matrix: \n", i, "\n")
#
# # dot lambda with i matrix for lam diagonal
# lam = (np.dot(i, l))
# print("i multiplied with lamda: \n", lam, "\n")
#
#
# # subtraction of I multiple from A matrix
# matrix = matrix - lam
# print("U matrix minus the Lam multiple: "
#       "\n", matrix, "\n")


###########################################


# The Eigenvalue


# find the determinant and difference
# # det = det(A-λI)=0
# def isEigen(matrix):
#     det = matrix
#     det2 = []
#     for x in det:
#         for y in x:
#             det2.append(y)
#     print("the vectorized matrix: \n", det2, "\n")
#     det3 = (det2[0] * det2[2]) - (det2[1] * det2[3])
#     if det3 == 0:
#         print("\n Lambda (", l, ") is an eigenvalue")
#         return det3
#     elif det3 != 0:
#         print("Lambda (", l, ") is not an eigenvalue")
#         return det3

def eigens2(matrix):
    return np.linalg.eigvals(np.array(matrix))

# print(isEigen(matrix))
print("\neigenvalues: ", np.linalg.eigvals(np.array(matrix)))


#########################################################


# values of det(A-λI ) = 0
