aluno = {}
aluno['nome'] = str(input('Insira o nome do aluno: '))
aluno['media'] = float(input('Insira a media do aluno: '))
if aluno['media'] > 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno[situação] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')