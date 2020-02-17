def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p


def prob_k(k):
    n = 50
    return factorial(2 * n)/((factorial(k) ** 2) * (factorial(n - k) ** 2))


sum = 0
for i in range(0, 50):
    sum += prob_k(i) * ((1/4) ** 100)

print(sum)
