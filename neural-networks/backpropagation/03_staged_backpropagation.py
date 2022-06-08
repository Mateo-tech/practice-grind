# Caching some of the values during the forward pass to make
# our live easier during the backprop.
#
# f(x, y) = (x + σ(y)) / (σ(x) + (x + y)^2)

import math

# Input
x = 3
y = -4

# Forward pass
sig_y = 1.0 / (1 + math.exp(-y))
numer = x + sig_y
sig_x = 1.0 / (1 + math.exp(-x))
xpy = x + y
xpysqr = xpy**2
den = sig_x + xpysqr
invden = 1.0 / den
f = numer * invden

# Backpropagation - f = numer * invden

dnumer = invden
dinvden = numer

# Backprop invden = 1.0 / den
dden = (-1.0 / (den**2)) * dinvden

# Backprop den = sigx + xpysqr
dsigx = (1) * dden
dxpysqr = (1) * dden

# Backprop xpysqr = xpy**2
dxpy = (2 * xpy) * dxpysqr

# Backprop xpy = x + y
dx = (1) * dxpy 
dy = (1) * dxpy  

# Backprop sigx = 1.0 / (1 + math.exp(-x))
dx += ((1 - sig_x) * sig_x) * dsigx 

# Backprop num = x + sigy
dx += (1) * dnumer                      
dsigy = (1) * dnumer    

# Backprop sigy = 1.0 / (1 + math.exp(-y))
dy += ((1 - sig_y) * sig_y) * dsigy  