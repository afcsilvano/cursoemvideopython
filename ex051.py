print('=' * 21)
print('10 TERMOS DE UMA P.A.')
print('=' * 21)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = t1 + (10-1) * r
for c in range(t1, dec + r, r):
    print('{}'.format(c), end=' ')
