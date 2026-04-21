'''
-------------------------------------------------
64-
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
PELO TECLADO. O PROGRAMA SO VAI PARAR QUANDO O USUARIO
DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL,
MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA
ENTRE ELES (DESCONSIDERANDO O FLAG).
-------------------------------------------------
'''

numero = contador = soma = 0
numero = int(input('Digite um numero [999 para parar]: '))

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(contador, soma))
