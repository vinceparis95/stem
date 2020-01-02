# import numpy, a pythonic math package jawn
import numpy as np


######################################

# 1. Scalars (0-D tensors)

# create a numpy array
numpyArray = np.array([])
print("empty list: ", numpyArray, "\n")

# adding a single number scalar
scalar = np.append(numpyArray, 3)
print("scalar value: ", scalar, "\n")


########################################

# 2. Vectors (1-D tensors)

# a vector, or a set of numbers
vector = np.array([1, 2, 3])
print("vector: ", vector)
print("shape: \n", vector.shape, "\n")

# multiply the vector with the scalar
print("vector times scalar = ", vector * scalar, "\n")


#######################################################

# 3. Matrices (2-D tensors)

# a 2-D matrix, or set of sets
matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print("2-D matrix: \n", matrix)
print("shape: \n", matrix.shape, "\n")

# a higher dimensional tensor
# like a 3-D matrix:
tensor = np.array([[[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]])
print("3-D matrix: \n", tensor)
print("shape: \n", tensor.shape, "\n")


########################################################

