soma = 0
while True:
    n = int(input('Digite um numero'))
    if n == 999:
        break
    soma += n
print(f'A soma dos numero é igual a {soma}')