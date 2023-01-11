si = 0  #soma idades
for c in range (1,5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c))
    lista.append(int(input('Digite a idade da {}ª pessoa: '.format(c))))
    gen = int(input('''Selecione o gênero da {}ª pessoa:
     [1] masculino
     [2] feminino
     '''.format(c)))
    si += idade
    m = si/4
    if gen == 1:
        velho = max(lista)
print('A média de idade entre os selecionados é de {} anos.'.format(m))
print