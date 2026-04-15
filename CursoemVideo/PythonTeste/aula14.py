'''
for c in range(1, 10+1):
    print(c)
print('FIM')
'''

'''
c = 1
while c <= 10:
    print(c)
    c += 1
print('FIM')
'''

'''
r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    print('FIM')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))


'''
    -------------------------------------------------
    57-
    FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
    MAS SO ACEITE OS VALORES 'M' OU 'F'.
    CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE
    ATÉ TER UM VALOR CORRETO.
    -------------------------------------------------
    58-
    MELHORE O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI
    'PENSAR' EM UM NUMERO ENTRE 0 E 10. SÓ QUE AGORA O 
    JOGO VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO
    FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER
    -------------------------------------------------
    59- 
    CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE
    UM MENU NA TELA:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA
    EM CADA CASO.
    -------------------------------------------------
    60-
    FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E
    MOSTRE O SEU FATORIAL.
    EX:
    5 ! = 5 X 4 X 3 X 2 X 1 = 120
    -------------------------------------------------
    61-
    REFAÇA O EXERCICIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO
    DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSAO
    USANDO A ESTRUTURA WILE.
    -------------------------------------------------
    62-
    MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUARIO
    SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA
    ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR '0 TERMOS'.
    -------------------------------------------------
    63-
    ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO
    QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE
    UMA SEQUENCIADE FIBONACCI
    EX:
    0 - 1 - 3 - 5 - 8
    -------------------------------------------------
    64-
    CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
    PELO TECLADO. O PROGRAMA SO VAI PARAR QUANDO O USUARIO
    DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL,
    MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA
    ENTRE ELES (DESCONSIDERANDO O FLAG).
    -------------------------------------------------
    65-
    CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS
    PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MEDIA
    ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR
    VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO
    SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
    -------------------------------------------------
    # https://www.youtube.com/watch?v=LH6OIn2lBaI&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=72
'''