from numpy import e
import numpy as np

def sigmoid(z):
    """computes the sigmoid of z."""

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the sigmoid of each value of z (z can be a matrix,
#               vector or scalar).

# =============================================================

# option1: sigmoid = 1 / (1 + exp(-z))
# option2: sigmoid = expit(z)
    g = 1.0 / (1.0 + np.exp(-z))
    return g
