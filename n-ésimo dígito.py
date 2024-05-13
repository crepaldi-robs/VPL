def nesimo(a, n):
    aux, sz = a, 0
    while aux > 0:
        aux //= 10
        sz += 1

    aux = a
    for i in range(sz-n):
        aux //= 10
    if n > sz:
        aux = 0

    return aux % 10
