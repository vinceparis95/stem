######################################

from qiskit import \
    QuantumCircuit, QuantumRegister, \
    ClassicalRegister, execute, Aer, \
    IBMQ, BasicAer

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


backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()


##############################


counts = result.get_counts(qc)
print('counts:',counts)

####################################################

outputstate = result.get_statevector(qc, decimals=3)
print(outputstate)

# draw the circuit
qc.draw()

#####################################################



