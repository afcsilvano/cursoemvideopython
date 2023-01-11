n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
if(n1>n2>n3):
    maior = n1
    menor = n3
if(n1>n3>n2):
    maior = n1
    menor = n2
if(n2>n1>n3):
    maior = n2
    menor = n3
if(n2>n3>n1):
    maior = n2
    menor = n1
if(n3>n2>n1):
    maior = n3
    menor = n1
if(n3>n1>n2):
    maior = n3
    menor = n2
print('O maior número é {}, já o menor é {}.'.format(maior, menor))

