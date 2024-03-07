# + -> adição
# - -> subtração
# * -> multiplicação
# / -> divisão
# ** -> potencia
# // -> divisão inteira
# % -> resto da divisão (modulo)
# == -> igual
# = -> recebe
# 5 // 2 == 2(o que deu) -> 5 % 2 == 1(o que sobrou)
# raiz quadrada -> **(1/2) elevado a meio
# raiz cubica -> **(1/3) elevado a um terço
#Ordem de precedencia:
# 1()
# 2**
# 3 *,/,//,%, -> quem aparecer primeiro
# 4 +, -
# -----------------------------------------------
# :20 em f -> adiciona 20 espaços para tal direção
#nome = input('Qual é o seu nome? ')
#print(f'Prazer em te conhecer {nome:20}!')
#print(f'Prazer em te conhecer {nome:>20}!')
#print(f'Prazer em te conhecer {nome:=^20}!')
#da pra usar o f para operações tbm
#n1 = int((input('Um valor: ')))
#n2 = int((input('Outro valor: ')))
#print(f'A soma vale {n1+n2}')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f} ', end='')
print(f'A divisão inteira é {di}, e a potencia é {e}')