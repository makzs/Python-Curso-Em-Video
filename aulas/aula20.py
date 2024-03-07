#def lin():
#    print('-' * 30)
#
#
#lin()
#print('CURSO EM VIDEO')
#lin()
#print('GUSTAVO')
#lin()
#print('APRENDER PYTHON')
#lin()
#
#def mensagem(msg):
#    print(30 * '-')
#    print(msg)
#    print(30 * '-')
#
#mensagem(' CURSO EM VIDEO ')
#mensagem(' APRENDA PYTHON ')
#
#a = 4
#b = 5
#s = a + b
#print(s)
#a = 8
#b = 9
#s = a + b
#print(s)
#a = 2
#b = 1
#s = a + b
#print(s)
#print()
#
#def soma(a, b):
#    s = a + b
#    print(s)
#
#
#soma(4, 5)
#soma(8, 9)
#soma(2, 1)
#
#def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#   print(f'A soma A + B = {s} ')
#
#
#soma(b=4, a=5)
#
#def contador(*num):
#    for valor in num:
#        print(f'{valor}', end=' ')
#    print('FIM')
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} numeros!')
#
#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)
#
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)