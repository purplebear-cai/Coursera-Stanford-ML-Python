from numpy import asfortranarray, squeeze, asarray
from gradientFunction import gradientFunction
import numpy as np
from sigmoid import sigmoid

def gradientFunctionReg(theta, X, y, Lambda):
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
    # theta.shape = (n+1, )
    # X.shape = (m, n+1)
    # y.shape = (m, 1)
    y = np.squeeze(y)
    grad = (1.0 / m) * np.dot(sigmoid(np.dot(X, theta)).T - y, X).T + (float(Lambda) / m) * theta

    # we only apply gradient to 1, 2, ..., n+1
    grad_without_reg = (1.0/m) * np.dot(sigmoid(np.dot(X, theta)).T - y, X).T
    grad[0] = grad_without_reg[0]
    return grad
