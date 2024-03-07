jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print(30 * '-')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'Na partida {c}, fez {jogador["gols"][c]}')
print(f'Foi um total de {jogador["total"]} gols')
