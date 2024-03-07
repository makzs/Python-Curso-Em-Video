def leiaint(valor):
    while valor.isnumeric() == False:
        print('ERRO! VALOR NÃO É NUMERICO')
        valor = input('Tente novamente: ')
    print('Valor numerico digitado!')
    print(f'O valor é igual a {valor}')


n = input('Digite um valor: ')
leiaint(n)