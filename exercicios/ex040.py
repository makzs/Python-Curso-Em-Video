import time
from time import sleep
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota1 + nota2) / 2
print('Processando...')
time.sleep(2)
print(f'Sua média é {m}')
if m < 5:
    print(f'você foi \033[1;31mREPROVADO\033[m!')
elif m >= 5 and m < 7:
    print(f'Você esta de \033[1;33mRECUPERAÇÃO\033[m!')
else:
    print(f'Você foi \033[1;32mAPROVADO\033[m!')