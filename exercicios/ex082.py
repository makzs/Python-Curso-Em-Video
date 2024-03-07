lista = []
listapar = []
listaimpar = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Esse valor esta na lista tente novamente')
    else:
        lista.append(valor)
        if valor % 2 == 0:
            listapar.append(valor)
        else:
            listaimpar.append(valor)
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opcao == 'N':
            break
print(f'A lista completa é {lista}')
print(f'A lista dos pares é {listapar}')
print(f'A lista dos impares é {listaimpar}')