import time
print(30 * '==')
print('Bem vindo ao Banco Fleeca!')
print(30 * '==')
sal = float(input('Qual é o valor de seu salario? '))
casa = float(input('Qual é o valor da casa que deseja comprar? '))
ano = float(input('Em quantos anos deseja pagar a casa? '))
print('Processando...')
time.sleep(2)
prestacaon = (casa / ano)
prestacaom = ( casa / ano) / 12
print(f'Sua prestação anual vai ser de R${prestacaon:.2f}!')
print(f'Sua prestação mensal vai ser de R${prestacaom:.2f}!')
seguro = sal * 30 / 100
if prestacaom <= seguro:
    print('Compra aprovada')
else:
    print(f'Compra reprovada, sua parcela de {prestacaom:.2f} é maior que 30% de seu salario: {seguro}')

