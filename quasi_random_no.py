import numpy as np
from matplotlib import pyplot as plt


def aldg(alpha, u0, n):
    random_nums = [u0]
    for i in range(1, n):
        ui = (random_nums[i - 1] + alpha) % n
        random_nums.append(ui)
    return random_nums


if __name__ == "__main__":
    size = 10000
    random_xs = aldg(alpha=np.sqrt(2) - 1, u0=1, n=size)
    random_ys = aldg(alpha=np.sqrt(5) - 1, u0=10, n=size)
    plt.scatter(random_xs, random_ys)
    plt.show()
