from costFunction import costFunction
from sigmoid import sigmoid
import numpy as np

def costFunctionReg(theta, X, y, Lambda):
    """
    Compute cost and gradient for logistic regression with regularization

    computes the cost of using theta as the parameter for regularized logistic regression and the
    gradient of the cost w.r.t. to the parameters.
    """
    # Initialize some useful values
    m = len(y)   # number of training examples

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta.
#               You should set J to the cost.
#               Compute the partial derivatives and set grad to the partial
#               derivatives of the cost w.r.t. each parameter in theta

# =============================================================
# theta.shape = (n+1, )                                                        
# X.shape = (m, n+1)                                                            
# y.shape = (m, 1)  ==>  we need to reshape this to (m,) using np.squeeze()
# h = sigmoid(np.dot(X, theta)) ==> returns (m, 1) vector
# J = -1/m * (y*log(h) + (1-y)*log(1-h)).sum()
    y = np.squeeze(y)
    first = y * np.transpose(np.log(sigmoid(np.dot(X, theta))))
    second = (1 - y) * np.transpose(np.log(1 - sigmoid(np.dot(X, theta))))
    reg = (Lambda * 1.0 / (2.0 * m)) * np.power(theta[1:theta.shape[0]], 2).sum()
    J = -1.0 / m * (first + second).sum() + reg
    return J
