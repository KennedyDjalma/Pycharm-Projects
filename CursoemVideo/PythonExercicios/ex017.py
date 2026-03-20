'''FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO
E DO CATETO ADJACENTE DE UM TRIANGULO OPOSTO E DO CATETO
ADJACENTE DE UM TRIANGUL RETANGULO, CALCULE E MOSTRE O
COMPRIMENTO DA HIPOTENUSA'''


''' co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))
hi = (co ** 2 + ca ** 2) ++ (1/2)
print('A hipotenusa vai medir {}'.format(hi)) '''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {}'.format(hi))