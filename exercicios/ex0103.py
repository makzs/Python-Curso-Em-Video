def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols na partida!')


n = str(input('Insira o nome do jogador: '))
g = str(input('Insira o numero de gols do jogador: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else: ficha(n, g)