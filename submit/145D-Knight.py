import numpy as np


MOD = 10**9 + 7

X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)

else:
    if (Y < X/2) or (Y > 2*X):
        print(0)
    
    else:
        def extgcd(a, b):
            if b == 0:
                x = 1
                y = 0
            else:
                y, x = extgcd(b, a%b)
                y -= a//b * x
            return x, y

        def low_inverse(a):
            ret, _ = extgcd(a, MOD)
            return ret

        def low_combination(m, n):
            # calculate (m+n)!/n!m!
            ret = 1
            numerator = m + n
            for i in range(min(m, n)):
                inv_i = low_inverse(i + 1)
                ret = ret * (numerator - i) * inv_i % MOD
            return ret

        h = (2 * X - Y) // 3
        v = (2 * Y - X) // 3

        print(low_combination(h, v))
