import random
from time import sleep
nome = input('''Olá, nem te vi aí! Qual o seu nome?
Digite seu nome: ''')
print('\033[1;32mEu me chamo {}.\033[m'.format(nome))
print('...')
sn = str(input('Muito prazer {}!, eu me chamo Matheus, vamos jogar um jogo? [S/N]: '.format(nome))).upper()
while sn != 'S' and sn != 'N':
    print('\033[31mEsse dígito não é válido, somente digite S para sim ou N para não.\033[m')
    sn = str(input('Muito prazer {}!, eu me chamo Matheus, vamos jogar um jogo? [S/N]: '.format(nome))).upper()
if sn == 'S':
    print('\033[1;32mVamos.\033[m')
    sleep(0.5)
    print('Legal! Vamos lá.')
    sleep(0.3)
    print('''O jogo é simples, eu vou pensar em um número de 0 a 10 e você tem que
adivinhar em qual número eu estou pensando.''')
    sleep(1)
    input('Digite enter para iniciar: ')
    print('\033[1;32mVamos começar.\033[m')
    na = random.randint(0, 10)  #numero aleatorio
    sleep(1)
    nj = int(input('Digite o número: '))  #numero jogador
    nt = 1  #numero tentativas
    while nj != na:
        print('ERROOU, tente outro número.')
        sleep(0.2)
        nj = int(input('Digite o número: '))
        nt += 1
    print('Parabéns! eu escolhi o número {}. Você precisou de {} palpites para acertar.'.format(na, nt))
elif sn == 'N':
    sleep(0.2)
    print('\033[1;32mNão, valeu.\033[m')
    sleep(0.5)
    print('Ok, tudo bem, talvez mais tarde.')
