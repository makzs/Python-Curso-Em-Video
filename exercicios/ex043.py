peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))
imc = peso/(altura**2)
print(f'Seu peso é {peso}, sua altura é {altura} então seu IMC é igual a {imc:.1f}!')
if imc < 18.5:
    print('Você esta abaixo do peso!')
elif 18.5 <= imc < 25: # imc >= 18.5 and imc < 25
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')