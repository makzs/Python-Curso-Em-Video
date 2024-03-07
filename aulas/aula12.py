nome = str(input('Qual é o seu nome? '))
if nome == 'Erik':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum aqui no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome ruinzinho')
print(f'Tenha um bom dia {nome}')

