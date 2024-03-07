from time import sleep
from random import randint
def sorteio(lst):
    print('sorteando valores')
    for c in range(0, 5):
        n = randint(1, 20)
        sleep(0.3)
        numeros.append(n)
        print(n, end=' ', flush=True)
def somapar(total):
    total = 0
    for c, v in enumerate(numeros):
        if v % 2 == 0:
            total += v
            print('-> ', end='')
            print(f'{v}', end=' ')
    print()
    print(f'A soma dos numeros pares são {total}')


numeros = list()
print(sorteio(numeros))
print(somapar(numeros))