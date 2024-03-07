num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para converter: 
\033[31m [ 1 ] converter para BINARIO \033[m
\033[34m [ 2 ] converter para OCTAL \033[m
\033[33m [ 3 ] converter para HEXADECIMAL \033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para \033[1;31m BINARIO \033[m é igual a \033[31m {bin(num)[2:]}\033[m!')
elif opcao == 2:
    print(f'{num} convertido para \033[1;34m OCTAL \033[m é igual a \033[34m {oct(num)[2:]}\033[m!')
elif opcao == 3:
    print(f'{num} convertido para \033[1;33m HEXADECIMAL \033[m é igual a \033[34m {hex(num)[2:]}\033[m!')
else:
    print('Opção invalida! tente novamente')