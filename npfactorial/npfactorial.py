import numpy as np

def factorial(k):
    """
    A simple function that computes the factorial using python.

    :int k: the number of which we want to compute the factorial.   
    """
    return np.prod((np.arange(1,k+1)))

