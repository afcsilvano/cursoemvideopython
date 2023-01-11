d = float(input('Qual a distância da viagem? '))
dc = d * 0.50
dl = d * 0.45
if(d<=200):
    print('O valor da viagem é R${:.2f}.'.format(dc))
else:
    print('O valor da viagem é R${:.2f}.'.format(dl))
