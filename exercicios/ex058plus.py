from random import randint
computador = randint(0, 10)
print('Acabo de pensar em um numero entre 0 e 10')
print('Tente adivinhar qual foi!')
acertou = False
paplpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    paplpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente: ')
        elif jogador > computador:
            print('Menos.. Tente novamente: ')
print(f'Acertou com {paplpites} tentativas. Parabens!')