import numpy as np

print("\n1. Multiplying Scalars, Vectors, and Matrices", "\n")

print("##############################################\n")

print("multiplying scalars and vectors\n")
# a scalar
scalar = np.array([[3]])
print("the scalar: \n", scalar)

# a row vector
vector = np.array([[1, 2, 3]])
print("the vector: \n", vector)

# simple products
print("the product of the scalar times the vector: \n", scalar * vector)
print("the product of the vector times the vector: \n", vector * vector, "\n")

print("###########################################\n")

print("transposing and multiplying vectors\n")

# the transposed vector
vector = np.array([[1, 2, 3]])
print("the original vector: \n", vector)

trvector = np.transpose(vector)
print("the transposed vector: \n", trvector)
print("vector times transposed vector: \n", vector * trvector)
print("the dot product of the vector times the transposed vector: \n", np.dot(vector,trvector),"\n")

print("###########################################\n")

print("transposing and multiplying matrices\n")

# a 2-D matrix, or set of sets
matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print("the original matrix: \n", matrix)
trmatrix = np.transpose(matrix)
print("the transposed matrix: \n", trmatrix)
print("matrix times transposed matrix: \n", np.dot(matrix, trmatrix), "\n")


print("############################################\n")


print("2. Different Types of Matrix Multiplications\n")


# # outer product matrix multiplication
# print("the outer product of the matrix with the transposed matrix: \n", np.outer(matrix, trmatrix), "\n")
#
# # kron product matrix multiplication
# print("the kronecker product of the matrix with the transposed matrix: \n", np.kron(matrix, trmatrix), "\n")
#
# # dot product of 2 matrices
# # a 2-D matrix, or set of sets
# matrix = np.array([[1, 2, 3],
#                    [1, 1, 3],
#                    [-3, 2, 19]])
# print("original matrix: \n", matrix)
# trmatrix = np.transpose(matrix)
# print("transposed matrix: \n", trmatrix, "\n")
# print("dot product of 2 matrices: \n", np.dot(matrix, trmatrix), "\n")
# print("equivalent to (v1 * w1) + (v2 * w2*) + (v3 * w3)")

print("#############################################################")


