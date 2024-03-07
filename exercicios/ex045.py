import random
import time
from time import sleep
nome = ''
nomec = ''
print(30 * '--')
print('!JOGO DO PEDRA PAPEL TESOURA!')
print(30 * '--')
print('''Qual é a sua jogada? 
\033[1;31m[ 1 ] pedra\033[m
\033[1;32m[ 2 ] papel\033[m
\033[1;33m[ 3 ] tesoura\033[m ''')
opcao = int(input())
if opcao == 1:
    nome = 'pedra'
elif opcao == 2:
    nome = 'papel'
elif opcao == 3:
    nome = 'tesoura'
computador = random.randint(1, 3)
if computador == 1:
    nomec = 'pedra'
elif computador == 2:
    nomec =  'papel'
elif computador == 3:
    nomec = 'tesoura'
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
if opcao == computador:
    print(10 * '=-')
    print(f'Computador jogou {nomec}')
    print(f'Jogador jogou {nome}')
    print(10 * '=-')
    print('EMPATE!')
elif opcao == 1 and computador == 3 or opcao == 2 and computador == 1 or opcao == 3 and computador == 2:
    print(10 * '=-')
    print(f'Computador jogou {nomec}')
    print(f'Jogador jogou {nome}')
    print(10 * '=-')
    print('Você me derrotou! :(')
elif opcao == 3 and computador == 1 or opcao == 1 and computador == 2 or opcao == 2 and computador == 3:
    print(10 * '=-')
    print(f'Computador jogou {nomec}')
    print(f'Jogador jogou {nome}')
    print(10 * '=-')
    print('EU GANHEI HAHAHAHA mais um passo para a revolução das maquinas!')
else:
    print('Que jogada é essa? isso é pedra papel tesoura! tente novamente')