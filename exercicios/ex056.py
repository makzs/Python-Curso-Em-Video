soma = 0
media = 0
idadem = 0
nomem = ''
contm = 0
for c in range(1, 5):
    nome = str(input(f'Qual é o nome da {c}° pessoa? ')).strip()
    idade = int(input(f'Qual é a idade da {c}° pessoa? '))
    sexo = int(input(f'Qual é o sexo da {c}° pessoa? [1] Masculino / [2] Feminino '))
    soma += idade
    if c == 1:
        idadem = idade
        nomem = nome
    if idade > idadem and sexo == 1:
        nomem = nome
        idadem = idade
    if sexo == 2 and idade > 21:
        contm += 1
media = soma / 4
print(f'O homem mais velho tem {idadem} anos e se chama {nomem}')
print(f'A media de idade do grupo é de {media}')
print(f'O numero de mulheres que tem mais de 21 anos é de {contm}')
# media de idade, nome do homem mais velho e quantas mulheres tem mais de 21 anos