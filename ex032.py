ano = int(input('Digite um ano: '))
ad = ano % 4
if(ad == 0):
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))