valores = (int(input('Insira um valor: ')), int(input('Insira outro valor: ')),
            int(input('Insira mais um valor: ')), int(input('Insira o ultimo valor: ')),)
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'A posição que aparece o primeiro 3 é na {valores.index(3)} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=',')