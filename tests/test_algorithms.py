import unittest
import numpy as np
import numpy.testing as npt
from algorithms.gradient_descent_algorithms import gradient_descent_alg
from algorithms.linear_regression_algorithm import regression

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