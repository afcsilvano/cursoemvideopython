from datetime import date  # importacao data
t = 0  # total maior
m = 0  # total menor
for c in range(1, 8):  # repeticao
    d = int(input('Digite o {}° ano de nascimento: '.format(c)))  # datas
    a = date.today().year  # ano atual
    i = a - d  # idade
    if i > 17:
        t += 1
    else:
        m += 1
print('{} pessoas são maiores de idade.'.format(t))