'''
FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL,
MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
'''

maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))
