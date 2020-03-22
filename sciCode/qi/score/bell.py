
import cirq


#####################################################

# the Bell State , or the simplest truly qi state

########################################################

# write out the four qubit
a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")

##############################################

# write out the ops

ops = [cirq.H(a), cirq.H(b),
       cirq.CNOT(b, c),
       cirq.H(b),
       cirq.CCX(a,b,c),
       cirq.measure(a,b,c)]
circuit = cirq.Circuit.from_ops(ops)
print(circuit)

