def metade(p, format=False):
    p = p / 2
    return p if format is False else moeda(p)


def dobro(p, format=False):
    p = p * 2
    return p if format is False else moeda(p)


def aumentar(p, n, format=False):
    p = p + (p * n/100)
    return p if format is False else moeda(p)


def diminuir(p, n, format=False):
    p = p - (p * n/100)
    return p if format is False else moeda(p)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')