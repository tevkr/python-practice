def f11(s):
    return [int(i) for i in s]


def f12(s):
    return len(set(s))


def f13(s):
    return s[::-1]


def f14(x, s):
    return [i for i, j in enumerate(s) if j == x]


def f15(s):
    return sum(s[::2])


def f16(s):
    return max(s, key=len)