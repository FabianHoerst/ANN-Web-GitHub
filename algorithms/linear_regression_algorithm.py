'''
File is containing algorithms performing regression (linear, batch, stoch, mini_batch)
'''
# import numpy module for calculations
import numpy as np

def regression(polynomial_order, x, y, x_ground_truth):
    '''
    Function, that is performing the linear regression algorithm to find the best approximation for a given dataset X,y

    Args:
    :param polynomial_order: integer between 0 and n (n=len(x))
    :param x: Vektor of x values, x=1xn
    :param y: Vektor of y values, y=1xn
    :param x_ground_truth: ground truth vector x, used for comparison

    Returns:
    :return Theta: Vector containing the parameters theta
    :return y_predict: Predicted y values
    '''

    # test if condition polynomial order <= n is met
    elements = len(x)
    if polynomial_order > elements:
        raise ValueError('polyonmial order is higher then the number of datapoints. No regression possible')

    # build feature vector (X=[0, x, x^2, x^3, ... , x^polynomial_order)
    X = np.zeros([elements, polynomial_order + 1])
    for i in range(0, polynomial_order + 1):
        X[:,i] = x**i

    # calculate the optimal parameters theta
    Theta = np.linalg.inv(X.T @ X) @ X.T @ y

    # do some calculations for plotting
    elements_pred = len(x_ground_truth)
    X_ground_truth = np.zeros([elements_pred, polynomial_order + 1])
    for i in range(0, polynomial_order + 1):
        X_ground_truth[:,i] = x_ground_truth**i
    y_predict = X_ground_truth @ Theta

    return Theta, y_predict

def batch_regression(X,y, learning_rate, iterations, initial_theta = 0):
    '''
    Function, that is performing the batch linear regression algorithm using gradient descent
    with summing the loss over all datapoints, loss functions is squared error

    Args:
    :param X = features
    :param y = value
    :param learning_rate = learning rate of the algorithm
    :param iterations = number of iterations
    :param initial_theta = initialization of theta

    Returns:
    :return Theta: Vector containing the parameters theta
    :return y_predict: Predicted y values
    '''
    # get number of features
    features = len(X[0,:])

    # initialize theta vector
    if initial_theta == 0:
        theta = np.zeros(features)
    else:
        theta = initial_theta

    # perform gradient descent to find theta
    for i in range(iterations):
        dMSE = 2*X.T@(X@theta - y)
        theta = theta - learning_rate*dMSE

    # predict values for plotting
    y_predict = X@theta
    return theta, y_predict

def stoch_regression(X, y, learning_rate, iterations, initial_theta=0):
    '''
    Function, that is performing the stochastic linear regression algorithm using gradient descent
    with calculating the loss of one datapoint, loss function is squared error

    Args:
    :param X = features
    :param y = value
    :param learning_rate = learning rate of the algorithm
    :param iterations = number of iterations
    :param initial_theta = initialization of theta

    Returns:
    :return Theta: Vector containing the parameters theta
    :return y_predict: Predicted y values
    '''
    # get number of features and elements
    features = len(X[0,:])
    elements = len(X[:,0])

    # initialize theta vector
    if initial_theta == 0:
        theta = np.zeros(features)
    else:
        theta = initial_theta

    # perform stochastic gradient descent by selecting one single datapoint
    for i in range(iterations):
        index = np.random.randint(elements)
        xi = X[index, :]
        yi = y[index]
        dMSE = 2*xi.T*(xi@theta-yi)
        theta = theta - learning_rate * dMSE

    # predict values for plotting
    y_predict = X @ theta
    return theta, y_predict


def minibatch_regression(X, y, learning_rate, iterations, batch_size, initial_theta=0):
    '''
    Function, that is performing the batch linear regression algorithm using gradient descent
    with summing the loss over a batch of datapoints, loss function is squared error

    Args:
    :param X = features
    :param y = value
    :param learning_rate = learning rate of the algorithm
    :param iterations = number of iterations
    :param initial_theta = initialization of theta

    Returns:
    :return Theta: Vector containing the parameters theta
    :return y_predict: Predicted y values
    '''
    # get number of features and elements
    features = len(X[0, :])
    elements = len(X[:, 0])

    # just perform algorithm if batch_size is not to high
    if (batch_size <= elements):
        #initialize theta
        if initial_theta == 0:
            theta = np.zeros(features)
        else:
            theta = initial_theta

        # build batch
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
    else:
        raise ValueError('batch_size is higher then the number of datapoints. No regression possible')