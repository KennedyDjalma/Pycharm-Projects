'''
CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR
JOGAR JOKENPÔ COM VOCÊ.
'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)

print('\033[4;36m -= \033[0m' * 10)
print('O computador escolheu\033[1;35m {} \033[0m'.format(itens[computador]))
print('O jogador escolheu \033[2;34m {} \033[0m'.format(itens[jogador]))
print('\033[4;36m -= \033[0m' * 10)

if computador == 0:  # PEDRA
    if jogador == 0:
        print('\033[4;32m EMPATOU \033[m')
    elif jogador == 1:
        print('\033[4;32m JOGADOR VENCEU \033[m')
    elif jogador == 2:
        print('\033[4;32m PC VENCEU \033[m')
    else:
        print('\033[4;31m JOGADA INVALIDA \033[m')

elif computador == 1:  # PAPEL
    if jogador == 0:
        print('\033[4;32m PC VENCEU \033[m')
    elif jogador == 1:
        print('\033[4;32m EMPATOU \033[m')
    elif jogador == 2:
        print('\033[4;32m JOGADOR VENCEU \033[m')
    else:
        print('\033[4;31m JOGADA INVALIDA \033[m')

elif computador == 2:  # TESOURA
    if jogador == 0:
        print('\033[4;32m JOGADOR VENCEU \033[m')
    elif jogador == 1:
        print('\033[4;32m PC VENCE \033[m')
    elif jogador == 2:
        print('\033[4;32m EMPATOU \033[m')
    else:
        print('\033[4;31m JOGADA INVALIDA \033[m')
