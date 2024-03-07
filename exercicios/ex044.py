preco = float(input('Preço das compras R$:'))
print('''Como deseja pagar? 
\033[31m[ 1 ] A vista (10% de desconto)\033[m
\033[32m[ 2 ] A vista no cartão (5% de desconto)\033[m
\033[33m[ 3 ] Em até 2x no cartão (preço normal)\033[m
\033[34m[ 4 ] Em 3x ou mais no cartão (20% de juros!)\033[m ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    desc = preco - (preco * 10 / 100)
    print(f'Seu produto que custava R${preco:.2f} ficou por R${desc:.2f}!')
    print('Tenha um bom dia e volte sempre!')
elif opcao == 2:
    desc = preco - (preco * 5 / 100)
    print(f'Seu produto que custava R${preco:.2f} ficou por R${desc:.2f}!')
    print('Tenha um bom dia e volte sempre!')
elif opcao == 3:
    parc = preco / 2
    print(f'Seu produto foi dividido em duas parcelas de R${parc:.2f}!')
    print('Tenha um bom dia e volte sempre!')
elif opcao == 4:
    parc = int(input('Em quantas parcelas deseja pagar?'))
    preco = preco + (preco * 20 / 100)
    npreco = preco / parc
    print(f'Seu produto vai custar R${preco:.2f} divididas em {parc:.2f} parcelas no valor de R${npreco:.2f}')
    print('Tenha um bom dia e volte sempre!')
else:
    print('Opção invalida, tente novamente')
