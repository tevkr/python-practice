import math


def f1_3(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum1 += (math.fabs(j) + 28 * pow(i, 7))
    for i in range(1, n + 1):
        sum2 += (pow(i, 2) + pow(i, 8) - 22)
    return 91 * sum1 - 76 * sum2

print(f'{f1_3(61, 71):.2e}')
print(f'{f1_3(23, 22):.2e}')