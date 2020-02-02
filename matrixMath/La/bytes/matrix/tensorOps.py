import numpy as np
import math
#"\n"

###############################

# the Dot product

################################
# x = 1
# y = 2
# z = 3
#
# # the vector
#
# vector = np.array([[x, y, z]])
# print("original vector: \n", vector)
#
#
# ####################################
#
#
# # transposing the vector
#
# trvector = np.transpose(vector)
# print("transposed vector: \n", trvector)
#
#
# ########################################
#
#
# # dot of the vectors
#
# print("dot of vectors: \n",
#       np.dot(vector, trvector), "\n")
#
#
# #######################################
#
#
# # create a matrix
#
# matrix = np.array([[ 1,  1,  1,  1],
#                    [-1,  1, -1,  1],
#                    [-1, -1,  1,  1],
#                    [ 1, -1,  -1, 1]])
# print("original matrix: \n", matrix)
#
#
# #########################################
#
# # transpose the matrix
#
# trmatrix = np.transpose(matrix)
# print("the transposed matrix: \n", trmatrix)
#
#
# #############################################
#
#
# # dot the matrix with its transpose
#
# dot = np.dot(matrix, trmatrix)
# print("dot of qubit: \n",
#       dot, "\n")
#
# coh = 1/(math.sqrt(4))
# coht = coh
# cohtm = coh*coht
# # cohtmb = cohtm*cohtm
# i = np.dot(cohtm, dot)
# print("i: \n", i, "\n")


##########################################

# the Tensor Product

##########################################


# build two vectors
vector0 = np.array([[1,0]])
vector1 = np.array([[0,1]])
vector0 = np.transpose(vector0)
print (vector0.shape, vector1.shape)
print("the vectors:\n", vector0,"\n", vector1,"\n \n")

# give their matrix product
tensor = np.kron(vector0,vector1)
print("the matrix product:\n", tensor, "\n")
print(tensor.shape,"\n \n", )

# create the x gate
matrix = np.array([[0,1], [1,0]])
print("the x matrix:\n", matrix, "\n")
print(matrix.shape, "\n \n")

# give inner for the 0 vector and the x matrix
print("the inner product of the x gate "
      "and the state 1 vector:\n",
      np.dot(matrix,vector0))


######################################################