'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
67
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS,
UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO
FOR NEGATIVO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

while True:
    n = int(input('Quer ver a tabuada de qula valor? '))
    if n < 0:
        break
    print('_-'*26)

    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

    print('_-'*26)
print('FIM DO PROGRAMA')