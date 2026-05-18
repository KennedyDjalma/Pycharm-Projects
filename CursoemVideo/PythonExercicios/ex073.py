'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
73
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS
DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM
DE COLOCAÇÃO. DEPOIS MOSTRE:
A - APENAS OS 5 PRIMEIROS  COLOCADOS.
B - OS ULTIMOS 4 COLOCADOS DA TABELA.
C - UMA LISTA COM OS TIMES EM ORDEM ALFABETICA.
D - EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo',
         'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba',
         'Botafogo', 'Atlético-MG', 'Internacional',
         'Vasco', 'Cruzeiro', 'Vitória', 'Grêmio', 'Santos',
         'Corinthians', 'Remo', 'Mirassol', 'Chapecoense')
print('-=\033[0;36m' * 25)
print(f'Lista de times do Brasileirão {times}')
print('\033[0;35m-=' * 25)

print(f'Os 5 primeiros são: {times[0:5]}')
print('\033[0;34m-=' * 25)

print(f'Os ultimos 4 colocados: {times[-4:]}')
print('\033[0;33m-=' * 25)

print(f'Uma lista de times na ordem alfabetica: {sorted(times)}')
print('\033[0;32m-=' * 25)

print(f'A posição do chapecoense é: {times.index("Chapecoense") + 1}')
