from time import sleep
print(19*'\033[1;31m=\033[m')
print('CALCULADORA DE FATORIAL')
print(19*'\033[1;31m=\033[m')
sleep(0.5)
numero = int(input('Para iniciar, digite o número: '))
fatorial = 1
numero2 = numero
print('\033[1;33mcalculando...\033[m')
sleep(3)
while numero2 > 1:
    fatorial *= numero2
    numero2 -= 1
print('O fatorial de {} é {}.'.format(numero, fatorial))
