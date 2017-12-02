from numpy import log
from sigmoid import sigmoid

import numpy as np

def costFunction(theta, X,y):
    """ computes the cost of using theta as the
    parameter for logistic regression and the
    gradient of the cost w.r.t. to the parameters."""

# Initialize some useful values
    m = y.size # number of training examples


# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta.
#               You should set J to the cost.
#               Compute the partial derivatives and set grad to the partial
#               derivatives of the cost w.r.t. each parameter in theta
#
# Note: grad should have the same dimensions as theta

# theta.shape = (n+1, 1)
# X.shape = (m, n+1)
# y.shape = (m, 1)
# hypothesis function: h = 1/(1+exp(-theta.transpose * x)) = sigmoid(np.dot(x, theta)) ==> this returns (m, 1) vector
# cost function: J = -1/m * (y*log(h) + (1-y)*log(1-h)).sum()
    first = y * np.transpose(np.log(sigmoid(np.dot(X, theta))))
    second = (1-y) * np.transpose(np.log(1 - sigmoid(np.dot(X, theta))))
    J = -(1.0 / m) * (first + second).sum()
    return J
