'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
74
CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS ALEATORIOS
E COLOCAR EM TUPLA.
DEPOIS DISSO, MOSTRE A LISTAGEM DE NUMEROS GERADOS E
TAMBEM INDIQUE O MAIOR VALOR QUE ESTÃO NA TUPLA.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')