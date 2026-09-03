''' EXERCICIO 88
FACA UM PROGRAMA  QUE AJUDE UM JOGADOR DA MEGA SENA A
CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS
SERAO GERADOS E VAI SORTEAR 6 NUMEROS ENTRE 1 E 60 PARA
CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.
'''
from random import randint
from time import sleep

lista = list()
jogos = list()

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

quantidade = int(input('Quantos jogos deseja gerar? '))
total = 0
while total < quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break

    lista.sort()  # os numeros ficara em ordem crescente.
    jogos.append(lista[:])
    lista.clear()  # apaga a lista
    total += 1
    
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
