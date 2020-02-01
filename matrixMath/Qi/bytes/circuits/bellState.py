
import cirq


#####################################################

# the Bell State , or the simplest truly qi state

########################################################

# write out the four qubits
a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")
d = cirq.NamedQubit("d")

##############################################

# write out the ops

ops = [cirq.H(a), cirq.H(b),
       cirq.CNOT(b, c),
       cirq.H(b)], \
      cirq.CCNOT(a,b,c)
circuit = cirq.Circuit.from_ops(ops)
print(circuit)

