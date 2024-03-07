print(30 * '-')
print('BANCO BONDA 3')
print(30 * '-')
valor = float(input('Que valor voce deseja sacar? R$'))
quant50 = 0
quant20 = 0
quant10 = 0
quant1 = 0
while True:
    if valor > 0:
        if valor >= 50:
            valor -= 50
            quant50 += 1
        else:
            if valor >= 20:
                valor -= 20
                quant20 += 1
            else:
                if valor >= 10:
                    valor -= 10
                    quant10 += 1
                else:
                    if valor >= 1:
                        valor -= 1
                        quant1 += 1
                    else:
                        valor = 0
    else:
        break
print(print(30 * '-'))
print(f'quantidade de notas de 50: \033[31m{quant50}\033[m')
print(f'Quantidade de notas de 20: \033[31m{quant20}\033[m')
print(f'Quantidade de notas de 10: \033[31m{quant10}\033[m')
print(f'Quantidade de notas de 1: \033[31m{quant1}\033[m')
print(30 * '-')
