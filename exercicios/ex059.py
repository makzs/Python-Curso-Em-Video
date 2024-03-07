import time
opcao = 0
a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
while opcao != 5:
    print('O que deseja realizar com esses valores?')
    print(''' 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa ''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = a + b
        print('Processando...')
        time.sleep(1)
        print(f'A soma de {a} e {b} é igual a {soma}')
    elif opcao == 2:
        multi = a * b
        print('Processando...')
        time.sleep(1)
        print(f'A multiplicação de {a} e {b} é igual a {multi}')
    elif opcao == 3:
        if a > b:
            print(f'O valor {a} é maior que o valor {b}')
        else:
            print(f'O valor {b} é maior que o valor {a}')
    elif opcao == 4:
        a = int(input('Insira um novo valor: '))
        b = int(input('Insira um novo valor: '))
    elif opcao == 5:
        print('Desligando Programa...')
        time.sleep(1)
    else:
        print('Opção invalida! Tente novamente!')
print('Fim do programa! Volte sempre!')