from datetime import date
atual = date.today().year
cont = 0
contm = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano nasceu a {c}° pessoa? '))
    idade = (atual - nasc)
    if idade >= 18:
        cont += 1
    else:
        contm += 1
print(f'O numero de pessoas de menor idade é {contm}')
print(f'O numero de pessoas com maior idade é {cont}')