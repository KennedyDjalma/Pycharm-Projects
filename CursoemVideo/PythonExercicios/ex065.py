'''
-------------------------------------------------
65-
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MEDIA
ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR
VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO
SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
-------------------------------------------------
'''

resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / quantidade
print('Voce digitou {} numeros e a media foi {}.'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
