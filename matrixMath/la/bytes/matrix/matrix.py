import numpy as np

####################################

# The Tensor

####################################

# create a scalar

scalar = np.array([1])
print(scalar.shape)


#####################################

# create a vector

vector = np.array([1, 2, 3])
print(vector.shape)


######################################

# create a matrix

matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print(matrix.shape)


#######################################

# create a 3-D matrix

tensor = np.array([[[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]])
print(tensor.shape)


########################################

