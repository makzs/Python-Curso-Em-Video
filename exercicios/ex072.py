ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
     opcao = int(input('Digite um numero de 0 a 20: '))
     if opcao >= 0 <= 20:
            break
print(f'Voce digitou o numero {ext[opcao]}')