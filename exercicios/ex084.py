rapazeada = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(rapazeada) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    rapazeada.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print(30 * '-')
print(f'Voce cadastrou {len(rapazeada)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in rapazeada:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso doi do {menor}Kg. Peso de ', end='')
for p in rapazeada:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
