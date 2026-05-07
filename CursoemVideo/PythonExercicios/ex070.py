'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
70
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS
PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO
VAI CONTINUAR. NO FINAL MOSTRE:
A - QUAL O TOTAL GASTO NA COMPRA.
B - QUANTOS PRODUTOS CUSTAM MAIS DE R$1000.
C - QUAL É O NOME DO PRODUTO MAIS BARATO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
total = totmil = totbarato = cont = 0
barato = ' '
while True:
    produto = str(input('\033[0;35mNOME DO PRODUTO: '))
    preco = float(input('\033[0;34mPreço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1:
        totbarato = preco
        barato = produto
    else:
        if preco < totbarato:
            totbarato = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[0;31mQuer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('\033[0;34mFIM DO PROGRAMA')
print(f'\033[0;36mO total da compra foi: {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa {totbarato:.2f} é o {barato}')
