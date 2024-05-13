n = int(input("Tamanho da sequencia (n > 2): "))
primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))

r = segundo / primeiro

cur = segundo
ant = primeiro

isPG = True
while n - 2 > 0:
    ant = cur
    cur = int(input('Digite o proximo numero: '))

    if cur / ant != r:
        isPG = False
    n -= 1

print(isPG)
