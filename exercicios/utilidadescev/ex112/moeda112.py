def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO {entrada} é um preço invalido: ')
        else:
            valido = True
            return float(entrada)



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


def resumo(p, a=10, r=13):
    print(30 * '-')
    print('RESUMO DO VALOR'.center(30))
    print(30 * '-')
    print(f'Preço analisado:  \t{moeda(p)}')
    print(f'Dobro do preço:   \t{dobro(p, True)}')
    print(f'Metade do preço:  \t{metade(p, True)}')
    print(f'{a}% de aumento:  \t{aumentar(p, a, True)}')
    print(f'{r}% de redução:  \t{diminuir(p, r, True)}')
    print(30 * '-')


