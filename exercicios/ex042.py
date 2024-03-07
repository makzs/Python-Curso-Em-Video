r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))
print(f'As retas são {r1},{r2} e {r3}')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triangulo!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Todos os lados são iguais!')
        print('Esse triangulo é equilatero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Dois lados são iguais!')
        print('Esse triangulo é isosceles!')
    else:
        print('Todos os lados são difirentes!')
        print('Esse triangulo é escaleno!')
else:
    print('Essas retas não podem formar um triangulo!')
#
# Linhas 7 a 15 também podem ser feitas:
# if r1 == r2 == r3:
#   print('EQUILATERO')
# if r1 != r2 != r3 != r1:
#   print('ESCALENO')
# else:
#   print('ISOSCELES')
#