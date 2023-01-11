nc = input('Digite seu nome completo: ').strip()
nm = nc.split()
n1 = nm[0]
n2 = nm[len(nm)-1]
print('O seu primeiro nome é {},e o último é {}.'.format(n1, n2))
