import random
p1 = str(input('Insira o nome do primeiro: '))
p2 = str(input('Insira o nome do segundo: '))
p3 = str(input('Insira o nome do terceiro: '))
p4 = str(input('Insira o nome do quarto: '))
lista = [p1,p2,p3,p4]
e = random.choice(lista)
print(f'O escolhido foi {e}')