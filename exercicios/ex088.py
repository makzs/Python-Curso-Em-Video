import random
import time
valores = list()
num = list()
cont = 0
print(50 * '-')
print(f'                   MEGA SENA          ')
print(50 * '-')
jogos = int(input('Qual o numero de jogos que deseja? '))
print(f'SORTEANDO {jogos} JOGOS')
for c in range(0, jogos):
    while cont != 6:
        randola = random.randint(1, 60)
        valores.append(randola)
        cont += 1
    num.append(valores)
    print(f'Jogo {c+1}: {valores}')
    time.sleep(0.5)
    valores = list()
    cont = 0
print(50 * '-')
print(f'Todos os jogos em uma lista: {num}')