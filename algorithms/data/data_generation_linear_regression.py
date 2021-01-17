'''
Function to generate data for linear regression
'''
# import numpy for calculations
import numpy as np

def get_data_points(a6, a5, a4, a3, a2, a1, offset, data_point_number, x_min, x_max, noise, random_state):
    '''
    generate data points for the regression algorithm and the linear_regression application

    :param a6: coefficient for x^6
    :param a5: coefficient for x^5
    :param a4: coefficient for x^4
    :param a3: coefficient for x^3
    :param a2: coefficient for x^2
    :param a1: coefficient for x^1
    :param offset: offset of the data
    :param data_point_number: number of datapoints
    :param x_min: minimum datapoint value
    :param x_max: maximum datapoint value
    :param noise: amplitude of the uniform distributed noise
    :param random_state: random state seed variable

    :return: x, y, x_ground_truth, y_ground_truth
    '''
    # set random seed to get reuseable noise
    np.random.seed(random_state)

    # set x vector and x_ground_truth vector
    x = np.linspace(x_min, x_max, data_point_number)
    x_ground_truth = np.linspace(x_min, x_max, abs(x_max-x_min)*500)
    epsilon = np.random.uniform(-noise, noise, data_point_number)

    # calculate ground_truth values y
    y_ground_truth = a6*np.power(x_ground_truth, 6) + a5*np.power(x_ground_truth, 5) + a4*np.power(x_ground_truth, 4) \
        + a3*np.power(x_ground_truth, 3) + a2*np.power(x_ground_truth, 2) + a1 * x_ground_truth + offset

    # calculate y with noise
    y = a6*np.power(x, 6) + a5*np.power(x, 5) + a4*np.power(x, 4) \
        + a3*np.power(x, 3) + a2*np.power(x, 2) + a1 * x + offset + epsilon

    return x, y, x_ground_truth, y_ground_truth