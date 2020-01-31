import numpy as np
from matrixMath.quantumComputing.bits.matrices.unitaries import isUnitary


#################################################


#################################################


# a cnot on a three qubit system


matrix1 = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1],])



isUnitary(matrix1)


oneonezero = np.array([[1, 0, 0, 0, 0, 0, 0, 0]]).transpose()

print(oneonezero)

print(np.dot(matrix1,oneonezero))

