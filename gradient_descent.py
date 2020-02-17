import numpy as np
from matplotlib import pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def func_h(x, y):
    """
    Function definition

    :param(float) x: Value of X Coordinate
    :param(float) y: Value of Y Coordinate
    :return(float): Function value of H
    """
    # p1 = ((x * np.sin(20 * y) + y * np.sin(20 * x)) ** 2) * np.cosh(x * np.sin(10 * x))
    # p2 = ((x * np.cos(20 * y) - y * np.sin(10 * x)) ** 2) * np.cosh(y * np.cos(20 * y))
    # return p1 + p2
    return (x ** 2) + (3 * (y ** 3))


def gd_h(x, y):
    """
    Deterministic Gradient Descent Calculator

    :param(float) x: Last X co-ordinate
    :param(float) y: Last Y co-ordinate
    :return(float, float): New Values for gradient descent
    """
    # dh1_dy = np.cosh(x * np.sin(10 * x)) * 2 * (x * np.sin(20 * y) + y * np.sin(20 * x)) * (
    #         20 * x * np.cos(20 * y) + np.sin(20 * x))
    # dh2_dy = 2 * np.cosh(y * np.cos(20 * y)) * (x * np.cos(10 * y) - y * np.sin(10 * x)) * (
    #         -10 * x * np.sin(10 * y) - np.sin(10 * x)) + ((x * np.cos(10 * y) - y * np.sin(10 * x)) ** 2) * (
    #              np.sinh(y * np.cos(20 * y))) * (np.cos(20 * y) - 20 * y * np.sin(20 * y))
    # dh1_dx = np.cosh(x * np.sin(10 * x)) * 2 * (x * np.sin(20 * y) + y * np.sin(20 * x)) * (
    #         np.sin(20 * y) + 20 * y * np.cos(20 * x)) + ((x * np.sin(20 * y) + y * np.sin(20 * x)) ** 2) * np.sinh(
    #     x * np.sin(10 * x)) * (10 * x * np.cos(10 * x) + np.sin(10 * x))
    # dh2_dx = np.cosh(y * np.cos(20 * y)) * 2 * (x * np.cos(10 * y) - y * np.sin(10 * x)) * (
    #         np.cos(10 * y) - 10 * y * np.cos(10 * x))
    # return dh1_dx + dh2_dx, dh1_dy + dh2_dy
    return (2 * x), (9 * (y ** 2))


def get_sample_unit_circle():
    """
    Get a random point from a unit circle

    :return(tuple]): Sample coordinates (X, Y)
    """
    theta = np.random.uniform(0, 2 * np.pi)
    sample_x = np.cos(theta)
    sample_y = np.sin(theta)
    return sample_x, sample_y


def delta_h(theta1_x, theta1_y, theta2_x, theta2_y):
    return func_h(theta1_x + theta2_x, theta1_y + theta2_y) - func_h(theta1_x - theta2_x, theta1_y - theta2_y)


def get_deterministic_gradient(last_x, last_y, alpha):
    gd_x, gd_y = gd_h(last_x, last_y)
    new_x = gd_x * alpha
    new_y = gd_y * alpha
    return new_x, new_y


def get_stochastic_gradient(last_x, last_y, alpha, beta):
    ui_x, ui_y = get_sample_unit_circle()
    del_h = delta_h(theta1_x=last_x, theta1_y=last_y, theta2_x=(beta * ui_x), theta2_y=(beta * ui_y))

    new_x = alpha * del_h * ui_x / (2 * beta)
    new_y = alpha * del_h * ui_y / (2 * beta)

    return new_x, new_y


if __name__ == "__main__":
    k = 1000

    # X, Y and H Values of the travel chain with a random starting point
    X = [np.random.uniform(-0.5, 0.5)]
    Y = [np.random.uniform(-0.5, 0.5)]
    h = [func_h(X[0], Y[0])]
    alpha = 0.5
    beta = 0.1

    for i in range(1, k):
        # x_i, y_i = get_deterministic_gradient(last_x=X[i - 1], last_y=Y[i - 1], alpha=alpha)
        x_i, y_i = get_stochastic_gradient(last_x=X[i - 1], last_y=Y[i - 1], alpha=alpha, beta=beta)
        X.append(x_i)
        Y.append(y_i)
        h.append(func_h(x_i, y_i))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # ax.scatter(X[:-1], Y[:-1], h[:-1], c='g', marker='o')
    ax.scatter(X[-1], Y[-1], h[-1], c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('H(X, Y)')

    plt.show()
