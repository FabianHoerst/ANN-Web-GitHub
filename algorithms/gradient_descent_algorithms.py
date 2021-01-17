'''
File is containing algorithms performing gradient descent
'''


# import numpy module for calculations
import numpy as np

def gradient_descent_alg(function, dfunction, x0, learning_rate, iterations):
    '''
    Function, that is performing the gradient descent to find a local minimum of a function

    Args:
    :param function: Target Function f(x)
    :param dfunction: Derivative of the objective function f: f'(x) = df(x)/dx
    :param x0: Start value of the gradient descent algorithm
    :param learning_rate: learning rate eta
    :param iterations: number of iteration steps for the algorithm

    Returns:
    :return x_final: last value of the gradient descent algorithm
    :return x_steps: all calculated x values during the algorithm
    :return y: corresponding y=f(x) values of the x_steps
    '''
    # define array to store calculated values
    x_steps = np.zeros(iterations+1)
    x_steps[0] = x0

    # iterative solving
    for i in range(iterations):
        x_steps[i+1] = x_steps[i] - learning_rate*dfunction(x_steps[i])

    # calculate corresponding function values
    y = function(x_steps)

    return x_steps[iterations], x_steps, y

