cont18 = 0
conth = 0
contm = 0
while True:
    print(30 * '-')
    print('CADASTRE UMA PESSOA')
    print(30 * '-')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    elif sexo == 'M':
        conth += 1
    elif idade < 20 and sexo == 'F':
        contm += 1
    print(30 * '-')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('FIM DO PROGRAMA! ')
print(f'Total de pessoas com 18 anos: {cont18}')
print(f'Total de homens cadastrados: {conth}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {contm}')