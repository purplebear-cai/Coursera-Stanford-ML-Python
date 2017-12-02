from numpy import round
from sigmoid import sigmoid
import numpy as np

def predict(theta, X):

    """ computes the predictions for X using a threshold at 0.5
    (i.e., if sigmoid(theta'*x) >= 0.5, predict 1)
    """

# ====================== YOUR CODE HERE ======================
# Instructions: Complete the following code to make predictions using
#               your learned logistic regression parameters.
#               You should set p to a vector of 0's and 1's
#


# =========================================================================
# theta.shape = (n+1, 1)                                                        
# X.shape = (m, n+1)                                                            
    sigmoid_score = sigmoid(np.dot(X, theta))
    p = sigmoid_score >= 0.5
    return p
