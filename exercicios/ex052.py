n = int(input('Insira um numero inteiro: '))
cont = 0
for c in range(1, 11):
    d = n % c
    if d == 0:
        cont += 1
if n != 1:
    if cont > 2:
        print('Não é um numero primo!')
    else:
        print('é um numero primo!')
else:
    print('Não é um numero primo!')