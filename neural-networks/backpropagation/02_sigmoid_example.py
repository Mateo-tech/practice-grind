#  Let's consider a more complex scenario with a neuron
# that computes the sigmoid function.
# The weights and biases are combined.

import math

# Input
w = [3, -3, -3] # Weights + bias
x = [-1, -2] # Data

# Forward pass
dot = w[0] * x[0] + w[1] * x[1] + w[2]
f = 1.0 / (1 + math.exp(-dot))

# Backward pass
ddot = (1 - f) * f # The complete gradient of the sigmoid

# Backprop step
dx = [w[0] * ddot, w[1] * ddot]
dw = [x[0] * ddot, w[1] * ddot, 1.0 * ddot]