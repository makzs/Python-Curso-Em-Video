#hipotenusa da maneira sem importação:
#co = float(input('Insira o valor do cateto oposto: '))
#ca = float(input('Insira o valor do cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa é {h:.2f}')
import math

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'A hipotenusa vai medir {h:.2f}')