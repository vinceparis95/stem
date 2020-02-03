import numpy as np
import math

###################################


# T e n s o r  O p e r a t i o n s


##################################
# the Dot Product
############################

# create the vector

vector = np.array([[1,0]])

#############################

# transpose the vector

trvector = np.transpose(vector)

###############################

#dot the vectors

np.dot(vector, trvector)


################################
# the Tensor Product
################################


# build two vectors
vector = np.array([[0,1]])
vector2 = np.array([[1,0]]).transpose()

######################################

# give their tensor product
tensor = np.kron(vector,vector2)

#################################

# give their dot product
dot= np.dot(vector,vector2)
print(dot)


##########################