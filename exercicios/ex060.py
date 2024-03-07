n = int(input('Digite um numero para calcular o fatorial: '))
multi = n
while n != 0:
    if n == 1:
        print(n, end='')
        break
    print(n, end=' x ')
    n -= 1
    multi = multi * n
print(f' = {multi}')

#from math import factorial -> mais facil