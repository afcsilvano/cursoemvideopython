from time import sleep
print(19*'\033[1;31m=\033[m')
print('\033[1mSEJA BEM-VINDO\033[m')
print(19*'\033[1;31m=\033[m')
sleep(0.5)
n1 = int(input('Digite o primeiro número: '))  # numero 1
n2 = int(input('Digite o segundo número: '))  # numero 2
sleep(1)
print(19*'\033[1;31m=\033[m')
print('\033[1mSELECIONE UMA DAS OPÇÕES\033[m')
print(19*'\033[1;31m=\033[m')
print('''[1] SOMAR
[2] MULTIPLICAR
[3] INFORMAR O MAIOR
[4] DIGITAR OUTROS NÚMEROS
[5] SAIR''')
opcao = int(input('Selecione a opção: '))
while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    print('\033[31messe dígito não é valido, tente novamente\033[m')
    sleep(0.5)
    print(19 * '\033[1;31m=\033[m')
    print('\033[1mSELECIONE UMA DAS OPÇÕES\033[m')
    print(19 * '\033[1;31m=\033[m')
    print('''[1] SOMAR
    [2] MULTIPLICAR
    [3] INFORMAR O MAIOR
    [4] DIGITAR OUTROS NÚMEROS
    [5] SAIR''')
    opcao = int(input('Selecione a opção: '))
while opcao == 4:
    print('\033[1;33maguarde...\033[m')
    sleep(1)
    n1 = int(input('Digite o primeiro número: '))  # numero 1
    n2 = int(input('Digite o segundo número: '))  # numero 2
    sleep(1)
    print(19 * '\033[1;31m=\033[m')
    print('\033[1mSELECIONE UMA DAS OPÇÕES\033[m')
    print(19 * '\033[1;31m=\033[m')
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] INFORMAR O MAIOR
[4] DIGITAR OUTROS NÚMEROS
[5] SAIR''')
    opcao = int(input('Selecione a opção: '))
if opcao == 1:
    r = n1 + n2
    print('A soma de {} e {} é {}'.format(n1, n2, r))
elif opcao == 2:
    r = n1 * n2
    print('A multiplicação de {} e {} é {}'.format(n1, n2, r))
elif opcao == 3:
    if n1 > n2:
        print('O maior número entre os escolhidos é {}.'.format(n1))
    elif n2 > n1:
        print('O maior número entre os escolhidos é {}.'.format(n2))
    else:
        print('Os dois números possuem o mesmo valor.')
elif opcao == 5:
    print('\033[1;31msaindo do programa...\033[m')
    sleep(1)
    print('\033[1;31mVocê saiu\033[m')
