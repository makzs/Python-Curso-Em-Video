soma = 0
quantp = 0
barato = 0
baraton = ' '
print(30 * '-')
print('MERCADINHO DA ESQUINA')
print(30 * '-')
while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: R$'))
    if soma == 0:
        barato = preco
        baraton = nome
    if preco < barato:
        barato = preco
        baraton = nome
    soma += preco
    if preco > 1000:
        quantp += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja registrar mais um produto? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total gasto na compra foi de: R${soma:.2f}')
print(f'O total de produtos no valor acima de R$1000 foi de: {quantp}')
print(f'O produto mais barato foi {baraton} que custa R${barato:.2f}')