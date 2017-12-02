from sigmoid import sigmoid
from numpy import squeeze, asarray
import numpy as np

def gradientFunction(theta, X, y):
    """
    Compute cost and gradient for logistic regression with regularization

    computes the cost of using theta as the parameter for regularized logistic regression and the
    gradient of the cost w.r.t. to the parameters.
    """

    m = len(y)   # number of training examples

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the gradient of a particular choice of theta.
#               Compute the partial derivatives and set grad to the partial
#               derivatives of the cost w.r.t. each parameter in theta


# =============================================================
# theta.shape = (n+1, 1)                                                        
# X.shape = (m, n+1)                                                            
# y.shape = (m, 1)
# grad = 1/m * ((h - y) * x).sum()
    grad = 1.0 / m * (np.dot(sigmoid(np.dot(X, theta)).T - y, X)).sum()
    return grad
