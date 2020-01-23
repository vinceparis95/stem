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
# print("dot of matrices: \n",
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

vector0 = np.array([[1,0]])
vector1 = np.array([[0,1]])
vector0 = np.transpose(vector0)

print (vector0.shape, vector1.shape)
print(vector0,"\n \n", vector1,"\n \n", )

tensor = np.kron(vector0,vector1)
print(tensor)

tensor2 = tensor.transpose()

print(tensor2.shape)