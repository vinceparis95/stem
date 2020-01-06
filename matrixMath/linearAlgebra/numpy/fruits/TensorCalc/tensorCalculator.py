import numpy as np


########################################################################

# Build a pythonic module that performs some linlog algebra on real data

########################################################################

# define a class
class tensorCalculator:

    # the init constructor
    def __init__(self, vals):
        self.vals = vals

    # a multiplier function
    def mult(self, inp):
        self.vals = self.vals * inp

    # a dot product function
    def dot(self, inp):
        self.vals = np.dot(self.vals, inp)


##########################################


matrix = tensorCalculator(np.array([3, 3]))
matrix.dot(np.array([3, 3]))
matrix.mult(np.array([3, 3]))
matrix.dot(np.array([2, 3]))
print(matrix.vals)
