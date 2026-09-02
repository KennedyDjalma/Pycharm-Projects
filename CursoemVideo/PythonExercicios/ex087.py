''' EXERCICIO 87
APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
A - A SOMA DE TODOS OS VALORES PARES DIGITADOS.
B - A SOMA DOS VALORES DA TERCEIRA COLUNA.
C - O MAIOR VALOR DA SEGUNDA LINHA.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é: {somapar}.')

print('-=' * 30)
for linha in range(0, 3):
    somacol += matriz[linha][2]
print(f'Asoma dos valores da terceira coluna: {somacol}.')

print('-=' * 30)
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior}.')
