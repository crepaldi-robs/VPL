def media(lista: list) -> float:
    " Devolve a media dos elementos de 'lista'. "
    # fazer
    mean = 0
    for l in lista:
        mean += l
    mean = mean/len(lista)

    return mean


def acimade(lista: list, limiar: float) -> list:
    " Devolve lista com os elementos de 'lista' > 'limiar'. "
    # fazer
    resp = []
    for l in lista:
        if l > limiar:
            resp.append(l)

    return resp


def main():
    '''
    Funcao principal do programa

    Le um numero n > 0 e uma sequencia de n reais e exibe os numeros acima da
    media.
    '''
    # fazer
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(float(input()))

    print(acimade(seq, media(seq)))


# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    main()