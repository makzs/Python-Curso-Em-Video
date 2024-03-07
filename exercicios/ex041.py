from datetime import date
atual = date.today().year
nasc = int(input('Insira o ano de nascimento do atleta: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc}, agora em {atual} tem {idade} anos!')
if idade <= 9:
    print('Sua categoria é \033[1;31mMIRIM\033[m!')
elif idade <= 14:
    print('Sua categoria é \033[1;31mINFANTIL\033[m!')
elif idade <= 19:
    print('Sua categoria é \033[1;31mJUNIOR\033[m!')
elif idade <= 25:
    print('Sua categoria é \033[1;31mSENIOR\033[m!')
else:
    print('Sua categoria é \033[1;31mMASTER\033[m!')