import random
print(30 * '=-')
print('JOGO DE ADVINHAÇÃO')
print(30 * '=-')
computador = random.randint(1, 10)
print('Pensei em um numero entre 1 e 10, tente adivinhar qual é!')
palpite = int(input('Qual é o seu palpite? '))
cont = 1
while palpite != computador:
    palpite = int(input('Errou! qual sua proxima tentativa? '))
    cont += 1
print(f'Parabens voce acertou que eu pensei no {computador}!')
print(f'Voce precisou de {cont} tentativas')