def lin():
    print(20 * '-')
def area(l, c):
    a = l * c
    print(f'A area de um terreno de {l}x{c} é de {a:.1f}m²')


print('Controle de terrenos')
lin()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)