import numpy as np


mat = np.array([1,0,0,1])
mat2= mat.reshape((2,2))
print("matrix:\n", mat2, "\n")
print("matrix shape:\n", mat2.shape, "\n")

eigs = np.linalg.eigvals(mat2)

print("the eigens:\n", eigs, "\n")