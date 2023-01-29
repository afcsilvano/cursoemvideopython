tn = num = soma = 0
while True:
    num = int(input('Digite um valor: '))
    if num != 999:
        soma += num
        tn += 1
    else:
        break
print('A soma entre os {} valores digitados é {}'.format(tn, soma))
