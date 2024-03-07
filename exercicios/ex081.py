lista = []
cont = 0
while True:
    valor = int(input('Insira um valor: '))
    if valor in lista:
        print('Esse valor esta na lista tente novamente!')
    else:
        lista.append(valor)
        cont += 1
        print('Valor adicionado com sucesso!')
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Foram digitados {cont} numeros')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'Tem o numero 5 na lista!')
else:
    print('Não tem o numero 5 na lista!')