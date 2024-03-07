maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input(f'Quanto pesa a {c}° pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi de {maior}')
print(f'O menor peso foi de {menor}')