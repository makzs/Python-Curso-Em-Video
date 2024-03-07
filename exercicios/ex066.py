cont = 0
soma = 0
while True:
    n = (int(input('Digite um numero: ')))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} numeros e a soma entre eles é igual a {soma}!')