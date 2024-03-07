mont = 0
cont = 0
n = int(input('Digite um numero: '))
while n != 999:
    mont += n
    cont += 1
    n = int(input('Digite mais um numero (se deseja parar digite 999): '))
print(f'Voce digitou {cont} numeros e a soma entre eles foi igual a {mont}')