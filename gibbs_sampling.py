import numpy as np
from matplotlib import pyplot as plt


def get_samples_gibbs(n, x0, y0):
    x = [x0]
    y = [y0]

    for i in range(1, n):
        mean_x = 3 + (y[i - 1] - 2) / 3
        sd_x = np.sqrt(3)
        x.append(np.random.normal(loc=mean_x, scale=sd_x))

        mean_y = 2 + 3 * (x[i] - 3) / 4
        sd_y = np.sqrt(9 / 4)
        y.append(np.random.normal(loc=mean_y, scale=sd_y))
    return x, y


if __name__ == "__main__":
    X, Y = gibbs_samples = get_samples_gibbs(n=10000, x0=2, y0=2)
    plt.scatter(x=X, y=Y)
    plt.show()
