import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('hmmm, pelos meus cálculos...')
print('o seno desse ângulo equivale a {:.2f}'.format(sen))
print('o cosseno desse ângulo equivale a {:.2f}'.format(cos))
print('a tangente desse ângulo equivale a {:.2f}'.format(tg))
