from time import sleep
print('Vamos descobrir qual é o maior numero!')
a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo numero: '))
c = float(input('Insira o terceiro numero: '))
print(f'Seus números são {a}, {b}, e {c}')
print('Processando...')
sleep(2)
if a > b and a > c:
    print(f'O número {a} é o maior!')
    if b > c:
        print(f'E o {c} é o menor!')
    else:
        print(f'E o {b} é menor! ')
elif b > c:
    print(f'O número {b} é o maior!')
    if a > c:
        print(f'E o {c} é o menor!')
    else:
        print(f'E o {a} é o menor!')
else:
    print(f'O número {c} é o maior!')
    if a > b:
        print(f'E o {b} é o menor!')
    else:
        print(f'E o {a} é o menor!')
print('Fim da analise')