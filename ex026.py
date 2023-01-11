frase = input('digite uma frase: ')
frasens = frase.strip()
mfrase = frasens.lower()
na = mfrase.count('a')
pia = (mfrase.find('a')+1)
pfa = (mfrase.rfind('a')+1)
print('Na frase "{}" a letra "a" aparece {} vezes, sendo pela primeira vez na posição {},e pela última na posição {}.'.format(frasens, na, pia, pfa))


