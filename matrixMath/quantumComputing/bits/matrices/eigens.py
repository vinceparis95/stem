import numpy as np
from matrixMath.quantumComputing.toys.matrixGenerator.MatrixGenerator import matrix

#####################################

# Eigenvalues

####################################


# matrix spawning from QMG
print("the matrix is : \n", matrix,"\n")
# print("the matrix times its transpose: \n",
#       isUnitary(matrix), "\n")
# print("the matrix shape is: \n",
#       matrix.shape, "\n")


####################################

n = -1
print("lamda: \n", n, "\n")

# n x n I matrix * scalar λ (lambda)
i = np.eye(2)
print("the i matrix: \n", i, "\n")

lam = (np.dot(i, n))
print("i multiplied with lamda: \n", lam, "\n")


###############################################


# subtraction of I multiple from A matrix
matrix = matrix - lam
print("og matrix minus the I multiple: "
      "\n", matrix, "\n")


############################################


# find the determinant and difference
# # det = det(A-λI)=0
# det = matrix
# det2 = []
# for x in det:
#     for y in x:
#         det2.append(y)
# print(det2)

# def isEigen(matrix):
#     det = matrix
#     det2 = []
#     for x in det:
#         for y in x:
#             det2.append(y)
#     if (det2[0]*det2[2]) - (det2[1]*det2[3]) == 0:
#         print(n, "\n : the eigenvalue")
#         print((det2[0]*det2[2]) - (det2[1]*det2[3]))


# print(isEigen(matrix))
# print("eigenvalues: ", np.linalg.eigvals(np.array(matrix)))



####################################


# values of det(A-λI ) = 0
