import numpy as np
import math

#########################

# the Q u b i t

#########################

# | 0 } = [[ 1 ],
#          [ 0 ]]

state0 = np.array([[1,0]])

##########################

# | 1 } = [[ 0 ],
#          [ 1 ]]
state1 = np.array([[0,1]])

############################

# | 2 } = [[ 0 ],
# #        [ 0 ]
#          [ 1 ]
#          [ 0 ]]
state2 = np.array([[0,0,1,0]])

##############################

# | 3 } = [[ 0 ],
# #        [ 0 ]
#          [ 0 ]
#          [ 1 ]]
state3 = np.array([[0,0,0,1]])


#################################

# Q u a n t u m  R e g i s t e r

#################################
import cirq


# create a qubit on the score
qubit = cirq.GridQubit(0,0)
print(qubit)

