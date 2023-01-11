from random import randint
print('''==========JOKENPÔ DO MATHEUS===========''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''[0] PEDRA
[1] PAPEL
[2] TESOURA
Digite sua opção: '''))
computador = randint(0, 2)
print('=-' * 11)
print('Você escolheu {}'.format(itens[jogador]))
print('Eu escolhi {}'.format(itens[computador]))
print('=-' * 11)
if computador == 0:
    if jogador == 0:
        print('Parece que empatamos, vamos jogar novamente.')
    elif jogador == 1:
        print('Hm, você venceu, quero jogar novamente.')
    elif jogador == 2:
        print('HA HA, ganhei de você!! vai querer uma revanche?')
elif computador == 1:
    if jogador == 0:
        print('HA HA, ganhei de você!! vai querer uma revanche?')
    elif jogador == 1:
        print('Parece que empatamos, vamos jogar novamente.')
    elif jogador == 2:
        print('Hm, você venceu, quero jogar novamente.')
elif computador == 2:
    if jogador == 0:
        print('Hm, você venceu, quero jogar novamente.')
    elif jogador == 1:
        print('Hm, você venceu, quero jogar novamente.')
    elif jogador == 2:
        print('Parece que empatamos, vamos jogar novamente.')
