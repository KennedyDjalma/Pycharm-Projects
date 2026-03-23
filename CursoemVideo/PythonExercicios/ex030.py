'''
CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA
SE ELE É PAR OU IMPAR.
'''

num = int(input('Digite um numero inteiro: '))
resultado = num % 2
print('o resultado foi {}'.format(resultado))
if resultado == 0:
    print('{} é um numero par'.format(num))
else:
    print('{} é um numero impar'.format(num))

