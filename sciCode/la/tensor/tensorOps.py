import numpy as np


#################################

# Tensor Operations

#################################

# create a space

vector1 = np.array([[1,0]])
vector2 = np.array([[0,1]])
matrix1 = np.array([[0,1],[1,0]])
matrix2 = np.array([[1,0],[0,1]])


##################################

# Vector dot product

vectorDotProduct = np.vdot(vector1, vector2)


########################################

# Inner product

innerProduct = np.inner(vector1, vector2)

#########################################

# Outer product

outerProduct = np.outer(vector1, vector2)

###########################################

#Tensor dot product

tensorDotProduct = np.tensordot(matrix1, matrix2)

##################################################

# Kronecker product

kronProduct = np.kron(matrix1, matrix2)

###############################################

print("vectordot: \n", vectorDotProduct, "\n")
print("inner product:\n", innerProduct, "\n")
print("outer product: \n", outerProduct, "\n")
print("tensor dot:\n", tensorDotProduct, "\n")
print("kron: \n", kronProduct)