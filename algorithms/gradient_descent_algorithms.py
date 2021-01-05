import numpy as np

def gradient_descent_alg(function, dfunction, x0, learning_rate, iterations):
    '''
    Function, that is performing the gradient descent to find a local minimum of a function

    Args:
        function: Target Function f(x)
        dfunction: Derivative of the objective function f: f'(x) = df(x)/dx
        x0: Start value of the gradient descent algorithm
        learning_rate: learning rate eta
        iterations: number of iteration steps for the algorithm

    Returns:
        x_final: last value of the gradient descent algorithm
        x_steps: all calculated x values during the algorithm
        y: corresponding y=f(x) values of the x_steps
    '''

    x_steps = np.zeros(iterations+1)
    x_steps[0] = x0

    # iterative solving
    for i in range (iterations):
        x_steps[i+1] = x_steps[i] - learning_rate*dfunction(x_steps[i])

    # calculate corresponding function values
    y = function(x_steps)

    return x_steps[iterations], x_steps, y

def stochastic_gradient_descent_alg(function, dfunction, x0, learning_rate, iterations):
    '''
    Function, that is performing the gradient descent to find a local minimum of a function

    Args:
        function: Target Function f(x)
        dfunction: Derivative of the objective function f: f'(x) = df(x)/dx
        x0: Start value of the gradient descent algorithm
        learning_rate: learning rate eta
        iterations: number of iteration steps for the algorithm

    Returns:
        x_final: last value of the gradient descent algorithm
        x_steps: all calculated x values during the algorithm
        y: corresponding y=f(x) values of the x_steps
    '''

    x_steps = np.zeros(iterations+1)
    x_steps[0] = x0

    # iterative solving
    for i in range (iterations):
        x_steps[i+1] = x_steps[i] - learning_rate*dfunction(x_steps[i])

    # calculate corresponding function values
    y = function(x_steps)

    return x_steps[iterations], x_steps, y