print('Sequencia de fibonacci')
n = int(input('Quantos termos voce deseja mostrar? '))
f1 = 0
f2 = 1
f3 = 0
cont = 3
print(f'{f1} -> {f2}', end=' ')
while cont <= n:
    f3 = f1 + f2
    print(f' -> {f3}', end=' ')
    f1 = f2
    f2 = f3
    cont += 1
print('-> FIM')