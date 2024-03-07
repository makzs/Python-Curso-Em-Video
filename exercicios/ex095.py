lista = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador} jogou? '))
    gols.clear()
    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('resposta invalida')
    if opcao == 'N':
        break
print(50 * '-=')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print(40 * '-')
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(40 * '-')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print('ERRO não existe esse codigo')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')