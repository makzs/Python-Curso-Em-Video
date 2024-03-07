n = int(input('Insira o numero que voce deseja saber a tabuada: '))
for c in range(1, 11):
    multi = n * c
    print(f'\033[31m{c} x {n}\033[m = \033[34m{multi}\033[m')