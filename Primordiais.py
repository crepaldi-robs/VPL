def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


n = int(input("Digite n: "))
primordial = 1

for i in range(2, n+1, 1):
    if isPrime(i):
        primordial *= i

print(primordial)
