print('10 TERMOS DE UMA PA feat WHILE')
i = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
valor = i
cont = 0
print(i, end=' -> ')
while cont != 9:
    valor += r
    if cont != 8:
        print(valor, end=' -> ')
    else:
        print(valor, end= ' -> FIM')
    cont += 1