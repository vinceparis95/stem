######################################

from qiskit import \
    QuantumCircuit, QuantumRegister, \
    ClassicalRegister, execute, Aer, \
    IBMQ, BasicAer

import numpy as np


################################################

# set up the quantum register with one wire
quantumRegister = QuantumRegister(1, name='quantumRegister')

# set up the classical register with one wire
classicalRegister = ClassicalRegister(1, name='classicalRegister')

# set up the quantum circuit
qc = QuantumCircuit(quantumRegister, classicalRegister)

######################################################


# write the value to 0
qc.reset(quantumRegister)

# place it in a superposition of 1 and 0
qc.h(quantumRegister)
print(qc)

qc.measure(quantumRegister, classicalRegister)


#######################################################


backend = BasicAer.get_backend ('statevector_simulator')
job = execute(qc, backend)
result = job.result()


####################################################


outputState = result.get_statevector(qc, decimals=3)
outputStateNumpy = np.array(outputState)
outputStateNumpy = [int(x) for x in outputState]
print("\n the random bit value: " , outputStateNumpy)

# draw the circuit
# qc.draw()


#####################################################



