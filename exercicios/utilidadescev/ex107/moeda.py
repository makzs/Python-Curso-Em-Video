def metade(p):
    p = p / 2
    return p


def dobro(p):
    p = p * 2
    return p


def aumentar(p, n):
    p = p + (p * n/100)
    return p


def diminuir(p, n):
    p = p - (p * n/100)
    return p


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.',',')