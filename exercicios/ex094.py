lista = list()
mulheres = list()
pessoa = dict()
cont = 0
idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo? [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            if pessoa['sexo'] == 'F':
                mulheres.append(pessoa['nome'])
            break
        else:
            print('SEXO INVALIDO')
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']
    cont += 1
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('RESPOSTA INVALIDA')
    if opcao == 'N':
        break
print('FIM DO PROGRAMA')
print(lista)
print(30 * '-')
print(f'Foram cadastradas {cont} pessoas')
media = idade / cont
print(f'A media de idade das pessoas é de {media:5.2f}')
print(f'A lista de mulheres: {mulheres}')
print(f'A lista das pessoas com idades acima da media: ', end='')
if pessoa['idade'] >= media:
    print(pessoa)
print('ENCERRADO')