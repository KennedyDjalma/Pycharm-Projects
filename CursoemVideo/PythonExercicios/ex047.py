'''
CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES
QUE ESTÃO NO INTERVALO ENTRE 1 E 50.
'''

''' EXEMPLO 1
for n in range(1, 50+1):
    if n % 2 == 0:
        print(n, end=' ')
'''

for n in range(2, 51, 2):
    print(n, end=' ')
