n = int(input("n: "))
m = n ** 3

ok = True
for i in range(1, m+1, 2):
    s = i

    j = i + 2
    while s < m:
        s += j
        j += 2

    if s == m and ok:
        ok = False
        for r in range(i, j, 2):
            print(r, end=' ')
