def f22(x):
    a = x & 0xff
    b = x & 0x100
    c = x & 0x1fffe00
    d = x & 0xfe000000
    a <<= 16
    b <<= 23
    c >>= 9
    d >>= 1
    x = a + b + c + d
    return x
