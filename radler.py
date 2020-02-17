
import matplotlib.pyplot as plt


def get_count(amount, cost=0.60, pfand=0.25):
    total = cost + pfand
    count = 0
    while amount >= total:
        curr_count = int(amount / total)
        count += curr_count
        amount -= (curr_count * total)
        amount += curr_count * pfand
    return count


if __name__ == "__main__":
    for i in range(10, 2000, 10):
        y = get_count(i)
        print(i, y)
        plt.plot(i, y, 'ro')
    plt.show()
