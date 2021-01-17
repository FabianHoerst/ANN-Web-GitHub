'''
Test file for linear_regression_algorithm.py
'''
import unittest
import numpy as np
import numpy.testing as npt
from algorithms.linear_regression_algorithm import regression

# helper functions
def function1(x):
    return x ** 4 - 4 * x ** 2

def dfunction1(x):
    return 4 * x ** 3 - 8 * x

# unittests for Linear Regression
class TestLinearRegression(unittest.TestCase):

    def test_ideal_theta(self):
        '''
        Test that the algorithm calculates the ground truth theta under ideal conditions
        '''
        x = np.linspace(-5,5,1000)
        y = function1(x)
        theta, y_pred = regression(4, x, y, x)
        npt.assert_array_almost_equal(theta, [0,0,-4,0,1], 6)

    def test_y_prediction(self):
        '''
        Test that the algorithm calculates the ground truth y under ideal conditions
        '''
        x = np.linspace(-5, 5, 1000)
        y = function1(x)
        theta, y_pred = regression(4, x, y, x)
        npt.assert_array_almost_equal(y_pred, y, 6)

    def test_order_error(self):
        '''
        Test whether the algorithm stops if the polynomial order is higher then the number of datapoints
        '''
        x = np.linspace(-5, 5, 1000)
        y = function1(x)
        self.assertRaises(ValueError, lambda:regression(1006, x, y, x))

if __name__ == "__main__":
    unittest.main()