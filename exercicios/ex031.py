d = float(input('Insira a distancia de sua viagem em Km: '))
if d <= 200:
    p = d * 0.50
    print(f'Sua viagem não é longa, vai lhe custar R${p:.2f}')
else:
    p = d * 0.45
    print(f'Sua viagem é longa vai lhe custar R${p:.2f}')
print('Boa viagem')