n = int(input())
inv = 0
sz = 0

m = n
while m > 0:
    m //= 10
    sz += 1

while n > 0:
    inv += (10 ** (sz-1)) * (n % 10)

    n //= 10
    sz -= 1

print(inv)
