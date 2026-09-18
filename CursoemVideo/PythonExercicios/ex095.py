'''
EX095
APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VARIOS
JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE
DETALHES DO APROVEITAMENTO DE CADA JOGADOR.
'''

time = list()
jogador = dict()
partidas = list()

while True:      # LER OS DADOS DE VARIOS JOGADORES
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, total + 1):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)  # Soma dos gols
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break     # FIM. LER OS DADOS DE VARIOS JOGADORES

print('-=' * 30)    # CRIANDO CABECALHO
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()              # FIM. CRIANDO CABECALHO

print('-=' * 30)     # MOSTRAR RESULTADO
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-=' * 30)      # FIM. MOSTRAR RESULTADO

while True:     # QUAL JOGADOR QUER VER OS DADOS
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo da {busca}!')
    else:
        print(f'    -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}  ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    => Na partida {i}, fez {g} gols.')
            # FIM. QUAL JOGADOR QUER VER OS DADOS
