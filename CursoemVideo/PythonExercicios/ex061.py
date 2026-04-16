'''
-------------------------------------------------
61-
REFAÇA O EXERCICIO 51, LENDO O PRIMEIRO TERMO E A
RAZÃO
DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA
PROGRESSAO
USANDO A ESTRUTURA WILE.
------------------------------------------------
'''

print('Gerador de PA')
print(' - ='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')



