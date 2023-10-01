#TABELA DA SÉRIE B 2023 (01/10/2023)
tabela = ('Vitória', 'Sport Recife', 'Juventude', 'Guarani', 'Novorizontino', 'Criciúma', 'Atlético-GO', 'Vila Nova',
          'Mirassol', 'CRB', 'Ceará', 'Botafogo-SP', 'Ituano', 'Sampaio Corrêa', 'Ponte Preta', 'Avaí', 'Chapecoense',
          'Tombense', 'Londrina', 'ABC')
resp = int(input('''[1] Ver o G5
[2] Ver o Z4
[3] Ver a tabela em ordem alfabética
[4] Ver a posição do Avaí
Selecione uma opção: '''))
if resp == 1:
    for time in tabela[:5]:
        print(time)
elif resp == 2:
    for time in tabela[16:]:
        print(time)
elif resp == 3:
    tabela_ordenada = sorted(tabela)
    for time in tabela_ordenada:
        print(time)
elif resp == 4:
    print('O Avaí se encontra na {}° posição da tabela'.format(tabela.index('Avaí')+1))
else:
    print('Opção não é válida, tente novamente.')
