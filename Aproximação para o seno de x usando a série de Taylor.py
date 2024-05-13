import math


def taylor(x, n):
    approx = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            approx += (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        else:
            approx -= (x ** (2 * i + 1)) / math.factorial(2 * i + 1)

        i += 1
    return approx


a, b = map(float, input().split(sep=' '))
n = int(a)
x = float(b)

sin = math.sin(x)
seno = taylor(x, n)

print('{} : {:6.3f} = {:6.3f}?'.format(n, seno, sin))
