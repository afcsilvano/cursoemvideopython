input('Pressione enter para iniciar: ')
soma = 0
for c in range (1, 500, 2):
        if c % 3 == 0:
                soma = soma + c
print('{}'.format(soma))
