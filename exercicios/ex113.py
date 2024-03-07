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


def leiafloat(valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print('ERRO, por favor digite um valor valido.')
            continue
        except (KeyboardInterrupt):
            print('O usuario decidiu nao inserir o valor.')
            return 0
        else:
            return n


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')