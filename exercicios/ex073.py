times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Ateltico-PR', 'Bahia',
         'Sao paulo', 'Fluminense', 'Sport Recife',
         'EC-Vitoria', 'Coritiba', 'Avai', 'Ponte preta',
         'Ateltico-GO')
print(30 * '-=')
print('Lista de times: ')
print(f'Lista de times {times}')
print(30 * '-=')
print(f'Os 5 primeiros são: {times[0:5]}')
print(30 * '-=')
print(f'Os 4 ultimos são: {times[-4:]}')
print(30 * '-=')
print(f'Em ordem alabetica: {sorted(times)}')
print(30 * '-=')
print(f'O chapecoense esta na {times.index("Chapecoense")} posição')