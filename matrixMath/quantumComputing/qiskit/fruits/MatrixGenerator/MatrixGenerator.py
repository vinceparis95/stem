
######################################

from qiskit import \
    QuantumCircuit, QuantumRegister, \
    ClassicalRegister, execute, Aer, \
    IBMQ, BasicAer

import numpy as np
import math


################################################

# single wire quantum register
quantumRegister = QuantumRegister(1, name='quantum register')

# single wire classical register
classicalRegister = ClassicalRegister(1, name='classical register')

# the quantum circuit, or score
qc = QuantumCircuit(quantumRegister, classicalRegister)

######################################################


# quantum value is 0, or | 1, 0 >
qc.reset(quantumRegister)

# superposition the wire between 1 and 0
qc.h(quantumRegister)
print(qc)

qc.measure(quantumRegister, classicalRegister)


#######################################################


backend = BasicAer.get_backend ('statevector_simulator')
job = execute(qc, backend)
result = job.result()


####################################################


x = np.array([[0, 1], [1, 0]])
h = np.array([[1, 1], [1, -1]])
ht = h.transpose()


####################################################


outputState = result.get_statevector(qc, decimals=3)
outputStateNumpy = np.array(outputState)
outputStateNumpy = [int(x) for x in outputStateNumpy]


####################################################


# create a method to take a random bit
# and produce a new quantum matrix

def matrixGen(outputStateNumpy):
    if outputStateNumpy == [1, 0]:
        print("the x gate: \n")
        return x
    elif outputStateNumpy == [0, 1]:
        print("the h gate: \n")
        return h


matrix = matrixGen(outputStateNumpy)
print(matrix, "\n")


################################################


# draw the circuit
# qc.draw()


#####################################################


coh = 1/(math.sqrt(2))
coht = coh
cohtm = coh*coh

hUnitarityTest = np.dot(h, ht)*cohtm
