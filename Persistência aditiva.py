n = int(input("n: "))
i = 0  # persistencia aditiva
# Calcular persistencia sequencia a0, a1, ..., an
while True:
    m = 0
    while n > 0:
        m += n % 10
        n //= 10
    n = m
    i += 1
    if m // 10 == 0:
        break

print(i)  # Exibir persitencia aditiva
