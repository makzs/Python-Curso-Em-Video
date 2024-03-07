t = int(input('Quantos dias alugados? '))
d = float(input('Quantos Km rodados? '))
p = (t * 60) + (d * 0.15)
print(f'O total a pagar é de R${p:.2f} ')
