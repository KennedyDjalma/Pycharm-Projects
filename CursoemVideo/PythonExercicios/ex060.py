'''
    ----------------------------------------------
60-
    FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E
    MOSTRE O SEU FATORIAL.
    EX:
    5 ! = 5 X 4 X 3 X 2 X 1 = 120
    ---------------------------------------------
'''

from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ' , end=' ')
    f *= c
    c -= 1
print('{}.'.format(f))



