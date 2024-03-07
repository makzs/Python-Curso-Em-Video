print('10 TERMOS DE UMA PA feat WHILE')
i = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
valor = i
cont = 0
ncont = 0
x = 1
print(i, end=' -> ')
while cont != 9:
    valor += r
    if cont != 8:
        print(valor, end=' -> ')
    else:
        print(valor, end= ' -> PAUSA')
    cont += 1
while x != 0:
    x = int(input(' Deseja mostrar mais quantos termos? '))
    ncont = x + cont
    while cont != ncont:
        valor += r
        if cont != ncont-1:
            print(valor, end=' -> ')
        else:
            print(valor, end= ' -> PAUSA')
        cont += 1
print('Fim do programa')
