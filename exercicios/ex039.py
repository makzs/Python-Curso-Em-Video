from datetime import date
atual = date.today().year
data = int(input('Digite o ano de seu nascimento: '))
anos = atual - data
print(f'Quem nasceu em {data} tem {anos} anos em {atual}')
if anos < 18:
    prazo = 18 - anos
    futuro = atual + prazo
    print(f'Ainda não é hora de se alistar! falta {prazo} anos')
    print(f'Seu alistamento vai ser no ano de {futuro}')
elif anos == 18:
    print('É hora de se alistar!')
else:
    prazo = anos - 18
    passado = atual - prazo
    print(f'Ja passou {prazo} anos do alistamento!')
    print(f'Seu alistamento foi em {passado}')