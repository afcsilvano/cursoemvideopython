import math
co = float(input('qual o cateto oposto? '))
ca = float(input('qual o cateto adjacente? '))
hip = math.sqrt((co**2)+(ca**2))
print('O valor da hipotenusa é de {:.2f}!'.format(hip))
