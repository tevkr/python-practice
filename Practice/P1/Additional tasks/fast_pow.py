def test_fast_pow():
    for i in range(100):
        for j in range(100):
            assert fast_pow(i, j) == pow(i, j), (i, j, fast_pow(i, j), pow(i, j))


def fast_pow(base, power):
    result = 1
    while power > 0:
        if power % 2 == 0:
            power //= 2
            base *= base
        else:
            power -= 1
            power //= 2
            result *= base
            base *= base
    return result


test_fast_pow()