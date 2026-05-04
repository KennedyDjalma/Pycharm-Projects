'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
66
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUARIO
DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL
MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA
ENTRE ELES (DESCONSIDERANDO O FLAG.)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

n = s = c = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print('A soma dos {} numeros vale {}.'.format(c, s))
