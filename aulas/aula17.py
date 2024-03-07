#LISTAS SÃO MUTAVEIS []
# .append -> adicionar mais uma variavel
# .insert -> trocar o valor da variavel
# metodos de eliminação:
# del -> eliminar um valor da variavel digitando o indice
# pop -> eliminar valor da variavel (geralmente o ultimo mas da pra especificar)
# remove -> eliminar valor digitando o valor
# eliminando o valor os que tão na frente vão pra tras
#
#Organizar por ordem: valores.sort()
#Organizar por ordem reversa: valores.sort(reverse=true)
#
#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#print(num)
#num.sort()
#print(num)
#num.sort(reverse=True)
#print(num)
#print(f'Essa lista tem {len(num)} elementos')
#
#num = [2, 4, 9, 1]
#num.insert(2, 2)
#num.remove(2) # o remove só remove o primeiro 2 que aparece
#if 4 in num:
#    num.remove(4)
#else:
#    print('Não achei o numero 4')
#print(num)
#
#valores = []
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))
#
#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista')
#
#a = [2, 3, 4, 7]
#b = a
#b[2] = 8
#print(f'Lista A: {a}')
#print(f'Lista B: {b}')
# !!!! Os dois mudam pois o python cria uma ligação não uma copia
#
a = [2, 3, 4, 7]
b = a[:] # b recebe todos os itens de a, não criando uma copia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

