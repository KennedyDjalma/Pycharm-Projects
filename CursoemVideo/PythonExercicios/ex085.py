''' EXERCICIO 85
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR SETE
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA UNICA
QUE MANTENHA SEPARADOS OS VALORES PARES E IMPARES.
NO FINAL, MOSTRE OS VALORES PARES E IMPARES EM ORDEM
CRESCENTE.
'''
#https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=107
numero = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-='*30)
print(f'Todos os valores: {numero}')