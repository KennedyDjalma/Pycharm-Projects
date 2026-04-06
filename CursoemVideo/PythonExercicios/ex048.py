'''
FAÇA UM PROGRAMA QUE CALCULE A SOMA DE TODOS OS NUMEROS IMPAR
QUE SÃO MULTIPLOS DE 3 E QUE SE ENCONTRAM NO INTERVALO DE
1 ATÉ 500.
'''

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print ('A soma de todos os {} numeros é {}'.format(contador, soma))
