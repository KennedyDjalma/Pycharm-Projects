'''
EX091
CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUE UM DADO E TENHA
RESULTADOS ALEATORIOS. GUARDE ESSES RESULTADO EM UM
DICIONARIO. NO FINAL, COLOQUE ESSE DICIONARIO EM ORDEM,
SABENDO QUE O VENCEDOR TIROU MAIOR NUMERO NO DADO.
'''

# Importar numeros aleatorios.
from random import randint

# Importar o tempo para aparecer o número sorteado
from time import sleep

#serve para importar a função itemgetter do módulo operator.
from operator import itemgetter

# Criando o dicionário
jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1,6),
    'jogador4': randint(1, 6),
}
#
ranking = list()

print('Valores Sorteados: ')

# Para cada Chave(k), em Valor(v) de jogo.itens()
# Mostrar qual Jogador tirou qual numero no dado.
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1) #Tempo de 1 segundo para mostrar o número sorteado.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True )
# key=itemgetter(1)      É uma função que retorna um "getter" (um objeto chamável) que
# busca itens de uma sequência (lista, tupla) ou de um dicionário,
# usando índices ou chaves. Muito usado em ordenação (sorted) ou
# em situações em que você precisa acessar elementos específicos
# de forma rápida.

# Tratando o resultado como uma lista
print('-'*40)
print('== RANKING DOS JOGADORES ==')

# Mostrar o Rancking
# Para cada indice(i) e valor(v) enumere a lista
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)