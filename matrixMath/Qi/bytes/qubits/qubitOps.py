###################

from matrixMath.Qi.bytes.qubits.qubitTest import isUnitary
import numpy as np
import math

###############################################

# the X Matrix

x = np.array([[1, 0], [0, 1]])

# the transpose of the X
xt = x.transpose()

print(isUnitary(x))


###############################################


#The Z Matrix

z = np.array([[1, 0], [0, -1]])
print("The Z matrix is a",
      z.shape, "matrix \n")
print("Z looks like: \n",
      z, "\n")

zt = z.transpose()
print("Zs transpose looks like: \n",
      zt, "\n")

dot = np.dot(z, zt)
print("Z times its own transpose: \n", dot)


################################


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
print("the dot of the two qubits is:"
      " \n", dot, "\n")

# these are the Imaginary coefficients
# for the og hadamard and its transpose
coh = 1/(math.sqrt(2))
coht = 1/(math.sqrt(2))

# we multiply them
cohtm = coh*coht
print("the square of one over the root of two is: "
      "\n", cohtm, "\n")

# multiply the coefficent product
# with the hadamard dot product
i = cohtm*dot
print("the cofficient product"
      "times the dot product "
      "equals the identity matrix: \n",
      i, "\n")


######################################




