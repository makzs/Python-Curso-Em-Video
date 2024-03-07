while True:
    n = int(input('Qual numero deseja ver a tabuada? '))
    if n < 0:
        break
    print(50 * '-')
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print(50 * '-')
print('Fim do programa!')