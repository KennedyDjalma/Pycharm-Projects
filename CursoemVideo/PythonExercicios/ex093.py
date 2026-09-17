'''
EX093
CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM
JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR
E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE
DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TIDP ISSO SERA
GUARDADO EM UM DICIONARIO, INCLUINDO O TOTAL DE GOLS
FEITOS DURANTE O CAMPEONATO.
'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, total+1):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas) #Soma dos gols

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-='*30)
