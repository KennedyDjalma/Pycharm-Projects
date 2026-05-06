'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
68
FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O PC.
O JOGADOR SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE
CONQUISTOU NO FINAL DO JOGO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('\033[0;32mPar ou impar? [P / I] \033[m')).strip().upper()[0]
    print(f'Você jogou {jogador} e o pc {pc} total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('GANHOU')
            v += 1
        else:
            print('GAME OVER')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('GANHOU')
            v += 1
        else:
            print('GAME OVER')
            break
print(f'FIM DE JOGO! Voce venceu {v} vezes.')