def leiaint(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('ERRO, por favor digite um valor valido.')
            continue
        except (KeyboardInterrupt):
            print('O usuario decidiu nao inserir o valor.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc