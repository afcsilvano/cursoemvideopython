valor = float(input('Digite o valor do produto: '))
forma = int(input('''Qual será a forma de pagamento?
[1] cartão
[2] dinheiro
'''))
if forma == 1:
    fpg = int(input('Em quantas vezes o pagamento será feito? '))
    if fpg == 1:
        vf = valor - valor / 100 * 5
    elif fpg == 2:
        vf = valor
    elif fpg > 2:
        vf = valor + valor/100*20
else:
    vf = valor - valor / 10
print ('O valor total a pagar é R${:.2f}.'.format(vf))




