from qiskit import *

circuit = QuantumCircuit(3,3)
circuit.barrier()
print(circuit.draw())


#############################


circuit.h(0)
circuit.barrier()
print(circuit.draw())


#######################


circuit.h(1)
circuit.cx(1,2)
circuit.barrier()
print(circuit.draw())


#####################


circuit.cx(0,1)
circuit.h(0)
circuit.barrier()
print(circuit.draw())


###########################


circuit.measure([0,1],[0,1])
circuit.cx(1,2)
circuit.cz(0,2)
print(circuit.draw())


#############################


simulator = Aer.get_backend("qasm_simulator")
res = execute(circuit,simulator, shots=1024).result()
counts = res.get_counts()


#####################################################


from qiskit.tools.visualization import plot_histogram
plot_histogram(counts).show()
print(counts)
