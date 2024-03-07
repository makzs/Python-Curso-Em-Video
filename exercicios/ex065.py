soma = 0
cont = 0
opcao = 'S'
n = int(input('Digite um valor: '))
maior = n
menor = n
while opcao == 'S':
    soma += n
    cont += 1
    n = int(input('Digite mais um numero: '))
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print('Fim do programa!')
media = soma / cont
print(f'Voce digitou {cont} numeros e a media é igual a {media}')
print(f'O maior numero digitado foi o {maior}')
print(f'O menor numero digitado foi o {menor}')