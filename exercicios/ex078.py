lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Insira um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'Voce digitou o valores: {lista}')
print(f'O maior valor da lista foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor da lista foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()