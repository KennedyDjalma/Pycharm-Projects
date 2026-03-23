'''
ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO
INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR
QUAL FOI O NUMERO ESCOLHIDO PELO PC. O PROGRAMA DEVERÁ
ECREVER NA TELA SE O USUARIO VENCEU OU NÃO.
'''

from random import randint
from time import sleep

pc = randint(0, 5) #O PC VSI ESCOLHER O NUMERO.
print('-=-' *20)
player = int(input('Em que numero eu pensei? '))
print('-=-' *20)
print('PROCESSANDO...')

if player == pc:
    print('VOCE ACERTOU!')
else:
    print('VOCE NAO ACERTOU!')