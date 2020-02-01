import numpy as np


####################################

# a scalar

scalar = np.array([1])
print("scalar: \n", scalar, "\n")


#####################################

# a vector

vector = np.array([1, 2, 3])
print("vector: ", vector)
print("shape: \n", vector.shape, "\n")


######################################

# a matrix

matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print("2-D matrix: \n", matrix)
print("shape: \n", matrix.shape, "\n")


#######################################

# a 3-D tensor

tensor = np.array([[[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]])
print("3-D matrix: \n", tensor)
print("shape: \n", tensor.shape, "\n")


########################################

