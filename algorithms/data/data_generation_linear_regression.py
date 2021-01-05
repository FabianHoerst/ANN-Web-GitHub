import numpy as np

def get_data_points(a6, a5, a4, a3, a2, a1, offset, data_point_number, x_min, x_max, noise, random_state):
    np.random.seed(random_state)

    x = np.linspace(x_min, x_max, data_point_number)
    x_ground_truth = np.linspace(x_min, x_max, abs(x_max-x_min)*500)
    epsilon = np.random.uniform(-noise, noise, data_point_number)

    y_ground_truth = a6*np.power(x_ground_truth, 6) + a5*np.power(x_ground_truth, 5) + a4*np.power(x_ground_truth, 4) \
        + a3*np.power(x_ground_truth, 3) + a2*np.power(x_ground_truth, 2) + a1 * x_ground_truth + offset

    y = a6*np.power(x, 6) + a5*np.power(x, 5) + a4*np.power(x, 4) \
        + a3*np.power(x, 3) + a2*np.power(x, 2) + a1 * x + offset + epsilon

    return x, y, x_ground_truth, y_ground_truth