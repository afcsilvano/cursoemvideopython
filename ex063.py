from time import sleep
print(19*'\033[1;31m=\033[m')
print('SEQUÊNCIA DE FIBONACCI')
print(19*'\033[1;31m=\033[m')
sleep(0.5)
n = int(input('Digite quantos elementos você deseja ver: '))
t1 = 0
t2 = 0
t3 = 1
while t1 < n:
    print('{}'.format(t2), end=' ')
    t4 = t2
    t2 = t3
    t3 += t4
    t1 += 1
