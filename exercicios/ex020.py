import random
p1 = str(input('Insira o nome do primeiro aluno: '))
p2 = str(input('Insira o nome do segundo aluno: '))
p3 = str(input('Insira o nome do terceiro aluno: '))
p4 = str(input('Insira o nome do quarto aluno: '))
lista = [p1,p2,p3,p4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
