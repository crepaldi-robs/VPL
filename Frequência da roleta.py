def main():
    # Escreva seu programa aqui
    n = int(input('Digite n:'))

    l = []
    for i in range(37):
        l.append(0)

    for i in range(n):
        x = int(input('Lancamento:'))
        l[x] += 1

    cont_inutil = 0

    for i in range(37):
        if l[i] == 0:
            cont_inutil += 1
        elif l[i] == 1:
            print(f'Numero {i} ocorreu {l[i]} vez')
        else:
            print(f'Numero {i} ocorreu {l[i]} vezes')


# NAO ALTERE O TRECHO ABAIXO
if __name__ == "__main__":
    main()
