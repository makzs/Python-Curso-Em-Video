soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print(soma)
print(f'Esses foi a soma dos {cont} impares multiplos de tres')