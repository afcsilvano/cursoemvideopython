from time import sleep
print(19*'\033[1;31m=\033[m')
print('10 PRIMEIROS TERMOS DE UMA P.A.')
print(19*'\033[1;31m=\033[m')
sleep(0.5)
termo = int(input('Digite o primeiro termo: '))
progressao = int(input('Digite a progressão: '))
pa = 0
c = 0
print('{}'.format(termo), end=' ')
while c < 9:
    c += 1
    pa = termo + (c * progressao)
    print('{}'.format(pa), end=' ')
