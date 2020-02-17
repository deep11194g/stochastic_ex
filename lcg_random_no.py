import numpy as np
from matplotlib import pyplot as plt


def lcg(a, m, z0, n):
    random_nums = np.array([z0])
    cycl_idx = -1
    for i in range(1, n):
        z = (a * random_nums[i-1]) % m
        random_nums = np.append(random_nums, z)
        if z == z0:
            cycl_idx = i
            break
    return random_nums/m, cycl_idx


if __name__ == "__main__":
    a = 7
    m = (2 ** 13) - 1
    z = 1
    size = 10000
    rand_nums, cycl = lcg(a, m, z, size)
    print(cycl)

    # x = np.linspace(0, 1, 10)
    # plt.hist(rand_nums, bins=x)
    # plt.show()
    # freq, base = np.histogram(rand_nums)
    # print(freq, base)

