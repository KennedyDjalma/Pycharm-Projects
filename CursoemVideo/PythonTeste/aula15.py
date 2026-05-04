'''
cont = 1
while cont <= 10:
    print(cont, ',', end=' ')
    cont += 1
print('FIM')
'''

'''
n = cont = 0
while n != 999:
    n = int(input('Digite um numero: '))
    cont += 1
print(cont)
'''

'''
n = cont = 0
while cont < 5:
    n = int(input('Digite um numero: '))
    cont += 1
print(cont)
'''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))


''' USANDO AS F's STRINGS
nome = 'Kennedy'
idade = 29
salario = 5000
cidade = 'Lagoa'

print(f'O {nome} tem {idade} anos e recebe {salario} reais em {cidade}.')
'''

'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
66
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS 
PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUARIO
DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL
MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA
ENTRE ELES (DESCONSIDERANDO O FLAG.)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
67
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS,
UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO
FOR NEGATIVO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
68
FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O PC.
O JOGADOR SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE
CONQUISTOU NO FINAL DO JOGO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
69
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS
PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERA
PERGUNTAR SE O USUARIO QUER OU NÃO CONTINUAR. NO FINAL,
MOSTRE:
A - QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
B - QUANTOS HOMENS FORAM CADASTRADOS.
C - QUANTAS MULHERES TEM MENOS DE 20 ANOS.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
70
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS
PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO
VAI CONTINUAR. NO FINAL MOSTRE:
A - QUAL O TOTAL GASTO NA COMPRA.
B - QUANTOS PRODUTOS CUSTAM MAIS DE R$1000.
C - QUAL É O NOME DO PRODUTO MAIS BARATO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
71
CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM
CAIXA ELETRONICO. NO INICIO, PERGUNTE AO USUARIO
QUAL O VALOR SACADO (VALOR INTEIRO) E O PROGRAMA
VAI INFORMAR QUANTAS CEDULAS DE CADA VALOR SERÃO
ENTREGUES. OBS: CONSIDERE QUE O CAIXA POSSUI
CEDULAS DE R$50, R$20, R$10, E R$1.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

'''