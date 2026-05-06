'''
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
'''
tot18 = toth = totm20 = 0

while True:
    idade = int(input("Qual a sua idade? "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0]

    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        toth += 1

    if sexo == 'F' and idade <= 20:
        totm20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break

print(f'\033[0;35mO total de pessoas com mais de 18 anos: {tot18}')
print(f'\033[0;32mO total de homens cadastrados: {toth}')
print(f'\033[0;33mO total de mulheres com até 20 anos: {totm20}')
