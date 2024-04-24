from npfactorial.npfactorial import factorial
import numpy as np
def test_1():
    assert np.linalg.norm(1-factorial(1))<1e-5

def test_2():
    assert np.linalg.norm(2-factorial(2))<1e-5

def test_3():
    assert np.linalg.norm(6-factorial(3))<1e-5