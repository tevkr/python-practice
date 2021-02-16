import math
def f14(n):
    if n == 0:
        return 8
    else:
        return math.fabs(f14(n-1))+(1/53)*pow((f14(n-1)),2)