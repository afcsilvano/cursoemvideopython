import random
numeros_aleatorios = tuple(random.randint(1, 100) for c in range(5))
maior_valor = max(numeros_aleatorios)
menor_valor = min(numeros_aleatorios)
print(numeros_aleatorios)
print('O menor valor é {} e o maior é {}.'.format(menor_valor, maior_valor))
