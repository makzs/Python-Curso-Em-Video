import random
cont = 0
while True:
    print('Vamos jogar par ou impar:')
    escolha = (str(input('Deseja ser par ou impar? [P/I] '))).strip().upper()[0]
    if escolha == 'P' or 'I':
        jogador = int(input('Que numero ira jogar? (1 a 10) '))
        computador = random.randint(1, 10)
        soma = jogador + computador
        print(f'Eu joguei {computador} e voce jogou {jogador}, no total foi {soma}')
        if escolha == 'P':
            if soma % 2 == 0:
                print('Voce venceu parabens! vamos jogar novamente!')
                cont += 1
            else:
                print('HAHA parece que eu venci, toma essa!')
                break
        if escolha == 'I':
            if soma % 2 != 0:
                print('Voce venceu parabens! vamos jogar novamente!')
            else:
                print('HAHA parece que eu venci, toma essa!')
                break
    else:
        print('Resposta invalida, tente novamente!')
print(f'Jogo finalizado, voce venceu {cont} vezes')