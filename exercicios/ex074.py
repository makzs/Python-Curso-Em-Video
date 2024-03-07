import random
lista = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
        random.randint(1, 10), random.randint(1, 10),)
for n in lista:
    print(f'{n} ', end='')
print(f'\nO maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')