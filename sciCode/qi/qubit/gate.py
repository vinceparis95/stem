###########################################################

import numpy as np
import cirq
import math


#################################

# G a t e s

#################################

# the X Matrix

x = np.array([[0, 1], [1, 0]])

state1 = [1,0]

flipped = np.dot(x,state1)

print(flipped)


##############################

# the Hadamard
#
#       | 0 } + | 1 }
#       _____________
#          root2

# create the basic tensor
h = np.array([[1,  1],
              [1, -1]])

# get the tensor transpose
htranspose = h.transpose()

# get the haddy coefficient
hcoefficient = 1/(math.sqrt(2))

# dot the tensor with its transpose
dot = np.dot(h,htranspose)

# square the coefficient
hcoefficientmul = hcoefficient*hcoefficient

# print the squared coefficient with the dot
print(hcoefficientmul*dot)

##########################

# S u p e r P o s i t i o n

###########################

# create a qubit on a score
qubit = cirq.GridQubit(0,1)
print(qubit)

#################################

# place qubit into superposition
circuit = cirq.Circuit.from_ops([
    cirq.H(qubit),
    # add measurement
    cirq.measure(qubit)])
print(circuit)

####################################

# simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit,
                       repetitions=9)
print(result)

######################################



