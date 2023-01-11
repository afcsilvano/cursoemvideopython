from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento do atleta: '))
idade = atual - nasc
if idade <= 9:
    print('O atleta possui {} anos e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta possui {} anos e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta possui {} anos e está na categoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta possui {} anos e está na categoria SÊNIOR.'.format(idade))
else:
    print('O atleta possui {} anos e está na categoria MASTER.'.format(idade))
