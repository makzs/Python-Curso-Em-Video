lista = list()
valores = list()
while True:
    nome = str(input('Nome: '))
    valores.append(nome)
    nota1 = float(input('1° Nota: '))
    valores.append(nota1)
    nota2 = float(input('2° Nota: '))
    valores.append(nota2)
    media = (nota1 + nota2) / 2
    valores.append(media)
    lista.append(valores)
    valores = list()
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(50 * '-=')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(30 * '-')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for c in range(0, len(lista)):
        if resposta == c:
            print(f'Notas de {lista[c][0]} são ', end='')
            print(lista[c][1], end=' e ')
            print(lista[c][2])
    if resposta == 999:
        break
print('PROGRAMA FINALIZADO')