from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar imediatamente')
elif idade > 18:
    saldo = idade - 18
    print('''Já passou o tempo do seu alistamento.
    Você deveria ter se alistado há {} anos.'''.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('''Você ainda não tem idade para se alistar.
    Você deve se alistar daqui há {} anos.'''.format(saldo))
