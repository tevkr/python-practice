import math


def f1_1(x):
    return ((70 * pow(x, 8)) + (53 * pow(x, 3)) + 91) / ((pow(x, 6)) - (pow(x, 7) / 86) - 85) - (
            (math.tan(x)) - (math.fabs(x)) + 49) / ((pow(x, 5)) + x - 74) + (
                   (56 * pow(x, 4)) + (pow(x, 7))) / ((pow(x, 3)) + (pow(x, 8) / 18))


print(f'{f1_1(20):.2e}')
print(f'{f1_1(39):.2e}')