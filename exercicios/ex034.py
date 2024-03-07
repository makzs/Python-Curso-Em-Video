s = float(input('Insira o valor do seu salario: '))
if s > 1250:
    a = (s * 10 / 100)
    sn = s + a
    print(f'Seu salario de R${s:.2f} teve um aumento de R${a:.2f} e agora se tornou R${sn:.2f}!')
else:
    a = (s * 15 / 100)
    sn = s + a
    print(f'Seu salario de R${s:.2f} teve um aumento de R${a:.2f} e agora se tornou R${sn:.2f}! ')
print('Bom trabalho!')
