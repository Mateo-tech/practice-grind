import numpy as np

# Forward pass
W = np.random.randn(5, 10)
X = np.random.randnd(10, 3)
D = W.dot(X)

dD = np.random.randn(*D.shape)
dW = dD.dot(X.T)
dX = W.T.dot(dD)