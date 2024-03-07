v = float(input('Qual é a velocidade do carro em Km/h? '))
if v > 80:
    print('PARE IMEDIATAMENTE!')
    m = (v - 80) * 7
    print(f'Voce ultrapassou o limite de velocidade e foi multado em {m:.2f}R$!')
else:
    print('Você esta dentro do limite de velocidade muito bem!')
print('Tenha um bom dia, dirija com segurança!')
