###################

import numpy as np
import math

################################


# the X Matrix

x = np.array([[1, 0],[0,1]])
print("the X Matrix is a ",
      x.shape, " matrix \n")
print("X looks like: \n", x,
      "\n")

# the transpose of the X
xt = x.transpose()
print("X's transpose looks like: "
      "\n", xt, "\n")

# the X Matrix times its transpose
# is the identity matrix
i = x*xt
print("X times its transpose is = "
      "\n ", i, "\n")


##################################


# the Hadamard Matrix


h = np.array([[1, 1],
              [1, -1]])

print("the Hadamard Matrix: "
      "\n", h, "\n")

# the transpose of the Hadamard
ht = h.transpose()
# the transpose equals the original matrix
print("the transpose of the hadamard: ",
      "\n", ht, "\n")

# do the matmul
dot = np.dot(h,ht)
print("the dot of the two matrices is:"
      " \n", dot, "\n")

# these are the coefficients
# for the og hadamard and its transpose
coh = 1/(math.sqrt(2))
coht = 1/(math.sqrt(2))

# we multiply them
cohtm = coh*coht
print("the square of one "
      "over the root of two"
      " is \n", cohtm, "\n")

# multiply the coefficent product
# with the hadamard dot product
i = cohtm*dot
print("the cofficient product"
      "times the dot product "
      "equals the identity matrix: \n",
      i, "\n")


######################################

