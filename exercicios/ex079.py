lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Esse valor esta na lista! tente novamente')
    else:
        lista.append(valor)
        print('Esse valor não esta na lista')
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'A lista de numero que voce digitou em ordem é {sorted(lista)}')