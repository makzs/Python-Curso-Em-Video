soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'insira seu {c}° numero inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Foram identificados {cont} numeros pares e a soma deles foi de {soma}')