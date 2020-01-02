
# The TreeLogger is a quantum-classical hybrid network
# It is a type of binary classifier

#######################################################

# import torch
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torchvision import datasets, models, transforms

# import pennylane
import pennylane as qml
from pennylane import numpy as np

# import some other tools
import time
import os
import copy

#########################################################

# OpenMP: number of parallel threads.
os.environ["OMP_NUM_THREADS"] = "1"
n_qubits = 4                # Number of qubits
step = 0.0004               # Learning rate
batch_size = 4              # Number of samples for each training step
num_epochs = 1              # Number of training epochs
q_depth = 6                 # Depth of the quantum circuit (number of variational layers)
gamma_lr_scheduler = 0.1    # Learning rate reduction applied every 10 epochs.
q_delta = 0.01              # Initial spread of random quantum weights
rng_seed = 0                # Seed for random number generator
start_time = time.time()    # Start of the computation# timer

# initialize pennylane operator
dev = qml.device("default.qubit", wires=n_qubits)
# initialize a torch jawn
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")




