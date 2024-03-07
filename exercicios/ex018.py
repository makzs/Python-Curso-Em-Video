import math
a = float(input('Insira o valor do angulo: '))
seno = math.sin(math.radians(a))
print(f'O angulo {a} tem seno de {seno:.2f}')
cosseno = math.cos(math.radians(a))
print(f'O cosseno de {a} é de {cosseno:.2f}')
tangente = math.tan(math.radians(a))
print(f'A tangente de {a} é igual a {tangente:.2f}')

