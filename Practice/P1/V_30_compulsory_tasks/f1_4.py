import math


def f1_4(n):
    if n == 0:
        return 8
    else:
        return math.fabs(f1_4(n-1))+(1/53)*pow((f1_4(n-1)),2)


print(f'{f1_4(14):.2e}')
print(f'{f1_4(12):.2e}')