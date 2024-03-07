import random
from time import sleep
print(80 * '=')
print('Irei pensar em numero entre 0 e 5 tente adivinhar!')
print(80 * '=')
npc = random.randint(0,5)
nus = int(input('Qual você acha que é o numero? '))
if nus > 5:
    print('Esse numero é invalido!')

if nus < 0:
    print('Esse numero é invalido! ')

print('Processando...')
sleep(2)
print(f'Eu pensei no número {npc} e você chutou {nus}')
if nus == npc:
    print('Parabens Você acertou!')
else:
    print('Você errou, mais sorte da proxima vez!')