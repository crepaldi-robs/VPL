n = int(input("Digite o valor de n: "))
i = 1
# modifique a condicao na linha abaixo
while i * (i + 1) * (i + 2) < n:
    i = i + 1

if i * (i + 1) * (i + 2) == n:
    print("sim")
else:
    print("nao")
# exibir "sim" se for triangular,
# "nao" caso contrario
