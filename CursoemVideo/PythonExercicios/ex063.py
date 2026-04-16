'''
63-
ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO
QUALQUER E MOSTRE NA TELA OS N
PRIMEIROS ELEMENTOS DE
UMA SEQUENCIADE FIBONACCI
EX:
0 - 1 - 1 - 2 - 3 - 5 - 8
------------------------------------------------
'''
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
