import numpy as np


####################################

# a scalar

scalar = np.array([1])
print(scalar.shape)


#####################################

# a vector

vector = np.array([1, 2, 3])
print(vector.shape)


######################################

# a matrix

matrix = np.array([[1, 2, 3],
                   [1, 2, 3],
                   [1, 2, 3]])
print(matrix.shape)


#######################################

# a 3-D matrix

tensor = np.array([[[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]],
                   [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]])
print(tensor.shape)


########################################

