''' FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE
NA TELA O VALOR DE SENO, COSSENO E TANGENTE DESSE ANGULO'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
