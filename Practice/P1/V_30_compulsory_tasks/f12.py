import math
def f12(x):
    if x < 44:
        return x + 17 * pow(x, 7)
    elif 44 <= x < 59:
        return (pow((math.sin(x) + pow(x, 3) - 85), 7) / 87) + math.fabs(x)
    elif 59 <= x < 80:
        return pow(x, 2) - math.cos(x)
    else:
        return math.fabs(12 * pow(x, 4)) - 4 * pow(x, 6) + 49