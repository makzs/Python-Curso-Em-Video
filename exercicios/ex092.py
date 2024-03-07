from datetime import date
atual = date.today().year
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = atual - (int(input('Ano de nascimento: ')))
pessoa['ctps'] = int(input('Carteira de trabalho: (0 se não tiver) '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (atual - pessoa['contratação']))
print()
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')