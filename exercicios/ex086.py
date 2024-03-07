lista = [[], [], []]
valor = 0
for c in range(0, 3):
    valor = int(input(f'Digite um valor para a posição [0, {c}]: '))
    lista[0].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor para a posição [1, {c}]: '))
    lista[1].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor para a posição [2, {c}]: '))
    lista[2].append(valor)
print(30 * '=-')
print(f' [   {lista[0][0]}   ] ', end=''), print(f' [   {lista[0][1]}   ] ', end=''), print(f' [   {lista[0][2]}   ] ')
print(f' [   {lista[1][0]}   ] ', end=''), print(f' [   {lista[1][1]}   ] ', end=''), print(f' [   {lista[1][2]}   ] ')
print(f' [   {lista[2][0]}   ] ', end=''), print(f' [   {lista[2][1]}   ] ', end=''), print(f' [   {lista[2][2]}   ] ')