print(30 * '=-')
print('10 TERMOS DE UMA PA')
print(30 * '=-')
i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = i + (10 - 1) * r
for c in range(i, f + r, r):
    print(c, end=' -> ')
print('FIM')

#gambiarra que fiz pra funcionar tbm:
#if r > 1:
#    f = 10 * r
#else:
#    f = 11 * r
#for c in range(i, f, r):
#    print(c, end=' -> ')
#    if c < 10:
#        f = +1