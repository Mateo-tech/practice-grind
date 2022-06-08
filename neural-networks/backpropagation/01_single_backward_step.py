# This is an example of a single backward/backprop step of a function
# f(x, y, z) = (x + y)z
# i.e. we compute the derivatives w.r.t. to the parameters and update the values

# Input
x = -2
y = 5
z = -4

# Forward pass
q = x + y
f = q * z

# Backward pass
dfdz = q
dfdq = z
dqdx = 1.0
dqdy = 1.0

# Backprop step
dfdx = dfdq * dqdx
dfdy = dfdq * dqdy