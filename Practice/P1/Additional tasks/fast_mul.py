def test_fast_mul():
    for i in range(100):
        for j in range(100):
            assert fast_mul(i, j) == i * j, (i, j, fast_mul(i, j), i * j)


def fast_mul(a, b, sum=0):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b + sum
    if a % 2 == 1:
        sum += b
    return fast_mul(a // 2, b * 2, sum)


test_fast_mul()