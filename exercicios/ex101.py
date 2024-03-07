from datetime import date
def voto(nasc):
    atual = date.today().year
    idade = atual - nasc
    print(f'Com {idade} anos ')
    if 15 < idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    elif idade >= 18:
        return 'VOTO OBRIGATORIO'
    elif idade <= 15:
        return 'NÃO VOTA'


nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))