#temp = int(input('Quantos anos tem seu carro? '))
#if temp <= 3:
#    print('Carro novo!')
#else:
#    print('Lata velha em')
#print('FIM')
#
#em 3 linhas apenas:
#temp = int(input('Quantos anos tem seu carro? '))
#print('Carro novo!'if temp<=3 else'carro velho')
#print('FIM')
#
#nome = str(input('Qual seu nome? ')).strip()
#nome = nome.lower()
#if nome == 'erik':
#    print('Que nome bonito! ')
#else:
#    print('Seu nome é bobo')
#print(f'Tenha um bom dia {nome}')
#
n1 = float(input('Insira a sua primeira nota: '))
n2 = float(input('Insira a sua segunda nota: '))
n3 = float(input('Insira a sua terceira nota: '))
m = (n1 + n2 + n3) / 3
print(f'A sua média é {m}')
if m >= 6.0:
    print('Boa média parabens!')
else:
    print('Estude mais!')