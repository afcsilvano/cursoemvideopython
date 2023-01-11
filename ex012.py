pa = float(input('Qual é o preço atual do produto? '))
print('Com 5% de desconto, o preço irá de R${:.2f} para R${:.2f}'.format(pa, pa-((pa/100)*5)))
