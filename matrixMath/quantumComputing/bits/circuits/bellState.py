
import cirq

a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")
d = cirq.NamedQubit("d")
ops = [cirq.H(a), cirq.H(b), cirq.CNOT(b, c), cirq.H(b)], cirq.CCNOT(a,b,c)
circuit = cirq.Circuit.from_ops(ops)
print(circuit)

