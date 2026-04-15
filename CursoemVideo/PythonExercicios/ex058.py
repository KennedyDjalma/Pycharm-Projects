'''
58-
    MELHORE O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI
    'PENSAR' EM UM NUMERO ENTRE 0 E 10. SÓ QUE AGORA O
    JOGO VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO
    FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER
    -------------------------------------------------
'''

'''
pc = randint(0, 5) #O PC VSI ESCOLHER O NUMERO.
print('-=-' *20)
player = int(input('Em que numero eu pensei? '))
print('-=-' *20)
print('PROCESSANDO...')

if player == pc:
    print('VOCE ACERTOU!')
else:
    print('VOCE NAO ACERTOU!'
'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador e acabei de pensar em um numero entre 0 e 10')
print('será que voce consegue acertar?')

palpites = 0
acertou = False
while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Voce acertou com {} palpites'.format(palpites))


