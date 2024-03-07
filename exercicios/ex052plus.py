num = int(input('Digite o numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')