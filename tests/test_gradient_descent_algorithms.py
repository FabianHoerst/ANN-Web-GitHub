'''
Test file for linear_regression_algorithm.py
'''
import unittest
import numpy as np
from algorithms.gradient_descent_algorithms import gradient_descent_alg

# helper functions
def function1(x):
    return x ** 4 - 4 * x ** 2

def dfunction1(x):
    return 4 * x ** 3 - 8 * x

# unittests for gradient descent algorithm
class TestGradientDescent(unittest.TestCase):

    def test_solution1(self):
        '''
        Test that the result is true if starting value is 2
        '''
        x_final, x_steps, y = gradient_descent_alg(function1, dfunction1, 2, 0.0001, 100000)
        x_final = round(x_final, 8)
        self.assertEqual(x_final, round(np.sqrt(2), 8))

    def test_solution2(self):
        '''
        Test that the result is true if starting value is -2
        '''
        x_final, x_steps, y = gradient_descent_alg(function1, dfunction1, -2, 0.0001, 100000)
        x_final = round(x_final, 8)
        self.assertEqual(x_final, round(-np.sqrt(2), 8))

    def test_length(self):
        '''
        Test that the result is having the same right length
        '''
        x_final, x_steps, y = gradient_descent_alg(function1, dfunction1, -2, 0.0001, 100000)
        self.assertEqual(len(x_steps), 100001)

if __name__ == "__main__":
    unittest.main()