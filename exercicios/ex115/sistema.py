from lib import *
from lib.arquivo import *
from lib.interface import *
from time import sleep


arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resp = (menu(['Ver lista de pessoas', 'Cadastrar pessoa', 'Sair do sistema']))
    if resp == 1:
        # opção de listar o conteudo de um arquivo!
        lerArquivo(arquivo)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        print('Saindo do sistema até logo')
        break
    else:
        print('\033[31mErro! Digite uma opção valida!\033[m')
        sleep(2)
