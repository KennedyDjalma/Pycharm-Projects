'''
REFAÇA O DESAFIO 9, MOSTRANDO A  TABUADA DE UM NUMERO QUE
O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO FOR
'''

num = int(input('Tabuada de: '))
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(num, c, num * c))
    