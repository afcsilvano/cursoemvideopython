s = float(input('Qual o seu salário? '))
ag = s + ((s/100)*15)
ap = s + ((s/100)*10)
if(s<=1250):
    print('Seu novo salário é R${:.2f}'.format(ag))
else:
    print('Seu novo salário é R${:.2f}'.format(ap))