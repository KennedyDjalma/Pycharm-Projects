''' EXERCICIO 85
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR SETE
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA UNICA
QUE MANTENHA SEPARADOS OS VALORES PARES E IMPARES.
NO FINAL, MOSTRE OS VALORES PARES E IMPARES EM ORDEM
CRESCENTE.
'''
numero = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

print('-='*30)
numero[0].sort() #Ordenaar os numeros pares
numero[1].sort() #Ordenaar os numeros ímpares
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')
