# help(print)
#
#def contador(i,f,p):
#    """
#    -> Faz uma contagem e mostra na tela
#    :param i: inicio da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    HaCkEd By AnGeL oF ThE nIgHT
#    """
#    c = i
#    while c <= f:
#        print(f'{c}', end=' ')
#        c += p
#    print('Fim')
#
#help(contador)
#
#def somar(a=0,b=0,c=0): #parametro opcional
#    """
#    -> somar até tres valores
#    :param a: primeiro valor
#    :param b: segundo valor
#    :param c: terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma vale {s}')
#
#
#somar(1, 5, 12)
#somar(b=3, c=2)
#somar()
#help(somar)
#
#def teste(b):
#    global y
#    y = 8
#    x = 9 # escopo local
#    a = 8 #escopo local
#    b += 4
#    print(f'Na função teste, y vale {y}')
#    print(f'Na função teste, b vale {b}')
#    print(f'Na função teste, a vale {a}')
#   print(f'Na função teste, x vale {x}')
#    print(f'Na função teste n vale {n}')
#
#
#n = 2 #escopo global
#a = 5 #escopo global
#y = 7 #escopo global
#print(f'No programa principal, y vale {y}')
#print(f'No programa principal, a vale {a}')
#print(f'No programa principal, n vale {n}')
#print(f'No programa principal, x vale {x}') -> vai dar erro pois o escopo era local e nao global
#teste(a)
#
#def somar(a=0, b=0, c=0):
#    s = a + b + c
#    return s
#
#
#r1 = somar(3, 2, 5)
#r2 = somar(2, 2)
#r3 = somar(6)
#
#print(f'Os resultados foram {r1}, {r2}, {r3}')
#
#def fatorial(num=1):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#   return f
#
#
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os resultados são {f1}, {f2}, {f3}')
#
def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('é par!')
else:
    print('Não é par!')