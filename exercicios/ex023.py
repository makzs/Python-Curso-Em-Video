#impossivel fazer sem o if ou repetição
#num = int(input('Insira um numero de 0 a 9999: '))
#n = str(num)
#print(f'Analisando o numero {num}')
#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')
#
#forma matematica:
num = int(input('Insira um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
