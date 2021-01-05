import numpy as np
from sklearn.linear_model import LinearRegression

def regression(polynomial_order, x, y, x_ground_truth):
    '''
    Function, that is performing the linear regression algorithm to find the best approximation for a given dataset X,y

    Args:
        polynomial_order: integer between 0 and n (n=len(x))
        x: Vektor of x values, x=1xn
        y: Vektor of y values, y=1xn
        x_ground_truth: ground truth vector x, used for comparison

    Returns:
        Theta: Vector containing the parameters theta
        y_predict: Predicted y values
    '''

    # test if condition polynomial order <= n is met
    elements = len(x)
    if polynomial_order > elements:
        raise ValueError('polyonmial order is higher then the number of datapoints. No regression possible')

    X = np.zeros([elements, polynomial_order + 1])
    for i in range(0, polynomial_order + 1):
        X[:,i] = x**i

    Theta = np.linalg.inv(X.T @ X) @ X.T @ y

    elements_pred = len(x_ground_truth)
    X_ground_truth = np.zeros([elements_pred, polynomial_order + 1])
    for i in range(0, polynomial_order + 1):
        X_ground_truth[:,i] = x_ground_truth**i
    y_predict = X_ground_truth @ Theta

    return Theta, y_predict

def batch_regression(X,y, learning_rate, iterations, initial_theta = 0):
    '''
    Function, that is performing the batch linear regression algorithm using gradient descent
    with summing the loss over all datapoints

    Args:
        X = features
        y = value
        learning_rate = learning rate of the algorithm
        iterations = number of iterations
        initial_theta = initialization of theta

    Returns:
        Theta: Vector containing the parameters theta
        y_predict: Predicted y values
    '''
    features = len(X[0,:])

    if initial_theta == 0:
        theta = np.zeros(features)
    else:
        theta = initial_theta

    for i in range(iterations):
        dMSE = 2*X.T@(X@theta - y)
        theta = theta - learning_rate*dMSE

    y_predict = X@theta
    return theta, y_predict


def stoch_regression(X, y, learning_rate, iterations, initial_theta=0):
    '''
    Function, that is performing the stochastic linear regression algorithm using gradient descent
    with calculating the loss of one datapoint

    Args:
        X = features
        y = value
        learning_rate = learning rate of the algorithm
        iterations = number of iterations
        initial_theta = initialization of theta

    Returns:
        Theta: Vector containing the parameters theta
        y_predict: Predicted y values
    '''
    features = len(X[0, :])
    elements = len(X[:, 0])

    if initial_theta == 0:
        theta = np.zeros(features)
    else:
        theta = initial_theta

    for i in range(iterations):
        index = np.random.randint(elements)
        xi = X[index, :]
        yi = y[index]
        dMSE = 2 * xi.T * (xi @ theta - yi)
        theta = theta - learning_rate * dMSE

    y_predict = X @ theta
    return theta, y_predict


def minibatch_regression(X, y, learning_rate, iterations, batch_size, initial_theta=0):
    '''
    Function, that is performing the batch linear regression algorithm using gradient descent
    with summing the loss over all datapoints

    Args:
        X = features
        y = value
        learning_rate = learning rate of the algorithm
        iterations = number of iterations
        initial_theta = initialization of theta

    Returns:
        Theta: Vector containing the parameters theta
        y_predict: Predicted y values
    '''
    features = len(X[0, :])
    elements = len(X[:, 0])

    if (batch_size <= elements):
        if initial_theta == 0:
            theta = np.zeros(features)
        else:
            theta = initial_theta

        index_list = np.arange(0, elements, 1)
        batch_list = np.arange(0, batch_size, 1)
        for i in range(iterations):
            index_list = np.random.permutation(index_list)

            X_batch = X[index_list[batch_list], :]
            y_batch = y[index_list[batch_list]]
            dMSE = 2 * X_batch.T @ (X_batch @ theta - y_batch)
            theta = theta - learning_rate * dMSE

        y_predict = X @ theta
        return theta, y_predict